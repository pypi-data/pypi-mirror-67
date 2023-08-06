from aiohttp import web

from opentrons import types
from .session import CheckCalibrationSession, CalibrationCheckTrigger
from .models import SpecificPipette, MoveLocation, JogPosition


async def get_session(request: web.Request, session) -> web.Response:
    """
    GET /calibration/check/session

    If a session exists, this endpoint will return the current status.

    Otherwise, this endpoint will return a 404 with links to the post request.
    """
    return web.json_response(status=200)


async def create_session(request):
    """
    POST /calibration/check/session

    If a session exists, this endpoint will return a 409 with links to delete.
    If none exists, this will create a session and return its status.

    The status message is in the shape of:
    :py:class:`.models.CalibrationSessionStatus`
    """
    session_type = request.match_info['type']
    session_storage = request.app['com.opentrons.session_manager']
    current_session = session_storage.sessions.get(session_type)
    if not current_session:
        hardware = request.config_dict['com.opentrons.hardware']
        await CheckCalibrationSession.build(hardware)
        new_session = CheckCalibrationSession(hardware)
        session_storage.sessions[session_type] = new_session
        return web.json_response(status=201)
    else:
        router = request.app.router
        path = router.get('sessionExit')
        error_response = {
            "message": f"A {session_type} session exists."
                       "Please delete to proceed.",
            "links": {"deleteSession": str(path.url_for(type=session_type))}}
        return web.json_response(error_response, status=409)


async def delete_session(request: web.Request, session):
    """
    DELETE /calibration/check/session

    Endpoint to delete a session if it exists.
    """
    session_type = request.match_info['type']
    session_storage = request.app['com.opentrons.session_manager']

    await session.delete_session()
    del session_storage.sessions[session_type]
    response = {'message': f"Successfully deleted {session_type} session."}
    return web.json_response(response, status=200)


async def load_labware(request: web.Request, session) -> web.Response:
    await session.trigger_transition(CalibrationCheckTrigger.load_labware)
    return web.json_response(status=200)


async def prepare_pipette(request: web.Request, session) -> web.Response:
    req = await request.json()
    pipette = SpecificPipette(**req)
    await session.trigger_transition(CalibrationCheckTrigger.prepare_pipette,
                                     pipette_id=pipette.pipetteId)
    return web.json_response(status=200)


async def confirm_step(request: web.Request, session) -> web.Response:
    req = await request.json()
    pipette = SpecificPipette(**req)
    await session.trigger_transition(CalibrationCheckTrigger.confirm_step,
                                     pipette_id=pipette.pipetteId)
    return web.json_response(status=200)


# TODO: BC: make this function idea "confirm point" instead of "move"
async def move(request: web.Request, session) -> web.Response:
    req = await request.json()
    moveloc = MoveLocation(**req)
    if hasattr(moveloc.location, 'offset'):
        # using getattr to avoid error raised by Union of deck position and
        # tiprack position having different attributes.
        offset = getattr(moveloc.location, 'offset')
        location = {
            "locationId": moveloc.location.locationId,
            "offset": types.Point(*offset)}
    else:
        position = getattr(moveloc.location, 'position')
        location = {
            "locationId": moveloc.location.locationId,
            "position": types.Point(*position)}
    await session.trigger_transition(CalibrationCheckTrigger.confirm_step,
                                     pipette_id=moveloc.pipetteId,
                                     request_location=location)
    return web.json_response(status=200)


async def jog(request: web.Request, session: 'CheckCalibrationSession'):
    req = await request.json()
    jog_position = JogPosition(**req)
    await session.trigger_transition(CalibrationCheckTrigger.jog,
                                     jog_position.pipetteId,
                                     types.Point(*jog_position.vector))
    return web.json_response(status=200)


async def pick_up_tip(
        request: web.Request, session: 'CheckCalibrationSession'):
    req = await request.json()
    pipette = SpecificPipette(**req)
    await session.trigger_transition(CalibrationCheckTrigger.pick_up_tip,
                                     pipette.pipetteId)
    return web.json_response(status=200)


async def invalidate_tip(
        request: web.Request, session: 'CheckCalibrationSession'):
    req = await request.json()
    pipette = SpecificPipette(**req)
    await session.trigger_transition(CalibrationCheckTrigger.invalidate_tip,
                                     pipette.pipetteId)
    return web.json_response(status=200)


async def confirm_tip(
        request: web.Request, session: 'CheckCalibrationSession'):
    req = await request.json()
    pipette = SpecificPipette(**req)
    await session.trigger_transition(
        CalibrationCheckTrigger.confirm_tip_attached,
        pipette.pipetteId)
    return web.json_response(status=200)

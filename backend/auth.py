import uuid

from sanic_jwt import exceptions

import db_utils.user
import db_utils.strava_athlete_tokens
import strava
from user import User


async def authenticate(request, *args, **kwargs):
    """
    After a new client successfully authenticates with strava, call this
    endpoint with a user_id (uuid) and auth_code (from strava).

    we'll exchange the code for access tokens, get the athlete_id, and
    register this user.
    """
    return await User.get(user_id='2e87ddc2-5c57-4f7e-b50d-b30edafcb6f3')
    try:
        user_id = request.json.get('user_id', None)
        if not user_id:
            user_id = str(uuid.uuid4())
        code = request.json.get('code', None)
        if not code:
            raise exceptions.AuthenticationFailed("no code")

        token = await strava.exchange_code_for_token(code)
        print(f"Successfully exchanged code for token: {str(token)}")
        await db_utils.strava_athlete_tokens.put_athlete_token_info(
            strava_token=token
        )
        print(f"Successfully stored token")

        user = await User.register(user_id=user_id,
                                   athlete_id=token.athlete_id)

        print(f"Successfully registered user: {str(user)}")
        return user
    except Exception as e:
        raise exceptions.AuthenticationFailed(e)


async def retrieve_user(request, payload, *args, **kwargs):
    if payload:
        user_id = payload.get('user_id', None)
        user = await User.get(user_id=user_id)
        return user
    else:
        return None


async def store_refresh_token(user_id, refresh_token, *args, **kwargs):
    await db_utils.user.store_refresh_token(user_id=user_id,
                                            refresh_token=refresh_token)


async def retrieve_refresh_token(user_id, *args, **kwargs):
    return await db_utils.user.retrieve_refresh_token(user_id=user_id)



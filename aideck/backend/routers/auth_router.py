"""
Authentication router for AIDECK (JWT/OAuth2)
"""


from fastapi import APIRouter, HTTPException, status, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from aideck.backend.modules.security.auth import authenticate_user
from aideck.backend.modules.security.jwt_handler import create_jwt_token, verify_jwt_token
from fastapi_limiter.depends import RateLimiter
from authlib.integrations.starlette_client import OAuth

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

# OAuth2 setup (example with GitHub)
oauth = OAuth()
oauth.register(
    name='github',
    client_id='GITHUB_CLIENT_ID',
    client_secret='GITHUB_CLIENT_SECRET',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)


@router.post("/login", dependencies=[Depends(RateLimiter(times=5, seconds=60))])
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    token = create_jwt_token({"sub": user["username"], "role": user["role"]})
    return {"access_token": token, "token_type": "bearer"}

# OAuth2 login endpoint
@router.get("/oauth2/github")
async def oauth2_github_login(request: Request):
    redirect_uri = request.url_for('oauth2_github_callback')
    return await oauth.github.authorize_redirect(request, redirect_uri)

@router.get("/oauth2/github/callback")
async def oauth2_github_callback(request: Request):
    token = await oauth.github.authorize_access_token(request)
    user = await oauth.github.get('user', token=token)
    user_info = user.json()
    # Here you would create/find user in DB and issue JWT
    jwt_token = create_jwt_token({"sub": user_info["login"], "role": "user"})
    return {"access_token": jwt_token, "token_type": "bearer"}


@router.get("/me", dependencies=[Depends(RateLimiter(times=10, seconds=60))])
def read_users_me(token: str = Depends(oauth2_scheme)):
    payload = verify_jwt_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return {"username": payload.get("sub"), "role": payload.get("role")}

# from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from datetime import datetime, timedelta
import os
from fastapi import HTTPException, status
from fastapi.security import HTTPBearer
from jose import jwt, JWTError, ExpiredSignatureError

from schema import TokenData

GOOGLE_CLIENT_ID = "175712151730-dblfkundctnmakngt8iok09dmf0p0nmp.apps.googleusercontent.com"
client_secrets_file = "client_secret_web.json"
# to allow Http traffic for local dev
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
SECRET_KEY = "secretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRED = 1

oauth2_scheme = HTTPBearer()

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile",
            "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/callback"
)

CREDENTIALS_EXCEPTIONS = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)
CREDENTIALS_EXCEPTIONS_EXPIRED = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="token expired",
    headers={"WWW-Authenticate": "Bearer"},
)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRED)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email")
        if email is None:
            raise CREDENTIALS_EXCEPTIONS
        return email
    except ExpiredSignatureError:
        raise CREDENTIALS_EXCEPTIONS_EXPIRED
    except JWTError:
        raise CREDENTIALS_EXCEPTIONS


def refresh_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except ExpiredSignatureError:
        payload = jwt.get_unverified_claims(token)
    except JWTError:
        raise CREDENTIALS_EXCEPTIONS
    email = payload.get("email")
    if email is None:
        raise CREDENTIALS_EXCEPTIONS
    return create_access_token({"email": email})

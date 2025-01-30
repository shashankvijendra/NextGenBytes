from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from models import User
from datetime import timedelta, datetime
from helper import SECRET_KEY, ALGORITHM

# Set up authentication
def authenticate_user(username: str, password: str):
    # Replace with your own user database query
    if user := User(username=username, email="user@example.com", password=password):
        return user
    raise HTTPException(status_code=401, detail="Invalid username or password")

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
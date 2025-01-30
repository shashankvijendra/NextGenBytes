from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

# Set up JWT secret key and algorithm
SECRET_KEY = "TESTING"
ALGORITHM = "HS256"

# Set up password hashing
pwd_context = CryptContext(schemes=["bcrypt"], default="bcrypt")

# Set up OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

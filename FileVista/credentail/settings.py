import os
from decouple import config

SENDER_EMAIL = config('SENDER_EMAIL', cast=str)
SENDER_PASSWORD = config('SENDER_PASSWORD', cast=str)

GOOGLE_CLIENT_ID = config('GOOGLE_CLIENT_ID', cast=str)
GOOGLE_SECRET_CODE = config('GOOGLE_SECRET_CODE', cast=str)
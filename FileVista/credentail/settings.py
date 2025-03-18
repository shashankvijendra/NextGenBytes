import os
from decouple import config

SENDER_EMAIL = config('SENDER_EMAIL', cast=str)
SENDER_PASSWORD = config('SENDER_PASSWORD', cast=str)
from pathlib import Path
from decouple import config # Insert the code here.

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=True, cast=bool)
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
SECRET_KEY = os.getenv('SECRET_KEY')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
import os
from typing import Dict


class Auxiliary:
    """ This class is used to load data of .env file."""

    @staticmethod
    def get_django_key() -> Dict:
        return {"key": os.getenv("SECRET_KEY_DJANGO")}

    @staticmethod
    def get_debug_mode()->Dict:
        mode = True
        if os.getenv("DEBUG_MODE") == 'False':
            mode = False

        return{"mode":mode}

    @staticmethod
    def get_sqlite_location() -> Dict:
        return{
            "location":os.getenv("LOCATION_SQLITE_DB")
        }

    @staticmethod
    def get_static_url():
        return{
            "static_url":os.getenv("STATIC_URL")
        }

    def get_media_url():
        return{
            "media_url":os.getenv("MEDIA_URL")
        }
    
    def get_email_credentials():
        email_use_tls = True

        if os.getenv("EMAIL_USE_TLS") == 'False':
            email_use_tls = False
        return {
            "use_tls":email_use_tls,
            "host": os.getenv("EMAIL_HOST"),
            "user": os.getenv("MAIL_HOST_USER"),
            "password":os.getenv("EMAIL_HOST_PASSWORD"),
            "port":os.getenv("EMAIL_PORT")

        }

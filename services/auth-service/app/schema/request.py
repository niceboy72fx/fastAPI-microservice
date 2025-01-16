from datetime import datetime

from pydantic import BaseModel

from app.schema.user_schema import User


class SignIn:
    def __init__(self, email: str, password: str):
        pass


class SignUp:
    def __init__(self, first_name: str, last_name: str,user_name: str, password: datetime = None):
        pass


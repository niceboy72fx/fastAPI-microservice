from sqlmodel import Field
from datetime import datetime
from app.model.base_model import BaseModel
from config.enum import Gender, Status, Role

class User(BaseModel, table=True):
    first_name: str = Field
    last_name: str = Field
    date_of_birth: datetime
    gender:  Gender = SQLField(nullable=False)
    phone: str = Field
    email: str = Field(unique = True)
    status: Status = SQLField(nullable=False)

class Role(BaseModel, table=True):
    name: str = Field
    description: str = Field

class Permission(BaseModel, table=True):
    name: str = Field
    description: str = Field
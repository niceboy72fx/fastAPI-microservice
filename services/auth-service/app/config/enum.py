from enum import Enum

class Gender(Enum):
    MALE: 1
    FEMALE: 2

class UserStatus(Enum):
    ACTIVE: "active"
    INACTIVE: "inacvtive"
    LOCKED: "locked"
    NONE: "none"

class Role(Enum):
    OWNER: 'owner'
    ADMIN: 'admin'
    USER: 'user'

class TokenType(Enum):
    REFRESH_TOKEN,
    ACCESS_TOKEN
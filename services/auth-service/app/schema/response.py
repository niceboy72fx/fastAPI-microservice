from datetime import datetime

class BaseResponse:
    def __init__(self, created_at: datetime = None, updated_at: datetime = None, status: str, message: str):
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()
        self.status = status
        self.message = message
    def to_dict(self):
        return self.__dict__

class Token(BaseResponse):
    def __init__(self, access_token: str, refresh_token: str, **kwargs):
        super().__init__(**kwargs)
        self.access_token = access_token
        self.refresh_token = refresh_token

    def to_dict(self)
        base_dict = super().to_dict()
         base_dict["result"] = {
            "access_token": self.access_token,
            "refresh_token": self.refresh_token
        }
        return base_dict

from fastapi import APIRouter, FastAPI, HTTPException

class AuthenticationController:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/login", self.login_controller, methods=["POST"])
        self.router.add_api_route("/register",self.register_controller, methods=["POST"] )
        self.router.add_api_route("/access-token",self.new_access_token, methods=["GET"] )
        
    async def login_controller(self):
        pass
    
    async def register_controller(self):
        pass
    
    async def new_access_token(self, authorization: str = Header(None)):
        pass

item_controller = AuthenticationController()

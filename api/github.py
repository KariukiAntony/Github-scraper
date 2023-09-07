from fastapi import APIRouter
from api.schema import User

user = APIRouter(tags=["GITHUB SCRAPER"])

@user.post("/username")
def get_user_credentials(user: User):
          username = user.username
          return {"userinfo":username }

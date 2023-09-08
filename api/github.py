from fastapi import APIRouter, status
from api.schema import User
import requests
from bs4 import BeautifulSoup

user = APIRouter(tags=["GITHUB SCRAPER"])


@user.get("/")
def index():
        return {"message": "Hello world"}, status.HTTP_200_OK


@user.post("/username")
def get_user_credentials(user: User):
          username = user.username
          content = check_if_user_has_an_account(username)
          if content:
                  print("Yes, has a github username")
                  return {"success":f"user with username: {username} have a github account" }, status.HTTP_200_OK
                  

          return {"failed":f"user with username: {username} does not have a github account" }, status.HTTP_404_NOT_FOUND



def check_if_user_has_an_account(username: str):
        response = requests.get(url=f"https://github.com/{username}")
        if response.status_code == 200:
                return response.content
        
        return False
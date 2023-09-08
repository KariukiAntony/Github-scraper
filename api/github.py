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
                  content_info = BeautifulSoup(content, "html.parser")
                  avarter_image = get_avarter_image(content=content_info)
                  username1 = get_user_github_username(content=content_info)
                  data_bio_text = get_bio_text(content=content_info)
                  return {"avarter_image":avarter_image,
                           "profile_username": username1,
                           "Bio": data_bio_text
                           }, status.HTTP_200_OK
                  

          return {"failed":f"user with username: {username} does not have a github account" }, status.HTTP_404_NOT_FOUND



def check_if_user_has_an_account(username: str):
        response = requests.get(url=f"https://github.com/{username}")
        if response.status_code == 200:
                return response.content
        
        return False

def get_avarter_image(content):
        avarter_image = content.find("div", class_="js-profile-editable-replace")
        avarter_image = avarter_image.find("a")
        src = avarter_image.find("img").get("src")
        alt = avarter_image.find("img").get("alt")
        print({"src": src, "alt": alt} )
        return {"src": src, "alt": alt}

def get_user_github_username(content):
         profile_username = content.find("div", class_="js-profile-editable-replace")
         username = profile_username.find("span", class_="p-name vcard-fullname d-block overflow-hidden").text.replace("  ", "")
         username = profile_username.find("span", class_="p-name vcard-fullname d-block overflow-hidden").text.replace(" ", "")
         username = username.replace("\n", "")
         if username:
            return username
         
         return None

def get_bio_text(content):
        data_bio_text = content.find("div", class_="p-note user-profile-bio mb-3 js-user-profile-bio f4")
        if data_bio_text:
             data_bio_text = data_bio_text.get("data-bio-text")
             return data_bio_text
        
        return None
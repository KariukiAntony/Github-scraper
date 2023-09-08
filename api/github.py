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
                  avarter_image = get_Avatar_image(content=content_info)
                  username1 = get_user_github_username(content=content_info)
                  data_bio_text = get_bio_text(content=content_info)
                  navbar = get_user_navbar_info(content=content_info)
                  print(navbar)
                  return {"Avatar_image":avarter_image,
                           "profile_username": username1,
                           "Bio": data_bio_text,
                           "followers": get_user_followers(content=content_info),
                           "following": get_number_of_user_following(content=content_info),
                           "location": get_user_location(content=content_info),
                           "organization": get_user_organization(content=content_info),
                           "social_accounts": get_user_social_links(content=content_info),
                           "Repositories": navbar[0],
                           "projects": navbar[1],
                           "packages": navbar[2],
                           "stars": navbar[3],
                           "contributions": user_number_of_contribution(content=content_info),
                           "Private contribution": get_user_private_contrib(content=content_info)
                           }, status.HTTP_200_OK
                  

          return {"failed":f"user with username: {username} does not have a github account" }, status.HTTP_404_NOT_FOUND



def check_if_user_has_an_account(username: str):
        response = requests.get(url=f"https://github.com/{username}")
        if response.status_code == 200:
                return response.content
        
        return False

def get_Avatar_image(content):
        avarter_image = content.find("div", class_="js-profile-editable-replace")
        avarter_image = avarter_image.find("a")
        src = avarter_image.find("img").get("src")
        alt = avarter_image.find("img").get("alt")
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

def get_user_followers(content):
        followers = content.find("span", class_="text-bold color-fg-default")
        if followers:
                followers = followers.string
                return followers
        
        return 0

def get_number_of_user_following(content):
        following = content.find_all("span", class_="text-bold color-fg-default")[1]
        if following:
                following = following.string
                return following
                
        return 0

def get_user_location(content):
        location = content.find("span", class_="p-label")
        if location:
                return location.text
        
        return None

def get_user_organization(content):
        organization = content.find("span", class_="p-org")
        if organization:
                return  organization.text
        
        return None

def get_user_social_links(content):
        socials = []
        social_link = content.find("ul", class_="vcard-details")
        social_links = social_link.find_all("li", class_="vcard-detail pt-1")
        for link in social_links:
           socials.append(link.find("a", class_="Link--primary").get("href"))

        if len(socials) > 0:
              return socials
           
        return None

def get_user_navbar_info(content):
       repositories = content.find_all("span", class_="Counter")
       repos = repositories[0].text
       projects = repositories[1].text
       packages = repositories[2].text
       star_earned = repositories[3].text
       return [repos, projects, packages, star_earned]

def user_number_of_contribution(content):
       contrib = content.find("h2", class_="f4 text-normal mb-2")
       answer = contrib.string
       answer = answer[7: 12].replace("\n", "")
       return answer+" contributions in the last year"

def get_user_private_contrib(content):
       private = content.find("span",class_="f4 lh-condensed m-0 color-fg-muted")
       if private:
          private_text = private.text[13:15].replace("\n", "")
          return private_text+ " contributions in private repositories"

       return None
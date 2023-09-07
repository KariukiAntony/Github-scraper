# import requests
# from bs4 import BeautifulSoup

# url = "https://github.com/ochiengotieno304/"
# # https://github.com/cryceTruly
# # https://github.com/samoraMachel
# # https://github.com/ochiengotieno304/
# # https://github.com/kariukiAntony
# # https://github.com/kenStarry

# response = requests.get(url=url)

# content = BeautifulSoup(response.content, "html.parser")
# profile_content = content.find("div", class_="js-profile-editable-replace")
# profile_content = profile_content.find("a")
# src = profile_content.find("img").get("src")
# alt = profile_content.find("img").get("alt")
# # print({"src": src, "alt": alt} )

# profile_username = content.find("div", class_="js-profile-editable-replace")
# username = profile_username.find("span", class_="p-name vcard-fullname d-block overflow-hidden").text.replace("  ", "")
# # username = profile_username.find("span", class_="p-name vcard-fullname d-block overflow-hidden").text.replace(" ", "")
# # print(username.replace("\n", ""))

# data_bio_text = content.find("div", class_="p-note user-profile-bio mb-3 js-user-profile-bio f4")
# data_bio_text = data_bio_text.get("data-bio-text")

# followers = content.find("span", class_="text-bold color-fg-default")
# followers = followers.string + " followers"


# following = content.find_all("span", class_="text-bold color-fg-default")[1]
# following = following.string + " following"

# location = content.find("span", class_="p-label")

# organization = content.find("span", class_="p-org")

# socials = []
# social_link = content.find("ul", class_="vcard-details")
# social_links = social_link.find_all("li", class_="vcard-detail pt-1")
# for link in social_links:
#           socials.append(link.find("a", class_="Link--primary").get("href"))

# nav_bar_info = []
# repositories = content.find_all("span", class_="Counter")
# repos = repositories[0]
# projects = repositories[1]
# packages = repositories[2]
# star_earned = repositories[3]
# print(star_earned.text)
import asyncio
 
async def fn():
    print('This is ')
    await asyncio.sleep(2)
    print('asynchronous programming')
    await asyncio.sleep(3)
    print('and not multi-threading')
 
asyncio.run(fn())
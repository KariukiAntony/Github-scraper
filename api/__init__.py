from fastapi import FastAPI
from api.github import user
def create_app():

          app = FastAPI()
          app.include_router(user)

          return app
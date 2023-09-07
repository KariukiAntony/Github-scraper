import uvicorn
from api import create_app

app = create_app()

if __name__ == "__main__":
          uvicorn.run("main:app", reload=True, port=5000)
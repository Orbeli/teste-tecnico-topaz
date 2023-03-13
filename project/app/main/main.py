from dotenv import load_dotenv

from fastapi import FastAPI

load_dotenv()


app = FastAPI(
    title="REPORTS GITHUB",
    version="1.0.0"
)

from app.main.routes import *
from app.middleware.middleware import TimerMiddleware
from fastapi import FastAPI
from app.models import models
from app.controllers import common,chat_controller

from fastapi.middleware.cors import CORSMiddleware
from app.db.db import engine


app = FastAPI(debug=True)

@app.route("/")
def hc():
    return {
    "APP": "lon",
    "VERSION": "0.1"
}

app.add_middleware(TimerMiddleware)

# Configure CORS settings
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def create_app():
    models.Base.metadata.create_all(bind=engine)
    app.include_router(common.router, prefix="/common")
    app.include_router(chat_controller.router, prefix="/chat")
    return app


create_app()


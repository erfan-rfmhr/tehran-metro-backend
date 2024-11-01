from fastapi import FastAPI

from config.utils import lifespan

app = FastAPI(lifespan=lifespan)

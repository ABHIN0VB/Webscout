from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.database import init_db
from app.config import get_settings
from app.api import research, products, scraper, analytics
import logging

logging.basicConfig(level=logging.INFO)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

settings = get_settings()

app = FastAPI(title="WebScout API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL, "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(research.router)
app.include_router(products.router)
app.include_router(scraper.router)
app.include_router(analytics.router)

@app.get("/api/health")
async def health_check():
    return {"status": "ok"}

@app.get("/")
async def root():
    return {"app": "WebScout", "version": "1.0.0"}

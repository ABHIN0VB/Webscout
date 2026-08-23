import logging
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from app.config import get_settings

logger = logging.getLogger(__name__)
settings = get_settings()

Base = declarative_base()

# Attempt primary database engine (PostgreSQL or configured DB)
db_url = settings.DATABASE_URL
if not db_url or "postgresql" in db_url:
    # Try creating engine; fallback mechanism in init_db
    pass

engine = create_async_engine(db_url, echo=False)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def init_db():
    global engine, async_session_maker
    logger.info(f"Initializing database with URL: {engine.url}...")
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("Database initialized successfully.")
    except Exception as e:
        logger.warning(f"Could not connect to primary database ({e}). Falling back to local SQLite database...")
        fallback_url = "sqlite+aiosqlite:///./webscout.db"
        engine = create_async_engine(fallback_url, echo=False)
        async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("Local SQLite database initialized successfully at ./webscout.db")


async def get_db():
    async with async_session_maker() as session:
        yield session

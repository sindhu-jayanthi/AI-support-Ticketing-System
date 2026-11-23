import os
from dotenv import load_dotenv
from database_models import Base
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
load_dotenv()
DATABASEURL = os.getenv("DATABASE_URL")
if not DATABASEURL:
    raise ValueError("DATABASE_URL is missing from .env")
engine=create_async_engine(DATABASEURL,echo=True)
sessionLocal=async_sessionmaker(engine,expire_on_commit=False,class_=AsyncSession)
async def get_db():
    async with sessionLocal() as session: # async with manages the session lifecycle and ensures it gets closed.
        yield  session #provides the session to the API endpoint through FastAPI's dependency injection.

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
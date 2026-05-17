# handles DB connection
import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
PASSWORD = quote_plus(PASSWORD)

print("USERNAME:", USERNAME)
print("PASSWORD:", PASSWORD)
print("ENV FILE EXISTS:", os.path.exists(".env"))
print("PORT:", PORT)

DB_URL = f"postgresql+asyncpg://{USERNAME}:{PASSWORD}@{DB_HOST}:{PORT}/{DB_NAME}"

# print("DB_URL:", DB_URL) 


engine = create_async_engine(
    DB_URL,
    pool_size=10,          # number of persistent connections
    max_overflow=20,       # extra temporary connections   (total = 30 connections max)
    pool_timeout=30,       # wait time before timeout
    pool_recycle=1800,     # recycle connections every 30 mins
    pool_pre_ping=True,     # checks dead connections  //check if connections are alive before using them
    echo = False #it prints all the SQL queries in the console, useful for debugging but should be False in production
)

AsyncSessionLocal = sessionmaker(bind = engine, 
                                 class_ = AsyncSession,
                                 autoflush=False, 
                                 autocommit = False,
                                 expire_on_commit = False)

#injects db session to routes/services
async def get_db():
    async with AsyncSessionLocal() as db: #creates a new session for each request and ensures it's properly closed after use, even if an error occurs.
        yield db



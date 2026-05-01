# handles DB connection
import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

PORT = os.getenv("PORT", "5432")
USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
PASSWORD = quote_plus(PASSWORD)

print("USERNAME:", USERNAME)
print("PASSWORD:", PASSWORD)
print("ENV FILE EXISTS:", os.path.exists(".env"))

DB_URL = f"postgresql://{USERNAME}:{PASSWORD}@localhost:{PORT}/{DB_NAME}"

print("DB_URL:", DB_URL) 


engine = create_engine(DB_URL)

sessionlocal = sessionmaker(bind = engine, autoflush=False, autocommit = False)

#injects db session to routes/services
def get_db():
    db = sessionlocal()
    
    try: 
        yield db
    finally:
        db.close()



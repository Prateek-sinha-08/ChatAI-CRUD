This is the first file that's been craeted 
---
Setup your env first
---

## backend
- put .env here.
~~~

GROQ_API_KEY=YOUR_API_KEY
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=YOUR_LANGSMITH_API_KEY
LANGSMITH_PROJECT="pr-abandoned-exposure-93"


ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
SECRET_KEY = ""

DB_USERNAME = "your db username (eg; postgres)"
DB_PASSWORD = "your db password"
DB_NAME = "db name"
DB_PORT = port 
~~~

### Topics to Learn
- Connection Pooling in SQLAlchemy
- Multi Agent and setup.
- Memory Long Term in langgraph
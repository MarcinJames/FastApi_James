# FastApi_James
FastApi with Python using MongoDB and Oauth2


FastAPI app using PyMongo, Pydantic, FastAPI JWT Auth package, and Docker-compose.


   Start with MongoDB Docker container:
  $ docker-compose up -d
  
   Execute this command to initialize the FastAPI server with Uvicorn:
  $ uvicorn app.main:app --host localhost --port 8000 --reload

FastAPI generates the API docs that comply with OpenAPI standards

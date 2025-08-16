// prerequisites 
Install Postgres and set up (note down user and password)
Install python

// clone repo

// create virtual env
python -m venv venv

// install all required packages/libraries using:
pip install -r requirements.txt

// Replace your password in app/db/database.py -> DATABASE_URL = "postgresql://postgres:<password>@localhost:5432/fastapidb"
// if your password include "@" in it , Eg: demo@123 , you shloud replace "@" with "%40" in above url

// run application from root folder : uvicorn app:main:app --reload

// navigate to http://127.0.0.1:8000/docs 
// this is a Swagger UI , which give all apis to try out 

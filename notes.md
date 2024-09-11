## Commands used for this project

# create virtual environment
```  
python3 -m venv my_env
```
# Activate virtual environment
``` 
source my_env/bin/activate
```
# Deactivate virtual environment
``` 
deactivate
```
# -----------------------------------------------------------------------

# Install Django and version
```
python3 -m pip install Django
python3 -m django --version
```

# create startup project
```  
django-admin startproject mysite
```
# run migration / different port
``` 
cd mysite
python3 manage.py migrate
python manage.py migrate 8080
```
# Run Server
```
python3 manage.py runserver
```

# ModuleNotFoundError: No module named 'psycopg2'
```
https://stackoverflow.com/questions/12906351/importerror-no-module-named-psycopg2
```
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

# Create inital migration
```
python3 manage.py makemigrations blog
```

# Inspect the SQL output of your first migration
```
python3 manage.py sqlmigrate blog 0001
```

# run migration 
``` 
cd mysite
python3 manage.py migrate
```
# Run Server / different port
```
python3 manage.py runserver
python3 manage.py runserver 8080
```

# Create superuser
```
python3 manage.py createsuperuser
```


# ModuleNotFoundError: No module named 'psycopg2'
```
https://stackoverflow.com/questions/12906351/importerror-no-module-named-psycopg2
```
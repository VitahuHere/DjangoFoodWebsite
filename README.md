# Business website for food packages
Find your favourite recipes and order ingredients for them right away

# Install
Install dependencies with:
```
pip install -r requirements.txt
```
Install PostgreSQL from their [website](https://www.postgresql.org/download/)
### Optional Docker:
Install Docker from their [website](https://www.docker.com/get-started)

# Preparations
Navigate to directory and run:
```
python (or python3 if on linux or MacOS) manage.py makemigrations && python manage.py migrate
```
### Optional Docker
Navigate to directory and run:
```
docker-compose up
```

# Usage
To start local server run:
```
python manage.py runserver
```
or to specify ip and port:
```
python manage.py runserver 192.168.0.0:8080
```

# For more documentation, runserver and go to documentation/
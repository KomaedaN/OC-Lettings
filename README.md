## Environment

- Clone this repository 
- Create a virtual environment: "python -m venv env"
- Activate the virtual environment: "env/Scripts/activate.ps1"
- Install requirements: pip install -r requirements.txt

## Environment variable 

- cd ```/Python-OC-Lettings-FR/oc_lettings_site```
- Create a ".env" file inside "oc_lettings_site" folder
- Add your Sentry dsn and Django key value like this: 
```
SENTRY_DSN=YOURVALUE
DJANGO_KEY=YOURVALUE
```


## Run site

- cd ```/Python-OC-Lettings-FR```
- Run server: "python manage.py runserver"

## Linting and unit tests

- cd ```/Python-OC-Lettings-FR```
- Linting: "flake8"
- Tests: pytest

## Sentry 

- Create a project on Sentry
- Find your DSN go to your project "settings" > "SDK SETUP" > "Client Keys (DSN)" > "DSN"
- Sentry error can be tested at /sentry-debug/

## Heroku

- Create a new Heroku app
- In this app go to "settings" > "Config Vars"
- Then create "SENTRY_DSN" variable and add your Sentry link

## Docker

- Pull your image from DockerHub: ```docker pull username/image:tag``` 
- To run Use: ```docker run --env-file oc_lettings_site/.env -e PORT=8000 -p 8000:8000 username/image:tag```

## CircleCI

- In you CircleCI project go to "Project Settings" > Environment Variables 
- Then create all this Variables and add your values:
```
DOCKER_PASSWORD	
DOCKER_REPO	
DOCKER_USERNAME	
HEROKU_API	
HEROKU_NAME	
HEROKU_PASSWORD	
HEROKU_USERNAME	
SENTRY_DSN
```

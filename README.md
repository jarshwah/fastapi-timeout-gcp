# Direktor

A redirection service, with business logic removed, to repro a GCP Cloud Run issue.

## Local Setup

```
pyenv local 3.8.x  # whatever your python 3.8 is, make sure it's active
poetry install
poetry run pre-commit install -f
```

## Local Server

Run the docker image, which will expose port 9050 for testing:

```
docker-compose build app
docker-compose up app
```

Then you can test with curl or HTTPie:

```
http "http://127.0.0.1:9050/some/path/?state=example.com|ignore"

HTTP/1.1 302 Found
date: Wed, 27 May 2020 03:48:46 GMT
location: https://example.com/some/path/
server: uvicorn
transfer-encoding: chunked
```

You might want to avoid running under docker if you want to debug. See examples below.

## Deploying

This project will auto-deploy on commit to master. A github action will trigger
to deploy the project according to the config in `infrastructure/cloud-build.yml`,
as long as linting and tests pass.

Manual Deploy:

```
gcloud config set project <projectname>
gcloud builds submit --config infrastructure/cloud-build.yml
```

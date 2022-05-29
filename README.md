[![Python application](https://github.com/bleakview/pyapiexample/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/bleakview/pyapiexample/actions/workflows/python-app.yml)   [![publish to docker registry](https://github.com/bleakview/pyapiexample/actions/workflows/push_to_docker_hub.yml/badge.svg)](https://github.com/bleakview/pyapiexample/actions/workflows/push_to_docker_hub.yml)

# PyApiExample

Hi ! This is an example written in Python 3 for a start point on how to write a FastAPI API with SQLAlchemy.
It supports pytest and you can test api with swagger via http://localhost:<port>/docs.
If you directly run docker container it will use sqlite.
You can change default port with PORT environment variable.
You can change default database with mysql with the following syntax.
mysql+aiomysql://\<username>:\<password>@\<mysql host>:\<mysql port>/\<mysql database>

The repo also includes a docker compose file so that you can test without installing.

On very change code test will be run and a new docker image will bu pushed to
[https://hub.docker.com/repository/docker/bleakview/pyapiexample](https://hub.docker.com/repository/docker/bleakview/pyapiexample).

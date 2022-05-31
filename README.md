[![Python CI](https://github.com/bleakview/pyapiexample/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/bleakview/pyapiexample/actions/workflows/python-app.yml)   [![publish to docker registry](https://github.com/bleakview/pyapiexample/actions/workflows/push_to_docker_hub.yml/badge.svg)](https://github.com/bleakview/pyapiexample/actions/workflows/push_to_docker_hub.yml)

# Python Api Example
  
<img src="https://bleakview.github.io/git/pyapiexample/images/pyapiexample.jpg" alt="swagger example image" width="800"/>

  
This is an example written in Python for a start point on how to write a FastAPI with SQLAlchemy. 
It supports python testing and you can test api with swagger via 
```
http://localhost:8000/docs/
```
If you would like to test with docker comment was given below.
```
docker run --name pyapiexample -d -p 8000:8000 bleakview/pyapiexample:1.0.1
```
  
If you directly run docker container it will use sqlite. The docker compose file in this repository will invoke the image with mysql with the command given below.  
```
docker-compose up
```
There are two environment variables that you can use with this image.  
**DB_CONNECTION_URL** MySql DSN string for SQLAlchemy with aiomysql  
**PORT** Port number  
    
On very change code test will be run and a new docker image will bu pushed to  
[https://hub.docker.com/r/bleakview/pyapiexample](https://hub.docker.com/r/bleakview/pyapiexample).

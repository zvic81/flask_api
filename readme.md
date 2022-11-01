


# Flask_api
Flask_api is a Python application for test api rest on flask and using postgresql




## Requirements

- Python 3.7+
- psycopg2-binary
- Flask
- apiflask
- installed docker engine in Linux

## Installation

For Linux :
- 1) Clone the repository from GitHub. Then install all the dependencies.
```bash
$ git clone git@github.com:zvic81/flask_api.git
```
- 2) Run script for building docker images and running it
```bash
$ ./ install.sh
```
- 3) Try open http://127.0.0.1:5000 for swagger gui app or use Postman
- 4) If no response - check docker, must be  2 images running (postgres and flask_api)
```bash
$ docker ps
```
- If no images - run app images manually
```bash
$ docker run \
  --name pst \
  -e POSTGRES_PASSWORD=test1234 \
  -e POSTGRES_USER=zvic \
  -d \
  -p 5433:5432 postgr
$ docker run -p5000:5000 --net=host flask_api
```
- 5) Try again open http://127.0.0.1:5000 for swagger gui app or use Postman

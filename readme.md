


# Flask_api
Flask_api is a Python application for test api rest on flask and using postgresql




## Requirements

- Python 3.7+
- psycopg2-binary --not need if use compose
- Flask  --not need if use compose
- apiflask  --not need if use compose
- installed docker compose in Linux

## Installation

For Linux :
- 1) Clone the repository from GitHub. Then install all the dependencies.
```bash
$ git clone git@github.com:zvic81/flask_api.git
```
- 2) Run docker compose for building docker images and running it, need file docker-compose.yml in dir flask_api
```bash
$  cd flask_api
$  docker compose up -d
```
- 3) Try open http://127.0.0.1:5000 for swagger gui app or use Postman

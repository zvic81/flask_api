# Flask_api
Flask_api is a Python application for test API REST. It's the model of simple storehouse. API lets view, create and delete goods in DB and orders for buyers. Added simple authentication with google oAuth2 and JWT tokens.

Used technologies:
- APIFlask
- psycopg2
- pytest
- FlaskJWT
- GoogleAuth
- Docker compose
- Github Action

## Requirements

- Python 3.7+
- Installed docker compose in Linux

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

## Description
For google oAuth there must be file client_secret_web.json in project root dir. URL for file https://console.cloud.google.com/apis/credentials?project=vzaharov

Endpoints:

- get /docs - main page for swagger documentation, some function may be ran there
- get /goods' - get all goods in short view
- get /orders - get all orders for current user. Need jwt token given in endpoint /login. Endpoint gives only orders with email user from jwt token
- get /goods/<int:good_id> - get entire information for good with id
- post /goods - add new good to DB
- post /orders - add new order
- put /goods/<int:good_id>' - change good with id
- delete /goods/<int:good_id> - delete good with id
- get /login - enter login-email for protected access
- get /callback - servise endpoint for reciving jwt token after authentication
- get /refresh - get new token if current is expired, Need send refresh token

There is samples json requests in file flask_api.postman_collection

There is file linting-and-pull-request in dir .github  - script for github action. It makes checking linting and auto pull request to branch main

There are tests in dir tests, description in every script

Structure of DB and test data in file db/flask_db.sql
# flask_api

flask_api is a Python application for test api rest on flask and using postgresql

## Installation

Clone the repository from GitHub. Then create a virtual environment, and install all the dependencies.

```bash
git clone git@github.com:zvic81/flask_api.git
python -m pip install -r requirements.txt
```

## Usage
1) restore database from /db_sql. Command for bash in /db_sql/readme. Backup in flask_db.sql
2)Check if exists database flask_db in postgres and exists user flask_user
3) run in bash python3 main.py
4) If no errors see Running on http://127.0.0.1:5000
5) open in browser http://127.0.0.1:5000, there is available adresses
6) use 'postman' for methods put post delete. format json: { "name":"bananas", "price":8, "manufacture_date":"2/11/11", "picture_url":"gogle.com" } 



## Contributing



# flask_api

flask_api is a Python application for test api rest on flask and using postgresql

## Installation

Clone the repository from GitHub. Then install all the dependencies.

```bash
git clone git@github.com:zvic81/flask_api.git
python3 -m pip install -r requirements.txt
```

## Usage
1) restore database from /db_sql.Backup in flask_db.sql Command for bash
```bash
./createFlaskDB.sh
```

 
2) Check if exists database flask_db in postgres and exists user flask_user.
3) Check and correct 'password' for user flask_user and "db_name" in file config.py
4) run in bash python3 main.py
5) If no errors see Running on http://127.0.0.1:5000
6) open in browser http://127.0.0.1:5000, there is available adresses
7) use 'postman' for methods put post delete. format json: { "name":"bananas", "price":8, "manufacture_date":"2/11/11", "picture_url":"gogle.com" } 



## Contributing



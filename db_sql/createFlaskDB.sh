#!/bin/bash
# creating postgressql database flask_db , role flask_user with password flask_user and table goods
sudo -u postgres psql < flask_db.sql

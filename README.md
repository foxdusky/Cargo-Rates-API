# Cargo-Rates API

This API is designed to calculate the cost of cargo insurance based on data from the database

# [Project Structure](./project-structure.md)

# Edpoints

## POST api/user/create/

Endpoint for registering a new client has a username uniqueness check under the hood. After successful
registration, it gives the token

## GET api/user/current/

Endpoint for getting information about the current user.

## POST api/insurance/upload/

Endpoint for uploading data about insurance rates

## POST api/insurance/cost/

Endpoint for getting insurance cost by declared value, cargo type and date

# Deploy

Execute the command

~~~
git clone https://github.com/foxdusky/Cargo-Rates-API.git
~~~

OR

~~~
gh repo clone foxdusky/Cargo-Rates-API
~~~

create an env file in the root of the repository

ENV EXAMPLE

~~~
COMPOSE_PROJECT_NAME='YOUR_COMPOSE_PROJECT_NAME'

# DEV OR PROD ENVIRONMENT
IS_DEV_ENV=1

SECRET_KEY='YOUR_SECRET_KEY'

POSTGRES_USER='YOUR_POSTGRES_USER'
POSTGRES_PASSWORD='YOUR_POSTGRES_PASSWORD'

#REPLACE @POSTGRES_USER:@POSTGRES_PASSWORD TO THE REAL ONE

DB_CON_STR=postgresql://@POSTGRES_USER:@POSTGRES_PASSWORD@db:5432/postgres

# Migration con str
#REPLACE @POSTGRES_USER:@POSTGRES_PASSWORD TO THE REAL ONE
#DB_CON_STR=postgresql://@POSTGRES_USER:@POSTGRES_PASSWORD@localhost:5432/postgres


# REPLACE THAT TO REAL PATHS IF THAT IS PROD ENVIRONMENT
SSL_KEY_FILE=./.env
SSL_CERT_FILE=./.env


~~~

run using docker

~~~
docker-compose up -d --build
~~~

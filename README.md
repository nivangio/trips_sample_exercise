# Trips Sample Exercise 

This repository contains a process to read in Data with specified structure (region, origin_coord, destination_coord, datetime, datasource) from a CSV file in a specified URL and store it into a SQL-like (OLAP or OLTP) DB.

## About

The repository contains one main executable `main.py` that does the mentioned process. As the file is read in a stream line by line, there is no danger of an Out of Memory exception due to a file too large.

## Prerequisites

In order for it to work, you will need to have a DB Instance with the corresponding Database with Postgis extension and Table. Below a series of steps to test it. Keep in mind, that the Postgres Instance will be containerized and may not adjust to your requirements:
  
  * Clone repository: `git clone https://github.com/nivangio/trips_sample_exercise.git` (Avoid this step if you've done it before)
  * Go to the source folder: `cd trips_sample_exercise`
  * Make a dir to mount as volume: `mkdir postgres_volume`
  * Initialize Engine: `sh start_postgres.sh` (**NOTE**: You may need sudo privileges)
  * Create DB: `psql -U postgres --host localhost -c 'CREATE DATABASE TRIPS;'` (**NOTE**: If you do not edit default engine configurations in the previous step, password is 'abcd')
  * Create Postgis Extension: `psql --host localhost -d trips --user postgres -c 'CREATE EXTENSION postgis';`
  * Create Table: `sh create_table.sh`

## Usage

The solution is containerized and for that reason it can be ran using Docker. In order to keep database string connections as well as data source origins safe and flexible, they are passed as environment variables. To run the Docker, follow these steps:

  * Clone repository: `git clone https://github.com/nivangio/trips_sample_exercise.git` (Avoid this step if you've done it before)
  * Go to the source folder: `cd trips_sample_exercise`
  * Create a copy of .env.example file: `cp .env.example .env`
  * Edit .env file and pass corresponding values
  * Build docker image: `docker build . -t trips_sample` (**NOTE**: You may need sudo privileges)
  * Run docker image: `docker run --network host --name execution --env-file .env trips_sample` (**NOTE**: You may need sudo privileges)

The solution stores the errored records in a log. If you would like to keep them persistently outside the container, you have to mount the log folder in a local folder on image run:

`docker run --network host -v /path/to/persistent/storage:/home/app/logs --name execution --env-file .env trips_sample`
 

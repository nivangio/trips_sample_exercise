# Trips Sample Exercise 

This repository contains a process to read in Data with specified structure (region, origin_coord, destination_coord, datetime, datasource) from a CSV file in a specified URL and store it into a SQL-like (OLAP or OLTP) DB.

## About

The repository contains one main executable `main.py` that does the mentioned process. As the file is read in a stream line by line, there is no danger of an Out of Memory exception due to a file too large.

## Usage

The solution is containerized and for that reason it can be ran using Docker. In order to keep database string connections as well as data source origins safe and flexible, they are passed as environment variables. To run the Docker, follow these steps:

  * Clone repository: `git clone https://github.com/nivangio/trips_sample_exercise.git`
  * Go to the created folder: `cd trips_sample_exercise`
  * Create a copy of .env.example file: `cp .env.example .env`
  * Edit .env file an pass corresponding values
  * Build docker image: `docker build . -t trips_sample` (**NOTE**: You may need sudo privileges)
  * Run docker image: `sudo docker run --network host --name execution --env-file .env trips_sample`
 

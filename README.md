# Trips Sample Exercise 

This repository contains a process to read in Data with specified structure (region, origin_coord, destination_coord, datetime, datasource) from a CSV file in a specified URL and store it into a SQL-like (OLAP or OLTP) DB.

## About

The repository contains one main executable `main.py` that does the mentioned process. As the file is read in a stream line by line, there is no danger of an Out of Memory exception due to a file too large.

## Usage

The solution is containerized and for that reason it can be ran using Docker. In order to keep database string connections as well as data source origins safe and flexible, they are passed as environment variables. To run the Docker, follow these steps:

  * Install PostgreSQL Instance: For development purposes, you can use the bash docker 

#!/bin/bash


##This file is just for creating a local isolated DB instance for testing anddevelopment purposes.
docker run -d \
    -p 5432:5432 \
    --name trips-db \
    -e POSTGRES_PASSWORD=abcd \
    -e PGDATA=/var/lib/postgresql/data/pgdata \
    -v postgres_volume:/var/lib/postgresql/data \
    postgis/postgis

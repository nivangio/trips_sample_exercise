--This script generates the table
CREATE TABLE public."TRIPS"(

    id serial PRIMARY KEY,
    region varchar(50),
    origin_coord GEOMETRY(POINT,4326),
    destination_coord GEOMETRY(POINT,4326),
    datetime timestamp,
    datasource varchar(25)
);

CREATE INDEX idx_origin_coord_trips on public."TRIPS" using GIST(origin_coord);
CREATE INDEX idx_destination_coord_trips on public."TRIPS" using GIST(destination_coord);
CREATE INDEX idx_datetime_trips on public."TRIPS"(datetime);
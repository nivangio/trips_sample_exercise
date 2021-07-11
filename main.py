from get_file_by_line import get_file_by_line
from os import getenv
from psycopg2 import connect
from setup_logger import setup_logger

##Create Lgger
logger = setup_logger("insert_registers", "/home/app/logs/inserts", recurrency="H")

##Under scenarios where more flexibility is required the statement wouldn't be hardcoded
base_query = """ insert INTO public."TRIPS"(region,origin_coord,destination_coord, datetime, datasource) VALUES (%s, %s, %s, %s, %s)"""

connection = connect(getenv("CONNECTIONSTRING"))

with connection.cursor() as cur:
    for i in get_file_by_line(getenv("DATA_URL")):

        try:
            cur.execute(base_query, tuple(i))
        ##Log registers that cannot be sent
        except Exception as e:
            logger.error("Could not insert {}. Reason: {}".format(str(i), e.args[0]))
connection.commit()
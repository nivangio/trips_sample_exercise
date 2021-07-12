from get_file_by_line import get_file_by_line
from os import getenv
from psycopg2 import connect
from setup_logger import setup_logger

##Create Lgger
logger = setup_logger("insert_registers", "/home/app/logs/inserts", recurrency="H")

##Under scenarios where more flexibility is required the statement wouldn't be hardcoded
base_query = """ insert INTO public."TRIPS"(region,origin_coord,destination_coord, datetime, datasource) VALUES (%s, %s, %s, %s, %s)"""

connection = connect(getenv("CONNECTIONSTRING"))

file_path = "/home/app/input_files/" + getenv("FILENAME")
with connection.cursor() as cur:
    n_elems = 0
    for i in get_file_by_line(file_path):

        try:
            cur.execute(base_query, tuple(i))
            logger.info("{} inserted succesfully".format(str(i)))
        ##Log registers that cannot be sent
        except Exception as e:
            logger.error("Could not insert {}. Reason: {}".format(str(i), e.args[0]))
        n_elems += 1
        ### Commit every 1000 entries
        if n_elems % 1000 == 0:
            connection.commit()
            print(str(n_elems) + "lines read")
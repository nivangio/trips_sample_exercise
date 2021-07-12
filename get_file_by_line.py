##This function takes a path and reads the content in line by line to avoid overwhelming the memory if
##the file is too big.
from requests import get

def get_file_by_line(path):

    ##Enclose get in with to ensure connection close after its finished
    with open(path) as f:
        ##Assum first line is header
        f.readline()

        line = f.readline()
        ##Enter the loop
        while line:
            ##Read in
            row = line.split(",")

            ##Prepare for next line
            line = f.readline()
            yield row
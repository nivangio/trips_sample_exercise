##This function takes a url and returns the content in stream chunks to avoid overwhelming the memory if
##the file is too big.
from requests import get

def get_file_by_line(url):

    ##Enclose get in with to ensure connection close after its finished
    with get(url, stream=True) as r:

        ##Get file size
        total_size = int(r.headers["Content-length"])

        ##Set read size to 0
        read_size = 0

        ##Iterate over lines
        for ind, line in enumerate(r.iter_lines()):
            read_size += len(line)
            progress = read_size/total_size
            ##Assume first line is headers
            if ind == 0:
                continue

            row = line.decode('utf-8').split(",")
            print("Progress : %d%%" % (round(progress * 100)))
            yield row
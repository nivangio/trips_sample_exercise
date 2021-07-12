FROM python:3.8-slim

##Install libraries
RUN apt-get -y update && apt-get install -y libpq-dev python3-dev g++

RUN mkdir /home/app
WORKDIR /home/app
COPY . .
RUN pip install -r requirements.txt
RUN mkdir /home/app/logs
RUN mkdir /home/app/input_files

ENV PYTHONPATH=/home/app/

CMD ["python", "main.py"]
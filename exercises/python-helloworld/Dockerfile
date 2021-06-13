FROM python:3.8
LABEL maintainer="Willy Aguirre"

WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

# command to run on container start
CMD [ "python", "app.py" ]

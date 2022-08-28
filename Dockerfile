FROM python:3.9

WORKDIR /usr/src/app
COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install psycopg2-binary

EXPOSE 8000
EXPOSE 5000
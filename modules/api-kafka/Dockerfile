FROM python:3.7-alpine

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev bash
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD [ "./wait-for-it.sh", "kafka1:9091", "--", "python", "./main.py" ]
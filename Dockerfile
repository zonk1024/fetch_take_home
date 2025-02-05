# syntax=docker/dockerfile:1

FROM python:3.13

WORKDIR /code

COPY requirements.txt /code/

EXPOSE 8000

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["fastapi", "run", "app.py"]

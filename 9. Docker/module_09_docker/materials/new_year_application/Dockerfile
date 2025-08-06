FROM python:3.12-slim

COPY static/ /app/static/
COPY templates/ /app/templates/

COPY requirements.txt /app/

RUN python -m pip install -r /app/requirements.txt

COPY app.py /app

WORKDIR /app

ENTRYPOINT ["python", "app.py"]

FROM python:3.10-alpine

COPY main.py /app/main.py

CMD ["python", "/app/main.py"]

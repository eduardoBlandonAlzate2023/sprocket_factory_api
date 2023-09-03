FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN useradd appuser && chown -R appuser /app
USER appuser

COPY . .

CMD ["python", "run.py"]

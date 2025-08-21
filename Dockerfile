FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app/app
COPY ./data /app/data

EXPOSE 8511

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8511"]
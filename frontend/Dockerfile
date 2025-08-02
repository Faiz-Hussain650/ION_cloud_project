FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

ENV DB_HOST=postgres
ENV DB_NAME=hello_db
ENV DB_USER=hello_user
ENV DB_PASS=hello_pass

EXPOSE 5000
CMD ["python", "app.py"]

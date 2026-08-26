FROM python:3.8-slim-buster

WORKDIR /home/myapp

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip setuptools>=78.1.1 && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5050

CMD ["python3", "sample_app.py"]
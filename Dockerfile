FROM python:3.13

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir graphviz && \
    apt-get update && apt-get install -y graphviz && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

CMD ["python", "main.py"]

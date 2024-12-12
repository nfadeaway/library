FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential libpq-dev curl && \
    apt-get clean

RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g yarn

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN yarn --cwd /app/frontend install

ENTRYPOINT ["/app/entrypoint.sh"]

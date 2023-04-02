FROM python:3.10.10-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y ffmpeg git curl && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install "git+https://github.com/openai/whisper.git" 

COPY . .

ENV PORT 8080
ENV PYTHONUNBUFFERED 1

EXPOSE 8080

CMD uvicorn main:app --host 0.0.0.0 --port $PORT



FROM python:3.10.6-alpine3.16

RUN apk --update add git less openssh && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/* && \
    mkdir code

WORKDIR /code

CMD ["sh", "-c", "git clone https://github.com/tiwx2/flask-backend-aws.git . && pip install -r requirements.txt && python3 app.py"]

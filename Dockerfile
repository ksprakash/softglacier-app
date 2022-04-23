FROM python:latest
LABEL project=softglacier Name=Sai
WORKDIR /usr/src/app
COPY .  .
RUN apt update -y && \
    apt install jq -y && \
    pip install --no-cache-dir  -r requirements.txt

ARG version=`cat version.json | jq .version`

EXPOSE 3000

CMD [ "python", "app.py"]
     

FROM python:3
ENV NEW_RELIC_LICENSE_KEY=""
ENV NEW_RELIC_APP_NAME=TREINAMENTO-NR
ENV NEW_RELIC_DISTRIBUTED_TRACING_ENABLED=true
ENV NEW_RELIC_LOG_LEVEL=info
WORKDIR /app

COPY . .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["newrelic-admin", "run-program"]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

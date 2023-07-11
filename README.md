# treinamento-newrelic

## Set variable
In Dockerfile set the variable value. The KEY, you will find in you newrelic account.
```
NEW_RELIC_LICENSE_KEY=<KEY>
```

## Build
```
docker build -t treinamento .
``` 

## Run
```
docker run -p 80:5000 --name treinamento treinamento .
``` 

## Acess
```
http://localhost
```
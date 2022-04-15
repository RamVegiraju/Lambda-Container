# Lambda-Container
Example of creating a Lambda container image

## Steps

```
docker build -t image-name .

docker run -p 9000:8080 image-name

curl --request POST \
  --url http://localhost:8080/2015-03-31/functions/function/invocations \
  --header 'Content-Type: application/json' \
  --data '{"Input": 4}'
```

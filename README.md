# Lambda-Container
Example of creating a Lambda container image

## [Blog](https://medium.com/towards-data-science/building-aws-lambda-container-images-5c4a9a15e8a2)

## Steps

```
docker build -t image-name .

docker run -p 9000:8080 image-name

curl --request POST \
  --url http://localhost:9000/2015-03-31/functions/function/invocations \
  --header 'Content-Type: application/json' \
  --data '{"Input": 4}'
```

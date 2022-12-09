## Generating gRPC files
`pip install grpcio-tools`

`python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ location.proto`


export DB_USERNAME=postgres
export DB_PASSWORD=123456
export DB_HOST=127.0.0.1
export DB_PORT=5432
export DB_NAME=postgres
export KAFKA_SERVER=localhost:9091
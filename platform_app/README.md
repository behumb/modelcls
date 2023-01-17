# platform App

A docker compose service "platform_queues" run a script, that read images from `platform/images_files` directory and send load result to rabbitmq queues. Also it's consume requests from modelclsApp and save received data in `platform_app/db/sql_app.db`.

Script params should be placed in `.env` file (can be specified in docker-compose config) or in `docker-compose.yaml` directly.

```lombok.config
RABBITMQ_USER=admin
RABBITMQ_PASSWORD=pass
RABBITMQ_HOST=rabbitmqServer
RABBITMQ_PORT=5672

RABBITMQ_CONSUME_QUEUE=to_ai
RABBITMQ_PRODUCE_QUEUE=from_ai
```


## Docker

```
cd existing_repo
docker-compose up
```



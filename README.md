# CS165 Project

## To run

Create a `.env` file from the `.env.example` file, and edit as needed.

```
docker-compose up
```

## To setup database

```
docker exec cs165_web_1 flask db init
```

## Migrate database

```
docker exec cs165_web_1 flask db migrate -m "migration message"
docker exec cs165_web_1 flask db upgrade
```
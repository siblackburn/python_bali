Docker
======

## Commands

### Build all containers

```bash
docker-compose -f docker/docker-compose-dev.yml build
```

### Bring all containers up
```bash
docker-compose -f docker/docker-compose-dev.yml up
```

### Bring all containers up in the background
```bash
docker-compose -f docker/docker-compose-dev.yml up -d
```

### Bring all containers down
```bash
docker-compose -f docker/docker-compose-dev.yml down
```

### Print all running containers

```bash
docker ps
```

### Look at the logs of a container
```bash
docker logs docker_my_simple_flask_app_1 -f
```

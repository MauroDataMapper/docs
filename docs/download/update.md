To update your **Mauro Data Mapper** to a newer version:

1. Pull a new docker container to run
2. Stop the container that is running
3. Start up the new container (using the same start up parameters used to start it before)

This can be done through Docker Desktop or from the command line.

## From the command line
### Pull new docker container
```bash
--8<-- "docs/download/docker-pull.md"
```

### Stop container

List the containers:
```bash
docker ps
```

Stop the **Mauro Data Mapper** container with:
```bash
docker stop <CONTAINER ID>
```

### Start it up again
Using the new docker image, start the new container using exactly the same parameters that were used to start
the previous version.

E.g.
If you were running the container in the foreground, it would look similar to:
```bash
docker run --rm -it -p 8080:8080 \
  -v /my/docker/files/init:/opt/init:ro \
  -v /my/docker/files/data:/var/lib/postgresql/data \
  --8<-- "docs/download/docker-image.md"
```

Or in the background:
```bash
docker run --rm -d -p 8080:8080 \
  -v /my/docker/files/init:/opt/init:ro \
  -v /my/docker/files/data:/var/lib/postgresql/data \
  --8<-- "docs/download/docker-image.md"
```

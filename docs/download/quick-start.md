# Get started with **Mauro Data Mapper**

## Install Docker
Install [Docker](https://www.docker.com/get-started), or via your distro's package manager if you prefer.
## Pull the latest _Mauro Data Mapper_ image
```bash
--8<-- "docs/download/docker-pull.md"
```
## Create a folder/directory to persistent your data
```bash
cd ~
mkdir mdm_data
```
## Download some configuration
--8<-- "docs/download/docker-ready.md"

## Run it!

To run the container in the foreground, you can use:
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

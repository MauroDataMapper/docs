#### Foreground
To run the container in the foreground, you can use:
```bash
docker run --rm -it -p 8080:8080 \
  -v /my/docker/files/init:/opt/init:ro \
  -v /my/docker/files/data:/var/lib/postgresql/data \
  --8<-- "docs/download/docker-image.md"
```

| Part                                              | Meaning                                                                                                                                                                                              | 
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| docker run                                        | The docker command                                                                                                                                                                                   |
| --rm                                              | Remove the container when it stops                                                                                                                                                                   | 
| -it                                               | You can use CTRL-C to exit the container from the command line, and see the start-up trace<br/>-i means --interactive Keep STDIN open even if not attached<br/> -t means --tty Allocate a pseudo-TTY | 
| -p 8080:8080                                      | Publish to the host's port 8080 from the container's port 8080                                                                                                                                       | 
| -v /my/docker/files/init:/opt/init:ro             | Create a mount from:<br/>/my/docker/files/init<br/> that surfaces at:<br/>/opt/init<br/> in the container, in read-only mode (ro)                                                                    | 
| -v /my/docker/files/data:/var/lib/postgresql/data | Create a mount from:<br/>/my/docker/files/data<br/> that surfaces at:<br/>/var/lib/postgresql/data in the container                                                                                  | 
| --8<-- "docs/download/docker-image.md"            | The image to run                                                                                                                                                                                     |

#### Background
To run the container in the background, you can use:
```bash
docker run --rm -d -p 8080:8080 \
  -v /my/docker/files/init:/opt/init:ro \
  -v /my/docker/files/data:/var/lib/postgresql/data \
  --8<-- "docs/download/docker-image.md"
```

| Part | Meaning                                                     |
|------|-------------------------------------------------------------|
| -d   | --detach Run container in background and print container ID |

You can see it running in docker:
```bash
docker ps
```

And stop it with:
```bash
docker stop <CONTAINER ID>
```

## System requirements

The simplest installation method is to run our preconfigured application using [Docker](https://www.docker.com).  
Any operating system, on a server or desktop, running **Docker** can run **Mauro Data Mapper**, but please note that some organisations may restrict
the use of
**Docker** on virtual machines.

We advise a minimum of 2 CPUs and 4GBs RAM just to run this system this does not allow for the requirements to have an operating system running as
well. Therefore we recommend a 4 CPU and 8GB RAM server.

The default install of Docker inside Linux configures the docker engine with unlimited access to the server's resources, however if running in Windows
or Mac OS X the Docker Toolbox will need to be configured

---

## Installing Docker and Docker Compose

You will need to install [Docker](https://www.docker.com/get-started) and [Docker Compose](https://github.com/docker/compose).  **Docker Compose** is
included as part of the standard **'Docker Desktop'** for Windows and MacOS.

To run **Mauro Data Mapper**, the minimum versions are as follows:

* **Docker Engine:** 19.03.8
* **Docker Compose:** 1.25.5

!!! Warning If you're running on Ubuntu the default version of `docker-compose` installed with apt-get is currently 1.17.1, and you might get the
error message:
```
Building docker compose ERROR: Need service name for --build-arg option
```
In this case, you should uninstall `docker-compose` and re-install directly from Docker, following
[the instructions here](https://docs.docker.com/compose/install/).

---

## Docker Machine configuration

The default `docker-machine` in a Windows or Mac OS X environment is configured to make use of one CPU and 1GB RAM. This is not enough RAM to reliably
run the **Mauro Data Mapper** system and so should be increased.

On Linux the docker machine is the host machine so there is no need to build or remove anything.

### Native Docker

If using the **Native Docker** then edit the preferences of the **Docker** application and increase the RAM to at least 4GB. You will probably need to
restart **Docker** after doing this.

### Docker Toolbox

If using the **Docker Toolbox** then you will need to perform the following in a **'docker'** terminal:

```bash
# Stop the default docker machine
$ docker-machine stop default

# Remove the default machine
$ docker-machine rm default

# Replace with a more powerful machine (4096 is the minimum recommended RAM, if you can give it more then do so)
$ docker-machine create --driver virtualbox --virtualbox-cpu-count "-1" --virtualbox-memory "4096" default
```

### Use the default Docker Machine

When controlling using **Docker Machine** via your terminal shell it is useful to set the `default` docker machine. Type the following at the command
line, or add it to the appropriate bash profile file:

```bash
eval "$(docker-machine env default)"
```

If not you may see the following error:

`Cannot connect to the Docker daemon. Is the docker daemon running on this host?`

---

For more information about administration of your running Docker instance, please see the [Administration guide](../administration)



<!--  LocalWords:  maurodatamapper Postgres postgres arg mdm ui args
 -->
<!--  LocalWords:  yml mauro Backend Plugins plugins runtimeOnly FQ
 -->
<!--  LocalWords:  gradle keycloak plugin thats Dockerfile FQDN url
 -->
<!--  LocalWords:  PGPASSWORD TRANSPORTSTRATEGY lucene EMAILSERVICE
 -->
<!--  LocalWords:  CORS emailservice mc 1GB 4GB rm virtualbox cpu env
 -->
<!--  LocalWords:  eval ps rmi grep qf rmv Dockviz dockviz nate deps
 -->
<!--  LocalWords:  Kitematic Bintray apk postgresql ENTRYPOINT CMD
 -->
<!--  LocalWords:  arg1 LabKey
 -->

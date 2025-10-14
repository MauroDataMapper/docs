
The simplest installation method is to run our preconfigured application using [Docker](https://www.docker.com).  
Any operating system, on a server or desktop, running **Docker** can run **Mauro Data Mapper**, but please note that
some organisations may restrict the use of **Docker** on virtual machines.

If you are using a desktop environment, it is handy to install [Docker Desktop](https://docs.docker.com/desktop/).

## Images

--8<-- "docs/download/docker-table.md"

To pull in a docker image, in your terminal run the corresponding 'pull command' from the above table for the image you wish to use.
Or use the Images tab in Docker Desktop to pull it from Hub repositories.

### System requirements
You will need to install [Docker](https://www.docker.com/get-started).

We advise running these docker images on an operating system with a minimum of 4 CPUs and 8GBs RAM with:

* **Docker Engine:** 20.10.21 or higher

## Docker configuration

### Linux
The default install of Docker inside Linux configures the Docker Engine with unlimited access to the server's resources.

### Windows / macOS
On Windows or macOS the Docker Toolbox may need to be configured further: the _default_ `docker-machine`
on a Windows or macOS environment may be initially configured to use less CPU and RAM
than is required to reliably run the **Mauro Data Mapper** system, so these should be increased accordingly. 

### Docker Desktop
On Docker Desktop, go to the Settings (a cog icon), then the resources,
and set the CPU limit to be at least 4 and the Memory limit to be at least 8GB. Press 'Apply & restart'

### Native Docker

If using the **Native Docker** then edit the preferences of the **Docker** application and increase the RAM to at
least 4GB and 4CPU cores.

You will probably need to restart **Docker** after doing this.

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

When controlling using **Docker Machine** via your terminal shell it is useful to set the `default` docker machine.
Type the following at the command line, or add it to the appropriate bash profile file:

```bash
eval "$(docker-machine env default)"
```

If not you may see the following error:

`Cannot connect to the Docker daemon. Is the docker daemon running on this host?`

---


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

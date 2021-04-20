
## System requirements

The simplest installation method is to run our preconfigured application using [Docker](https://www.docker.com).  Any operating 
system - server or desktop - running Docker can run the Mauro Data Mapper, but please note that some organisations may restrict the use of 
Docker on virtual machines.


## Installing Docker and Docker Compose

You will need to install [Docker](https://www.docker.com/get-started), and [Docker Compose](https://github.com/docker/compose).  Docker Compose is 
included as part of the standard 'Docker Desktop' for Windows and MacOS.

To run Mauro, the minimum versions are as follows:

* **Docker Engine:** 19.03.8
* **Docker Compose:** 1.25.5

!!! Warning
    **If you're running on Ubuntu** the default version of `docker-compose` installed with apt-get is currently 1.17.1, and you might get the error 
    message:
    ```
    Building docker compose
    ERROR: Need service name for --build-arg option
    ```
    In this case, you should uninstall `docker-compose` and re-install directly from Docker, following 
    [the instructions here](https://docs.docker.com/compose/install/).

---

## Docker Machine configuration

The default `docker-machine` in a Windows or Mac OS X environment is configured to make use of one CPU and 1GB RAM: this is not enough RAM to 
reliably run the Mauro Data Mapper system, and so should be increased.

On Linux the docker machine is the host machine so there is no need to build or remove anything.

### Native Docker

If using the Native Docker then edit the preferences of the Docker application and increase the RAM to at least 4GB,
you will probably need to restart Docker after doing this.

### Docker Toolbox

If using the Docker Toolbox then as such you will need to perform the following in a 'docker' terminal.

```bash
# Stop the default docker machine
$ docker-machine stop default

# Remove the default machine
$ docker-machine rm default

# Replace with a more powerful machine (4096 is the minimum recommended RAM, if you can give it more then do so)
$ docker-machine create --driver virtualbox --virtualbox-cpu-count "-1" --virtualbox-memory "4096" default
```

### Use the default Docker Machine

When controlling using Docker Machine via your terminal shell it is useful to set the `default` docker machine.
Type the following at the command line, or add it to the appropriate bash profile file:

```bash
eval "$(docker-machine env default)"
```

If not you may see the following error: `Cannot connect to the Docker daemon. Is the docker daemon running on this host?`

## Git repository

The Mauro Docker configuration repository can be found here: 
[https://github.com/MauroDataMapper/mdm-docker](https://github.com/MauroDataMapper/mdm-docker).  Different branches provide different 
configurations: we recommend checking out the `main` branch which will provide the latest releases of back-end and front-end.  Alternatively, you 
can check out a specific tag to install a specific front-end / back-end combination: tagged releases of Docker take the form `Ba.b.c_Fx.y.z` where 
`a.b.c` is the tagged version of the back-end, and `x.y.z` is the tagged version of the front-end.  You can also check out 


!!! Information
    If you're running on an internal server with SSH access forbidden by a firewall, you can use the following link to access the repository via 
    HTTPS: [SSH over HTTPS document](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/using-ssh-over-the-https-port).

## Overview

The Docker Compose configuration defines two interacting containers: 

* Postgres 12 [`postgres`] - Postgres Database
* Mauro Data Mapper [`maurodatamapper`] - Mauro Data Mapper

The first of these is a standard Postgres container with an external volume for persistent storage.  The second builds on the standard Apache 
Tomcat container, which hosts built versions of the Mauro application.  The Postgres container must be running whenever the Mauro application 
starts.  The Mauro container persists logs, and Lucene indexes, to shared folders which can be found in the docker repository folder. 

## Building

At present, the Mauro application must be checked out, compiled, and deployed within the Mauro / Tomcat container.  Some shell scripts have been 
provided to run this process on a `*nix` system, and are described below.  We plan to streamline this process in the very near future.   

### Make / Update

```bash
# Build the entire system
./make

Usage ./make [-b COMMIT_BRANCH] [-f COMMIT_BRANCH]

-b, --back-end COMMIT_BRANCH    : The commit or branch to checkout and build for the back-end from mdm-core.
-f, --front-end COMMIT_BRANCH   : The commit or branch to checkout and build for the front-end from mdm-ui
```

The `make` command will build all the necessary base images and then perform a `docker-compose build` to complete the build.  It is preconfigured 
within each branch of the Mauro Docker repository, so the `-b` and `-f` options only need specifying if you wish to configure a different build 
configuration.

This script runs the following:

* build an updated OS version of tomcat which is where the application will run - `mdm/tomcat:9.0.27-jdk12-adoptopenjdk-openj9`
* build the base SDK image for building the application in - `mdm/sdk_base:grails-4.0.6-adoptopenjdk-12-jdk-openj9`
* build an initial image with the code checked out and dependencies installed - `mdm/mdm_base:develop`

Once these 3 images are built the main `docker-compose` service will be able to build without the use of the `make` file.

An update script runs a similar process, but can be used to update to a different version of the back-end / front-end.

```bash
# Update an already built system
./update

Usage ./update [-b COMMIT_BRANCH] [-f COMMIT_BRANCH]

-b, --back-end COMMIT_BRANCH    : The commit or branch to checkout and build for the back-end from mdm-core.
-f, --front-end COMMIT_BRANCH   : The commit or branch to checkout and build for the front-end from mdm-ui
```

Once the `./make` script has been run once the commit/branch choice can be altered by changing the build args in the `docker-compose.yml` file.

```yml
mauro-data-mapper:
    build:
        context: mauro-data-mapper
        args:
            MDM_APPLICATION_COMMIT: develop
            MDM_UI_COMMIT: develop
            ...
```

### Additional Backend Plugins

Additional plugins can be found at the [Mauro Data Mapper Plugins](https://github.com/MauroDataMapper-Plugins) organisation page.
Each of these can be added as dependencies by adding them to the `ADDITIONAL_PLUGINS` build argument within the `docker-compose.yml` file.  These 
dependencies should be provided in a semi-colon separated list in the gradle style, they will be split and each will be added as a `runtimeOnly`
dependency.

Example
```yml
 mauro-data-mapper:
        build:
            context: mauro-data-mapper
            args:
                ADDITIONAL_PLUGINS: "uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-authentication-keycloak:1.0.1"
```

Will add the keycloak plugin to the `dependencies.gradle` file:
```gradle
runtimeOnly uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-authentication-keycloak:1.0.1
```

### Running Multiple Instances

If running multiple docker-compose instances then they will all make use of the same initial images, therefore you only need to run the `./make` 
script once per server.

### SSH Firewalled Servers

Some servers have the 22 SSH port firewalled for external connections.
If this is the case you can change the `base_images/sdk_base/ssh/config` file,

* comment out the `Hostname` field that's currently active
* uncomment both commented out `Hostname` and `Port` fields, this will allow git to work using the 443 port which will not be blocked.

---

## Run Environment

Please see `mauro-data-mapper/Dockerfile` for all defaults

### Required to be overridden

The following variables need to be overridden/set when starting up a new mauro-data-mapper image.
Usually this is done in the docker-compose.yml file. It should not be done in the Dockerfile as each instance which starts up may use different
values.

* `MDM_FQ_HOSTNAME` - The fully-qualified domain name (FQDN) of the server where the catalogue will be accessed
* `MDM_PORT` - The port used to access the catalogue
* `MDM_AUTHORITY_URL` - The full URL to the location of the catalogue. This is considered a unique identifier to distinguish any instance from
  another and therefore no 2 instances should use the same URL.
* `MDM_AUTHORITY_NAME` - A unique name used to distinguish a running MDM instance and boostrap an initial Mauro *Authority*
* `PGPASSWORD` - This should be the password for the postgres instance being connected. When using the `docker-compose.yml` file and the configured
  postgres instance this should be left alone.
* `EMAIL_USERNAME` - To allow the catalogue to send emails this needs to be a valid username for the `EMAIL_HOST`
* `EMAIL_PASSWORD` - To allow the catalogue to send emails this needs to be a valid password for the `EMAIL_HOST` and `EMAIL_USERNAME`
* `EMAIL_HOST` - This is the FQDN of the mail server to use when sending emails

### Optional

* `CATALINA_OPTS` - Java options to be passed to the Tomcat application server
* `DATABASE_HOST` - The host of the database. If using docker-compose this should be left as `postgres` or changed to the name of the database service
* `DATABASE_PORT` - The port of the database
* `DATABASE_NAME` - The name of the database which the catalogue data will be stored in
* `DATABASE_USERNAME` - Username to use to connect to the database
* `DATABASE_PASSWORD` - Password to use to connect to the database
* `EMAIL_PORT` - The port to use when sending emails
* `EMAIL_TRANSPORTSTRATEGY` - The transport strategy to use when sending emails
* `SEARCH_INDEX_BASE` - The directory to store the lucene index files in
* `EMAILSERVICE_URL` - The url to the special email service, this will result in the alternative email system being used
* `EMAILSERVICE_USERNAME` - The username for the email service needs to be valid for `EMAIL_SERVICE_URL`
* `EMAILSERVICE_PASSWORD` - The password for the email service needs to be valid for `EMAIL_SERVICE_URL`

### Environment Notes

**Database**
:   The system is designed to use the postgres service provided in the docker-compose file, therefore there should be no need to alter any of
    these settings. Only make alterations if running postgres as a separate service outside docker-compose.

**MDM_FQ_HOSTNAME** & **MDM_PORT**
:   The provided values will be used to define the CORS allowed origins. The port will be used to define http or https
    (443), if its not 80 or 443 then it will be added to the url generated. The host must be the host used in the web url when accessing the catalogue
    in a web browser.

**Email** 
:   The standard email properties will allow emails to be sent to a specific SMTP server. The `emailservice` properties override this and
    send the email to the specified email service which will then forward it onto our email SMTP server.

---

## Docker Reference

## Running

Before running please read the [parameters](#run-environment) section first.

With `docker` and `docker-compose` installed, run the following:

```bash
# Build all the images
$ docker-compose-dev build

# Start all the components up
$ docker-compose up -d

# To only start 1 service
# This will also start up any of the services the named service depends on (defined by `links` or `depends_on`)
$ docker-compose up [SERVICE]

# To push all the output to the background add `-d`
$ docker-compose up -d [SERVICE]

# Stop background running and remove the containers
$ docker-compose down

# To update an already running service
$ docker-compose-dev build [SERVICE]
$ docker-compose up -d --no-deps [SERVICE]

# To run in production mode
$ docker-compose-prod up -d [SERVICE]
```

If you run everything in the background use `Kitematic` to see the individual container logs.
You can do this if running in the foreground and its easier as it splits each of the containers up.

If only starting a service when you stop the service docker will *not* stop the dependencies that were started to allow the named service to start.

The default compose file will pull the correct version images from Bintray, or a locally defined docker repository.

---

For more information about administration of your running Docker instance, 



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

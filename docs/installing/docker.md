!!! Information

	 See the [Docker Setup](./docker-setup) section before installing Mauro using Docker.


## Git repository

Depending on the operating system of the server you are running on, you may first need to install `git` to checkout the Mauro application.  You 
can read more about installing `git` on different operating systems here: [Getting Started - Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

The **Mauro Docker** configuration repository can be found here: 
[https://github.com/MauroDataMapper/mdm-docker](https://github.com/MauroDataMapper/mdm-docker).  Where you clone it is up to you, but on a *nix 
system we recommend cloning into `/opt/` (for optional software packages)


Different branches provide different configurations. We recommend checking out the `main` branch which will provide the latest releases of back-end 
and front-end.  Alternatively, you can check out a specific tag to install a specific front-end / back-end combination. Tagged releases of 
**Docker** take the form `Ba.b.c_Fx.y.z` where `a.b.c` is the tagged version of the back-end and `x.y.z` is the tagged version of the front-end.


!!! Information
    If you're running on an internal server with SSH access forbidden by a firewall, you can use the following link to access the repository via 
    HTTPS: [SSH over HTTPS document](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/using-ssh-over-the-https-port).
    
---

## Overview

The **Docker Compose** configuration defines two interacting containers: 

* Postgres 12 [`postgres`] - Postgres Database
* Mauro Data Mapper [`maurodatamapper`] - Mauro Data Mapper

The first of these is a standard **Postgres** container with an external volume for persistent storage.  The second builds on the standard **Apache 
Tomcat** container, which hosts built versions of the **Mauro** application.  The **Postgres** container must be running whenever the **Mauro** application 
starts.  The **Mauro** container persists logs and Lucene indexes to shared folders which can be found in the docker repository folder. 

### Default username / password

The docker installation is empty on initialisation - it comes with one pre-configured user: with the username `admin@maurodatamapper.com` and the
password `password`.  We *strongly recommend* changing this password on first login, and then setting up personal user accounts for individual users.

---

## Building

Once cloned then running the standard docker-compose build command will build the images necessary to run the services.

```bash
# Build the entire system
$ ./docker-compose build
```
### Additional Backend Plugins

Additional plugins can be found at the [Mauro Data Mapper Plugins](https://github.com/MauroDataMapper-Plugins) organisation page. A complete list with
versions can also be found in the [installation documentation](https://maurodatamapper.github.io/installing/plugins/)
please note that while we will do our best to keep this page up-to-date there may be circumstances where it is behind, therefore we recommend using
our official GitHub Plugins organisation to find the latest releases and all available plugins.

Each of these can be added as `runtimeOnly` dependencies by adding them to the `ADDITIONAL_PLUGINS` build argument for the `mauro-data-mapper`
service build.

These dependencies should be provided in a semi-colon separated list in the gradle style, they will be split and each will be added as a `runtimeOnly`
dependency.

Example

```yaml
 mauro-data-mapper:
   build:
     context: mauro-data-mapper
     args:
       ADDITIONAL_PLUGINS: "uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-excel:3.0.0"
```

Will add the Excel plugin to the `dependencies.gradle` file:

```gradle
runtimeOnly uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-excel:3.0.0
```

#### Dynamic Versions

You can use [dynamic versioning](https://docs.gradle.org/current/userguide/single_versions.html) to add dependencies, however this comes with a risk
that it pulls a version which does not comply with your expected version of mdm-application-build/mdm-core which may cause conflicts with other
plugins, therefore we do **not** advise this approach.

Example

```yaml
 mauro-data-mapper:
   build:
     context: mauro-data-mapper
     args:
       ADDITIONAL_PLUGINS: "uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-excel:3.+"
```

This will add the latest minor version of the Excel plugin.


### Theme

Mauro comes with a default user interface theme - with the standard blue branding, and default text on the home page.  This can be overridden in 
the `docker-compose.yml` file, with instructions provided in the [Branding guide](../installing/branding/branding).  The default theme is called 
`default` and can be set with:

```yaml
 MDM_UI_THEME_NAME: "default"
```


### Running multiple instances

If running multiple docker-compose instances then they will all make use of the same initial images, therefore you only need to run the `./make` 
script once per server.

### SSH firewalled servers

Some servers have the 22 SSH port firewalled for external connections.
If this is the case you can change the `base_images/sdk_base/ssh/config` file:

* Comment out the `Hostname` field that's currently active
* Uncomment both commented out `Hostname` and `Port` fields, this will allow git to work using the 443 port which will not be blocked

---

## Run environment

By adding variables to the `<service>.environment` section of the docker-compose.yml file you can pass them into the container as environment variables. These will override
any existing configuration variables which are used by default. Any defaults and normally used environment variables can be found in the relevant service's Dockerfile at
the `ENV` command.

### postgres service

* `POSTGRES_PASSWORD` 

	This sets the postgres user password for the service, as per the documentation at [Postgres Docker Hub](https://hub.docker.com/_/postgres), 
	t must be set for a docker postgres container. We have set a default but you can override if desired. 
	If you do override it, you will also need to change the `PGPASSWORD` env variable in the mauro-data-mapper section.
	
* `DATABASE_USERNAME` 

	This is the username which will be created inside the Postgres instance to own the database which the MDM service will use. 
	The username is also used by the MDM service to connect to the postgres instance, 
	therefore if you change this you *MUST* also supply it in the environment args for the MDM service
	
* `DATABASE_PASSWORD`

  This is the password set for the `DATABASE_USERNAME`. It is the password used by the MDM service to connect to this postgres container.

### mauro-data-mapper service

There is a huge amount of variables which either need to be set or can be overridden depending on what plugins have been installed and what features
you want. Therefore you can find all the information on configuring MDM [here](../configuring/overview).

There are 2 environment variables which are not used directly by MDM and these are both optional to be overridden in the compose file.

* `PGPASSWORD`

  This is the postgres user's password for the postgres server. This is an environment variable set to allow the MDM service to wait till the postgres
  service has completely finished starting up. It is only used to confirm the Postgres server is running and databases exist. After this it is not
  used again.
  **If you change `POSTGRES_PASSWORD` you must change this to match**
  **This can ONLY be overridden in the docker-compose.yml file**

* `CATALINA_OPTS`

  Java Opts to be passed to Tomcat **This can ONLY be overridden in the docker-compose.yml file**

### Environment Notes

#### Database

The system is designed to use the postgres service provided in the docker-compose file, therefore there should be no need to alter any of these
settings. Only make alterations if running postgres as a separate service outside of docker-compose.

#### Email

The standard email properties will allow emails to be sent to a specific SMTP server.

---

## Docker Reference

### Running

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

If only starting a service when you stop, the service docker will **not** stop the dependencies that were started to allow the named service to start.

The default compose file will pull the correct version images from Bintray, or a locally defined docker repository.

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

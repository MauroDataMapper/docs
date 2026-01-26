There are 3 variations of changing the database which may be considered:

* Using the postgres service but using different database name, username and/or password.
* Using an external database server/service outside of the docker-compose network.

!!! Information
    
    We cannot recommend using a databasing system other than postgreSQL as we have custom SQL inside the API which uses postgres specific features. 

!!! Warning

    The postgres user which MDM uses to connect **must** be a postgres superuser. This is because we enable and disable foreign keys during major deletes to allow
    the deletions to happen in a reasonble time.

## Changing the postgres service variables

The following properties can be altered inside the postgres service. Any properties which can be defined at runtime can be set in the `docker-compose.yml` `environment` block. There is a fixtures file which is run when the container first starts up, and **only** when it is first started. Once the container has been started and the postgres volume exists, then the fixtures file will **not** be run again. If you wish to change or rebuild, then you will need to remove the docker volume for the postgres service.

`POSTGRES_PASSWORD`
: This is the password for the postgres user. Changing this password requires you to change the `PGPASSWORD` in the mauro-data-mapper environment.

`DATABASE_NAME`
: This is the name of the database which will be created for the provided username/password.
This can be defined at runtime and will be the database which all the MDM data will be stored into, the database will be created when the postgres container first starts.

`DATABASE_USERNAME`
: This is the username for the user the MDM service will use to talk to the postgres service. 
This can be defined at runtime and will be created as a superuser. 

`DATABASE_PASSWORD`
: This is the password set for the given username.
This can be defined at runtime.

Changing the above 3 database properties will require the following environment block variables to be set for MDM to set the following 3 properties, 
these will override and set the grails `yml` property defined removing the need for you to set it in the `build.yml` or `runtime.yml` files.

| postgres property | mdm property | grails property |
|---|---|---|
| `DATABASE_NAME` | `DATABASE_NAME` | `database.name` |
| `DATABASE_USERNAME` | `DATASOURCE_USERNAME` | `dataSource.username` | 
| `DATABASE_PASSWORD` | `DATASOURCE_PASSWORD` | `dataSource.password` |


## Using an external postgres service

!!! Information

    An example of this might be when using Amazon Web Services (AWS) to provide the database hosting solution.

If using this option we recommend commenting out or deleting the postgres service from the `docker-compose.yml` file to avoid any confusion.
You will also need to remove the following block from the MDM service, as this section tells the MDM service to wait till the postgres service is running
and adds a network link between the 2 containers.

```yaml
depends_on:
    - postgres
```

You will need to set the following properties in the `environments` block of the MDM service,
this will inform the service where to find postgres and to wait till it can talk to it before proceeding.
They will also provide the connection details required, any of the following properties set will override the stated grails yml properties (the property name in brackets),
so you should not set them in the `build.yml` or `runtime.yml` file as the environment properties will override whatever is there.

`DATABASE_HOST` (`database.host`)
: This is the full hostname or IP address of the server running the postgres service.

`DATABASE_POST` (`database.port`)
: This is the port of the server which postgres can be found at.

`DATABASE_NAME` (`database.name`)
: This is the name of the database which all the MDM data will be stored into.

`DATASOURCE_USERNAME` (`dataSource.username`)
: This is the username for the user the MDM service will use to talk to the postgres database.

`DATABASE_PASSWORD` (`dataSource.password`)
: This is the password set for the given username.


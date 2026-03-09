An installation of **Mauro Data Mapper** holds three (3) components:

1. *Micronaut backend* with REST API
2. *Web-based frontend* user interface
3. *Postgres database* to hold the data models

## The all-in-one docker image
The all-in-one docker image holds all three components for simplicity, and it will run without further configuration.

However, to be able to use Mauro, you will need to be able to:

1. sign in to the user interface or API, and
2. to persist the data held by the database whenever the container is stopped or restarted.

Some additional configuration is required.

For this purpose, these file mount points are available to access and persist the files used by the docker container:

| Internal mount point     | Purpose                      | Required?                            |
|--------------------------|------------------------------|--------------------------------------|
| /opt/init                | Holds start up configuration | <span style="color:green">Yes</span> |
| /var/lib/postgresql/data | Holds Postgres data          | <span style="color:green">Yes</span> |
| /var/logs                | Logs                         | No                                   |
| /database                | Holds database snapshots     | No                                   |

The configuration held under */opt/init* must be set up to sign in,
and */var/lib/postgresql/data* must be persisted for the data to survive restart.

To access the REST API and User Interface, this TCP port is available:

| Port  | Purpose                  |
|-------|--------------------------|
| 8080  | REST API, User interface |

When running the container, the docker run command should have port 8080 open to access the user interface
and the Mauro backend REST API service. 

### How the container starts up
On running the docker container:

1. The database is established, and any SQL are imported.
2. Micronaut plugins and configuration are installed, and micronaut is started.

#### Postgres data
*/var/lib/postgresql/data* is where Postgres will find and hold the **Mauro Data Mapper** data models.

At start-up */var/lib/postgresql/data* will be checked for any existing Postgres database files.
If none are found, the database will be initialised and an empty database will be created and stored there.

#### Configure
*/opt/init* is scanned for configuration files, scripts, plugins, and other resources.

Under */opt/init* there are two sub-directories involved in start-up:

<pre>
/opt/init/
    | - postgres/
    | - micronaut/
</pre>

| Sub&#160;directory | Start up actions                                                                                                                                                                                                                |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| postgres/          | *.sh* shell scripts will be run<br/>*.sql* will be run by Postgres                                                                                                                                                              |
| micronaut/         | *.sh* shell scripts will be run<br/>*.jar* Java ARchive files set up as Mauro plugins<br/>_application-\*.yml_ installed as Micronaut's configuration<br/>*all other files* will be copied to Micronaut's *resources/* directory. |

#### postgres/
Once the database has been established, */opt/init/postgres* is processed,
and any SQL (if present) will be imported.
<pre>
/opt/init/
    | - postgres/
        | - my_import_data.sql
</pre>

#### micronaut/
When the database configuration has finished, */opt/init/micronaut/* is processed:

* **Mauro** plug-ins (these are *.jar* files)
* Micronaut configuration files such as: *application-mauro.yml*, *application-datasources.yml*

<pre>
/opt/init/
    | - postgres/
    | - micronaut/
        | - application-mauro.yml
        | - yourFavouritePlugin.jar
</pre>

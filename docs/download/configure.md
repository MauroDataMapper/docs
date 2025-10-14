An installation of **Mauro Data Mapper** has three (3) components:

1. *Micronaut backend* with REST API
2. *Web-based frontend* user interface
3. *Postgres database* to hold the data models

## The all-in-one docker image
The all-in-one docker image holds all three components for simplicity, and it will run without further configuration.
However, to be able to use Mauro, you will need to be able to (1) sign in
to the user interface, and (2) to persist the data held by the database when the container is restarted. For these
the creation of three folders/directories and one file is required.

This kind of container exposes these mount points:

| Mount point              | Purpose                     | Required |
|--------------------------|-----------------------------|----------|
| /opt/init                | Start up with configuration | Yes      |
| /var/lib/postgresql/data | Persists Postgres data      | Yes      |
| /var/logs                | Logging                     | No       |
| /database                | Database snapshots          | No       |

which can be used to access, and persist files used by the docker container.
Of these */opt/init* and */var/lib/postgresql/data* are essential for use.

And these TCP ports:

| Port  | Purpose                  |
|-------|--------------------------|
| 8080  | REST API, User interface |
| 5432  | Postgres database        |

which can be used to access the user interface and also the REST API (8080), and the Postgres database (5432) .

### Start-up

#### Configuration
As the docker container starts up the components, it will look under */opt/init* for configuration files, scripts,
plugins, and other resources.

There are two sub-directories under */opt/init*:

<pre>
/opt/init/
    | - postgres/
    | - micronaut/
</pre>

| Sub&#160;directory | Start up actions                                                                                                                                                                                      |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| postgres/          | *.sh* scripts will be run<br/>*.sql* will be run in Postgres                                                                                                                                          |
| micronaut/         | *.sh* scripts will be run<br/>*.jar* files loaded as plugins<br/>*application.yml* installed as Micronaut's configuration<br/>*all other files* will be copied to Micronaut's *resources/* directory. |

Use /opt/init at start up to include any plugins as *.jar* files, and set your own version of *application.yml*

<pre>
/opt/init/
    | - postgres/
    | - micronaut/
        | - application.yml
        | - yourFavouritePlugin.jar
</pre>

#### Database
The start-up will also look under */var/lib/postgresql/data* for any existing Postgres database files.
If none are found, it will initialise the database in that directory and then process */opt/init/postgres*

<pre>
/opt/init/
        | - postgres/
        | - micronaut/
/var/lib/postgresql/data
    | - Many
    | - Files
    | - Written
    | - By
    | - Postgres
</pre>


#### Example start-up configuration and run

For example, create a directory tree for your docker container to use:

<pre>
/my/docker/files/
    | - data/
    | - init/
        | - micronaut/
            | - application.yml
</pre>

Where *data/* is going to be where the Postgres database files are kept, and *init/micronaut/* is where the
configuration *application.yml* is going to go.

Fill in *application.yml* with some configuration:

```yaml
micronaut:
  application:
    name: sandbox
    client:
      connect-timeout: 11s

  server:
    port: 8080
    max-request-size: 500mb
    multipart:
      max-file-size: 500mb
    cors:
      enabled: true
  router:
    static-resources:
      default:
        paths: classpath:public
        mapping: /**
        enabled: true
      swagger:
        paths: classpath:META-INF/swagger
        mapping: /swagger/**
      swagger-ui:
        paths: classpath:META-INF/swagger/views/swagger-ui
        mapping: /swagger-ui/**
  security:
    enabled: true
    authentication: session
    redirect:
      enabled: false
    endpoints:
      login:
        enabled: true
        path: '/api/authentication/login'
      logout:
        enabled: true
        path: '/api/authentication/logout'
        get-allowed: true
      oauth:
        enabled: true
    reject-not-found: false
    authentication-provider-strategy: any

  caches:
    items-cache:
      initial-capacity: 10000
      maximum-weight: 1_000_000_000
      expire-after-write: 1h
      record-stats: true
    security-cache:
      initial-capacity: 10000
      maximum-weight: 1_000_000_000
      expire-after-write: 1h
      record-stats: true
    api-property-cache:
      initial-capacity: 1000
      maximum-weight: 1_000_000_000
      expire-after-write: 1h
      record-stats: true

endpoints:
  routes:
    enabled: true
    sensitive: true
  beans:
    enabled: true
    sensitive: true
  flyway:
    enabled: true
    sensitive: true
  caches:
    enabled: true
    sensitive: true

jackson:
  serialization:
    writeDatesAsTimestamps: false

datasources:
  default:
    url: jdbc:postgresql://localhost:5432/sandbox
    username: sandbox
    password: sandbox
    dialect: POSTGRES
    db-type: postgres
    driver-class-name: org.postgresql.Driver


javamail:
  authentication:
    username: $$username$$ # Replace me!
    password: $$password$$ # Replace me!
  properties:
    mail:
      smtp:
        port: 587 # Replace me!
        auth: true
        starttls:
          enable: true
        host: $$host$$ # Replace me!

mauro:
  federation:
    subscribed-catalogues.max: 50
  audit:
    scope: ALL
  users:
    -   email: admin@maurodatamapper.com
        first-name: admin
        last-name: admin
        temp-password: a_password
  groups:
    -   name: Administrators
        isAdmin: true
        members:
          - admin@maurodatamapper.com
  api-keys:
    -   name: My first API Key
        email: admin@maurodatamapper.com
        refreshable: true
        expiry: 2025-12-31
```

Pull a docker image (see [Docker images](./docker.md) for the list):

```bash
docker pull maurodatamapper/mauro:0.0.1-beta
```

Start a container with user interface port open and local directories mounted:

```bash
docker run --rm -p 8080:8080 -v /my/docker/files/init:/opt/init:ro -v /my/docker/files/data:/var/lib/postgresql/data -it maurodatamapper/mauro:0.0.1-beta
```

Visit http://<span/>yourhostname:8080/ in your browser.

The above *application.yml* has some *micronaut.mauro:* configuration for users, groups, and API keys.
Sign in with those credentials, in the above example that would be:

*admin@<span/>maurodatamapper.com*<br/>
*a_password*

### Bootstrapping users, groups and api keys

Before you can sign in to Mauro, you need configure a user.
This is done via the application.yml file that is passed to the container via */opt/init/micronaut/application.yml*
to configure Micronaut. See above.

    users:
        -   email: admin@maurodatamapper.com
            first-name: admin
            last-name: admin
            temp-password: mypassword
    groups:
        -   name: Administrators
            isAdmin: true
            members:
                - admin@maurodatamapper.com
    api-keys:
        -   name: My first API Key
            email: admin@maurodatamapper.com
            refreshable: true
            expiry: 2025-12-31

### Running the container

Point the container at your *init/* directory, and expose the port micronaut is running on:

    # docker run --rm -p 8080:8080 -v /path/to/your/init:/opt/init:ro -it maurodatamapper/mauro:0.0.2-SNAPSHOT

To persist the data between shutdown and startup, you must also connect the container to */var/lib/postgresql/data* as read/write.

## Running the container with existing data

Either import *.sql* scripts are present in */opt/init/postgres* to be imported at startup, or a pre-existing postgres database
is present in */var/lib/postgresql/data*. In both these cases, make sure that the datasource for postgres matches up with the
*application.yml* configuration


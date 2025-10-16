An installation of **Mauro Data Mapper** has three (3) components:

1. *Micronaut backend* with REST API
2. *Web-based frontend* user interface
3. *Postgres database* to hold the data models

## The all-in-one docker image
The all-in-one docker image holds all three components for simplicity, and it will run without further configuration.
However, to be able to use Mauro, you will need to be able to

1. sign in to the user interface or API, and
2. to persist the data held by the database when the container is restarted.

Some additional configuration, in the form of specifically three folders/directories and one file, is required.

To be able to access and persist files used by the docker container, these file mount points are exposed for use:

| Mount point              | Purpose                 | Required?                            |
|--------------------------|-------------------------|--------------------------------------|
| /opt/init                | Start up configuration  | <span style="color:green">Yes</span> |
| /var/lib/postgresql/data | Persist Postgres data   | <span style="color:green">Yes</span> |
| /var/logs                | Logging                 | No                                   |
| /database                | Hold database snapshots | No                                   |

Of these */opt/init* and */var/lib/postgresql/data* must be set up.

To access REST API, and the Postgres database, the docker container also exposes these TCP ports for use:

| Port  | Purpose                  |
|-------|--------------------------|
| 8080  | REST API, User interface |
| 5432  | Postgres database        |

The docker run command will need port 8080 open to access the user interface and/or the Mauro backend REST API service. 

### Start-up

#### Configuration
On running the image as a docker container, */opt/init* is scanned for configuration files, scripts,
plugins, and other resources.

Under */opt/init* there are two sub-directories involved in start-up:

<pre>
/opt/init/
    | - postgres/
    | - micronaut/
</pre>

| Sub&#160;directory | Start up actions                                                                                                                                                                                                               |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| postgres/          | *.sh* shell scripts will be run<br/>*.sql* will be run by Postgres                                                                                                                                                             |
| micronaut/         | *.sh* shell scripts will be run<br/>*.jar* Java ARchive files set up as Mauro plugins<br/>*application.yml* installed as Micronaut's configuration<br/>*all other files* will be copied to Micronaut's *resources/* directory. |

Use */opt/init* to include any plugins as *.jar* files, and set your own version of *application-mauro.yml* like this:

<pre>
/opt/init/
    | - postgres/
    | - micronaut/
        | - application-mauro.yml
        | - yourFavouritePlugin.jar
</pre>

The minimal set-up for */opt/init/* looks like this:

<pre>
/opt/init/
    | - micronaut/
        | - application-mauro.yml
</pre>

#### Database
At start-up */var/lib/postgresql/data* will be checked for any existing Postgres database files.
If none are found, the database will be initialised creating an empty database.
Once the database has been established, the contents of */opt/init/postgres* will be processed.

The file structure now looks like:

<pre>
/opt/init/
    | - postgres/
    | - micronaut/
        | - application-mauro.yml

/var/lib/postgresql/data
    | - Many
    | - Files
    | - Written
    | - By
    | - Postgres
</pre>


#### Example start-up configuration and run

Putting this all together, create a directory tree available for your docker container to use:

##### 1. Create directories
<pre>
/my/docker/files/
    | - data/
    | - init/
        | - micronaut/
            | - application-mauro.yml
</pre>

Where *data/* is going to be where the Postgres database files are kept, and *init/micronaut/* is where the
configuration *application-mauro.yml* is going to go.

##### 2. Configure users, groups, API keys
Fill in *application-mauro.yml* with some configuration:

```yaml
mauro:
  users:
    -   email: admin@maurodatamapper.com
        first-name: admin
        last-name: admin
        temp-password: a_password
  groups:
    -   name: Administrators
        is-admin: true
        members:
          - admin@maurodatamapper.com
  api-keys:
    -   name: My first API Key
        email: admin@maurodatamapper.com
        refreshable: true
        expiry: 2027-12-31
```

##### 3. Pull docker
Pull a docker image (see [Docker images](./docker.md) for the list):

```bash
docker pull maurodatamapper/mauro:0.0.1-beta
```

##### 4. Start container
Start a container with user interface port open and local directories mounted:

```bash
docker run --rm -p 8080:8080 -v /my/docker/files/init:/opt/init:ro -v /my/docker/files/data:/var/lib/postgresql/data -it maurodatamapper/mauro:0.0.1-beta
```

##### 5. View in browser
Visit http://<span/>yourhostname:8080/ in your browser.

The above *application-mauro.yml* has some *mauro:* configuration for users, groups, and API keys.
Sign in with those credentials. In the above example that would be:

*admin@<span/>maurodatamapper.com*<br/>
*a_password*

Once set-up:

 * Stopping the container will shutdown cleanly.
 * The *docker run* command will start it again.
 * You can edit the start up files, and restart the container again.
 * You can replace the docker image with a newer version using the *docker pull* command,
stop the previous container, and start the new one.

### Bootstrapping users, groups and api keys

Edit */opt/init/micronaut/application-mauro.yml* to look similar to this:

```yaml
mauro:
    users:
        -   email: admin@maurodatamapper.com
            first-name: admin
            last-name: admin
            temp-password: mypassword
    groups:
        -   name: Administrators
            description: optional description
            is-admin: true
            members:
                - admin@maurodatamapper.com
    api-keys:
        -   name: My first API Key
            email: admin@maurodatamapper.com
            key: optional UID key
            refreshable: true
            expiry: 2027-12-31
```
#### Users

| Field          | Purpose                              | Mandatory? |
|----------------|--------------------------------------|------------|
| email          | is the user name as an email address | Yes        |
| first-name     | First name                           | Yes        |
| last-name      | Last name                            | Yes        |
| temp-password  | A temporary/initial password         | Yes        |

#### Groups

| Field       | Purpose                                             | Mandatory? | Default |
|-------------|-----------------------------------------------------|------------|---------|
| name        | is the user name as an email address                | Yes        |         |
| description | Description of the group                            | No         | Blank   |
| is-admin    | Whether the members of the group are administrators | No         | false   |
| members     | A list of usernames                                 | No         | Empty   |

#### Api-keys

| Field       | Purpose                                                          | Mandatory? | Default              |
|-------------|------------------------------------------------------------------|------------|----------------------|
| name        | A unique name for the API key                                    | Yes        |                      |
| email       | The user the key belongs to                                      | Yes        |                      |
| key         | A given API key                                                  | No         | Creates a new key    |
| expiry      | yyyy-MM-dd date when the key will expire                         | No         | 1 Year from creation |
| refreshable | When the key expires, it may be refreshed with a new expiry date | No         | false                |

For any optional field, if you don't wish to set a value for it,
omit it from the configuration rather than including it as blank.

### Running the container

#### Foreground
To run the container in the foreground, you can use:
```bash
docker run --rm -it -p 8080:8080 -v /my/docker/files/init:/opt/init:ro -v /my/docker/files/data:/var/lib/postgresql/data maurodatamapper/mauro:0.0.1-beta
```

| Part                                              | Meaning                                                                                                                                                                                              | 
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| docker run                                        | The docker command                                                                                                                                                                                   |
| --rm                                              | Remove the container when it stops                                                                                                                                                                   | 
| -it                                               | You can use CTRL-C to exit the container from the command line, and see the start-up trace<br/>-i means --interactive Keep STDIN open even if not attached<br/> -t means --tty Allocate a pseudo-TTY | 
| -p 8080:8080                                      | Publish to the host's port 8080 from the container's port 8080                                                                                                                                       | 
| -v /my/docker/files/init:/opt/init:ro             | Create a mount from:<br/>/my/docker/files/init<br/> that surfaces at:<br/>/opt/init<br/> in the container, in read-only mode (ro)                                                                    | 
| -v /my/docker/files/data:/var/lib/postgresql/data | Create a mount from:<br/>/my/docker/files/data<br/> that surfaces at:<br/>/var/lib/postgresql/data in the container                                                                                  | 
| maurodatamapper/mauro:0.0.1-beta                  | The image to run                                                                                                                                                                                     |

#### Background
To run the container in the background, you can use:
```bash
docker run --rm -d -p 8080:8080 -v /my/docker/files/init:/opt/init:ro -v /my/docker/files/data:/var/lib/postgresql/data maurodatamapper/mauro:0.0.1-beta
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

### Running the container with existing data

#### Option 1 existing database

Put a pre-existing postgres database into your *data/* directory

#### Option 2 SQL import

Put some import *.sql* scripts into your *init/postgres* directory for one start-up.

### Data source

For both options, you may want to change the default *DATABASE_NAME*, *DATABASE_USERNAME*, or *DATABASE_PASSWORD*

Edit *init/micronaut/application-datasources.yml* :

```yaml
datasources:
  default:
    url: jdbc:postgresql://localhost:5432/sandbox
    username: sandbox
    password: sandbox
    dialect: POSTGRES
    db-type: postgres
    driver-class-name: org.postgresql.Driver
```

Create *env.list* with corresponding values:
```dotenv
DATABASE_NAME=sandbox
DATABASE_USERNAME=sandbox
DATABASE_PASSWORD=sandbox
```

And then run the container with these environment variables set: DATABASE_NAME, DATABASE_USERNAME, DATABASE_PASSWORD ,
using *--env-file*

```bash
docker run .... --env-file env.list
```

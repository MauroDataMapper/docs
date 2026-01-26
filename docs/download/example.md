Make a directory tree available for your docker container to mount:

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

<small>(The *data/* directory does not need to be at the same location)</small>

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

##### 3. Pull a docker image

--8<-- "docs/download/docker-table.md"

```bash
--8<-- "docs/download/docker-pull.md"
```

##### 4. Start the container
Start the container with user interface port open and the local directories mounted:

```bash
docker run --rm -p 8080:8080 \
  -v /my/docker/files/init:/opt/init:ro \
  -v /my/docker/files/data:/var/lib/postgresql/data \
  -it \
  --8<-- "docs/download/docker-image.md"
```

(The above will start the container in the foreground - which is useful for seeing trace and interacting through the terminal.
Read [Running](../run) to find a detailed description of the docker command, for example running the container in the background.)

##### 5. View user interface in browser
Visit http://<span/>yourhostname:8080/ in your browser.

The above *application-mauro.yml* has some *mauro:* configuration for users, groups, and API keys.
Sign in with those credentials. In the above example that would be:

*admin@<span/>maurodatamapper.com*<br/>
*a_password*

##### Behaviours to note

 * Stopping the container will cause it to shutdown cleanly: it is safe to do that.
 * [Running](../run) The *docker run* command using the same parameters will start it again. The data will persist in */my/docker/files/data*
 * You can edit the start up files, and restart the container again.
 * [Updating](../update) You can replace the docker image with a newer version using the *docker pull* command,
stop the previous container, and start the new one. 

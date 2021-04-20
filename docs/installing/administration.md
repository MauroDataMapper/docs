## Backing up the database

## Restoring from backup

## Updating to the latest version

## Checking version information

## Checking availability

## Re-building the search index

The search index improves the performance of searching, this content is stored in-memory (and persisted to files on disk at suitable intervals). 
In some places in the **Core**, it may also be used to speed up access to particular model contents.

The index is built using [Apache Lucene](https://lucene.apache.org) but managed in the code through Hibernate. 
This means that it is always kept in sync with the database contents, but it can be re-indexed if necessary - for example if searching provides 
incorrect or inconsistent results.  

Administrators may rebuild the Lucene index through the user interface: drop down the menu by clicking on your username in the top right of the 
screen; choose 'Configuration', and the 'Lucene' tab, and click "Rebuild Index".

Please do not leave the page whilst reindexing is in progress - the time required is dependent on the number of models saved in the system, but may 
take between 5 and 10 minutes for a large system.

Alternatively, an API call may be made: [see here](../rest-api/admin.md#system-actions) for details.  This `POST` call may be made with an 
existing session cookie, by passing username / password parameters as part of the call, or by passing an API Key.  Only those with system 
administrator role may perform this action.

The contents of the search index can be hard to inspect for debugging purposes! We use a tool called 
[Marple](https://github.com/flaxsearch/marple) but be sure to use a compatible version!


## Docker administration

### Cleaning up docker

Continually building docker images will leave a lot of loose snapshot images floating around, occasionally make use of:

* Clean up stopped containers - `docker rm $(docker ps -a -q)`
* Clean up untagged images - `docker rmi $(docker images | grep "^<none>" | awk "{print $3}")`
* Clean up dangling volumes - `docker volume rm $(docker volume ls -qf dangling=true)`

You can make life easier by adding the following to the appropriate bash profile file:

```bash
alias docker-rmi='docker rmi $(docker images -q --filter "dangling=true")'
alias docker-rm='docker rm $(docker ps -a -q)'
alias docker-rmv='docker volume rm $(docker volume ls -qf dangling=true)'
```

Remove all stopped containers first then remove all tagged images.

A useful tool is [Dockviz](https://github.com/justone/dockviz),
ever since docker did away with `docker images --tree` you can't see all the layers of images and therefore how much floating mess you have.

Add the following to the appropriate bash profile file:

 ```bash
 alias dockviz="docker run --privileged -it --rm -v /var/run/docker.sock:/var/run/docker.sock nate/dockviz"
 ```

Then in a new terminal you can run `dockviz images -t` to see the tree,
the program also does dot notation files for a graphical view as well.

### Multiple compose files

When you supply multiple files, `docker-compose` combines them into a single configuration.
Compose builds the configuration in the order you supply the files.
Subsequent files override and add to their successors.

```bash
# Apply the .dev yml file, create and start the containers in the background
$ docker-compose -f docker-compose.yml -f docker-compose.dev.yml -d <COMMAND>

# Apply the .prod yml file, create and start the containers in the background
$ docker-compose -f docker-compose.yml -f docker-compose.prod.yml -d <COMMAND>
```

We recommend adding the following lines to the appropriate bash profile file:

```bash
alias docker-compose-dev="docker-compose -f docker-compose.yml -f docker-compose.dev.yml"
alias docker-compose-prod="docker-compose -f docker-compose.yml -f docker-compose.dev.yml"
```
This will allow you to start compose in dev mode without all the extra file definitions

---

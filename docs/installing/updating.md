# Updating to the latest version

Updating an already running system can be performed in 1 of 2 ways. The **preferred** method would be to pull the latest version tag from the
repository and then rebuild the mauro-data-mapper service. However this may be hard if multiple changes have been made to the `docker-compose.yml` and
you're not familiar enough with git to handle stashing and merging.

```bash
# Update an already built system
# Fetch the latest commits
$ git fetch
# Stash any local changes
$ git stash
# Checkout/pull the version you want to update to
# e.g. git checkout B4.4.1_F6.0.0
$ git checkout <TAG>
# Unstash local changes, you may need to resolve any merge conflicts
$ git stash pop
# Build the new image
$ docker-compose build mauro-data-mapper
# Start the update
$ docker-compose up -d mauro-data-mapper
```

The alternative method is to use the update command script and pass in the new versions you want to update to. The downside with this method is if we
have made any changes to the Dockerfiles or base versions you will not have them.

```bash
# Update an already built system
# e.g ./update -b 4.4.1 -f 6.0.0
$ ./update -b <BACKEND_VERSION> -f <FRONTEND VERSION>
```

This will rebuild just the Mauro Data Mapper image with the latest version.

Occasionally, database migrations are required when updating to a new version. These run automatically when the application restarts, making use of
the [Flyway](https://flywaydb.org) versioning system. No manual steps are required from the user.

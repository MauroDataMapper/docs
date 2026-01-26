There are two (2) options that use/reuse an existing postgres database storing Mauro data models.

#### Option 1 connect an existing database

Attach a pre-existing postgres database to your *data/* directory

#### Option 2 run an SQL import

Import *.sql* script(s) by putting them into your *init/postgres* directory for one start-up cycle only (to run them once)

### Change the data source

For both options, you can change the default *DATABASE_NAME*, *DATABASE_USERNAME*, or *DATABASE_PASSWORD*

Edit *init/micronaut/application-datasources.yml* :

```yaml
datasources:
  default:
    url: jdbc:postgresql://localhost:5432/sandbox
    username: sandbox
    password: sandbox
```

The *DATABASE_NAME* is part of the *url* . E.g. in the above exampe it is 'sandbox'.

Running (restarting) the container will read these values and use them for configuring and connecting to the database.

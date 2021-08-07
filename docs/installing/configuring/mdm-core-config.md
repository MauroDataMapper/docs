## Required to be overridden

The following variables need to be overriden/set when building or starting up a new mauro-data-mapper image.

`grails.cors.allowedOrigins`
: Should be set to a single FQDN URL which is the host where MDM will be accessed from. If using a proxy to break SSL then the origin would be the
hostname where the proxy sits, not the host of the server running the docker containers. The origin must include the protocol, i.e. https or http

`maurodatamapper.authority.name`
: The full URL to the location of the catalogue. This is considered a unique identifier to distinguish any instance from another and therefore no 2
instances should use the same URL.

`maurodatamapper.authority.url`
: A unique name used to distinguish a running MDM instance.

`simplejavamail.smtp.username`
: To allow the catalogue to send emails this needs to be a valid username for the `simplejavamail.smtp.host`

`simplejavamail.smtp.password`
: To allow the catalogue to send emails this needs to be a valid password for the `simplejavamail.smtp.host` and `simplejavamail.smtp.username`

`simplejavamail.smtp.host`
: This is the FQDN of the mail server to use when sending emails

## Optional Overrides

The below, along with any property found in any config file, can be overridden. We have supplied a brief description of any properties which cannot be
found in the grails or spring documentation.

`database.host`
: The host of the database. If using docker-compose this should be left as `postgres` or changed to the name of the database service

`database.port`
: The port of the database

`database.name`
: The name of the database which the catalogue data will be stored in

`dataSource.username`
: Username to use to connect to the database. See the Postgres service environment variables for more information.

`dataSource.password`
: Password to use to connect to the database. See the Postgres service environment variables for more information.

`simplejavamail.smtp.port`
: The port to use when sending emails

`simplejavamail.smtp.transportstrategy`
: The transport strategy to use when sending emails

`hibernate.search.default.indexBase`
: The directory to store the lucene index files in
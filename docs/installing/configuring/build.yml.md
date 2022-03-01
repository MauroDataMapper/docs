Below is the default `build.yml` file built into the MDM image.

```yaml
---
# Database connection details
---
database:
    host: postgres
    port: 5432
    name: maurodatamapper
dataSource:
    username: maurodatamapperuser
    password: "this is provided but hidden in these docs"
---
# MDM configuration properties
---
maurodatamapper:
    authority:
        name: 'Mauro Data Mapper'
        url: http://localhost
---
# Standard Email configuration
---
simplejavamail:
    smtp:
        username:
        password:
        host:
        port: 587
    transportstrategy: SMTP_TLS
---
# mdm-plugin-email-proxy Configuration
---
#emailServiceUrl: 
#emailServiceUsername: 
#emailServicePassword: 
---
# CORS
# See http://docs.grails.org/latest/guide/theWebLayer.html#cors
---
grails:
    cors:
        enabled: true
        # The following are the defaults
        # allowedOrigins: [] # Cannot use allowedOrigins with *, they have to be clearly stated origins
        allowedOriginPatterns: [ '*' ]
        allowedMethods: [ 'GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'HEAD' ]
        allowedHeaders: [ 'origin', 'content-type', 'accept', 'authorization', 'pragma', 'cache-control' ]
        #exposedHeaders: null
        #maxAge: 1800
        #allowCredentials: true
hibernate:
    search:
        default:
            indexBase: '/lucene'

```
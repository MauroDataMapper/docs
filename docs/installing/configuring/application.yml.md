Below is the default application.yml file included in the main application.

```yaml
database:
    host: localhost
    port: 5432
    name: maurodatamapper
---
#Default for plugins/applications
---
maurodatamapper:
    security:
        public: false
    authority:
        name: 'Mauro Data Mapper'
        url: http://localhost
grails:
    profile: rest-api
    codegen:
        defaultPackage:  uk.ac.ox.softeng.maurodatamapper.application
    gorm:
        reactor:
            # Whether to translate GORM events into Reactor events
            # Disabled by default for performance reasons
            events: false
        failOnError: true
    resources:
        pattern: /**
info:
    app:
        name: '@info.app.name@'
        version: '@info.app.version@'
        grailsVersion: '@info.app.grailsVersion@'
spring:
    jmx:
        unique-names: true
    main:
        banner-mode: "off"
    groovy:
        template:
            check-template-location: false
    devtools:
        restart:
            additional-exclude:
                - '*.gsp'
                - '**/*.gsp'
                - '*.gson'
                - '**/*.gson'
                - 'logback.groovy'
                - '*.properties'

# Spring Actuator Endpoints are Disabled by Default
management:
    endpoints:
        enabled-by-default: false
        web:
            exposure:
                include:
                    - 'health'
                    - 'shutdown'
        jmx:
            exposure:
                include: '*'
    endpoint:
        shutdown:
            enabled: true
        health:
            enabled: true

---
grails:
    mime:
        disable:
            accept:
                header:
                    userAgents:
                        - Gecko
                        - WebKit
                        - Presto
                        - Trident
        types:
            json:
                - application/json
                - text/json
            hal:
                - application/hal+json
                - application/hal+xml
            xml:
                - text/xml
                - application/xml
            atom: application/atom+xml
            css: text/css
            csv: text/csv
            js: text/javascript
            rss: application/rss+xml
            text: text/plain
            all: '*/*'
    urlmapping:
        cache:
            maxsize: 1000
    controllers:
        defaultScope: singleton
    converters:
        encoding: UTF-8
    exceptionresolver:
        params:
            exclude:
                - password
                - tempPassword
    cors:
        enabled: true
        # The following are the defaults
        allowedOrigins: ['*']
        allowedMethods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'HEAD']
        allowedHeaders: ['origin', 'content-type', 'accept', 'authorization', 'pragma', 'cache-control']
        #exposedHeaders: null
        #maxAge: 1800
        #allowCredentials: true
    views:
        markup:
            autoEscape: true
            prettyPrint: false
            autoIndent: false
            autoNewLine: false
---
hibernate:
    cache:
        queries: false
        use_second_level_cache: true
        use_query_cache: true
        region:
            factory_class: org.hibernate.cache.jcache.JCacheRegionFactory
    javax:
        cache:
            provider: org.ehcache.jsr107.EhcacheCachingProvider
            missing_cache_strategy: create
    search:
        default.indexBase: '/tmp/lucene/mdm_application'

---
dataSource:
    pooled: true
    jmxExport: true
    formatSql: true
    driverClassName: org.postgresql.Driver
    dialect: org.hibernate.dialect.PostgreSQL10Dialect
    username: maurodatamapper
    password: MauroDataMapper1234
    dbCreate: none
    url: 'jdbc:postgresql://${database.host}:${database.port}/${database.name}'
---
```
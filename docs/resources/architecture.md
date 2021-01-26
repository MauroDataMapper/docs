## Overview

Mauro is built using a fairly common 'onion' design. At the heart is a standard, relational database where all data is primarily stored. All
interaction with the database is controlled through business logic within the '[Core](#core)' layer.

![System Acrhitecture](/images/architecture1.jpg)

### Relational Database

Mauro has been built on top of [PostgreSQL](https://www.postgresql.org), and in particular is tried and tested against PostgreSQL version 12.  
However, we've taken care not to use any clever features of plugins, and so much of the code _should_ run against any recent version of PostgreSQL.
Furthermore, since the interaction with the relational database is based upon the [Hibernate ORM](https://hibernate.org), it could even be possible to
rebuild against other database implementations, but we've yet to try. The only exception is during integration testing, in which an in-memory h2
database is used in order to speed-up testing.

System administrators with access to the database can access the data directly, and this is the preferred route for
[taking backups](/installing/administration). However, editing or interpreting the data directly through the database is not recommended, as this will
bypass the business logic in the core, with potential loss of system integrity.

### Core

The 'Core' component is built using [Grails](https://grails.org) (version 4), which is a Java-based Model-View-Controller framework. Code is typically
written in Groovy, which itself compiles down to Java. Much of the Grails framework is built on top of the widely-used Spring components.

The 'Core' codebase defines the object-oriented domain model, which specifies the structure and constraints on the underlying model. All program logic
is contained within _Services_ and _Controllers_, with _Views_ defining the structure of any outputs to procedures or requests.

### REST API

The REST API is a logical layer, defined completely within the 'Core' component, and is the standard way of interacting with the platform. A
standard [REST](https://en.wikipedia.org/wiki/Representational_state_transfer)-style interface makes use of standard HTTP commands - for example
`GET`, `POST`, `PUT`, and `DELETE`.  Each [REST endpoint](/rest-api/introduction) is defined by a _Controller_ and _View_ within the Grails 'Core'.
Some endpoints are aliased for ease of use, or backwards compatibility, and there is genericity built in to make programming against the API easier.
Plugins may extend the API with new endpoints.

Each endpoint typically receives and responds in JSON; some can use XML but this is less well tested.  Custom data formats apply in particular 
circumstances - for example when dealing with file attachments.

### Programming APIs

### User Interface

### Core Plugins

### Search Index

The search index is an in-memory, and direct file index used to improve the performance of searching. In some places in the Core, it may also be used
to speed up access to particular model contents. The index is built using [Apache Lucene](https://lucene.apache.org), but managed in the code through
Hibernate. This means that it is always kept in sync with the database contents, but it can be [re-indexed]() if necessary.

The contents of the search index can be hard to inspect for debugging purposes!  We use a tool called [Marple](https://github. com/flaxsearch/marple),
but be sure to use a compatible version!

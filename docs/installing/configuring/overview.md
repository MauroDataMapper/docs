To make life simpler and to avoid too many variables in the docker-compose.yml file we have supplied 2 preferred methods of overriding the defaults.

!!! Warning

     This replaces all of the previous releases environment variables setting in docker-compose.yml.

!!! Information

     Each plugin may supply some mandatory fields which need to be overridden. Please see each section to identify which fields these may be.
     Grails and Spring supply ample documentation for all their standard properties which can all also be overridden via the build or runtime files.
     Our documentation is intended to supply information for our own plugins or properties which we require to be overridden.

The preference order (by MDM) for loaded sources of properties is

1. Environment Variables
2. runtime.yml - See the default included [here](runtime.yml.md)
3. build.yml - See the default included [here](build.yml.md)
4. application.yml - See the default included [here](application.yml.md)
5. plugin.yml - there are multiple versions of these as each plugin we build may supply their own

## Environment Variables

Any grails configuration property found in any of the yml files can be overridden through environment variables. They simply need to be provided in
the "dot notation" form or (more appropriately) the "uppercase underscore separated" form rather than the "YML new line" format.

e.g. application.yml

```yaml
database:
    host: localhost
```

would be overridden by docker-compose.yml

```yaml
services:
    mauro-data-mapper:
        environment:
            database.host: another-host

```

or

```yaml
services:
    mauro-data-mapper:
        environment:
            DATABASE_HOST: another-host

``` 

## build.yml File

The build.yml file is built into the MDM service when the image is built and is a standard grails configuration file. Therefore any properties which
can be safely set at build time for the image should be set into this file. This includes any properties which may be shared between multiple
instances of MDM which all start from the same image.

Our recommendation is that if only running 1 instance of MDM from 1 cloned repository then you should load all your properties into the build.yml
file. For this reason we have supplied the build.yml file with all the properties which we either require to be overridden or expect may want to be
overridden.

## runtime.yml File

The runtime.yml file will be loaded into the container via the docker-compose.yml file. This is intended as the replacement for environment variable
overrides, where each running container might have specifically set properties which differ from a common shared image.

!!! Danger

    Do not change the environment variable `runtime.config.path` as this denotes the path inside the container where the config file will be found


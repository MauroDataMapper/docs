
The configurable YAML properties for the FHIR plugin are for the handling of the [micronaut](https://micronaut.io/) connections between the FHIR server and MDM.
Defaults are provided via the `plugin.yml` and it is unlikely you need to override them. These are micronaut properties and as such please see the 
micronaut [documentation](https://docs.micronaut.io/latest/guide/configurationreference.html) to understand what they are and how they affect the system.

## Defaults provided in the plugin.yml

```yaml
micronaut:
    codec:
        json:
            additional-types:
                - 'application/json+fhir;charset=utf-8'
    http:
        client:
            max-content-length: 33554430
            read-timeout: PT30S
```
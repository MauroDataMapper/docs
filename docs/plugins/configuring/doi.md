The following properties can be defined in the config yaml files or set using the RESTful API or the web UI.

!!! Information

    Once MDM has started up the only way to change the properties is via the RESTFful API/Web UI.
    See the [DOI Userguide](../user-guides/digital-object-identifiers/digital-object-identifiers.md) for more information.

!!! Warning

    The following property must also be set via the RESTful API or the web UI for the DOI plugin to work: `site.url`.

## Available Properties

`maurodatamapper.digitalobjectidentifiers.username`
: The username used to authenticate with when communicating with the DOI registry.

`maurodatamapper.digitalobjectidentifiers.password`
: The password used to authenticate with when communicating with the DOI registry.

`maurodatamapper.digitalobjectidentifiers.endpoint`
: The full HTTP web address for the DOI reigstry. e.g. `https://api.test.datacite.org`.

`maurodatamapper.digitalobjectidentifiers.prefix`
: The assigned DOI prefix to be used for all registered resources. e.g. `10.80079`.
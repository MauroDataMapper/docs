OpenID Connect has a range of properties which can be set in the yaml files.
Some of these take effect each time you start MDM, some are only used once and if they've been enabled before then they will be ignored on subsequent startups.
We supply defaults to ensure basic functionality however these can be overridden using the yaml files.

We store the basic information to bootstrap certain providers and set them up without any interaction through the admin interface/RESTful API.
The providers are currently

* [Google](#google)
* [Microsoft](#microsoft) (via microsoftonline)
* [KeyCloak](#keycloak)

## Control Properties

`maurodatamapper.openidConnect.session.timeout`
: This is the length of time which sessions will be kept active before being timed out, the default is 24 hours this overrides the usual session timeout of 30 minutes which 
is set for all non-OIC authenticated users. We do not recommend setting this lower than `24h` as this is the timeout after which users will be required to log back in via 
the OIC window.
Inside this timeout the API will keep the session alive connecting to the OIC provider as necessary to refresh the user's token.

## Bootstrapped Providers

Each of the providers has pre-configured defaults which are used to add them automatically if they are enabled.
These defaults (provided in each section for reference only) can be changed once the system has started up by using the admin interface/RESTful API,
see the [OIC Userguide](../user-guides/openid-connect/openid-connect.md) for more information.

### Google

`maurodatamapper.openidConnect.google.enabled`
: Defaults to false. If enabled then the other google properties will need to be provided.

`maurodatamapper.openidConnect.google.clientId`
: The client id used to identify and authenticate the MDM service.

`maurodatamapper.openidConnect.google.clientSecret`
: The client id used to identify and authenticate the MDM service.

* `discoveryDocumentUrl`: https://accounts.google.com/.well-known/openid-configuration
* `imageUrl`: https://upload.wikimedia.org/wikipedia/commons/5/53/Google_%22G%22_Logo.svg

### Microsoft

!!! Information
    
    Post-processing occurs with Microsoft to replace the `{tenant}` in the `issuerUrl` provided by the discoveryDocumentUrl with the `clientId`.
    If manually configuring a Microsoft provider you may have to manually edit the discovery document via the admin interface to perform the same. 

`maurodatamapper.openidConnect.microsoft.enabled`
: Defaults to false. If enabled then the other google properties will need to be provided.

`maurodatamapper.openidConnect.microsoft.clientId`
: The client id used to identify and authenticate the MDM service.

`maurodatamapper.openidConnect.microsoft.clientSecret`
: The client id used to identify and authenticate the MDM service.

* `discoveryDocumentUrl`: https://login.microsoftonline.com/common/.well-known/openid-configuration
* `imageUrl`: https://upload.wikimedia.org/wikipedia/commons/9/98/Microsoft_logo.jpg

### KeyCloak

!!! Information

    The `baseUrl` and `realm` fields are used to build the discoveryDocumentUrl for the boostrapped provider. 
    If creating a Keycloak provider via the Admin interface/RESTful API these properties are not needed as you can define the full URL to the discovery document

`maurodatamapper.openidConnect.keycloak.enabled`
: Defaults to false. If enabled then the other google properties will need to be provided.

`maurodatamapper.openidConnect.keycloak.baseUrl`
: The full URL where the keycloak provider can be found.

`maurodatamapper.openidConnect.keycloak.realm`
: The realm configured inside the keycloak provider for the MDM service to use.

`maurodatamapper.openidConnect.keycloak.clientId`
: The client id used to identify and authenticate the MDM service.

`maurodatamapper.openidConnect.keycloak.clientSecret`
: The client id used to identify and authenticate the MDM service.

* `discoveryDocumentUrl`: `${baseUrl}/realms/${realm}/.well-known/openid-configuration`
* `imageUrl`: https://upload.wikimedia.org/wikipedia/commons/2/29/Keycloak_Logo.png


## Defaults provided in the plugin.yml

```yaml
maurodatamapper:
    openidConnect:
        session:
            timeout: 24h
        google:
            enabled: false
        microsoft:
            enabled: false
            tenant: common
        keycloak:
            enabled: false
```
Mauro can use OpenID Connect (OIDC) to authenticate and authorise users.

Firstly, configure a provider that supports OpenID. E.g.

* [Keycloak](https://www.keycloak.org/)
* [Azure](https://learn.microsoft.com/en-us/azure/app-service/configure-authentication-provider-openid-connect)
* [Cognito](https://aws.amazon.com/cognito/)
* [Identity](https://developers.google.com/identity/openid-connect/openid-connect)
* [okta](https://developer.okta.com/)

You will get a _client secret_, and a _client id_ once you create an application client with a provider.

Once you have the _client secret_, a _client id_, and the issuer URL you can configure authentication by editing
*/opt/init/micronaut/application-mauro.yml* and add section like this:

```yaml
micronaut:
    security:
        oauth2:
            enabled: true
            clients:
                <<provider>>:
                    client-secret: <<your client secret>>
                    client-id: <<your client id>>
                    openid:
                        issuer: <<provider's issuer URL>>
                        authorization:
                            prompt: login
```

which will configure micronaut to produce an authorisation endpoint, and add another section like this:

```yaml
mauro:
    oauths:
        -   app-label: <<Your button label>>
            oauth-provider: <<provider>>
            create-user: true
            require-verified-email: false
```

which will configure **Mauro** to surface a log in button called `<<Your button label>>` on the user interface,
using the `<<provider>>` authentication.

E.g. if you were to call your `<<provider>>` _microsoft-azure_ it would look similar to this:

```yaml
micronaut:
    security:
        oauth2:
            enabled: true
            clients:
                microsoft-azure:
                    client-secret: <<your client secret>>
                    client-id: <<your client id>>
                    openid:
                        issuer: https://login.microsoftonline.com/<<some_uuid>>/v2.0
                        authorization:
                            prompt: login
mauro:
    oauths:
        -   app-label: Microsoft Azure
            oauth-provider: microsoft-azure
            create-user: true
            require-verified-email: false
```

### Proxies
If the container is being proxied, for the authentication process to work, please follow the [Proxy](../CORS/#proxy) instructions.
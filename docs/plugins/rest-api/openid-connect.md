## Introduction

The page covering [authentication](../../rest-api/authentication) explains how to authenticate with a basic username/password for a user created directly in Mauro. An alternative authentication method is to use an [OpenID Connect](https://openid.net/connect/faq/) identity service to authenticate users with an external provider/account system, and then authorize them to use Mauro.

In order use OpenID Connect identity providers, the Mauro instance must:

1. Have the **Mauro OpenID Connect Authentication plugin** installed.
2. Set up and configure one or more identity services that support the OpenID Connect protocol.
3. Add the configuration details of each identity provider to Mauro.

The full details of this set up can be viewed in the user guide [Using OpenID Connect](../../installing/openid-connect/openid-connect).

## Authenticating users

Assuming that the Mauro instance has been configured correctly and there is at least one OpenID Connect provider [configured in Mauro](#administration), endpoints will be exposed to handle authentication using those external services.

### Using authorization endpoints

There is an endpoint to fetch a list of OpenID Connect providers available in Mauro, which will provide the _authorization endpoints_:

<endpoint class="get">/api/openidConnectProviders</endpoint>

=== "Response body (JSON)"
    ```json
    [
        {
            "id": "0500cd44-6ca9-4bca-aa55-bbb188278d79",
            "label": "Google",
            "standardProvider": true,
            "authorizationEndpoint": "https://accounts.google.com/o/oauth2/v2/auth?scope=openid+email+profile&response_type=code&state=045d33af-2dc7-48cd-9111-a09c94faee49&nonce=%C3%B9%02%C2%BF%C5%93%07%C3%A9%C3%B4%27%EF%BF%BD%2C%22%C2%B3%C3%8D%07%C3%98%E2%80%A2%C3%91%C3%8C%C3%83%EF%BF%BD%26%CB%9C%C3%A4%05%C3%A17%C2%B1%19Q%C3%A13%E2%80%9C&client_id=375980182300-tc8sb8c1jelomnkmvqtkkqpl4g8lkp06.apps.googleusercontent.com",
            "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/5/53/Google_%22G%22_Logo.svg"
        },
        {
            "id": "61fa9235-7281-4738-87f1-763bf60e1d79",
            "label": "Keycloak",
            "standardProvider": true,
            "authorizationEndpoint": "https://jenkins.cs.ox.ac.uk/auth/realms/test/protocol/openid-connect/auth?scope=openid+email+profile&response_type=code&state=0f4e7148-28c4-407d-bad8-47052769e721&nonce=%C3%B9%02%C2%BF%C5%93%07%C3%A9%C3%B4%27%EF%BF%BD%2C%22%C2%B3%C3%8D%07%C3%98%E2%80%A2%C3%91%C3%8C%C3%83%EF%BF%BD%26%CB%9C%C3%A4%05%C3%A17%C2%B1%19Q%C3%A13%E2%80%9C&client_id=mdm",
            "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/2/29/Keycloak_Logo.png"
        }
    ]
    ```

The `authorizationEndpoint` is the key property value in each case, as this provides the URL to redirect to in order to start authenticating in the external service. The `authorizationEndpoint` value _must_ include an additional query parameter added by yourself called `redirect_uri`: this is the URL to the page that the identity provider will redirect back to once it has authenticated a user, also providing the session state needed for Mauro to authorize the user session.

!!! Information
    Before redirecting to the external identity server, track the `id` value of the OpenID Connect provider somewhere. This will be required later when authorizing the Mauro user session.

### Mauro authorization

When the OpenID Connect identity provider redirects back to the client (via the `redirect_uri` provided), it will provide three query parameters in the URL:

* `state`
* `session_state`
* `code`

All these parameters must be captured and the passed to the standard Mauro authentication endpoint via the request body:

<endpoint class="post">/api/authentication/login</endpoint>

=== "Request body (JSON)"
    ```json
    { 
        "openidConnectProvider": "0500cd44-6ca9-4bca-aa55-bbb188278d79",
        "state": <query param value>,
        "sessionState": <query param value>,
        "code": <query param value>,
        "redirectUri": "http://my.app.com/authorize"
    }
    ```

!!! Information
    The `redirectUri` passed to the login request body must _exactly_ match that passed as the `redirect_uri` query parameter at the point of redirecting to the OpenID Connect service.

If successful, the `/api/authentication/login` endpoint will return the same response as a standard login using a username and password. The user is now signed into Mauro and has an active session. The user also uses the same permissions and user groups model for accessing catalogue content as any other user.

## Administration

!!! Information
    The following endpoints can only be accessed by an administrator user.

### Getting providers

To get a list of available OpenID Connect providers registered in Mauro, the following endpoint can be used:

<endpoint class="get">/api/admin/openidConnectProviders</endpoint>

=== "Response body (JSON)"
    ```json
    {
        "count": 2,
        "items": [
            {
                "id": "0500cd44-6ca9-4bca-aa55-bbb188278d79",
                "lastUpdated": "2021-06-24T09:01:38.914Z",
                "label": "Google",
                "standardProvider": true,
                "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/5/53/Google_%22G%22_Logo.svg"
            },
            {
                "id": "61fa9235-7281-4738-87f1-763bf60e1d79",
                "lastUpdated": "2021-06-24T09:01:39.336Z",
                "label": "Keycloak",
                "standardProvider": true,
                "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/2/29/Keycloak_Logo.png"
            }            
        ]
    }
    ```

To get the full details of a particular OpenID Connect provider:

<endpoint class="get">/api/admin/openidConnectProviders/{id}</endpoint>

=== "Response body (JSON)"
    ```json
    {
        "id": "0500cd44-6ca9-4bca-aa55-bbb188278d79",
        "lastUpdated": "2021-06-24T09:01:38.914Z",
        "label": "Google",
        "standardProvider": true,
        "discoveryDocumentUrl": "https://accounts.google.com/.well-known/openid-configuration",
        "clientId": "375980182300-tc8sb8c1jelomnkmvqtkkqpl4g8lkp06.apps.googleusercontent.com",
        "clientSecret": "<secret value>",
        "authorizationEndpointParameters": {
            "id": "dae8564f-8272-4b99-ba1d-03c66f3ab34a",
            "lastUpdated": "2021-06-24T09:01:38.906Z",
            "scope": "openid email profile",
            "responseType": "code"
        },
        "discoveryDocument": {
            "id": "52108737-6fda-408e-b167-f6912bd37a18",
            "lastUpdated": "2021-06-24T09:01:38.91Z",
            "issuer": "https://accounts.google.com",
            "authorizationEndpoint": "https://accounts.google.com/o/oauth2/v2/auth",
            "tokenEndpoint": "https://oauth2.googleapis.com/token",
            "userinfoEndpoint": "https://openidconnect.googleapis.com/v1/userinfo",
            "endSessionEndpoint": "https://oauth2.googleapis.com/revoke",
            "jwksUri": "https://www.googleapis.com/oauth2/v3/certs"
        },
        "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/5/53/Google_%22G%22_Logo.svg"
    }
    ```

### Creating a provider

To add an OpenID Connect provider to Mauro depends on what _discovery_ information is available. There are two types of provider in Mauro:

* **Standard** - a `discoveryDocumentUrl` is provided, which allows Mauro to discover all other necessary endpoints to complete the setup of the provider (authorization, tokens, etc).
* **Non-Standard** - when a `discoveryDocumentUrl` is not available, the individual endpoints needed to complete the OpenID Connect provider setup can be provided manually.

Both use the following endpoint, but sends different request body content.

<endpoint class="post">/api/admin/openidConnectProviders</endpoint>

To create a **Standard** provider, include a similar request body:

=== "Request body (JSON)"
    ```json
    { 
        "label": "Provider name",
        "imageUrl": "http://image.com/logo.png",
        "standardProvider": true,
        "clientId": "<Provided by service>",
        "clientSecret": "<Provided by service>",
        "discoveryDocumentUrl": "https://url.to.some/discovery-document"
    }
    ```

!!! Information
    `imageUrl` is an optional field.

To create a **Non-Standard** provider:

=== "Request body (JSON)"
    ```json
    { 
        "label": "Provider name",
        "imageUrl": "http://image.com/logo.png",
        "standardProvider": false,
        "clientId": "<Provided by service>",
        "clientSecret": "<Provided by service>",
        "discoveryDocument": {
            "issuer": "<url>",
            "authorizationEndpoint": "<url>",
            "tokenEndpoint": "<url>",
            "userinfoEndpoint": "<url>",
            "endSessionEndpoint": "<url>",
            "jwksUri": "<url>"
        }
    }
    ```

!!! Information
    `userinfoEndpoint` and `endSessionEndpoint` are optional, all other discovery endpoints are required.

If successful, both return the same response as [getting a provider](#getting-providers).

### Update / Delete

To edit the properties of an OpenID Connect provider, use the following endpoints, with a request body similar to the JSON described in [Creating a provider](#creating-a-provider).

<endpoint class="put">/api/admin/openidConnectProviders/{id}</endpoint>

To delete an OpenID Connect provider, use the following endpoint.

<endpoint class="delete">/api/admin/openidConnectProviders/{id}</endpoint>
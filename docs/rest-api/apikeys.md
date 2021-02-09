API keys offer an alternative way to authenticate to the Mauro REST API instead of logging in with a username and password, and saving session 
cookies.  This is the recommended method for authenticating when you:

- have long-running processing scripts which could cause sessions to time-out between calls
- need to store authentication details in clear text for an external application to use

Each user can create multiple API keys, and so when sharing with multiple applications, can disable access individually.  API keys are also 
configured with a default expiry date for additional security.   

## Creating an API Key

API keys may be setup through the web interface or via the API.  To generate a first API key, the user must be logged ni using a username and 
password - either through the web interface, or through the REST API.  

Select 'API keys' from the user drop-down

![The API keys menu item in the User drop-down list](../images/apikeys/apikeys-menu.png)

This will take you to a list of existing API keys where you can edit or revoke existing keys, or create new ones.
The list displays, for each API key belonging to the user:

![The list of existing API keys](../images/apikeys/apikeys-list.png)

* **Name**  
  This is a human-readable name for each API key, which must be unique per-user.  Users can use the name to differentiate between different keys 
  used for different purposes.
  
* **Key**
  This is the key itself, which is a UUID, unique to this user.  Click 'copy' to copy this key to your clipboard.  
  
* **Expiry date**
  This is the date from which the API key will no-longer be valid.  For security purposes, every API key is given an expiry date, but may be 
  'refreshed' before expiry.
  
* **Refreshable**
  Whether this API key may be refreshed once it has expired.
  
* **Status**
  Whether this API key is 'active', or 'disabled'.
  
At the end of each row is a drop-down which offers options to disable active keys (or re-enable those that are disabled), and to delete keys.
To create a new API key, click the 'Create Key' button in the top right, which will open up the dialog below. 

![Dialog for creating a new API Key](../images/apikeys/apikeys-create.png)

In the form, you must complete the human-readable name, as described above, choose a number of days before expiry, and choose whether the key is 
to be refreshable on expiry or not.  Click 'Create Key' to complete API creation.


## Using an API Key

To use an API Key, simply add it into the headers of any REST API call.  

!!! info
    If you use API keys to authenticate, the session cookies are not used to persist identity and so the key should be passed with every call.

The header key should be `apiKey` and the value should be the UUID value of the API key itself.


## Using Postman

If you are using [Postman](../postman) as a client, there are two ways to configure the API key for a request, which both have the same 
result.  
You can use the 'Authorization' tab to set the details, as shown in the screenshot below.  You should set the **Key** field to be the text 
`apiKey`, the **Value** field to be the value of the API key, and in the **Add to** drop-down, select "Header".  The API key must be passed in the 
headers, not in the query parameters, which is the alternative option.

![Setting an API key in Postman using the Authorization tab](../images/apikeys/apikeys-postman-auth.png)

This method sets the headers automatically; you can also set them manually as shown in the screenshot below.  Again, you should use the header 
**key** field of `apiKey`, and the **value** field should be populated with the API key value.   

![Setting an API key in Postman using the Headers tab](../images/apikeys/apikeys-postman-headers.png)

## Refreshing an expired API key

When an API key has expired, and it has previously been marked as 'refreshable', then it may be refreshed - a new expiry date may be set.  
To do this, go to the API key list as above, and note that the 'expiry date' field now says that it has expired.  The '...' options at the end of 
the row now offer the option to refresh the APi key.  Choose this option, and in the next dialog, choose a new number of days for expiry.

![Refreshing an expired API key](../images/apikeys/apikeys-refresh.png)

## Revoking an API key

To revoke a particular API key, you can mark it as 'disabled'.  On the list of API keys, choose the '...' drop-down list of options, and choose 
'disable'.    The same option will allow you to re-enable the key if necessary.

!!! info
    It is good practice to set up different API keys for each application - in this way it is easy to revoke access to a single application 
    without having to recreate all other keys and updating other application settings.


## Managing keys through the REST API

!!! info
    Note that API Keys can only be managed by the user that they belong to.


Once [authenticated](authentication.md), the endpoint for listing existing API keys is:

<endpoint class="get">/api/catalogueUsers/**{catalogueUserId}**/apiKeys</endpoint>

This returns a [paginated](pagination.md) list of API keys as follows:

=== "Response body (JSON)"
    ```json
    {
      "count": X,
      "items": [
        {
            "id": "b845e98b-8a42-4332-9323-0c1fc6f5f1db",
            "apiKey": "b845e98b-8a42-4332-9323-0c1fc6f5f1db",
            "name": "Test API Key",
            "expiryDate": "2022-02-03",
            "expired": false,
            "disabled": true,
            "refreshable": false,
            "createdDate": "2021-02-03"
        },
        ...
      ]
    }
    ```
The parameters are as described above; the `id` field is the global primary key identifer for the key.

To create a new API key, post to the following endpoint:

<endpoint class="post">/api/catalogueUsers/**{userId}**/apiKeys</endpoint>

The body of the post method should be structured as follows:

=== "Request body (JSON)"
    ```json
    {
      "name":"My Name",
      "expiresInDays":365,
      "refreshable":true
    }
    ```

where the parameters are as described above.
To enable an existing, disabled API Key, you can use its ID (as described above), with the following endpoint:

<endpoint class="put">/api/catalogueUsers/**{catalogueUserId}**/apiKeys/**{apiKeyId}**/enable</endpoint> 

Similarly, to disable an existing, enabled API key, use the following:

<endpoint class="put">/api/catalogueUsers/**{catalogueUserId}**/apiKeys/**{apiKeyId}**/disable</endpoint>

To refresh an API key, provide the number of days before the next expiry with the following endpoint:

<endpoint class="put">/api/catalogueUsers/**{catalogueUserId}**/apiKeys/**{apiKeyId}**/refresh/**{expiresInDays}**</endpoint> 

Finally, to delete an API key identified by a particular UUID:

<endpoint class="delete">/api/catalogueUsers/**{catalogueUserId}**/apiKeys/**{id}**</endpoint>


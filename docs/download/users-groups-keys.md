
Edit */opt/init/micronaut/application-mauro.yml* to look similar to this:

```yaml
mauro:
    users:
        -   email: admin@maurodatamapper.com
            first-name: admin
            last-name: admin
            temp-password: mypassword
    groups:
        -   name: Administrators
            description: optional description
            is-admin: true
            members:
                - admin@maurodatamapper.com
    api-keys:
        -   name: My first API Key
            email: admin@maurodatamapper.com
            key: optional UID key
            refreshable: true
            expiry: 2027-12-31
```
#### Users

| Field          | Purpose                              | Mandatory? |
|----------------|--------------------------------------|------------|
| email          | is the user name as an email address | Yes        |
| first-name     | First name                           | Yes        |
| last-name      | Last name                            | Yes        |
| temp-password  | A temporary/initial password         | Yes        |

#### Groups

| Field       | Purpose                                             | Mandatory? | Default |
|-------------|-----------------------------------------------------|------------|---------|
| name        | is the user name as an email address                | Yes        |         |
| description | Description of the group                            | No         | Blank   |
| is-admin    | Whether the members of the group are administrators | No         | false   |
| members     | A list of usernames                                 | No         | Empty   |

#### Api-keys

| Field       | Purpose                                                          | Mandatory? | Default              |
|-------------|------------------------------------------------------------------|------------|----------------------|
| name        | A unique name for the API key                                    | Yes        |                      |
| email       | The user the key belongs to                                      | Yes        |                      |
| key         | A given API key                                                  | No         | Creates a new key    |
| expiry      | yyyy-MM-dd date when the key will expire                         | No         | 1 Year from creation |
| refreshable | When the key expires, it may be refreshed with a new expiry date | No         | false                |

For any optional field, if you don't wish to set a value for it,
omit it from the configuration rather than including it as blank.

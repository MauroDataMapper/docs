### Proxy

If you intend to serve the container through a webserver acting as a proxy, you will need to ensure the host, port, and scheme
that webserver answers to are passed to the container by way of HTTP headers so that the container knows where it is surfacing.

In the webserver proxy configuration, ensure that there are headers set for at least Host and Scheme.
E.g. in nginx _proxy_params_ it might read:

```properties
proxy_set_header X-Forwarded-Host $http_host;
proxy_set_header X-Forwarded-Proto $scheme;
```

Edit */opt/init/micronaut/application-mauro.yml* and add a section like this:
```yaml
micronaut:
    server:
        host-resolution:
            protocol-header: X-Forwarded-Proto
            host-header: X-Forwarded-Host
            port-header: X-Forwarded-Port
```

Whenever a user's browser contacts your webserver (e.g. https://example.com), a proxy connection is made to the container. The webserver will set the
X-Forwarded-Host header (e.g. to example.com) and the X-Forwarded-Proto header (e.g. to https) when requesting from the container.

If your webserver is running on a port that is not for HTTP (port 80) nor for HTTPS (port 443), configure X-Forwarded-Port .

### CORS
By default, the container will run on your host and, if the -p 8080:80 parameter is using with *docker run*, will run on the live http port 80 on your host.
However, if you wish to access the User Interface and/or the API from a different 'origin', you will need to configure CORS (Cross-Origin Resource Sharing) to grant
access for that other 'origin'.

Any 'origin' is different from another when the domain name, port, or scheme (http, https) is different. For example, if the container is running on *yourhost.com*,
and *-p 8080:80* is configured, the web server will surface at http://yourhost.com .

Therefore, you will need to configure CORS for any of:

 * Using HTTPS (scheme change from HTTP)
 * Connecting from a different domain name
 * Connecting from a different port

Edit */opt/init/micronaut/application-mauro.yml* and add a section like this:
```yaml
micronaut:
  server:
    cors:
      enabled: true
      configurations:
        ui:
          allowed-origins:
            - https://myhost.com
```

'allowed-origins' is a list, add more if required. If you need more that information of CORS in micronaut, there are detailed examples [in the Micronaut documentation](https://docs.micronaut.io/latest/guide/#corsAllowedOrigins)

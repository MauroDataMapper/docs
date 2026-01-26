
The simplest installation uses a ready-made **Mauro Data Mapper** application running in a [Docker](https://www.docker.com) container.  
Any operating system (Windows, Linux, MacOS), being a server or a desktop, that runs **Docker** can run **Mauro Data Mapper**. (Note that
some organisations may restrict the use of **Docker** when running on virtual machines)

### System requirements
You will need to install [Docker](https://www.docker.com/get-started).

If you are using a desktop environment, it is handy to install [Docker Desktop](https://docs.docker.com/desktop/) first.

We advise running these docker images on an operating system with:

* a minimum of 4 CPU cores
* 8GBs RAM
* **Docker Engine:** 20.10.21 or higher
* the Docker engine can run arm64, or amd64 architectures

## Available Docker Images

These are the Docker images available to 'pull' in:

--8<-- "docs/download/docker-table.md"

By either:

- From your **terminal** run the corresponding 'pull command' from the above table for the image you wish to use.
- From **Docker Desktop** use the Images tab to pull the image from Hub repositories.

## Docker configuration / resources available

### Docker Desktop
On Docker Desktop, go to the Settings (a cog icon), then the resources,
and set the CPU limit to be at least 4 and the Memory limit to be at least 8GB. Press 'Apply & restart'

### Linux Docker
The default install of Docker inside Linux configures the Docker Engine with unlimited access to the server's resources.

<!--  LocalWords:  maurodatamapper Installation Docker Linux Desktop Terminal Native Images Requirements
 -->

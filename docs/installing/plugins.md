We host a number of community plugins, the code for which are available in
our [GitHub 'Plugins' organisation](https://github.com/MauroDataMapper-Plugins)
Commits to master branches kick off a build process on our continuous integration server, and successfully-built artefacts are hosted on our instance
of [Artifactory](https://jenkins.cs.ox.ac.uk/artifactory).

Below is a list of all available plugins, along with their latest version number, release date, and any dependencies it has. More details about the
changes in each release can be found on the [Release Notes](/about/release-notes) page. To install a plugin, use the 'artefact name' as directed in
the [Intallating](/installing/docker) page.

# Importers / Exporters

<table style="width: 100%;">
    <thead>
        <tr>
            <th style="width: 25%;"><b>Plugin Name / Version</b></th>
            <th style="width: 20%;"><b>Release Date</b></th>
            <th style="width: 25%;"><b>Artefact name</b></th>
            <th style="width: 30%;"><b>Dependencies</b></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>Excel</b><br/>2.0.0-SNAPSHOT</td>
            <td> ?? </td>
            <td>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-csv:2.0.0-SNAPSHOT</td>
            <td>Core &gt; 4.0.0</td>
        </tr>
        <tr>
            <td><b>CSV</b><br/>2.0.0-SNAPSHOT</td>
            <td> ?? </td>
            <td>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-excel:2.0.0-SNAPSHOT</td>
            <td>Core &gt; 4.0.0</td>
        </tr>
        <tr>
            <td><b>MS SQL Server</b><br/>3.0.0-SNAPSHOT</td>
            <td> ?? </td>
            <td>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-database-sqlserver:3.0.0-SNAPSHOT</td>
            <td>Core &gt; 4.0.0</td>
        </tr>
        <tr>
            <td><b>PostgreSQL</b><br/>2.1.0-SNAPSHOT</td>
            <td> ?? </td>
            <td>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-database-postgresql:2.1.0-SNAPSHOT</td>
            <td>Core &gt; 4.0.0</td>
        </tr>
        <tr>
            <td><b>MySQL</b><br/>1.0.1-SNAPSHOT</td>
            <td> ?? </td>
            <td>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-database-mysql:1.0.1-SNAPSHOT</td>
            <td>Core &gt; 4.0.0</td>
        </tr>
        <tr>
            <td><b>Oracle SQL</b><br/>1.0.1-SNAPSHOT</td>
            <td> ?? </td>
            <td>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-database-oracle:1.0.0-SNAPSHOT</td>
            <td>Core &gt; 4.0.0</td>
        </tr>
        <tr>
            <td><b>AWS Glue</b><br/>1.0.0-SNAPSHOT</td>
            <td> ?? </td>
            <td>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-awsglue:1.0.0-SNAPSHOT</td>
            <td>Core &gt; 4.0.0</td>
        </tr>
    </tbody>
</table>

# Profiles

<table style="width: 100%;">
    <thead>
        <tr>
            <th style="width: 25%;"><b>Plugin Name / Version</b></th>
            <th style="width: 20%;"><b>Release Date</b></th>
            <th style="width: 25%;"><b>Artefact name</b></th>
            <th style="width: 30%;"><b>Dependencies</b></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>schema.org</b><br/>1.2.2-SNAPSHOT</td>
            <td> ?? </td>
            <td>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-profile-schema-org:1.2.0-SNAPSHOT</td>
            <td>Core &gt; 4.0.0</td>
        </tr>
        <tr>
            <td><b>HDR UK</b><br/>1.2.2-SNAPSHOT</td>
            <td> ?? </td>
            <td>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-profile-hdruk:1.2.0-SNAPSHOT</td>
            <td>Core &gt; 4.0.0</td>
        </tr>
    </tbody>
</table>

# Security

<table style="width: 100%;">
    <thead>
        <tr>
            <th style="width: 25%;"><b>Plugin Name / Version</b></th>
            <th style="width: 20%;"><b>Release Date</b></th>
            <th style="width: 25%;"><b>Artefact name</b></th>
            <th style="width: 30%;"><b>Dependencies</b></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>Keycloak Authentication</b><br/>1.0.1</td>
            <td> ?? </td>
            <td>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-authentication-keycloak:1.0.1</td>
            <td>Core &gt; 4.0.0</td>
        </tr>
    </tbody>
</table>

# Technical / Other

<table style="width: 100%;">
    <thead>
        <tr>
            <th style="width: 25%;"><b>Plugin Name / Version</b></th>
            <th style="width: 20%;"><b>Release Date</b></th>
            <th style="width: 25%;"><b>Artefact name</b></th>
            <th style="width: 30%;"><b>Dependencies</b></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>Freemarker Templating</b><br/>1.0.0-SNAPSHOT</td>
            <td> ?? </td>
            <td>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-freemarker:1.0.0-SNAPSHOT</td>
            <td>Core &gt; 4.0.0</td>
        </tr>
        <tr>
            <td><b>Sparql</b><br/>1.0.0-SNAPSHOT</td>
            <td> ?? </td>
            <td>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-sparql:1.0.0-SNAPSHOT</td>
            <td>Core &gt; 4.0.0</td>
        </tr>
    </tbody>
</table>


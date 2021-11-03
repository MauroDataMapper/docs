We host a number of community plugins, the code for which is available in
our [GitHub 'Plugins' organisation](https://github.com/MauroDataMapper-Plugins).
Commits to master branches kick off a build process on our continuous integration server and successfully-built artefacts are hosted on our instance
of [Artifactory](https://jenkins.cs.ox.ac.uk/artifactory).

Below is a list of all the available plugins, along with their latest version number, release date and any dependencies each has. More details about the
changes in each release can be found on the [Release Notes](/about/release-notes) page. To install a plugin, use the **'artefact name'** as directed in
the [Installing](../docker) page.

---

## Importers / Exporters

<table style="width: 100%;">
    <thead>
        <tr>
            <th style="width: 20%;"><b>Plugin name<br/>Version</b></th>
            <th style="width: 15%;"><b>Release date</b></th>
            <th style="width: 45%;"><b>Artefact name</b></th>
            <th style="width: 15%;"><b>Dependencies</b></th>
        </tr>
    </thead>
    <tbody>
<tr>
            <td><b>ART-DECOR</b><br/>1.1.0</td>
            <td>2021-11-03</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-artdecor:1.1.0</code></td>
            <td>Core &gt;= 4.11.0</td>
        </tr>
<tr>
            <td><b>AWS Glue</b><br/>1.4.0</td>
            <td>2021-11-03</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-awsglue:1.4.0</code></td>
            <td>Core &gt;= 4.11.0</td>
        </tr>
<tr>
            <td><b>CSV</b><br/>3.0.0</td>
            <td>2021-05-17</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-csv:3.0.0</code></td>
            <td>Core &gt;= 4.5.0</td>
        </tr>
<tr>
            <td><b>Excel</b><br/>4.0.1</td>
            <td>2021-07-12</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-excel:4.0.1</code></td>
            <td>Core &gt;= 4.7.0</td>
        </tr>
<tr>
            <td><b>Digital Object Identifiers</b><br/>1.2.0</td>
            <td>2021-11-03</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-digital-object-identifiers:1.2.0</code></td>
            <td>Core &gt;= 4.11.0</td>
        </tr>
<tr>
            <td><b>FHIR</b><br/>1.1.0</td>
            <td>2021-08-08</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-fhir:1.1.0</code></td>
            <td>Core &gt;= 4.8.0</td>
        </tr>
<tr>
            <td><b>MS SQL</b><br/>6.1.0</td>
            <td>2021-11-03</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-database-sqlserver:6.1.0</code></td>
            <td>Core &gt;= 4.11.0</td>
        </tr>
<tr>
            <td><b>MySQL</b><br/>4.1.0</td>
            <td>2021-11-03</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-database-mysql:4.1.0</code></td>
            <td>Core &gt;= 4.11.0</td>
        </tr>
<tr>
            <td><b>Oracle SQL</b><br/>5.1.0</td>
            <td>2021-11-03</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-database-oracle:5.1.0</code></td>
            <td>Core &gt;= 4.11.0</td>
        </tr>
<tr>
            <td><b>PostgreSQL</b><br/>5.1.0</td>
            <td>2021-11-03</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-database-postgresql:5.1.0</code></td>
            <td>Core &gt;= 4.11.0</td>
        </tr>
</tbody>
</table>

---

## Profiles

<table style="width: 100%;">
    <thead>
        <tr>
            <th style="width: 20%;"><b>Plugin Name<br/>Version</b></th>
            <th style="width: 15%;"><b>Release Date</b></th>
            <th style="width: 45%;"><b>Artefact name</b></th>
            <th style="width: 15%;"><b>Dependencies</b></th>
        </tr>
    </thead>
    <tbody>
<tr>
            <td><b>DCAT</b><br/>1.0.0</td>
            <td>2021-11-03</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-profile-dcat:1.0.0</code></td>
            <td>Core &gt;= 4.11.0</td>
        </tr>
<tr>
            <td><b>Dementia Platform</b><br/>1.0.0</td>
            <td>2021-11-03</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-profile-dementia-platform:1.0.0</code></td>
            <td>Core &gt;= 4.11.0</td>
        </tr>
<tr>
            <td><b>HDR UK</b><br/>1.0.0</td>
            <td>2021-11-03</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-profile-hdruk:1.0.0</code></td>
            <td>Core &gt;= 4.11.0</td>
        </tr>
<tr>
            <td><b>Schema.org</b><br/>1.0.0</td>
            <td>2021-11-03</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-profile-schema-org:1.0.0</code></td>
            <td>Core &gt;= 4.11.0</td>
        </tr>
</tbody>
</table>
## Security

<table style="width: 100%;">
    <thead>
        <tr>
            <th style="width: 20%;"><b>Plugin name<br/>Version</b></th>
            <th style="width: 15%;"><b>Release date</b></th>
            <th style="width: 45%;"><b>Artefact name</b></th>
            <th style="width: 15%;"><b>Dependencies</b></th>
        </tr>
    </thead>
    <tbody>
<tr>
            <td><b>Keycloak Integrated Authentication</b><br/>2.0.0</td>
            <td>2021-05-17</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-authentication-keycloak:2.0.0</code></td>
            <td>Core &gt;= 4.5.0</td>
        </tr>
<tr>
            <td><b>OpenID Connect Authentication</b><br/>1.2.0</td>
            <td>2021-11-03</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-authentication-openid-connect:1.2.0</code></td>
            <td>Core &gt;= 4.11.0</td>
        </tr>
</tbody>
</table>

---

## Technical / Other

<table style="width: 100%;">
    <thead>
        <tr>
            <th style="width: 20%;"><b>Plugin name<br/>Version</b></th>
            <th style="width: 15%;"><b>Release date</b></th>
            <th style="width: 45%;"><b>Artefact name</b></th>
            <th style="width: 15%;"><b>Dependencies</b></th>
        </tr>
    </thead>
    <tbody>
<tr>
            <td><b>Freemarker Templating</b><br/>1.1.0</td>
            <td>2021-03-04</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-freemarker:1.1.0</code></td>
            <td>Core &gt;= 4.7.0</td>
        </tr>
<tr>
            <td><b>SPARQL</b><br/>1.1.1</td>
            <td>2021-03-24</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-sparql:1.1.1</code></td>
            <td>Core &gt;= 4.2.0</td>
        </tr>
</tbody>
</table>


<!--  LocalWords:  plugins Artifactory plugin thead tr th tbody td br
 -->
<!--  LocalWords:  gt PostgreSQL AWS Keycloak Freemarker Sparql
 -->

---
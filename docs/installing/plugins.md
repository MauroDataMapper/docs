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
            <td><b>ART-DECOR</b><br/>2.2.0</td>
            <td>2022-08-16</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-artdecor:2.2.0</code></td>
            <td>Core &gt;= 5.2.0</td>
        </tr>
        <tr>
            <td><b>AWS Glue</b><br/>2.2.0</td>
            <td>2022-08-16</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-awsglue:2.2.0</code></td>
            <td>Core &gt;= 5.2.0</td>
        </tr>
        <tr>
            <td><b>CSV</b><br/>4.3.0</td>
            <td>2023-02-24</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-csv:4.3.0</code></td>
            <td>Core &gt;= 5.3.0</td>
        </tr>
        <tr>
            <td><b>Digital Object Identifiers</b><br/>2.2.0</td>
            <td>2022-08-16</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-digital-object-identifiers:2.2.0</code></td>
            <td>Core &gt;= 5.2.0</td>
        </tr>
        <tr>
            <td><b>Excel</b><br/>5.2.0</td>
            <td>2022-08-16</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-excel:5.2.0</code></td>
            <td>Core &gt;= 5.2.0</td>
        </tr>
        <tr>
            <td><b>FHIR</b><br/>2.3.0</td>
            <td>2023-02-24</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-fhir:2.3.0</code></td>
            <td>Core &gt;= 5.3.0</td>
        </tr>
        <tr>
            <td><b>MS SQL</b><br/>8.2.0</td>
            <td>2023-02-24</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-database-sqlserver:8.2.0</code></td>
            <td>Core &gt;= 5.3.0</td>
        </tr>
        <tr>
            <td><b>MySQL</b><br/>7.2.0</td>
            <td>2023-02-24</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-database-mysql:7.2.0</code></td>
            <td>Core &gt;= 5.3.0</td>
        </tr>
        <tr>
            <td><b>Oracle SQL</b><br/>6.2.0</td>
            <td>2023-02-24</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-database-oracle:6.2.0</code></td>
            <td>Core &gt;= 5.3.0</td>
        </tr>
        <tr>
            <td><b>PostgreSQL</b><br/>7.2.0</td>
            <td>2023-02-24</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-database-postgresql:7.2.0</code></td>
            <td>Core &gt;= 5.3.0</td>
        </tr>
        <tr>
            <td><b>XMI</b><br/>1.0.0</td>
            <td>2023-02-24</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-xmi-visualparadigm:1.0.0</code></td>
            <td>Core &gt;= 5.3.0</td>
        </tr>
        <tr>
            <td><b>XSD</b><br/>1.2.0</td>
            <td>2022-08-16</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-xsd:1.2.0</code></td>
            <td>Core &gt;= 5.2.0</td>
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
            <td><b>DCAT</b><br/>2.2.0</td>
            <td>2022-08-16</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-profile-dcat:2.2.0</code></td>
            <td>Core &gt;= 5.2.0</td>
        </tr>
        <tr>
            <td><b>Dementia Platform</b><br/>2.2.0</td>
            <td>2022-08-16</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-profile-dementia-platform:2.2.0</code></td>
            <td>Core &gt;= 5.2.0</td>
        </tr>
        <tr>
            <td><b>HDR UK</b><br/>2.3.0</td>
            <td>2023-02-24</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-profile-hdruk:2.3.0</code></td>
            <td>Core &gt;= 5.3.0</td>
        </tr>
        <tr>
            <td><b>Schema.org</b><br/>2.3.0</td>
            <td>2023-02-24</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-profile-schema-org:2.3.0</code></td>
            <td>Core &gt;= 5.3.0</td>
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
            <td><b>Keycloak Integrated Authentication</b><br/>3.3.0</td>
            <td>2022-08-16</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-authentication-keycloak:3.3.0</code></td>
            <td>Core &gt;= 5.2.0</td>
        </tr>
        <tr>
            <td><b>OpenID Connect Authentication</b><br/>2.2.0</td>
            <td>2022-08-16</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-authentication-openid-connect:2.2.0</code></td>
            <td>Core &gt;= 5.2.0</td>
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
            <td><b>Freemarker Templating</b><br/>2.2.0</td>
            <td>2022-08-16</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-freemarker:2.2.0</code></td>
            <td>Core &gt;= 5.2.0</td>
        </tr>
        <tr>
            <td><b>SPARQL</b><br/>2.2.0</td>
            <td>2022-08-16</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-sparql:2.2.0</code></td>
            <td>Core &gt;= 5.2.0</td>
        </tr>
</tbody>
</table>




<!--  LocalWords:  plugins Artifactory plugin thead tr th tbody td br
 -->
<!--  LocalWords:  gt PostgreSQL AWS Keycloak Freemarker Sparql
 -->

---
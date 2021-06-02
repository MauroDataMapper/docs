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
            <td><b>art-decor</b><br/>1.0.0</td>
            <td>2021-03-04</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-artdecor:1.0.0</code></td>
            <td>Core &gt;= 4.2.0</td>
        </tr>
        <tr>
            <td><b>AWS Glue</b><br/>1.3.0</td>
            <td>2021-03-04</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-awsglue:1.3.0</code></td>
            <td>Core &gt;= 4.2.0</td>
        </tr>
        <tr>
            <td><b>CSV</b><br/>3.0.0</td>
            <td>2021-05-17</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-csv:3.0.0</code></td>
            <td>Core &gt;= 4.5.0</td>
        </tr>
        <tr>
            <td><b>Excel</b><br/>3.0.0</td>
            <td>2021-05-17</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-excel:3.0.0</code></td>
            <td>Core &gt;= 4.5.0</td>
        </tr>
        <tr>
            <td><b>FHIR</b><br/>1.0.0</td>
            <td>2021-05-17</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-fhir:1.0.0</code></td>
            <td>Core &gt;= 4.5.0</td>
        </tr>
        <tr>
            <td><b>MS SQL</b><br/>3.2.0</td>
            <td>2021-05-14</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-database-sqlserver:3.2.0</code></td>
            <td>Core &gt;= 4.2.0</td>
        </tr>
        <tr>
            <td><b>MySQL</b><br/>2.2.0</td>
            <td>2021-05-14</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-database-mysql:2.2.0</code></td>
            <td>Core &gt;= 4.2.0</td>
        </tr>
        <tr>
            <td><b>Oracle SQL</b><br/>3.2.0</td>
            <td>2021-05-14</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-database-oracle:3.2.0</code></td>
            <td>Core &gt;= 4.2.0</td>
        </tr>
        <tr>
            <td><b>PostgreSQL</b><br/>3.2.0</td>
            <td>2021-05-14</td>
            <td><code>uk.ac.ox.softeng.maurodatamapper.plugins:mdm-plugin-database-postgresql:3.2.0</code></td>
            <td>Core &gt;= 4.2.0</td>
        </tr>
    </tbody>
</table>

---

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
            <td>Core &gt;= 4.2.0</td>
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
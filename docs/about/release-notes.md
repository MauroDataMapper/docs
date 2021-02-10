This page describes the changes for each component: 'core', 'ui', and the various centrally-maintained plugins and client libraries. For each, a table
is presented with version number, notable new features, notable pull requests, and any dependencies.

For more information about the structure and architecture of the code, please see our [system architecture](/resources/architecture/) pages.

In general, we try to use [Semantic Versioning](https://semver.org). In particular note that any version tagged as `0.x.y` should be considered
'beta' or for testing purposes only. In our code repositories, we use [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/), and so
the 'main / [master](https://github.com/github/renaming)' branch may be considered stable, but 'bleeding edge' features may be available within '
develop' or any feature branch.

Please see our [Installing Plugins](/installing/plugins) pages for details about build artefacts, and dependencies.

## Core

[GitHub](https://github.com/MauroDataMapper/mdm-core)
<table width="100%">
    <thead>
        <tr>
            <th width="25%"><b>Version</b></th>
            <th width="25%"><b>Release Date</b></th>
            <th width="50%"><b>Major Changes</b><img height="1px" width="500px"/></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>4.0.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-core/releases/tag/4.0.0">(GitHub Link)</a></td>
            <td>5th Feb 2021</td>
            <td>
                <em>Listing major changes since last release of Metadata Catalogue</em>
                <ul>
                    <li>Upgrade to Grails 4</li>
                    <li>Complete refactoring of code and underlying database</li>
                    <li>Modular code structure</li>
                    <li>Reference Data Model</li> 
                    <li>Removed access controls for individuals, increased the options for groups</li>
                    <li>Updated Security Module</li>
                    <li>API Keys / Access Tokens</li>
                    <li>Much-improved support for branching and merging</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

## UI

[GitHub](https://github.com/MauroDataMapper/mdm-ui)

<table width="100%">
    <thead>
        <tr>
            <th width="25%"><b>Version</b></th>
            <th width="25%"><b>Release Date</b></th>
            <th width="50%"><b>Major Changes</b><img height="1px" width="500px"/></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>5.0.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-ui/releases/tag/5.0.0">(GitHub Link)</a></td>
            <td>5th Feb 2021</td>
            <td>
                <em>Listing major changes since last release of Metadata Catalogue</em>
                <ul>
                    <li>Upgrade to Angular 9</li>
                    <li>Modular code structure</li>
                    <li>Refactored, simplified layout to all screens</li>
                    <li>Reference Data Model</li> 
                    <li>API Keys / access tokens</li>
                    <li>WYSIWYG HTML editor</li>
                    <li>Much-improved support for branching and merging</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

## Client Libraries

### Java

[GitHub](https://github.com/MauroDataMapper/mdm-api-java-restful)
<table width="100%">
    <thead>
        <tr>
            <th width="25%"><b>Version</b></th>
            <th width="25%"><b>Release Date</b></th>
            <th width="50%"><b>Major Changes</b><img height="1px" width="500px"/></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>2.0.0</b><br/><a href="">(GitHub Link)</a></td>
            <td>TBC</td>
            <td>First major Mauro release</td>
        </tr>
    </tbody>
</table>

### .NET

[GitHub](https://github.com/MauroDataMapper/mdm-api-dotnet-restful)
<table width="100%">
    <thead>
        <tr>
            <th width="25%"><b>Version</b></th>
            <th width="25%"><b>Release Date</b></th>
            <th width="50%"><b>Major Changes</b><img height="1px" width="500px"/></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>???</b><br/><a href="">(GitHub Link)</a></td>
            <td>TBC</td>
            <td>First major Mauro release</td>
        </tr>
    </tbody>
</table>

### Typescript

[GitHub](https://github.com/MauroDataMapper/mdm-resources)
<table width="100%">
    <thead>
        <tr>
            <th width="25%"><b>Version</b></th>
            <th width="25%"><b>Release Date</b></th>
            <th width="50%"><b>Major Changes</b><img height="1px" width="500px"/></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>4.2.0</b><br/><a href="">(GitHub Link)</a></td>
            <td>5th Feb 2021</td>
            <td>First major Mauro release</td>
        </tr>
    </tbody>
</table>



## Plugins

### Importers / Exporters

**AWS Glue** ([GitHub](https://github.com/MauroDataMapper-Plugins/mdm-plugin-awsglue))
<table width="100%">
    <thead>
        <tr>
            <th width="25%"><b>Version</b></th>
            <th width="25%"><b>Release Date</b></th>
            <th width="50%"><b>Major Changes</b><img height="1px" width="500px"/></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>1.1.1</b><br/></td>
            <td>10th Feb 2021</td>
            <td>Fix regression bug relating to saving data models</td>
        </tr>
        <tr>
            <td><b>1.0.1</b><br/></td>
            <td>8th Feb 2021</td>
            <td>Fix dependencies</td>
        </tr>
        <tr>
            <td><b>1.0.0</b></td>
            <td>5th Feb 2021</td>
            <td>First major Mauro release</td>
        </tr>
    </tbody>
</table>

**CSV** ([GitHub](https://github.com/MauroDataMapper-Plugins/mdm-plugin-csv))
<table width="100%">
    <thead>
        <tr>
            <th width="25%"><b>Version</b></th>
            <th width="25%"><b>Release Date</b></th>
            <th width="50%"><b>Major Changes</b><img height="1px" width="500px"/></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>2.0.0</b></td>
            <td>5th Feb 2021</td>
            <td>First major Mauro release</td>
        </tr>
    </tbody>
</table>

**MySQL** ([GitHub](https://github.com/MauroDataMapper-Plugins/mdm-plugin-database-mysql))
<table width="100%">
    <thead>
        <tr>
            <th width="25%"><b>Version</b></th>
            <th width="25%"><b>Release Date</b></th>
            <th width="50%"><b>Major Changes</b><img height="1px" width="500px"/></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>2.0.0</b></td>
            <td>5th Feb 2021</td>
            <td>First major Mauro release</td>
        </tr>
    </tbody>
</table>

**Oracle DB** ([GitHub](https://github.com/MauroDataMapper-Plugins/mdm-plugin-database-oracle))
<table width="100%">
    <thead>
        <tr>
            <th width="25%"><b>Version</b></th>
            <th width="25%"><b>Release Date</b></th>
            <th width="50%"><b>Major Changes</b><img height="1px" width="500px"/></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>3.0.0</b></td>
            <td>5th Feb 2021</td>
            <td>First major Mauro release</td>
        </tr>
    </tbody>
</table>


**PostgreSQL** ([GitHub](https://github.com/MauroDataMapper-Plugins/mdm-plugin-database-postgresql))
<table width="100%">
    <thead>
        <tr>
            <th width="25%"><b>Version</b></th>
            <th width="25%"><b>Release Date</b></th>
            <th width="50%"><b>Major Changes</b><img height="1px" width="500px"/></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>3.0.0</b></td>
            <td>5th Feb 2021</td>
            <td>First major Mauro release</td>
        </tr>
    </tbody>
</table>

**MS SQL Server** ([GitHub](https://github.com/MauroDataMapper-Plugins/mdm-plugin-database-sqlserver))
<table width="100%">
    <thead>
        <tr>
            <th width="25%"><b>Version</b></th>
            <th width="25%"><b>Release Date</b></th>
            <th width="50%"><b>Major Changes</b><img height="1px" width="500px"/></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>3.0.0</b></td>
            <td>5th Feb 2021</td>
            <td>First major Mauro release</td>
        </tr>
    </tbody>
</table>

**MS Excel** ([GitHub](https://github.com/MauroDataMapper-Plugins/mdm-plugin-excel))
<table width="100%">
    <thead>
        <tr>
            <th width="25%"><b>Version</b></th>
            <th width="25%"><b>Release Date</b></th>
            <th width="50%"><b>Major Changes</b><img height="1px" width="500px"/></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>2.0.0</b></td>
            <td>5th Feb 2021</td>
            <td>First major Mauro release</td>
        </tr>
    </tbody>
</table>


### Profiles

### Technical

**Apache Freemarker** ([GitHub](https://github.com/MauroDataMapper-Plugins/mdm-plugin-freemarker))
<table width="100%">
    <thead>
        <tr>
            <th width="25%"><b>Version</b></th>
            <th width="25%"><b>Release Date</b></th>
            <th width="50%"><b>Major Changes</b><img height="1px" width="500px"/></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>1.0.0</b></td>
            <td>5th Feb 2021</td>
            <td>First major Mauro release</td>
        </tr>
    </tbody>
</table>



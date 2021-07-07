This page describes the changes for each component: 'core', 'ui', and the various centrally-maintained plugins and client libraries. For each, a table
is presented with version number, notable new features, notable pull requests, and any dependencies.


For more information about the structure and architecture of the code, please see our [technical architecture](/resources/architecture/) pages.

In general, we try to use [Semantic Versioning](https://semver.org). In particular note that any version tagged as `0.x.y` should be considered
'beta' or for testing purposes only. 

In our code repositories, we use [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/), and so the 'main / [master](https://github.com/github/renaming)' branch may be considered stable, but 'bleeding edge' features may be available within 'develop' or any feature branch.

Please see our [Installing Plugins](/installing/plugins) pages for details about build artefacts and dependencies.

---

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
            <td><b>4.7.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-core/releases/tag/4.7.0">(GitHub Link)</a></td>
            <td>1st July 2021</td>
            <td>
                <ul>
                    <li>Bug fixes for dynamic profiles</li>
                    <li>Further improvements for versioning, versioned folders, and merging model branches</li>
                    <li>Other bug fixes</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><b>4.6.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-core/releases/tag/4.6.0">(GitHub Link)</a></td>
            <td>18th June 2021</td>
            <td>
                <ul>
                    <li>Bug fixes for dynamic profiles</li>
                    <li>More endpoints for versioned folders and versioning</li>
                    <li>Improve performance of terminology importer</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><b>4.5.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-core/releases/tag/4.5.0">(GitHub Link)</a></td>
            <td>18th May 2021</td>
            <td>
                <ul>
                    <li>Dynamic Profiles</li>
                    <li>Initial endpoints for Versioned Folders</li>
                    <li>Add Facets to all containers</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><b>4.4.1</b><br/><a href="https://github.com/MauroDataMapper/mdm-core/releases/tag/4.4.1">(GitHub Link)</a></td>
            <td>22nd April 2021</td>
            <td>
                <ul>
                    <li>Hidden / internal importer parameters</li>
                    <li>ATOM feed for known models</li>
                    <li>Bug fixes</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><b>4.3.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-core/releases/tag/4.3.0">(GitHub Link)</a></td>
            <td>26th Mar 2021</td>
            <td>
                <ul>
                    <li>Multiple bug fixes</li>
                    <li>More control over admin system properties</li>
                    <li>Add change notes to the edit history</li>
                    <li>Custom tag names on model branches</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><b>4.2.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-core/releases/tag/4.2.0">(GitHub Link)</a></td>
            <td>4th Mar 2021</td>
            <td>
                <ul>
                    <li>DataModel component import feature</li>
                    <li>Dataflow importer / exporter in XML / JSON </li>
                    <li>Fix for Lucene indexing failure</li>
                    <li>Fix for exception during model import</li>
                    <li>Back-end performance improvements</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><b>4.1.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-core/releases/tag/4.1.0">(GitHub Link)</a></td>
            <td>10th Feb 2021</td>
            <td>
                <ul>
                    <li>Fix for multi-model imports</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><b>4.0.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-core/releases/tag/4.0.0">(GitHub Link)</a></td>
            <td>1st Feb 2021</td>
            <td>
                <em>Listing major changes since last release of Metadata Catalogue</em>
                <ul>
                    <li>Upgrade to Grails 4</li>
                    <li>Complete refactoring of code and underlying database</li>
                    <li>Modular code structure</li>
                    <li>Reference Data Model</li> 
                    <li>Removed access controls for individuals, increased the options for groups</li>
                    <li>Updated Security Module</li>
                    <li>API Keys / access tokens</li>
                    <li>Much improved support for branching and merging</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

---

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
            <td><b>6.3.1</b><br/><a href="https://github.com/MauroDataMapper/mdm-ui/releases/tag/6.3.1">(GitHub Link)</a></td>
            <td>18th June 2021</td>
            <td>
                <ul>
                    <li>Basic support for external authentication</li>
                    <li>Improved Export error handling</li>
                    <li>Update merge tool</li>
                    <li>Enable subscription functionality by default</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><b>6.2.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-ui/releases/tag/6.2.0">(GitHub Link)</a></td>
            <td>18th June 2021</td>
            <td>
                <ul>
                    <li>Context view on model tree</li>
                    <li>Versioned folder features</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><b>6.1.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-ui/releases/tag/6.1.0">(GitHub Link)</a></td>
            <td>18th May 2021</td>
            <td>
                <ul>
                    <li>Properties, annotations and rules available on folders</li>
                    <li>Bug fix for default datatypes</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><b>6.0.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-ui/releases/tag/6.0.0">(GitHub Link)</a></td>
            <td>22nd April 2021</td>
            <td>
                <ul>
                    <li>Refresh of most model view screens, maximizing screen usage</li>
                    <li>Support for structured profiles</li>
                    <li>Publish / subscribe functionality</li>
                    <li>Support for user-provided themes</li>
                    <li>Many other bug fixes</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><b>5.2.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-ui/releases/tag/5.2.0">(GitHub Link)</a></td>
            <td>26th Mar 2021</td>
            <td>
                <ul>
                    <li>New screens for administrator system properties</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><b>5.1.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-ui/releases/tag/5.1.0">(GitHub Link)</a></td>
            <td>4th Mar 2021</td>
            <td>
                <ul>
                    <li>Global progress indicator</li>
                    <li>Fix for Markdown link editing</li>
                    <li>Other fixes / performance improvements</li>
                </ul>
            </td>
        </tr>
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
                    <li>Much improved support for branching and merging</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

---
## Plugins, client libraries, others

Release notes for plugins, client libraries, and other Mauro repositories are not formally listed here for ease of maintenance.  However, you can 
view the latest versions of each plugin on the [Plugins page](../../installing/plugins).  More details about tagged releases and issues addressed 
can be found on the individual GitHub repos (see the 'tags' section to view all releases).
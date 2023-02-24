This page describes the changes for each component: 'core', 'ui', and the various centrally-maintained plugins and client libraries. For each, a table
is presented with version number, notable new features, notable pull requests, and any dependencies.

For more information about the structure and architecture of the code, please see our [technical architecture](/resources/architecture/) pages.

We use [Semantic Versioning](https://semver.org) for all repositories, please note that anything labelled with `-SNAPSHOT` is under development and should be considered 
potentially unstable.

In our code repositories, we use [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/), 
and so the 'main / [master](https://github.com/github/renaming)' branch may be considered stable, 
but 'bleeding edge' features may be available within 'develop' or any feature branch.

Please see our [Installing Plugins](/installing/plugins) pages for details about build artefacts and dependencies.

The current full release is **2023.1** (a.k.a B5.3.0_F7.3.0).

---

## Core API

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
			<td><b>5.3.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-core/releases/tag/5.3.0">(GitHub Link)</a></td>
			<td>24th February 2023</td>
			<td>
				<ul>
					<li>Updated to Grails 5.3.2 and Groovy 3.0.11</li>
					<li>Pagination, listing and folder tree fixes</li>
					<li>Federation support for subscribing to OAuth-secured feeds</li>
					<li>Initial support for running on Amazon Aurora RDS</li>
					<li>Other fixes and performance improvements</li>
				</ul>
			</td>
		</tr>
		<tr>
			<td><b>5.2.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-core/releases/tag/5.2.0">(GitHub Link)</a></td>
			<td>18th August 2022</td>
			<td>
				<ul>
					<li>Updated to Grails 5.1.9</li>
					<li>Federation support for subscribing to Atom feeds</li>
					<li>Permissions fixes and improvements</li>
				</ul>
			</td>
		</tr>
        <tr>
            <td><b>5.1.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-core/releases/tag/5.1.0">(GitHub Link)</a></td>
            <td>29th April 2022</td>
            <td>
                <ul>
                    <li>Updated to Groovy 3.0.10</li>
					<li>Improvements to Reference Data Models</li>
					<li>Performance fixes and improvements</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><b>5.0.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-core/releases/tag/5.0.0">(GitHub Link)</a></td>
            <td>28th January 2022</td>
            <td>
                <ul>
                    <li>Updated to Java 17 (Temurin)</li>
                    <li>Updated to Grails 5.1.2</li>
                    <li>Updated to Groovy 3.0.9</li>
                    <li>Updated to Gradle 7.3.3</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><b>4.11.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-core/releases/tag/4.11.0">(GitHub Link)</a></td>
            <td>3rd November 2021</td>
            <td>
                <ul>
                    <li>Updates and bug-fixes for Profiles, Subscribed Catalogues, Reference Data Models and more</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><b>4.10.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-core/releases/tag/4.10.0">(GitHub Link)</a></td>
            <td>2nd September 2021</td>
            <td>
                <ul>
                    <li>Add API endpoints for editing Reference Data Models</li>
                    <li>Configurable bootstrapping in production mode</li>
                    <li>Many improvements and bug-fixes to Versioned Folders, merging and branching</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><b>4.9.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-core/releases/tag/4.9.0">(GitHub Link)</a></td>
            <td>24th August 2021</td>
            <td>
                <ul>
                    <li>Allow profiles to be editable after finalisation</li>
                    <li>Add derived field types for profiles</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><b>4.8.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-core/releases/tag/4.8.0">(GitHub Link)</a></td>
            <td>7th August 2021</td>
            <td>
                <ul>
                    <li>Updates to branching and finalising for Versioned Folders</li>
                    <li>Speed increase on finalising models</li>
                    <li>Add rules to merge functionality</li>
                    <li>Handle system configuration in multiple .yml files</li>
                    <li>Various improvements to base import functionality</li>
                    <li>Other bug fixes</li>
                </ul>
            </td>
        </tr>
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
			<td><b>7.3.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-ui/releases/tag/7.3.0">(GitHub Link)</a></td>
			<td>24th February 2023</td>
			<td>
				<ul>
					<li>Updates to Profiles, Favourites, and Code Sets</li>
					<li>Wizards for creating Reference Data Types and Models</li>
					<li>Visual improvements</li>
					<li>Other improvements and fixes</li>
				</ul>
			</td>
		</tr>
		<tr>
			<td><b>7.2.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-ui/releases/tag/7.2.0">(GitHub Link)</a></td>
			<td>18th August 2022</td>
			<td>
				<ul>
					<li>Updates to Search pages</li>
					<li>Updates to Bulk Editor</li>
					<li>Display of asynchronous jobs</li>
				</ul>
			</td>
		</tr>
        <tr>
            <td><b>7.1.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-ui/releases/tag/7.1.0">(GitHub Link)</a></td>
            <td>29th April 2022</td>
            <td>
                <ul>
                    <li>Updates and fixes to UI components including navigation tree, dialogs, and editors</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><b>7.0.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-ui/releases/tag/7.0.0">(GitHub Link)</a></td>
            <td>28th January 2022</td>
            <td>
                <ul>
                    <li>Updated to Angular 12</li>
                    <li>Updated to Node 14.18.1</li>
                    <li>Updated to NPM 8.3.0</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><b>6.7.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-ui/releases/tag/6.7.0">(GitHub Link)</a></td>
            <td>3rd November 2021</td>
            <td>
                <ul>
                    <li>Update admin session dashboard</li>
                    <li>Features for importing / extending data model components</li>
                    <li>Many updates and bug-fixes to a range of components (see full list on GitHub)</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><b>6.6.1</b><br/><a href="https://github.com/MauroDataMapper/mdm-ui/releases/tag/6.6.1">(GitHub Link)</a></td>
            <td>22nd September 2021</td>
            <td>
                <ul>
                    <li>Open ID Connect redirect issue fixed</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><b>6.6.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-ui/releases/tag/6.6.0">(GitHub Link)</a></td>
            <td>2nd September 2021</td>
            <td>
                <ul>
                    <li>Term search within Terminology fixed</li>
                    <li>Fix for advanced search within a folder</li>
                    <li>Improvements to merge diff tool</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><b>6.5.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-ui/releases/tag/6.5.0">(GitHub Link)</a></td>
            <td>24th August 2021</td>
            <td>
                <ul>
                    <li>Improvements to profiles and other DOI profile functionality</li>
                    <li>Fix to favourite highlighting</li>
                    <li>DataFlow presentation no-longer using paginated call</li>
                    <li>Open ID Connect conformance issue resolved</li>
                    <li>Various other bug fixes and layout improvements</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><b>6.4.0</b><br/><a href="https://github.com/MauroDataMapper/mdm-ui/releases/tag/6.4.0">(GitHub Link)</a></td>
            <td>7th August 2021</td>
            <td>
                <ul>
                    <li>Fix for making models publicly readable</li>
                    <li>DOI functionality (requires plugin)</li>
                    <li>Multiple updates to model merging tool</li>
                    <li>Fix to merge graph for Versioned Folders</li>
                    <li>Drag-and-drop ordering for Data Elements</li>
                    <li>"Select all" option for adding Terms to a Codeset</li>
                    <li>Tree icons for model items</li>
                    <li>Various other bug fixes</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><b>6.3.1</b><br/><a href="https://github.com/MauroDataMapper/mdm-ui/releases/tag/6.3.1">(GitHub Link)</a></td>
            <td>1st July 2021</td>
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
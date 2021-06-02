**Mauro Data Mapper** is an open source tool, supported by a small core team of developers who welcome contributions from the user community. 

There are
many ways to contribute, but before doing so we recommend that you join our community through our
[Zulip organisation](https://maurodatamapper.zulipchat.com) so that you can understand the priorities and see which tasks are already in progress. We
welcome any contributions, however small, and will ensure any contribution is credited appropriately.

Our immediate general priorities are in bug fixes, documentation, and the creation of plugins. In each case, we have tooling or templates to help get
started and the core development team are happy to provide additional support for contributing activities.

Before contributing to any of our repositories, please have a read of our **Contributor License Agreement**. Any submissions to our repositories will
be under this agreement to ensure that our code stays free of any further restrictions.

---

## Documentation

New members of the community and those with little experience collaborating with an Open Source community may like to start here. Our documentation
is under constant evaluation and improvement: screenshots and instructions need updating; API documentation needs further elaboration and examples while
user guides to new features need writing and updating. We're particularly interested in real-world examples of usage - experience reports that can be
turned into 'how-to' guides for others wanting to use **Mauro** in the future. Many of the examples we have are based on health data, so we're also keen
to get examples from other domains too.

The documentation can be found in the **'docs'** repository in the Mauro Github organisation; clone the repository into a suitable location. The whole
documentation website can be built using the [MkDocs tool](https://www.mkdocs.org). Follow the instructions to install it locally and run
`mkdocs serve` to build and host a version on your local machine. This will automatically update as you make changes to the source files.

Please create a new branch with your changes and submit a pull request with your changes when you're ready to submit them. Before accepting, we will
check for the following properties:

- That there are no conflicts with the existing **'develop'** branch of the documentation
- That there are no spelling mistakes or grammatical errors
- That there are no broken or invalid links in the new text

We may also ask some community members to review changes before they are published. Please add comments to your pull request to guide us on how best
to accept your changes.

Once your pull request has been accepted, the changes will be uploaded to the Github help pages as part of the next documentation **'release'**.

---

## Bug fixes

For developers getting started with our code base, fixing bugs is a great place to start. Lists of open issues are available on our Youtrack and
GitHub sites, or you may have found your own issue you'd like to dive in and fix. All our repositories use
the [GitFlow](https://nvie.com/posts/a-successful-git-branching-model/) model for managing code branches. New work should be created in a feature
branch. Our core repositories act on a **'pull request'** system and each repository will have criteria to meet before committing code. For the **Core** and
**UI** repositories, more information is given below.

With all contributions to the source code, we recommend you engage with the community first, to make sure no work is duplicated, and to understand the
current priorities.

### Core

The **Core** code is built using Gradle and Grails. Instructions for getting the code running locally are provided in the repository's README file.
Before accepting any pull requests, the core team will:

- Checkout the relevant branch and check that any new functionality works correctly
- Run all integration and unit tests (where this hasn't already been done by our build servers)
- Run `lint` tools over the code to ensure new code meets existing quality checks

Pull requests will only be accepted where there are no conflicts with the existing **'develop'** branch.

Developers are encouraged to run these checks on any pull request before submission, to ensure that they can be merged quickly.

### UI

The **UI** project is build using `npm` and `ng` and instructions for getting the code running locally are provided in the repository's README file. In
order to build against a working back-end server, you might like to first check-out the **Core** code and get that running, or use our Docker
installation to bring up a back-end which your copy of the web interface can communicate with.

Before approving a pull request in the **UI** repository, the core team will:

- Checkout the relevant branch and check that any new functionality works correctly
- run `ng test` to ensure that all tests pass correctly
- run `ng lint` and `npm run eslint` to check that any code changes are sensible
- check through the diff of the current branch to look for any unintended changes

Pull requests will only be accepted where there are no conflicts with the existing **'develop'** branch.

Developers are encouraged to run these checks on any pull request before submission, to ensure that they can be merged quickly.

---

## Plugin development

[Back-end plugins](../../resources/architecture/#grails-plugins) can be written to provide functionality for specific use cases. They can make use of
existing code **'hooks'**, such as importers, exporters, and profiles or they may simply provide additional API endpoints for particular purposes. 

The **Mauro Data Mapper** Plugins Github organisation provides template plugins for these use cases, which can be cloned and used as a starting point 
for the development of a new plugin.  

If your plugin has universal appeal, we'd be happy to host it within our organisation so that other users can find it.  Otherwise we can advertise 
it through these pages, or keep a pinned list within Zulip.


## Share your models

The development team would be pleased to receive details of any models that we might be able to re-use - either for sharing with the community,
or example models that can be used for demo purposes.

For real-world models that will be useful to other members of the community, we intend to use these pages to advertise either downloadable files, or
URLs that can be used to access publicly available models.

Please pay particular care to any copyright or licensing information on the model itself before sharing.   

---
<!--  LocalWords:  Zulip plugins Github MkDocs mkdocs Github Youtrack
 -->
<!--  LocalWords:  GitFlow npm eslint Plugin Github plugin
 -->

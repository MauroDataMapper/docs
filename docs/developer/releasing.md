# Releasing

The following process should be followed EXACTLY to release MauroDataMapper in its entirety. Please pay attention to versions and whats changed
between each git commit.

!!! Warning

    You will need git flow installed in the command line to be able to perform the release.
    Installation instructions are [here](https://github.com/nvie/gitflow/wiki/Installation).
    You will also need to make sure all your repositories are initialised as git-flow repositories.
    This can be done using `git flow init`, 
    however you MUST make sure you have checked out the `develop` and `main` branches before you initialise.

!!! Information

    Unless patching a release which has failed ALL releases should be the next MINOR release.
    If there is significant and appropriate change then a MAJOR release should be used.
    A PATCH release should only be done if the MINOR release failed and this is a release being done to fix that release failure.

!!! Information

    A unified view of the current build status of develop and main branches can be see [here](../build_status)

You should identify the following from the repositories before starting

* CORE_VERSION : The appropriate non-snapshot version from mdm-core/gradle.properties on the develop branch
* UI_VERSION : The appropriate non-snapshot version from mdm-ui/package.json on the develop branch

## mdm-core

```bash
git checkout main && git pull && git checkout develop && git pull
git flow release start ${CORE_VERSION}
```

Update gradle.properties

```bash
git commit -am "Release ${CORE_VERSION}"
git flow release finish -m "${CORE_VERSION}" ${CORE_VERSION}
```

Update gradle.properties to next minor snapshot

```bash
git commit -am 'Next snapshot'
git checkout main && git push && git checkout develop && git push && git push --tags
```

## mdm-resources

```bash
git checkout main && git pull && git checkout develop && git pull
git flow release start ${CORE_VERSION}
```

Update package.json version to CORE_VERSION

```bash
npm install && npm run build
git commit -am "Release ${CORE_VERSION}"
git flow release finish -m "${CORE_VERSION}" ${CORE_VERSION}
```

Update package.json version to next snapshot CORE_VERSION

```bash
npm install && npm run build
git commit -am 'Next snapshot'
git checkout main && git push && git checkout develop && git push && git push --tags
```

## mdm-ui

!!! Warning

    You must release mdm-resources first, or be able to use an existing release of mdm-resources

```bash
git checkout main && git pull && git checkout develop && git pull
git flow release start ${UI_VERSION}
```

Update package.json

* `version` to UI_VERSION
* `"@maurodatamapper/mdm-resources": "git+https://github.com/MauroDataMapper/mdm-resources.git#CORE_VERSION",`

```bash
npm install
```

!!! Caution

    MAKE SURE in `package.lock` that all the lines for mdm-resources that have a commit hash MATCH the hash for the release, 
    if NOT then delete all entries in the lock file for mdm-resources with a commit hash and run npm install again

```bash
git commit -am "Release ${UI_VERSION}"
git flow release finish -m "${UI_VERSION}" ${UI_VERSION}
```

Update package.json

* `version` to next minor snapshot UI_VERSION
* `"@maurodatamapper/mdm-resources": "git+https://github.com/MauroDataMapper/mdm-resources.git#develop",`

```bash
npm install
git commit -am 'Next snapshot'
git checkout main && git push && git checkout develop && git push && git push --tags
```

## mdm-application-build

!!! Warning

    You will need to wait for the main branch of mdm-core to finish before proceeding on the latest mdm-application-build

```bash
git checkout main && git pull && git checkout develop && git pull
git flow release start ${CORE_VERSION}
```

Update gradle.properties

```bash
git commit -am "Release ${CORE_VERSION}"
git flow release finish -m "${CORE_VERSION}" ${CORE_VERSION}
```

Update gradle.properties to next minor snapshot

```bash
git commit -am 'Next snapshot'
git checkout main && git push && git checkout develop && git push && git push --tags
```

## MDM plugins

!!! Warning

    You will need to wait for the main branch of mdm-core to finish before proceeding on the latest plugins

!!! Information

    This [repository](https://github.com/MauroDataMapper-Plugins/mdm-plugins) provides useful scripts and a unified live view 
    of the state of each branch build.

### Release Order

You will need to push some of the repositories in the correct order as they have dependencies on other plugins. The following plugins have a release
order, if not listed then there is not required order.

1. mdm-plugin-database
2. mdm-plugin-testing-utils
    1. mdm-plugin-database-mysql
    2. mdm-plugin-database-oracle
    3. mdm-plugin-database-postgresql
    4. mdm-plugin-database-sqlserver

### No changes waiting to be released

* You don't need to release these every time we release mdm-core
* However you should make sure all `develop` branches are updated to `mdmCoreVersion=${CORE_VERSION}` and then push the update.
* Any jobs which fail will need to have the code updated.
* If any of the code changes are in side the code base (not test changes) then you will need to release
* If only test code changes are needed or no changes are needed then don't do a release as we have proved it's still compatible

### Changes waiting to be released

* You should make sure the `develop` branch is updated to `mdmCoreVersion=${CORE_VERSION}` and then push the update
* Any tests which fail will need to have the code updated
* If any of the code changes are in side the code base (not test changes) then you will need to release with an updated `mdmCoreVersion`
* If only test code changes are needed or no changes are needed then release using the last `mdmCoreVersion` used as its still compatible

```bash
git checkout main && git pull && git checkout develop && git pull
git flow release start ${PLUGIN_VERSION}
```

* Update gradle.properties
* Update README.md "How to apply"

```bash
git commit -am "Release ${PLUGIN_VERSION}"
git flow release finish -m "${PLUGIN_VERSION}" ${PLUGIN_VERSION}
```

* Update gradle.properties to next minor snapshot
* DO NOT change the README.md file

```bash
git commit -am 'Next snapshot'
git checkout main && git push && git checkout develop && git push && git push --tags
```

## mdm-docker

!!! Warning

    You will need to wait for the main branch of mdm-application-build and mdm-ui to finish before proceeding

```bash
git checkout main && git pull && git checkout develop && git pull
git flow release start "B${CORE_VERSION}_F${UI_VERSION}"
```

Update docker-compose.yml

* The 2 commit ARGS
* The image tag to `B${CORE_VERSION}_F${UI_VERSION}`

Dry run and check it comes up as expected

```bash
docker-compose build
docker-compose up
```

If it all comes up.

```bash
git commit -am "Release B${CORE_VERSION}_F${UI_VERSION}"
git flow release finish -m "B${CORE_VERSION}_F${UI_VERSION}" "B${CORE_VERSION}_F${UI_VERSION}"
git checkout main && git push && git checkout develop && git push && git push --tags
```

## Document & Announce

!!! Information

    To be able to autogenerate the release documentation for plugins you will need to clone https://github.com/MauroDataMapper-Plugins/mdm-plugins.
    Then place all the plugins into this directory.

!!! Warning

    Remember to remove the following from the autogenerated plugins release output
    
    * Private Repositories
    * Unreleased plugins


### Documentation

This should be performed inside the `docs` repository.

```bash
git checkout main && git pull && git checkout develop && git pull
git flow release start "B${CORE_VERSION}_F${UI_VERSION}"
```

* Run `./releases.sh` in mdm-plugins.
* Remove the private repositories from the HTML format and copy into the `installing/plugins.md` file

```bash
git commit -am "Release B${CORE_VERSION}_F${UI_VERSION}"
git flow release finish -m "B${CORE_VERSION}_F${UI_VERSION}" "B${CORE_VERSION}_F${UI_VERSION}"
git checkout main && git push && git checkout develop && git push && git push --tags
```

### Zulip Announce

* Run `./releases.sh` in mdm-plugins.
* Copy the below markdown block into the `announce` stream of Zulip
* Update the versions for the applications
* Copy in the plain text format of the "releases" output underneath it

```markdown
# New Release

| Application | Version |
|-----------------|-----------|
| Docker | `B4.7.0_F6.3.1` |
| RESTful API | `4.7.0` |
| UI | `6.3.1` |
```

### Github

Each of the repositories requires the tag to be released and links to the issues fixed supplied.

* Navigate to the supplied tags page
* Select the latest tag and choose "Create release"
* Copy in the appropriate text from the below list, making sure to update 
  * the stated YouTrack version to the tag being released
  * the stated Github milestone

`mdm-core`
: [Tags Page](https://github.com/MauroDataMapper/mdm-core/tags)
    ```markdown
    See [Issues fixed](https://metadatacatalogue.myjetbrains.com/youtrack/issues/MC?q=%23Released%20%23B4.8.0)
    and [Milestones](https://github.com/MauroDataMapper/mdm-core/issues?q=is%3Aissue+milestone%3A4.8.0)
    ```
`mdm-ui`
: [Tags Page](https://github.com/MauroDataMapper/mdm-ui/tags)
    ```markdown
    See [Issues fixed](https://metadatacatalogue.myjetbrains.com/youtrack/issues/MC?q=%23Released%20%23F6.4.0)
    and [MileStones](https://github.com/MauroDataMapper/mdm-ui/issues?q=is%3Aissue+milestone%3A6.4.0)
    ```
`mdm-application`
: [Tags Page](https://github.com/MauroDataMapper/mdm-application-build/tags)
    ```markdown
    See [Issues fixed](https://metadatacatalogue.myjetbrains.com/youtrack/issues/MC?q=%23Released%20%23B4.8.0)
    and [Core Milestones](https://github.com/MauroDataMapper/mdm-core/issues?q=is%3Aissue+milestone%3A4.8.0)
    and [Application Milestones](https://github.com/MauroDataMapper/mdm-application-build/issues?q=is%3Aissue+milestone%3A4.8.0)
    ```
`mdm-docker`
: [Tags Page](https://github.com/MauroDataMapper/mdm-docker/tags)
    ```markdown
    See [Issues fixed](https://metadatacatalogue.myjetbrains.com/youtrack/issues/MC?q=%23Released%20%23B4.8.0%20%23F6.4.0)
    and [Core Milestones](https://github.com/MauroDataMapper/mdm-core/issues?q=is%3Aissue+milestone%3A4.8.0)
    and [Application Milestones](https://github.com/MauroDataMapper/mdm-application-build/issues?q=is%3Aissue+milestone%3A4.8.0)
    and [UI Milestones](https://github.com/MauroDataMapper/mdm-ui/issues?q=is%3Aissue+milestone%3A6.4.0)
    ```
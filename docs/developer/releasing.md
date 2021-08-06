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

You should identify the following from the repositories before starting

* CORE_VERSION : The appropriate non-snapshot version from mdm-core/gradle.properties on the develop branch
* UI_VERSION : The appropriate non-snapshot version from mdm-ui/package.json on the develop branch

## mdm-core

```bash
git checkout main && git pull && git checkout develop && git pull
git flow release start CORE_VERSION
```

Update gradle.properties

```bash
git commit -am 'Release CORE_VERSION'
git flow release finish 'CORE_VERSION'
```

Update gradle.properties to next minor snapshot

```bash
git commit -am 'Next snapshot'
git checkout main && git push && git checkout develop && git push && git push --tags
```

## mdm-resources

```bash
git checkout main && git pull && git checkout develop && git pull
git flow release start CORE_VERSION
```

Update package.json version to CORE_VERSION

```bash
npm install && npm run build
git commit -am 'Release CORE_VERSION'
git flow release finish 'CORE_VERSION'
```

Update package.json version to next snapshot CORE_VERSION

```bash
npm install
npm run build
git commit -am 'Next snapshot'
git checkout main && git push && git checkout develop && git push && git push --tags
```

## mdm-ui

You must release mdm-resources first, or be able to use an existing release of mdm-resources

```bash
git checkout main && git pull && git checkout develop && git pull
git flow release start UI_VERSION
```

Update package.json

* `version` to UI_VERSION
* `"@maurodatamapper/mdm-resources": "git+https://github.com/MauroDataMapper/mdm-resources.git#CORE_VERSION",`

```bash
npm install
```

!!! Caution

    MAKE SURE in `package.lock` that all the lines for mdm-resources that have a commit hash MATCH the hash for the release, 
    if NOT then delete all entries in the lock file for mdm-resources with a commit hash (2) and run npm install again

```bash
git commit -am 'Release UI_VERSION'
git flow release finish 'UI_VERSION'
```

Update package.json

* `version` to next minor snapshot UI_VERSION
* `"@maurodatamapper/mdm-resources": "git+https://github.com/MauroDataMapper/mdm-resources.git#develop",`

```bash
npm install
git commit -am 'Next snapshot'
git checkout main && git push && git checkout develop && git push && git push --tags
```

The next steps are required until we get Jenkins distributing the archive to artifactory

Checkout the release

```bash
git checkout UI_VERSION
```

Perform a clean install

```bash
npm ci
```

Build the distribution

```bash
npm run dist
```

There will now be a `tgz` file in the `dist` folder with the name `mdm-ui-${UI_VERSION}.tgz`. This needs to be deployed to artifactory.

1. Navigate to https://jenkins.cs.ox.ac.uk/ui/packages and log in.
1. Navigate to https://jenkins.cs.ox.ac.uk/ui/repos/tree/General/libs-release-local%2Fuk%2Fac%2Fox%2Fsofteng%2Fmaurodatamapper
1. Click 'Deploy' in the top right
1. Choose 'Single Deploy' and drop in the tgz file from the `dist` folder
1. Check then "Deploy as Maven Artifact"
    * Group ID : `uk.ac.ox.softeng.maurodatamapper`
    * Artifact ID : `mdm-ui`
    * Version : UI_VERSION
    * Classifier : LEAVE BLANK
    * Type: `tgz`
1. Click "Deploy"

## mdm-application-build

!!! Warning

    You will need to wait for the main branch of mdm-core to finish before proceeding on the latest mdm-application-build

```bash
git checkout main && git pull && git checkout develop && git pull
git flow release start CORE_VERSION
```

Update gradle.properties

```bash
git commit -am 'Release CORE_VERSION'
git flow release finish 'CORE_VERSION'
```

Update gradle.properties to next minor snapshot

```bash
git commit -am 'Next snapshot'
git checkout main && git push && git checkout develop && git push && git push --tags
```

## MDM plugins

!!! Warning

    You will need to wait for the main branch of mdm-core to finish before proceeding on the latest plugins

### No changes waiting to be released

* You don't need to release these every time we release mdm-core
* However you should make sure all `develop` branches are updated to `mdmCoreVersion=CORE_VERSION` and then push the update.
* Any jobs which fail will need to have the code updated.
* If any of the code changes are in side the code base (not test changes) then you will need to release
* If only test code changes are needed or no changes are needed then don't do a release as we have proved it's still compatible

### Changes waiting to be released

* You should make sure the `develop` branch is updated to `mdmCoreVersion=CORE_VERSION` and then push the update
* Any tests which fail will need to have the code updated
* If any of the code changes are in side the code base (not test changes) then you will need to release with an updated `mdmCoreVersion`
* If only test code changes are needed or no changes are needed then release using the last `mdmCoreVersion` used as its still compatible

```bash
git checkout main && git pull && git checkout develop && git pull
git flow release start PLUGIN_VERSION
```

* Update gradle.properties
* Update README.md "How to apply"

```bash
git commit -am 'Release PLUGIN_VERSION'
git flow release finish 'CORE_VERSION'
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
git flow release finish "B${CORE_VERSION}_F${UI_VERSION}"
git checkout main && git push && git checkout develop && git push && git push --tags
```

## Announce & Document

!!! Information

    To be able to autogenerate the release documentation for plugins you will need to clone https://github.com/MauroDataMapper-Plugins/mdm-plugins.
    Then place all the plugins into this directory.

!!! Warning

    Remember to remove the private repos from the autogenerated plugins release output

* Run `./releases.sh` in mdm-plugins.
* Documentation
    * Remove the private repositories from the HTML format and copy into the `docs/installing/plugins.md` file
    * Release the docs
* Zulip
    * Copy the below markdown block into the `announce` stream of Zulip
    * Update the versions for the applications
    * Xopy in the plain text format of the "releases" output underneath it

```markdown
# New Release

| Application | Version |
|-----------------|-----------|
| Docker | `B4.7.0_F6.3.1` |
| RESTful API | `4.7.0` |
| UI | `6.3.1` |
```
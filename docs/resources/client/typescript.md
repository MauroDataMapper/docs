## Introduction

The typescript library that implements communication with the back-end server is available as a stand-alone repository for incorporation into 
other applications - for example other web interfaces, or back-end functionality using `node.js`.  

The GitHub repository is called `mdm-resources` and is available within the [Mauro Data Mapper organisation](https://github.com/MauroDataMapper).


## API documentation

The API is documented using TypeDoc and the complete documentation can be [found here](./typedoc/index.html).

## Layout

Methods to call API functions are roughly broken down by resource type, with filenames conforming to the pattern:

`mdm-{resourceType}.resource.ts`

There are additional utility functions available in `mdm-validator.ts` and `mdm-resource.ts`.  An `index.ts` file lists all files for inclusion.

Each resource file defines a new class extending `MdmResource`, and provides methods for each endpoint.  These make use of the `simpleGet`, 
`simplePost`, etc methods defined in the super class.

## Including in applications

If you're using [Yarn](https://yarnpkg.com) or [NPM](https://www.npmjs.com), then you need the following line in your `.npmrc` or `.yarnrc` file:

```
@maurodatamapper:registry=https://npm.pkg.github.com`
```

You can then add a line such as the following to your `package.json` file:

```json
"dependencies": {
  ...  
  "@maurodatamapper/mdm-resources": "github:MauroDataMapper/mdm-resources#{version}"
}
```

Where `{version}` refers to a git tag or branch name.  

Within a typescript file, you can then add an import statement such as the following:

```typescript
import { MdmResourcesConfiguration } from '@maurodatamapper/mdm-resources';
```

or, as illustrated in the Mauro UI application, create a custom service to pull all the classes into a single location (see 
`mdm-resources.service.ts` within the `mdm-ui` project). 

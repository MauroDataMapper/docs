## Introduction

The TypeScript client library wraps the [REST API](../../rest-api/introduction.md) in TypeScript classes/functions to make it easy for 
JavaScript and TypeScript developers to interact with a Mauro instance. The TypeScript library that implements communication with the back-end 
server is available as a stand-alone repository for incorporation into other applications - for example other web interfaces, or back-end 
functionality using `node.js`.  This is in fact the client library that the **Mauro Data Mapper** user interface uses.

The GitHub repository is called `mdm-resources` and is available within the [Mauro Data Mapper organisation](https://github.com/MauroDataMapper).


## API documentation

The API is documented using [TypeDoc](https://typedoc.org/) and the complete documentation can be [found here](./typedoc/index.html).

## Layout

Methods to call API functions are roughly broken down by resource type, with filenames conforming to the pattern:

`mdm-{resourceType}.resource.ts`

There are additional utility functions available in `mdm-validator.ts` and `mdm-resource.ts`.  An `index.ts` file lists all files for inclusion.

## Resources

Each `mdm-{resourceType}.resource.ts` file defines a new class extending the super class [MdmResource](./typedoc/classes/mdmresource.html), and provides 
methods for each endpoint.  These make use of the [simpleGet()](./typedoc/classes/mdmresource.html#simpleget), 
[simplePost()](./typedoc/classes/mdmresource.html#simplepost), etc methods defined in the super class.

Every class that extends [MdmResource](./typedoc/classes/mdmresource.html) can optionally provide these in the 
[constructor](./typedoc/classes/mdmresource.html#constructor):

* [MdmResourcesConfiguration](./typedoc/classes/mdmresourcesconfiguration.html) - object to define configuration options for every HTTP request.
* [IMdmRestHandler](./typedoc/interfaces/imdmresthandler.html) - object to the REST handler that will process the requests. If not provided, the
[DefaultMdmRestHandler](./typedoc/classes/defaultmdmresthandler.html) will be used - see the [REST Handlers](#rest-handlers) section for further 
details.

## Including in applications

If you are using [NPM](https://www.npmjs.com) or [Yarn](https://yarnpkg.com), then you need the following line in your `.npmrc` or `.yarnrc` file:

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

Within a TypeScript file, you can then add an `import` statement such as the following:

```typescript
import { MdmResourcesConfiguration } from '@maurodatamapper/mdm-resources';
```

or, as illustrated in the Mauro UI application, create a custom service to pull all the classes into a single location (see 
`mdm-resources.service.ts` within the `mdm-ui` project).

## REST Handlers

`mdm-resources` provides a default implementation of the [IMdmRestHandler](./typedoc/interfaces/imdmresthandler.html) called 
[DefaultMdmRestHandler](./typedoc/classes/defaultmdmresthandler.html). This implementation uses the 
[fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) API to complete HTTP requests and return 
[promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) on each response.

This default implementation is usually sufficient for most scenarios, but it is also possible to replace this with your own implementation.
Reasons why you might want to do this are:

1. To use something other than `fetch()`. For example, Angular applications tend to use the built-in 
[HTTP Client](https://angular.io/guide/http) to return observable streams instead of promises.
2. To intercept any Mauro HTTP requests/responses to perform some custom operations, such as error handling on failed responses.

To use a custom REST handler, follow the steps below:

```typescript
// Define the class that implements `IMdmRestHandler`
export class CustomMdmRestHandler implements IMdmRestHandler {
  process(url: string, options: IMdmRestHandlerOptions) {
    // (Optional) pre-process step (e.g. logging)

    const response = /* Send HTTP request */

    // (Optional) post-process step (e.g. logging, error handling)

    return response;
  }
}

// For every MDM resource created, pass in the custom REST handler instance instead
const dataModelsResource = new MdmDataModelResource(null, new CustomMdmRestHandler());
```
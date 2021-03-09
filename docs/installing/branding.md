## Introduction

The Mauro Data Mapper Web interface can be customised to match an organisation's brand or styling. Creating a new theme requires developer effort, the
steps of which are detailed below.

### Angular Material

The [Angular Material](https://material.angular.io/) framework, which the UI uses for layout and controls, can support multiple themes (colour
palettes and typography), and can support dynamic switching of themes. However, the themes must be _precompiled_ into the application as part of the
stylesheets for the site. This means that themes must be prepared by a developer.

See also:

* [Angular Material theming guide](https://material.angular.io/guide/theming)
* [Theming your components](https://material.angular.io/guide/theming-your-components)

## Themes

### Overview

Themes in Mauro Data Mapper are organised in the project by name and uses folder and naming conventions to identify where files and CSS selectors are.
The conventions used are:

* **SASS files**: `src/style/themes/{name}.scss`
* **CSS theme class**: `.{name}-theme`
* **Asset files**: `src/assets/themes/{name}/*.*`

So, as an example, a custom theme called `nhs-digital` would be:

* **SASS files**: `src/style/themes/nhs-digital.scss`
* **CSS theme class**: `.nhs-digital-theme`
* **Asset files**: `src/assets/themes/nhs-digital/*.*`

### Switching Themes

To determine the theme to use for the site, update the `src/environments/environment.ts`:

```ts
export const environment = {
    // ...
    themeName: 'nhs-digital'
    // ...
};
```

!!! Note If the theme name is not provided, this will fall back to `default`.

### Importing Theme

Each theme requires a SASS file to define the colour palette and typography for the Angular Material theming system to use. This SASS file can also
override any other CSS selectors that do not affect the Material controls.

The `src/style/styles.scss` file is the place to import all theme files. The key parts are:

```scss
@import "~@angular/material/theming";

// Include the common styles for Angular Material. Only required to include this once!
@include mat-core();

/* 
Themes 
Import more theme SASS files here to make them available to the app
*/
@import "style/themes/default.scss";
@import "style/themes/nhs-digital.scss";
// ...etc

// More SASS files imported here...
```

!!! Note 
    Remember that Angular Material requires all themes to be precompiled, so all SASS files must be imported to include them as options. Only one
    theme will appear at a time though.

### Creating Themes

To create a new theme it is advised to copy `src/style/themes/default.scss` and make the necessary adjustments, then `@import` the new theme file
in `src/style/styles.scss`.

The specifics of the [Angular Material theme system](https://material.angular.io/guide/theming) should be referenced for better explanation. However,
in summary, you will need to define:

1. The _colour palettes_ required to represent:
    1. Primary colours
    2. Accented colours
    3. Warning colours
2. The _typography_ settings to use for text/font.

The Material mixins should then be included within a top-level CSS selector named after the theme - this CSS selector will be applied to the body of
the HTML page and therefore affect all DOM elements below it. The theme file should effectively include the following steps:

```scss
// Required for Angular Material
@import "~@angular/material/theming";

// Required for custom theming of MDM components
@import "../components/custom";

/* Define colour platte maps here ... */
$nhs-digital-theme-primary: mat-palette(...);
$nhs-digital-theme-accent: mat-palette(...);
$nhs-digital-theme-warn: mat-palette(...);

/* Create the colour theme */
$nhs-digital-theme: mat-light-theme(
                $nhs-digital-theme-primary,
                $nhs-digital-theme-accent,
                $nhs-digital-theme-warn
);

/* Define the typography settings to use... */
$nhs-digital-typography: mat-typography-config(...);

/* 
Define the top-level CSS class name. Name this in the format ".{name}-theme"
so the application can automatically use it for the page 
*/
.nhs-digital-theme {

  // Use the created theme variables to configure Angular Material
  @include angular-material-theme($nhs-digital-theme);
  @include angular-material-typography($nhs-digital-typography);

  // Some MDM components have also been added to the Angular Material theme system. Include this mixin to have these match the same theme
  @include mdm-custom-components-theme($nhs-digital-theme);

  /* Add any further CSS class overrides here... */
}
```

## Assets

Themeable assets, such as logos and images, should be stored under `src/assets/themes` under the specific sub-folder named after the theme. The file
names used should be consistent across all themes e.g. `logo.png`.

To consistently reference the correct asset path to use, the `ThemingService` can be injected into your component/service and use the `getAssetPath()`
function to get the correct path for an asset according to the current theme.

## Page Content

Some of the static content may be adjusted by an administrator to allow the end-users to make content edits instead of relying on developers. To edit
the content:

1. Sign in as an administrator - this feature is only available for administrators.
2. Click on the signed-in user menu and select "Configuration".
3. Click on the "Properties" tab.
4. Click "Add".
5. Select a property from the drop down list.

!!! Note
    It may be necessary to manually adjust the HTML source to set correct styling/markup for the content. This can be done by clicking on 
    the `</>` "Change Mode" toolbar button in each form edit field.

There are configuration properties available to modify the following:

## Logo

A static asset should also be provided for the logo in the navbar component as a default, however an image URL may also be provided if the logo is
hosted in another location e.g. CDN. To set a logo, modify the `theme.logo.url` property.

The `theme.logo.width` property is also provided to adjust the size of the logo in the space providd. Note that:

* The value entered for `theme.logo.width` must be supported by CSS e.g. `20px`, `1.2em`, etc
* The maximum width of the logo is `120px`. If the image is larger than this then it will be scaled down to fit.

## Footer

The copyright notice can be altered in the footer by changing the `content.footer.copyright` property.

## Home Page

The home page content can be modified to include custom content by splitting up the page content into sections.

!!! Note
    It is recommended to include correct HTML source and styling in these sections.

The following sections can be modified:

* `content.home.intro.left` - this is usually text content on the left column of the starting page section.
* `content.home.intro.right` - this is usually an image to display on the right column of the starting page section.
* `content.home.detail.heading` - this is usually the heading for the detail section underneath the introduction.
* `content.home.detail.column1 - 3` - these are the feature boxes that usually appear in the detail section underneath the introduction.

## Defaults

If no property values are provided for the above, then suitable defaults are used instead based on the current theme. To revert back to default values
for any property, simply delete the property from the configuration table.
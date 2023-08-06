# MkDocs Ko-fi Button Plugin

*An MkDocs plugin that let's you easily add a Ko-fi buttons with markdown*  
The plugin looks for Jinja style tags like `{{ko-fi}}` and replaces it with a Ko-fi button. It is possible to configure the text and color of the button.

## Setup

Install the plugin using pip:

``` bash
pip install mkdocs-ko-fi-button-plugin
```

Activate the plugin in `mkdocs.yml`:

``` bash
plugins:
    - search
    - ko-fi-button
```

## Config

### Mandatory

* `id` - Your Ko-fi ID. Can be found on your Ko-fi profile.

### Optional

* `type` - The type of button. Valid values are "widget" or "image". Default: widget
* `color` - The color of the button.
  * If `type == 'widget'`: In hex format. Default: #29abe0
  * If `type == 'image'`: Either "blue", "bluegray", "red", "green" or "black". Default: bluegray
* `text` - The text on the Ko-fi button.
  * If `type == 'widget'`: Default: "Support Me on Ko-fi"
  * If `type == 'image'`: Whatever text they have in the image.

For example:

``` bash
plugins:
    - search
    - ko-fi-button:
        id: "my_id"
        text: "My cool text"
        color: "#547884"
```

**Note:** Some MkDocs theme CSS conflicts with the widget styling. If that is the case and you cannot or will not update the CSS, the `type` config is useful. Set that to "image" and it should render properly. There will be no wiggly coffe mug though.

## Advanced config

In case the Ko-fi javascript is changed on the server side it is possible to configure the path and function calls. This will make it possible to still be able to get a working Ko-fi button widget until this plugin has been updated.

* `javascript_path` - The relative path to the javascript from https://ko-fi.com/. Default: "widgets/widget_2.js"
* `javascript_f1` - The init function. Default: "kofiwidget2.init"
* `javascript_f2` - The draw function. Default: "kofiwidget2.draw"

**Note:** These config options are only valid if `type` is set to "widget". They are ignored otherwise.


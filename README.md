# TemplateParser preprocessor for Foliant

Preprocessor which allows to use templates in Foliant source files. Preprocessor now supports only [Jinja2](http://jinja.pocoo.org/) templating engine, but more can be added easily.

## Installation

```bash
$ pip install foliantcontrib.templateparser
```

## Config

All params that are stated in foliant.yml are considered global params. All of them may be overriden in template tag options, which have higher priority.

```yaml
preprocessors:
    - templateparser:
        engine: jinja2
        engine_params:
            root: '/usr/src/app'
        context:
            param1: 1008
            param2: 'Kittens'
        param3: 'Puppies'
```

`engine`
:   name of the template engine which will be used to process template. Supported engines right now: `jinja2`.

`engine_params`
:   dictionary with parameters which will be transfered to the template engine.

`context`
:   dictionary with variables which will be redirected to the template.

_All parameters with other names are also transfered to the template, as if they appeared inside the `context` dictionary. (`param3` in the above example)_

> Please note that even if this may seem convenient, it is preferred to include template variables in the `context` dictionary, as in future more reserved parameters may be added which may conflict with your stray variables.

## Usage

To use the template in a Markdown file just insert a tag of the template engine name, for example:

```html
This is ordinary markdown text.
<jinja2>
This is a Jinja2 template:
I can count to five!
{% for i in range(5) %}{{ i + 1 }}{% endfor %}
</jinja2>
```

After making a document with Foliant this will be transformed to:

```
This is ordinary markdown text.

This is a Jinja2 template:
I can count to five!
12345
```

You can also use a general `<template>` tag, but in this case you have to specify the engine you want to use in the `engine` parameter:

```html
This is ordinary markdown text.
<template engine="jinja2">
This is a Jinja2 template:
I can count to five!
{% for i in range(5) %}{{ i + 1 }}{% endfor %}
</template>
```

### Sending variables to template

To send a variable to template, add them into the `context` option. This option accepts `yaml` dictionary format.

> Please note that foliant doesn't support multiline tag options yet, so use one-line dictionary format {'key1': value1, ...}

```html
<jinja2 context="{'name': Andy, 'age': 8}">
Hi, my name is {{name}}!
I am {{age}} years old.
{% for prev in range(age, 1, -1) %}
The year before I was {{prev}} years old.
{% endfor %}
</jinja2>
```

Result:

```
Hi, my name is Andy!
I am 8 years old.

The year before I was 8 years old.

The year before I was 7 years old.

The year before I was 6 years old.

The year before I was 5 years old.

The year before I was 4 years old.

The year before I was 3 years old.

The year before I was 2 years old.
```

### Extends and includes

Extends and includes work in templates. The path of the extending\included file is relative to the Markdown file where the template lives.

In Jinja2 engine you can override the path of the included\extended files with `root` engine_param. **Note that this param is relative to project root.**
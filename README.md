# WTF TinyMCE
TinyMCE editor extension for WTForms

## 1. Installation
Under your project environment run:

    $ pip install wtf-tinymce

## 2. Configuring
### 2.1. Initializing module
Under your application initialization (e.g. app = Flask(\__name__)) 
add module import and initialization:

    from wtf_tinymce import wtf_tinymce
    wtf_tinymce.init_app(app)

### 2.2. Adding template
In your create or edit templates (or custom templates with wtforms) 
add import:

    {% import 'wtf_tinymce/editor.html' as tinymce with context %}

and under your site footer block add template initialization like:
    
    {% block tail %}
        {{ super() }}
        {{ tinymce.init_wtf_tinymce(default_content_css='css/tinymce.css') }}
    {% endblock %}

Note: `default_content_css` is optional parameter with relative path 
under project static folder to your custom stylesheet for editor content.

## 3. Usage

    from wtf_tinymce.forms.fields import TinyMceField

    class MyForm(Form):
        text = TinyMceField(
            'My WTF TinyMCE Field label',
            tinymce_options={'toolbar': 'bold italic | link | code'}
        )

To optional parameter `tinymce_options` you can add any TinyMCE options
(see official documentation https://www.tinymce.com/docs/configure/
for details.

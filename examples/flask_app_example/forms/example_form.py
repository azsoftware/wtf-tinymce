from flask_wtf import FlaskForm
from wtf_tinymce.forms.fields import TinyMceField


class ExampleForm(FlaskForm):
    desc = TinyMceField(
        'WTF TinyMCE Field',
        tinymce_options={'toolbar': 'bold italic | link | code'}
    )

# -*- coding: utf-8 -*-

import bleach
from wtforms import TextAreaField

from .widgets import TinyMce


# Default tags and attributes to allow in HTML sanitization
SANITIZE_TAGS = [
    'p', 'br', 'strong', 'em', 'sup', 'sub', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'li', 'a', 'blockquote', 'code'
]
SANITIZE_ATTRIBUTES = {'a': ['href', 'title', 'target']}

DEFAULT_TOOLBAR = "undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | " \
                  "bullist numlist outdent indent | link image | charmap code"


class TinyMceField(TextAreaField):
    """
    Rich text field using TinyMCE.
    """
    widget = TinyMce()

    def __init__(
        self,
        # WTForms fields
        label=u'',
        validators=None,
        filters=(),
        description=u'',
        id=None,
        default=None,
        widget=None,
        _form=None,
        _name=None,
        _prefix='',

        # Additional fields
        content_css=None,
        linkify=True,
        nofollow=True,
        tinymce_options=None,
        sanitize_tags=None,
        sanitize_attributes=None,
        **kwargs
    ):
        super(TinyMceField, self).__init__(
            label=label, validators=validators, filters=filters, description=description, id=id, default=default,
            widget=widget, _form=_form, _name=_name, _prefix=_prefix, **kwargs
        )

        if tinymce_options is None:
            tinymce_options = {}
        else:
            # Clone the dict to preserve local edits
            tinymce_options = dict(tinymce_options)

        # Set defaults for TinyMCE
        tinymce_options.setdefault('plugins', "autolink link lists paste searchreplace code")
        tinymce_options.setdefault('toolbar', DEFAULT_TOOLBAR)
        tinymce_options.setdefault('width', "100%")
        tinymce_options.setdefault('height', "400")
        tinymce_options.setdefault('min_height', "100")
        tinymce_options.setdefault(
            'valid_elements',
            "p,br,strong/b,em/i,sup,sub,h3,h4,h5,h6,ul,ol,li,a[!href|title|target],blockquote,code"
        )
        tinymce_options.setdefault('statusbar', False)
        tinymce_options.setdefault('menubar', False)
        tinymce_options.setdefault('resize', True)

        # Remove options that cannot be set by callers
        tinymce_options.pop('content_css', None)
        tinymce_options.pop('script_url', None)
        tinymce_options.pop('setup', None)

        if sanitize_tags is None:
            sanitize_tags = SANITIZE_TAGS
        if sanitize_attributes is None:
            sanitize_attributes = SANITIZE_ATTRIBUTES

        self.linkify = linkify
        self.nofollow = nofollow
        self.tinymce_options = tinymce_options

        self._content_css = content_css
        self.sanitize_tags = sanitize_tags
        self.sanitize_attributes = sanitize_attributes

    @property
    def content_css(self):
        if callable(self._content_css):
            return self._content_css()
        else:
            return self._content_css

    def process_formdata(self, value_list):
        super(TinyMceField, self).process_formdata(value_list)
        # Sanitize data
        self.data = bleach.clean(
            self.data,
            tags=self.sanitize_tags,
            attributes=self.sanitize_attributes
        )

        if self.linkify:
            if self.nofollow:
                self.data = bleach.linkify(self.data)
            else:
                self.data = bleach.linkify(self.data, callbacks=[])

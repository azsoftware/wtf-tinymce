# -*- coding: utf-8 -*-

from wtforms.widgets import TextArea


class TinyMce(TextArea):
    """
    Rich text widget with Tiny MCE.
    """
    input_type = "tinymce"

    def __call__(self, field, **kwargs):
        c = kwargs.pop('class', '') or kwargs.pop('class_', '')
        if c:
            kwargs['class'] = u'%s %s' % ('richtext', c)
        else:
            kwargs['class'] = 'richtext'

        return super(TinyMce, self).__call__(field, **kwargs)

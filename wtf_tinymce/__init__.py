# -*- coding: utf-8 -*-

from flask import Blueprint


class WtfTinyMCEBlueprint(Blueprint):
    def init_app(self, app):
        app.register_blueprint(self)

wtf_tinymce = WtfTinyMCEBlueprint(
    'wtf_tinymce',
    __name__,
    static_folder='static',
    static_url_path='/_wtf_tinymce',
    template_folder='templates'
)

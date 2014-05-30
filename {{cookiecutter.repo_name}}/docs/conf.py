# -*- coding: utf-8 -*-
import re
import os
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinxcontrib.napoleon'
]
if os.getenv('SPELLCHECK'):
    extensions += 'sphinxcontrib.spelling',
    spelling_show_suggestions = True
    spelling_lang = 'en_US'

source_suffix = '.rst'
master_doc = 'index'
project = u'{{ cookiecutter.project_name }}'
copyright = u'{{ cookiecutter.year }}, {{ cookiecutter.full_name }}'
version = release = re.findall(
    'version="(.*)"',
    open(os.path.join(os.path.dirname(__file__), '../setup.py')).read()
)[0]

html_theme = 'pydoctheme'
html_theme_path = ['.']
pygments_style = 'trac'
templates_path = ['.']
html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
exclude_trees = ['pydoctheme']
html_split_index = True
html_sidebars = {
   '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
}
html_short_title = '%s-%s' % (project, version)
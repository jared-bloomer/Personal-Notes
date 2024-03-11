# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from datetime import datetime
import requests
import os
from base64 import b64decode
import json
import re
import subprocess
from urllib.parse import urlparse

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Personal Notes'
copyright = u'2023-2024, Jared Bloomer. Last built %s' % \
    datetime.now().strftime('%A, %B %d, %Y')
if os.environ.get('GIT_COMMIT', None) is not None:
    copyright += u' from %s' % os.environ['GIT_COMMIT']
author = 'Jared Bloomer'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.githubpages',
    'sphinx.ext.todo',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinx_last_updated_by_git',
    'sphinx_rtd_theme',
    # 'sphinx.ext.autosectionlabel'
]

templates_path = ['_templates']
exclude_patterns = []

source_suffix = '.rst'
master_doc = 'index'

html_favicon = 'favicon.ico'

version = u''
release = u''

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': False,
}
html_static_path = ['_static']

html_context = {
    'theme_vcs_pageview_mode': 'edit',
    'conf_py_path': '/source/'
}

if os.environ.get('GITHUB_ACTIONS') == 'true':
    html_context['display_github'] = True
    html_context['github_user'], html_context['github_repo'] = os.environ['GITHUB_REPOSITORY'].split('/')
    html_context['github_host'] = urlparse(os.environ['GITHUB_API_URL']).hostname
    html_context['github_version'] = os.environ.get(
        'GITHUB_REF_NAME',
        os.environ.get('GITHUB_HEAD_REF', os.environ.get('GITHUB_SHA'))
    )

html_css_files = [
    # thanks to: https://rackerlabs.github.io/docs-rackspace/tools/rtd-tables.html
    'theme_overrides.css'  # override wide tables in RTD theme
]

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Personal Notes.tex', project,
     author, 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, project, project,
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, project, project,
     author, project, 'Personal Notes I have gathered for reference.',
     'Miscellaneous'),
]

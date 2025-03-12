# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sphinx-docs-lab'
copyright = '2025, Charles Uneze'
author = 'Charles Uneze'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinxemoji.sphinxemoji',
    'hoverxref.extension',
]

# Emojis on the Website
#sphinxemoji_style = 'twemoji'

# Configure hoverxref options
hoverxref_roles = ['term',] 
hoverxref_role_types = {
    'term': 'tooltip',
}
#hoverxref_api_host = 'https://readthedocs.org'

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Website Theme
import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

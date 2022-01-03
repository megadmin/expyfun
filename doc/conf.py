# -*- coding: utf-8 -*-
#
# Expyfun documentation build configuration file, created by
# sphinx-quickstart on Fri Jun 11 10:45:48 2010.
#
# This file is execfile()d with the current directory set to its containing
# dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import inspect
import os
from os.path import relpath, dirname
import sys
from datetime import date
import sphinx_gallery  # noqa
import sphinx_bootstrap_theme  # noqa
from numpydoc import numpydoc, docscrape  # noqa

# Work around Pyglet annoyingness
assert 'pyglet' not in sys.modules
if 'sphinx' in sys.modules:
    s = sys.modules.pop('sphinx')
    import pyglet  # noqa
    sys.modules['sphinx'] = s
    del s

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
curdir = os.path.dirname(__file__)
sys.path.append(os.path.abspath(os.path.join(curdir, '..', 'expyfun')))
sys.path.append(os.path.abspath(os.path.join(curdir, 'sphinxext')))

import expyfun
if not os.path.isdir('_images'):
    os.mkdir('_images')

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.8'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.linkcode',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinx_gallery.gen_gallery',
    'sphinx_fontawesome',
    'numpydoc',
    'sphinx_bootstrap_theme',
]

autosummary_generate = True
autodoc_default_options = {'inherited-members': None}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'expyfun'
td = date.today()
copyright = u'2013-%s, expyfun developers. Last updated on %s' % (td.year,
                                                                  td.isoformat())
nitpicky = True

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = expyfun.__version__
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = "autolink"

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ['expyfun.']

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'bootstrap'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'navbar_title': 'expyfun',
    'source_link_position': "nav",  # default
    'bootswatch_theme': "yeti",
    'navbar_sidebarrel': False,  # Render the next/prev links in navbar?
    'navbar_pagenav': True,
    'globaltoc_depth': 0,
    'navbar_class': "navbar",
    'bootstrap_version': "3",  # default
    'navbar_links': [
        ("Getting started", "getting_started"),
        ("Examples", "auto_examples/index"),
        ("API reference", "python_reference"),
    ],
    }

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/favicon.ico"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static', '_images']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False
html_copy_source = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# variables to pass to HTML templating engine
build_dev_html = bool(int(os.environ.get('BUILD_DEV_HTML', False)))

html_context = {'use_google_analytics': True, 'use_twitter': True,
                'use_media_buttons': True, 'build_dev_html': build_dev_html}

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'expyfun-doc'

trim_doctests_flags = True

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/devdocs', None),
    'scipy': ('https://scipy.github.io/devdocs', None),
    'matplotlib': ('https://matplotlib.org', None),
    'sklearn': ('https://scikit-learn.org/stable', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable', None),
    'sounddevice': ('https://python-sounddevice.readthedocs.io', None),
    'rtmixer': ('https://python-rtmixer.readthedocs.io/en/latest', None),
    'pyglet': ('https://pyglet.readthedocs.io/en/latest', None),
    'mne': ('https://mne-tools.github.io/dev', None),
}

examples_dirs = ['../examples']
gallery_dirs = ['auto_examples']

sphinx_gallery_conf = {
    'doc_module': ('expyfun',),
    'examples_dirs': examples_dirs,
    'gallery_dirs': gallery_dirs,
    'backreferences_dir': 'generated',
    'plot_gallery': 'True',  # Avoid annoying Unicode/bool default warning
    'filename_pattern': r'/.*(?<!_)\.py$',  # anything that isn't *_.py
    'capture_repr': (),
}

numpydoc_class_members_toctree = False


# -----------------------------------------------------------------------------
# Source code links (adapted from SciPy (doc/source/conf.py))
# -----------------------------------------------------------------------------

def linkcode_resolve(domain, info):
    """
    Determine the URL corresponding to Python object
    """
    if domain != 'py':
        return None

    modname = info['module']
    fullname = info['fullname']

    submod = sys.modules.get(modname)
    if submod is None:
        return None

    obj = submod
    for part in fullname.split('.'):
        try:
            obj = getattr(obj, part)
        except:
            return None

    try:
        fn = inspect.getsourcefile(obj)
    except:
        fn = None
    if not fn:
        try:
            fn = inspect.getsourcefile(sys.modules[obj.__module__])
        except:
            fn = None
    if not fn:
        return None

    try:
        source, lineno = inspect.getsourcelines(obj)
    except:
        lineno = None

    if lineno:
        linespec = "#L%d-L%d" % (lineno, lineno + len(source) - 1)
    else:
        linespec = ""

    fn = relpath(fn, start=dirname(expyfun.__file__))

    if 'dev' in expyfun.__version__:
        return "https://github.com/LABSN/expyfun/blob/master/expyfun/%s%s" % (  # noqa
           fn, linespec)
    else:
        return "https://github.com/LABSN/expyfun/blob/maint/%s/expyfun/%s%s" % (  # noqa
           expyfun.__version__, fn, linespec)

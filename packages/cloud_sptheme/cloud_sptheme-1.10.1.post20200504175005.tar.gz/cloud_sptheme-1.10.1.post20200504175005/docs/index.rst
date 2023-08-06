===============================================
The Cloud Sphinx Theme
===============================================

.. rst-class:: without-title

.. caution::

  **2020-05-01: This project has moved to Heptapod!**

  Due to BitBucket deprecating Mercurial support, this package's public repository and issue tracker
  has been relocated.  It's now located at `<https://foss.heptapod.net/doc-utils/cloud_sptheme>`_,
  and is powered by `Heptapod <https://heptapod.net/>`_.
  Hosting is being graciously provided by the people at
  `Octobus <https://octobus.net/>`_ and `CleverCloud <https://clever-cloud.com/>`_!


This is release |release| of a small Python package named
:mod:`!cloud_sptheme`. It contains a `Sphinx <http://sphinx.pocoo.org/>`_ theme
named "Cloud", and some related Sphinx extensions. Cloud and its extensions
are primarily oriented towards generating html documentation for Python libraries.
It provides numerous small enhancements to make the html documentation html more interactive,
improve the layout on mobile devices, and other enhancements.

Contents
========
.. rst-class:: floater

.. seealso:: :ref:`What's new in v1.10 <whats-new>`

Themes
------
:doc:`Cloud Sphinx Theme <cloud_theme>`
    the main Sphinx theme provided by this package,
    and used by this documentation.

Markup Extensions
-----------------
The following extensions make some helpful enhancements to sphinx's markup.
They should all be theme-independant.

    :mod:`cloud_sptheme.ext.autodoc_sections`
        Patches :mod:`sphinx.ext.autodoc` to handle RST section headers
        inside docstrings.

    :mod:`cloud_sptheme.ext.autoattribute_search_bases`
        Patches :mod:`sphinx.ext.autodoc` so that ``.. autoattribute::``
        will also search parent classes for attribute docstrings.

    :mod:`cloud_sptheme.ext.docfield_markup`
        Patches Sphinx to permit tilde-prefixed markup in directives, 
        such as ``:raises ~myapp.MyException:``

    :mod:`cloud_sptheme.ext.escaped_samp_literals`
        Patches Sphinx to permit backslash-escaped ``{}`` characters within ``:samp:`` roles.

    :mod:`cloud_sptheme.ext.issue_tracker`
        Adds a special ``:issue:`` role for quickly linking to
        your project's issue tracker.

    :mod:`cloud_sptheme.ext.table_styling`
        Enhances ``.. table`` directive to support per-column
        text alignment and other layout features.

Meta Extensions
---------------
The following extensions add some additional capabilities and features
for building sphinx documentation.  They should all be theme-independant.

    :mod:`cloud_sptheme.ext.auto_redirect`
        Helper to alert users when documentation hosting has moved
        to a different url.

    :mod:`cloud_sptheme.ext.page_only`
        Directive that allows entire pages to be conditionally omitted from a build,
        similar to ``.. only::``.

    :mod:`cloud_sptheme.ext.relbar_links`
        Adds a TOC or other custom links to the top navigation controls.

    :mod:`cloud_sptheme.ext.role_index`
        Generates a "roleindex.json" of all document and cross-references,
        to help integrate sphinx documentation into a web application's context-aware help.

Theme-Specific Extensions
-------------------------
The following Sphinx extensions provide features used by the Cloud theme,
and may prove useful for documentation that needs a specific feature:

    :mod:`cloud_sptheme.ext.index_styling`
        Adds additional css styling classes to the index page.

Reference
---------
:doc:`install`
    requirements and installations instructions

:doc:`history`
    history of current and past releases

Online Resources
================

    .. rst-class:: html-plain-table

    ====================== ===================================================
    Homepage:              `<https://foss.heptapod.net/doc-utils/cloud_sptheme>`_
    Online Docs:           `<https://cloud-sptheme.readthedocs.io>`_
    Download & PyPI:       `<https://pypi.python.org/pypi/cloud_sptheme>`_
    ====================== ===================================================

Hosting
=======
Thanks to the people at `Octobus <https://octobus.net/>`_ and `CleverCloud <https://clever-cloud.com/>`_
for providing the repository / issue tracker hosting, as well as the development of `Heptapod <https://heptapod.net/>`_!

Thanks to `ReadTheDocs <https://readthedocs.io>`_ for providing documentation hosting!

.. index:: cloud; sphinx theme, sphinx theme; cloud

====================
"Cloud" sphinx theme
====================

Features
========
This package provides a theme called "Cloud", used to generate this documentation.
Aside from being just another Sphinx theme, it has a few special features:

*Toggleable sections*
    You can mark sections with ``.. rst-class:: html-toggle``,
    which will make the section default to being collapsed under html,
    with a "show section" toggle link to the right of the title.

*Additional CSS classes*
    It provides a couple of simple styling directives for adding
    variety to long Python library documentation:

    * You can mark tables with ``.. rst-class:: html-plain-table``
      to remove separating lines between rows.

    * You can mark ``<h2>`` sections with ``.. rst-class:: emphasize-children``
      to provide addition visual dividers between large numbers of sub-sub-sections.

*Navigation enhancements*
    It provides options (``roottarget``, ``logotarget``) which
    allow the table of contents to be a distinct
    from the front page (``index.html``) of the document. This allows
    a master table of contents to be maintained, while still allowing
    the front page to be fully customized to welcome readers.

*Additional styling options*
    It also provides a number of styling options controlling
    small details such as external links, document sizing, etc.
    See below.

    It also uses an adaptive layout to work well on all screen sizes
    from mobile phones to widescreen desktops.

*Google Analytics Integration*
    By enabling two theme options with ``conf.py``, Cloud will
    automatically insert a Google Analytics tracker to the bottom of each
    page, along with a polite link allowing users to set a cookie
    which opts them out.

List of Options
===============

Structure
---------
``roottarget``
    Sets the page which the title link in the navigation bar should point to
    (defaults to the special value ``"<toc>"``, which uses the table of contents).

``logotarget``
    Sets the page which the sidebar logo (if any) should point to
    (defaults to the special value ``<root>``, which just mirrors ``roottarget``).

Document Layout
---------------
``max_width``
    Sets the maximum document width, so the documentation does not stretch
    too far on wide monitors (defaults to ``11in``).

``minimal_width``
    Sets the maximum width where the "mobile" layout will be used.
    This layout omits the sidebar and everything else that can be trimmed,
    and is designed to (hopefully) be more usuable on mobile devices.
    (defaults to ``700px``).

``min_height``
    sets the minimum height of the page body (defaults to ``6in``).

.. versionchanged:: 1.7

    ``compact_width`` option has been removed, and will be ignored.
    (it previously provided an intermediate level of padding between ``minimal_width`` and ``max_width``).

.. _font-options:

Font Sizing
-----------
``default_layout_text_size``

    Sets the default font size for the whole document (defaults to ``87.5%``
    of browser default).

``minimal_layout_text_size``

    Sets the default font size for the whole document when the "mobile"
    layout is being used (defaults to ``75%`` of browser default).

Sidebar Layout & Styling
------------------------
``rightsidebar``
    whether the sidebar is on the right side instead of the left
    (defaults to ``false``).

``defaultcollapsed``
    whether the sidebar should start collapsed (defaults to ``false``).

``stickysidebar``
    whether the sidebar should "stick" in the current window
    (defaults to ``true``), otherwise it will scroll along with the page.

``highlighttoc``
    whether sidebar should highlight the sections which are currently
    being viewed (defaults to ``true``).

Sidebar Labels
--------------
``sidebar_localtoc_title``
    Override title of per-page table of contents (in ``localtoc.html`` sidebar).
    defaults to ``Page contents``.

``sidebar_prev_title``
    Override title of link to previous page (in ``relations.html`` sidebar).
    defaults to ``Previous page``.

``sidebar_next_title``
    Override title of link to next page (in ``relations.html`` sidebar).
    defaults to ``Next page``.

``sidebar_master_title``
    Override title of the front-page document link (in ``quicklinks.html`` sidebar).

``sidebar_root_title``
    Override title of the root document link (in ``quicklinks.html`` sidebar).

.. _decor-options:

Document Styling
----------------
``lighter_header_decor``
    Optional boolean flag which render headers in a lighter underlined
    style, rather than with a solid background.  Also enables other related
    stylistic changes.

``shaded_decor``
    Optional boolean flag which adds a slight amount of shading
    to sidebar, navbars, and section headers.

``borderless_decor``
    Optional boolean flag which makes page background match document background.
    Also enables other related stylistic changes.

Styling
-------
``externalrefs``
    Boolean flag that controls whether references should be displayed with an icon.
    (defaults to ``True``).

``externalicon``
    Optional image or string to prefix before any external links
    (defaults to ``⇗``, ignored if ``externalrefs=False``).

``issueicon``
    Optional image or string to prefix before any issue tracker links
    generated by :mod:`cloud_sptheme.ext.issue_tracker`
    (defaults to ``✧``, ignored if ``externalrefs=False``).

.. note::

    There are a number of options for changing the various colors
    and fonts used by this theme, which are still undocumented.
    A complete list can be found in the theme's configuration file
    (``/cloud_sptheme/themes/cloud/theme.conf``).

Other
-----
``googleanalytics_id``
    Setting this via ``html_theme_options`` to your GA id (e.g. ``UA-XXXXXXXX-X``)
    will enable a `Google Analytics <http://www.google.com/analytics>`_
    tracker for all pages in the document, as well insert a link in
    the footer allowing users to opt out of tracking.

``googleanalytics_path``
    Setting this allows limiting the tracker to a subpath,
    useful for shared documentation hosting (e.g. PyPI or ReadTheDocs).

.. _cloud-theme-usage:

Usage
=====
Using the theme
---------------
To use the cloud theme, make sure this package is installed properly,
then open your documentation's Sphinx ``conf.py`` file,
and make the following changes::

    # set the html theme
    html_theme = "cloud"
        # NOTE: there are also alternate versions named "redcloud" and "greencloud"

    # ... some contents omitted ...

    # [optional] set some of the options listed above...
    html_theme_options = { "roottarget": "index" }

.. rst-class:: floater

.. seealso::

    See the next page (:doc:`cloud_theme_test`) for examples of
    these options in action.

Section Styles
--------------

Emphasized Children
...................
Adding ``.. rst-class:: emphasize-children`` to a 2nd-level section header
will cause the headers of all of it's child sections to be emphasized with a solid background.
This is mainly useful for very long sections, where there needs to be
a visual divide between 3rd-level sections.

Toggleable Sections
...................
By adding ``.. rst-class:: html-toggle`` before any section header,
it can be made toggleable::

    .. rst-class:: html-toggle

    Toggleable Section
    ------------------

    This section is collapsed by default.

While toggleable sections start out collapsed by default,
you can use ``.. rst-class:: html-toggle expanded`` to override this.

Table Styles
------------
* Adding ``.. rst-class:: plain`` can be used to remove
  the row shading and other styling from a table.

* Adding ``.. rst-class:: centered`` can be used to center a table.

  .. deprecated:: 1.10.0, use docutils' ``:align: center`` directive instead.

* Adding ``.. rst-class:: fullwidth`` can be used to expand a table
  to the full width of the page.

.. seealso::
    The :mod:`~cloud_sptheme.ext.table_styling` extension
    for additional table styling abilities, e.g. per-column text alignment.

===========================================================================
:mod:`cloud_sptheme.ext.table_styling` - adds directives for styling tables
===========================================================================

.. module:: cloud_sptheme.ext.table_styling
    :synopsis: adds directives for styling tables

.. versionchanged:: 1.9

    Added ``:header-alignment:`` directive.

Overview
========
This Sphinx extension replaces the default ``.. table::`` directive
with a custom one, that supports a number of extra options for controlling
table layout on a per-column basis.

For example, the following snippet specifies relative widths for the
three columns, changes the text alignment for each column,
disables text-wrapping for the third column, and inserts
dividers between the columns::

    .. table:: Optional Caption
        :widths: 3 2 1
        :column-alignment: left center right
        :column-wrapping: true true false
        :column-dividers: none single double single

        =========== =========== ===========
        Width 50%   Width 33%   Width 16%
        =========== =========== ===========
        Line 1      This text   This text
                    should wrap will always
                    onto        be one line.
                    multiple
                    lines.
        Line 2      Centered.   Right-Aligned.
        Line 3      Centered    Right-Aligned
                    Again.      Again.
        =========== =========== ===========

This will then result in the following table:

.. table:: Optional Caption
    :widths: 3 2 1
    :column-alignment: left center right
    :column-wrapping: yes yes no
    :column-dividers: none single double single

    =========== =========== ===========
    Width 50%   Width 33%   Width 16%
    =========== =========== ===========
    Line 1      This text   This text
                should wrap will always
                onto        be one line.
                multiple
                lines.
    Line 2      Centered.   Right-Aligned.
    Line 3      Centered    Right-Aligned
                Again.      Again.
    =========== =========== ===========

Directive Options
=================
The enhanced ``.. table::`` directive supports the following options:

``:widths:``
    Sets proportional column widths

    This should be a space-separated list of positive integers,
    one for every column. The columns widths will be allocated
    proportionally (e.g. ``1 2 3`` for a 3-column table means the columns
    will use 16%, 33%, and 50% of the total width, respectively).

``:column-alignment:``
    Sets per-column text alignment

    This should be a comma/space-separated list of the following
    strings: ``left``, ``right``, ``center``, ``justify``.
    These are interpreted one per column. Extra values are ignored;
    if not enough values are provided, the remaining columns
    will default to ``left``.

    Alternately this can be a single word containing
    just the first letters: e.g. ``lrcj`` would be interpreted
    the same as ``left right center justify``.

``:header-alignment:``
    Sets per-column text alignment *for header rows*.

    This has the same format as ``:column-alignment:``.
    If specified, all headers rows will use these alignment values
    instead of the default column alignments.

``:column-wrapping:``
    Sets per-column text wrapping

    This should be a comma/space-separated list of
    either ``yes``/``true`` or ``no``/``false``. If ``yes`` (the default),
    words will wrap around if there is not enough horizontal space.
    If ``no``, whitespace-wrapping will be disabled for that column.
    Extra values are ignored;
    if not enough values are provided, the remaining columns
    will default to ``true``.

    Alternately this can be a single word containing
    just the first letters: e.g. ``ttf`` is the same as ``true true false``.

``:column-dividers:``
    Add dividers between columns

    This lets you specify custom vertical dividers between columns
    (ala what ``.. tabularcolumns::`` allows under latex).

    This should be a comma/space-separated list of
    ``none``, ``single``, or ``double``; based on the type of divider
    you want. There should be one of these for the left side of the table,
    for between each column, and for the right side of the table
    (e.g. a 4 entries for a 3-column table). Extra values are ignored;
    if not enough values are provided, the remaining columns will default to ``none``.

    Alternately this can be a single word containing
    just the number: e.g. ``0121`` is the same as ``none single double single``.

``:column-classes:``
    Add per-column css classes.

    This lets you specify css classes that will be assigned to each
    column, much like ``.. rst-class::``. This should either
    be a space-separated list containing one class per column,
    or a comma-separated list containing multiple classes for each column,
    separated by spaces. Extra values are ignored;
    if there are not enough values, or there are blank entries, those columns
    will not be assigned any custom classes.

    For example, ``a b, c , , d``
    would assign the classes ``a b`` to column 1, ``c`` to column 2,
    no custom classes for column 3, and ``d`` to column 4.

``:header-columns:``
    Specify number of "stub" columns

    Should be a non-negative integer specifying the number of
    columns (starting with the left side) that should be treated
    as "stub" or "header" columns, and should be styled accordingly.

Configuration
=============
This extension reads the following ``conf.py`` options:

    ``table_style_default_align``

        Optionally add default value for ``:align:`` directive.
        Sphinx 2 changed it's default to "centered" tables,
        setting this directive to "left" will restore the original behavior.

        .. versionadded:: 1.10.0

    ``table_styling_embed_css``

        Controls whether or not the custom css file should be included.
        Defaults to ``True``, set to ``False`` to disable.

    ``table_styling_class``

        By default, all HTML tables styled by this extension will
        have the css class ``"styled-table"`` added, to help with themeing support.
        Use this option to override with your own theme's preferred css class.

Internals
=========
.. note::

    This extension gets the job done by adding
    custom css classes to every cell in the generated html table.
    It then inserts a custom css file which provides styling
    implementing relevant parts of the above directives.
    While this extension is primarily tested with :mod:`!cloud_sptheme`,
    it should work with most Sphinx themes, any conflicts that occur
    are probably bugs.

.. todo:: make this autogenerate a matching ``.. tabularcolumns`` directive for latex.
.. todo:: allow ``:widths:`` to support ``em``, ``in``, ``%``

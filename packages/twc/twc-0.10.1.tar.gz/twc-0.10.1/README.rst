twc
===

**TWC - TaskWarrior Controller** (previously TaskWarrior Curses) is interactive
terminal frontend for task and TODO manager - TaskWarrior.

.. image:: https://gitlab.com/mgoral/twc/raw/master/docs/img/screenshot.png
    :align: center

For full documentation please refer to the `User Manual
<https://mgoral.gitlab.io/twc/>`_. There's also built-in help available
after pressing ``F1``.

Features
~~~~~~~~

* agendas - display several filters on a single screen simultaneously
  (influenced by `org-mode <https:orgmode.org>`_)
* create, modify, delete, annotate tasks
* bulk edits: select arbitrary tasks and modify them all at the same time
* autocomplete and tab-complete writing task descriptions, annotations, tags
  etc.
* styling and task formatting
* tasks and sub-tasks grouping (influenced by
  `taskwiki <https://github.com/tbabej/taskwiki>`_)
* synchronize tasks with task server
* status line showing arbitrary informations
* configurable key bindings
* search and incremental search of tasks - search can be case-sensitive,
  case-insensitive or smart-case (case sensitivite only when there are upper
  case characters in searched term)
* on-demand filtering of displayed tasks
* history of commands (scrolled with up and down arrows)

Introduction
~~~~~~~~~~~~

TWC works with a concept of "agendas" influenced and borrowed from the mighty
org-mode. Agenda is basically a view of several TaskWarrior filters (called
blocks) displayed on a single screen simultaneously. You can jump between
blocks and single tasks.

To add agenda, first create a configuration file inside
``~/.config/twc/config.py``. It is a regular Python file with exposed variable
``c`` which references a configuration object. You can add new blocks like that:

.. code:: python

    c.add_block(
        agenda='My Agenda',
        title='Next Tasks',
        filter='status:pending',
        sort='priority+,urgency-')

    c.add_block(
        agenda='My Agenda',
        title='Projects',
        filter='-WAITING and (+BLOCKING or +BLOCKED) and -INSTANCE',
        sort='project-,priority-,order+,urgency-',
        items='* description,tags:info:')

Style and colors
~~~~~~~~~~~~~~~~

TWC can be styled in any way you want. To change its colors use `c.set_style()`:

.. code:: python

    c.set_style('highlight', 'bg:ansiblue bold')
    c.set_style('error', 'fg:white bg:red')

Style examples:

- ``fg:white`` (white foreground, named color)
- ``bg:#000000`` (black background, hexadecimal notation)
- ``bold italic underline blink reverse hidden`` (supported style flags)

Any style name can be used in task formatting. Some interface elements however
use specific style names.

Formatting
~~~~~~~~~~

Block's ``items`` and ``statusleft`` and ``statusright`` parameters are
composed of lists of displayed items; they can be separated by comma, which
will produce space between items, or by "+" sign, which will concatenate items
to each other without leaving space between them.

Each item can be optionally followed by a name of style which should be applied
to this item and item-specific string formatting. When style or formatting are
added, they must be separated and ended by a colon ":": ``name:style:format:``.

All TaskWarrior's attribute names work as item names and there are some
additional names defined for either blocks and status line.

Example format strings are:

.. code:: python

    items = '[priority:warning:],(due:comment:%Y-%m-%d:),description'
    items = '[flags::%a%s%d:]+id,description,tags:info:

Items will be only displayed when they are present. For example if there are no
tags defined for a task, ``tags`` item will not produce any output.

Items might contain additional characters in place of their names and TWC will
try to intelligently/magically (with regular expressions ;)) guess name. These
additional charactes will be printed only when item is present so they can be
used e.g. to visually delimit some items from the others (e.g. surround tags
with braces, delimit items with "|" etc.)

Key bindings
~~~~~~~~~~~~

By default you can navigate with arrows or vim-style ``j`` and ``k``. Exit TWC
with ``q``.

You can bind and unbind keys with ``c.bind(key, command)`` and
``c.unbind(key)``. Refer to `User Manual <https://mgoral.gitlab.io/twc/>`_ for
a list of commands and other default key bindings.

Status line
~~~~~~~~~~~

Bottom status line displays arbitrary informations and is configurable by
two variables: ``statusleft`` and ``statusright``. They describe format similar
to the one described in `Formatting`_ The main difference is that task
attributes are referenced by ``task.<attribute>`` placeholder and that there
additional placeholders available.

.. code:: python

    c.set('statusleft', 'COMMAND,task.id')
    c.set('statusright', 'flags::%a:')

Status line items also include: ``taskrc``, ``command``, ``COMMAND``,
``agenda.pos``, ``agenda.size``, ``agenda.ppos``, ``flags``.

Installation
~~~~~~~~~~~~

First, make sure that TaskWarrior is installed on your system. TaskWarrior is
packaged for most of Linux distributions. Please refer to TaskWarrior's
`documentation <https://taskwarrior.org/download/>`_ for details.

TWC is distributed via `pypi <https://pypi.org/project/twc/>`_. You can
install it with pip:

.. code::

    $ pip3 install --user twc

or with pip wrapper like `pipsi <https://github.com/mitsuhiko/pipsi>`_:

.. code::

    $ pipsi install --python python3 twc

TWC reads your ``taskrc``. It'll use the default one, which is usually located
in ``~/.taskrc``, but you can change it with ``-t`` switch:

.. code::

    $ twc -t ~/dotfiles/my_taskrc

Termux
~~~~~~

TWC works on `Termux <https://termux.com/>`_, although there's currently a `bug
<https://github.com/regebro/tzlocal/pull/55>`_ in tzlocal - a library
indirectly used by TWC to get local timezone information.

Before running TWC on Termux you have to export the following environment
variable:

.. code:: shell

    export TZ=$(getprop persist.sys.timezone)

Termux emulates scroll events as key presses. You can bind them for easier
navigation:

.. code:: python

    c.bind('right', 'next-agenda')
    c.bind('left', 'prev-agenda')

License
~~~~~~~

TWC was created by Michał Góral.

TWC is free software, published under the terms of GNU GPL3 or any later
version. See LICENSE file for details.

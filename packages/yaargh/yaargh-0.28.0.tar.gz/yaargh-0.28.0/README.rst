Yaargh: Yet Another Argh
========================

Yaargh is a fork of Argh (https://github.com/neithere/argh/).

Why fork?
---------

The argh project is no longer maintained (https://github.com/neithere/argh/issues/124#issuecomment-383645696).
This project will attempt to fix issues and make improvements to the original project.
The intent is for all these changes to be made back to the original argh project
when that becomes possible, and for yaargh to act as a replacement until it is.

You can use yaargh as a drop-in replacement for argh (`import yaargh as argh`)
though see Compatability below.

In order to support using yaargh automatically even in applications where you can't easily change
the code, the optional feature `yaargh[import-argh]` will add a dummy `argh` module such that
`import argh` will use `yaargh`.

Highlights
----------

The most signifigant differences from ``argh``, and reasons you may prefer to use it:

- Commands that fail with a ``CommandError`` now exit with status ``1`` (failure) instead of
  status ``0`` (success). This is extremely important when used in scripts.

Compatability
-------------

While yaargh strives to maintain backwards compatability with argh and its existing behavior,
the nature of a library like `argh` with a large amount of "magic" behavior and defaults
means that what we consider the best default may change from version to version. For example,
help text wording may change.

In addition, there is behavior that is almost always a bug but that it is technically possible
some users rely on.

Both kinds of compatability breaks are listed below:

- If a function's type signature included a ``*varargs`` argument with an annotation of
  type ``str``, this annotation previously was ignored. Now, that annotation will be used
  as a help string. In almost all cases this should be fixing behavior to match user intent,
  but it will technically result in different ``--help`` output.

- Previously, if a function raised a ``yaargh.CommandError`` or an error explicitly marked as wrapped,
  then ``yaargh.dispatch()`` (and by extension ``yaargh.dispatch_command()`` and ``yaargh.dispatch_commands()``)
  would write the error message to the given ``error_file`` (by default ``sys.stderr``), then
  return. It now raises a SystemExit instead of returning. In almost all cases, ``dispatch()`` is
  the last thing the program does anyway, and parsing failures already caused a SystemExit to be
  raised so most users who need to do something after error will already be catching it.
  This is a signifigant break but is nessecary to allow non-zero exit codes for failed commands.

- Related to the above, commands that fail with a ``yaargh.CommandError`` or other wrapped error
  will now exit with status ``1``, indicating failure. Previously, unless the user did something to avoid it,
  the command would have returned from ``yaargh.dispatch()`` and subsequently exited success.
  In the vast majority of cases this would have been a latent bug likely to cause havoc in scripts
  or other systems which rely on status code to check if a command succeeded.
  You can use ``CommandError(message, code=0)`` to restore the previous behavior.

Original README
---------------

Building a command-line interface?  Found yourself uttering "argh!" while
struggling with the API of `argparse`?  Don't like the complexity but need
the power?

.. epigraph::

    Everything should be made as simple as possible, but no simpler.

    -- Albert Einstein (probably)

`Argh` is a smart wrapper for `argparse`.  `Argparse` is a very powerful tool;
`Argh` just makes it easy to use.

In a nutshell
-------------

`Argh`-powered applications are *simple* but *flexible*:

:Modular:
    Declaration of commands can be decoupled from assembling and dispatching;

:Pythonic:
    Commands are declared naturally, no complex API calls in most cases;

:Reusable:
    Commands are plain functions, can be used directly outside of CLI context;

:Layered:
    The complexity of code raises with requirements;

:Transparent:
    The full power of argparse is available whenever needed;

:Namespaced:
    Nested commands are a piece of cake, no messing with subparsers (though
    they are of course used under the hood);

:Term-Friendly:
    Command output is processed with respect to stream encoding;

:Unobtrusive:
    `Argh` can dispatch a subset of pure-`argparse` code, and pure-`argparse`
    code can update and dispatch a parser assembled with `Argh`;

:DRY:
    The amount of boilerplate code is minimal; among other things, `Argh` will:

    * infer command name from function name;
    * infer arguments from function signature;
    * infer argument type from the default value;
    * infer argument action from the default value (for booleans);
    * add an alias root command ``help`` for the ``--help`` argument.

:NIH free:
    `Argh` supports *completion*, *progress bars* and everything else by being
    friendly to excellent 3rd-party libraries.  No need to reinvent the wheel.

Sounds good?  Check the tutorial!

Relation to argparse
--------------------

`Argh` is fully compatible with `argparse`.  You can mix `Argh`-agnostic and
`Argh`-aware code.  Just keep in mind that the dispatcher does some extra work
that a custom dispatcher may not do.

Installation
------------

Using pip::

    $ pip install argh

Arch Linux (AUR)::

    $ yaourt python-argh

Examples
--------

A very simple application with one command:

.. code-block:: python

    import argh

    def main():
        return 'Hello world'

    argh.dispatch_command(main)

Run it:

.. code-block:: bash

    $ ./app.py
    Hello world

A potentially modular application with multiple commands:

.. code-block:: python

    import argh

    # declaring:

    def echo(text):
        "Returns given word as is."
        return text

    def greet(name, greeting='Hello'):
        "Greets the user with given name. The greeting is customizable."
        return greeting + ', ' + name

    # assembling:

    parser = argh.ArghParser()
    parser.add_commands([echo, greet])

    # dispatching:

    if __name__ == '__main__':
        parser.dispatch()

Of course it works:

.. code-block:: bash

    $ ./app.py greet Andy
    Hello, Andy

    $ ./app.py greet Andy -g Arrrgh
    Arrrgh, Andy

Here's the auto-generated help for this application (note how the docstrings
are reused)::

    $ ./app.py help

    usage: app.py {echo,greet} ...

    positional arguments:
        echo        Returns given word as is.
        greet       Greets the user with given name. The greeting is customizable.

...and for a specific command (an ordinary function signature is converted
to CLI arguments)::

    $ ./app.py help greet

    usage: app.py greet [-g GREETING] name

    Greets the user with given name. The greeting is customizable.

    positional arguments:
      name

    optional arguments:
      -g GREETING, --greeting GREETING   'Hello'

(The help messages have been simplified a bit for brevity.)

`Argh` easily maps plain Python functions to CLI.  Sometimes this is not
enough; in these cases the powerful API of `argparse` is also available:

.. code-block:: python

    @arg('text', default='hello world', nargs='+', help='The message')
    def echo(text):
        print text

The approaches can be safely combined even up to this level:

.. code-block:: python

    # adding help to `foo` which is in the function signature:
    @arg('foo', help='blah')
    # these are not in the signature so they go to **kwargs:
    @arg('baz')
    @arg('-q', '--quux')
    # the function itself:
    def cmd(foo, bar=1, *args, **kwargs):
        yield foo
        yield bar
        yield ', '.join(args)
        yield kwargs['baz']
        yield kwargs['quux']

Links
-----

* `Project home page`_ (GitHub)
* `Documentation`_ (Read the Docs)
* `Package distribution`_ (PyPI)
* Questions, requests, bug reports, etc.:

  * `Issue tracker`_ (GitHub)
  * `Mailing list`_ (subscribe to get important announcements)
  * Direct e-mail (neithere at gmail com)

.. _project home page: http://github.com/neithere/argh/
.. _documentation: http://argh.readthedocs.org
.. _package distribution: http://pypi.python.org/pypi/argh
.. _issue tracker: http://github.com/neithere/argh/issues/
.. _mailing list: http://groups.google.com/group/argh-users

Author
------

Developed by Andrey Mikhaylenko since 2010.

See file `AUTHORS` for a complete list of contributors to this library.

Support
-------

The fastest way to improve this project is to submit tested and documented
patches or detailed bug reports.

Otherwise you can "flattr" me: |FlattrLink|_

.. _FlattrLink: https://flattr.com/submit/auto?user_id=neithere&url=http%3A%2F%2Fpypi.python.org%2Fpypi%2Fargh
.. |FlattrLink| image:: https://api.flattr.com/button/flattr-badge-large.png
   :alt: Flattr the Argh project

Licensing
---------

Argh is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Argh is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with Argh.  If not, see <http://gnu.org/licenses/>.

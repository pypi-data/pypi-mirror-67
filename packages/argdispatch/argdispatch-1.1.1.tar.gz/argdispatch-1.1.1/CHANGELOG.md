* argdispatch 1.1.1 (2020-04-27)

    * Minor test and setup improvements.
    * Remove useless entry points (old tests that should not have made it to production).

    -- Louis Paternault <spalax+python@gresille.org>

* argdispatch 1.1.0 (2020-04-20)

    * Improvements
      * New methods `add_entrypoints_modules()` and `add_entrypoints_functions()` (closes #4).
      * Methods `add_module()` and `add_submodules()` now accept relative modules (closes #1).
      * Methods `add_module()` and `add_submodules()` now accept modules (not only module names) as arguments (closes #3).

    * Backward-incompatible changes (fixes for design mistakes)
      * Exceptions raised when importing broken modules are propagated (insted of "wrapped" in an ImporteError exception).
      * Remove option `path` from methods `add_module()` and `add_submodules()` (closes #5).
      * Replace broken option `forcepackage` with a working option `forcemain` (closes #6).

    * Setup
        * Setup: Drop setup.py as much as possible in favor of setup.cfg and pyproject.toml.
        * Add python3.7 and python3.8 support.
        * Drop python3.5 and python3.6 support.

    -- Louis Paternault <spalax+python@gresille.org>

* argdispatch 1.0.0 (2018-03-07)

    * Fix examples in README and documentation.
    * Drop python3.4 support
    * Minor code and documentation improvements.

    -- Louis Paternault <spalax+python@gresille.org>

* argdispatch 0.2.0 (2017-04-28)

    * Add python3.6 support.
    * Help message are no longer searched in `__main__` modules and in modules
      that are not packages. Closes #2.

        This adds a (minor) backward incompatibility, since some help messages
        are no longer searched in the same module they were searched before (or a
        no longer searched at all). However, this was necessary because it fixes
        a bad design. For instance, searching a help message in the docstring of
        a `__main__` package means importing it to access the docstring, and
        (maybe) importing it again to run it. This is discouraged, and displayed
        the warning (described in #2).

    -- Louis Paternault <spalax+python@gresille.org>

* argdispatch 0.1.1 (2016-05-21)

    * Fix default values for `ondouble` and `onerror` arguments.
    * Small internal and documentation fixes.

    -- Louis Paternault <spalax+python@gresille.org>

* argdispatch 0.1.0 (2016-04-14)

    * No change compared to beta version.

    -- Louis Paternault <spalax+python@gresille.org>

* argdispatch 0.1.0-beta1 (2016-04-12)

    * Initial release

    -- Louis Paternault <spalax+python@gresille.org>

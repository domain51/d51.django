d51.django
==========
A collection of reusable apps and extension for the Django framework


Introduction
------------
d51.django provides Django users with a set of tested, reusable applications
that extend the behavior of Django in new and interesting ways.  Among the apps
it provides are:

 * Simple blogs
 * A reusable invitation framework
 * Generic model scheduling
 * Hierarchical tagging
 * Extended authentication, include Twitter and Facebook
 * And, as they say, much more.


Installation
------------
This package contains no code, only the code necessary for building d51.django.
To build d51.django, you need the latest 1.0x version of [Fabric][], then run
the following to grab all of the source from its various repositories:

    fab src

You can then build or install the package using `setup.py` as you normally
would, or via Fabric using the setup command:

    fab setup:install
    fab setup:sdist

For convenience, there are the following functions available as well:

    fab install
    fab build
    fab sdist


Testing
-------
_TODO_


Legal
-----
d51.django is released under a dual license, 
[Common Development and Distribution License][CDDL] and [GPLv3][].

It is, in no way affiliated with the Django project or the Django Software
Foundation.  Django is a registered trademark of the Django Software
Foundation.

[Fabric]: http://fabfile.org/
[CDDL]: http://www.opensource.org/licenses/cddl1.php
[GPLv3]: http://opensource.org/licenses/gpl-3.0.html

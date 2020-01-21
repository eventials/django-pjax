django-pjax |Build Status| |Version|
====================================

An improvement of Django-PJAX_: The Django helper for jQuery-PJAX.

What's PJAX?
------------

PJAX is essentially AHAH_ ("Asynchronous HTML and HTTP"), except with
real permalinks and a working back button. It lets you load just a
portion of a page (so things are faster) while still maintaining the
usability of real links.

A demo makes more sense, so `check out the one defunkt put together`_.

Credits
-------

This project is an extension of Django-PJAX_ and all credits from the
original version goes to `Jacob Kaplan-Moss`_.

About
-----

This project keeps the original structure, but add new features to it,
and aims to keep django-pjax updated. Some goals are to keep this
project working with Python 2.7+ and 3.3+ and also Django 1.5+.

Feel free to submit a PR and contribute to this project.

Compatibility
-------------

-  Python 2.6+ or 3.2+
-  PyPy or PyPy3
-  CPython
-  Django 1.3+

Not all Django versions works with Python, PyPy or CPython. See the
Django docs to know more about supported versions.

Install
-------

Just run:

``pip install django-pjax``

Usage
-----

First, read about `how to use jQuery-PJAX`_ and pick one of the
techniques there.

Next, make sure the views you're PJAXing are using TemplateResponse_.
You can't use Django-PJAX with a normal ``HttpResponse``, only
``TemplateResponse``.

PJAX decorator
~~~~~~~~~~~~~~

The pjax decorator:

.. code:: python

    pjax(pjax_template=None, additional_templates=None, follow_redirects=False)

``pjax_template`` (str): default template.

``additional_templates`` (dict): additional templates for multiple
containers.

``follow_redirects`` (bool): if True, all django redirects will force a
page reload, instead of placing the content in the pjax context.

Decorate these views with the pjax decorator:

.. code:: python

    from djpjax import pjax

    @pjax()
    def my_view(request):
        return TemplateResponse(request, "template.html", {'my': 'context'})

After doing this, if the request is made via jQuery-PJAX, the
``@pjax()`` decorator will automatically swap out ``template.html`` for
``template-pjax.html``.

More formally: if the request is a PJAX request, the template used in
your ``TemplateResponse`` will be replaced with one with ``-pjax``
before the file extension. So ``template.html`` becomes
``template-pjax.html``, ``my.template.xml`` becomes
``my.template-pjax.xml``, etc. If there's no file extension, the
template name will just be suffixed with ``-pjax``.

You can also manually pick a PJAX template by passing it as an argument
to the decorator:

.. code:: python

    from djpjax import pjax

    @pjax("pjax.html")
    def my_view(request):
        return TemplateResponse(request, "template.html", {'my': 'context'})

You can also pick a PJAX template for a PJAX container and use multiple
decorators to define the template for multiple containers:

.. code:: python

    from djpjax import pjax

    @pjax(pjax_template="pjax.html",
          additional_templates={"#pjax-inner-content": "pjax_inner.html")
    def my_view(request):
        return TemplateResponse(request, "template.html", {'my': 'context'})

Class-based view
~~~~~~~~~~~~~~~~

If you'd like to use Django 1.3's class-based views instead, a PJAX
Mixin class is provided as well. Simply use ``PJAXResponseMixin`` where
you would normally have used ``TemplateResponseMixin``, and your
``template_name`` will be treated the same way as above.

You can alternately provide a ``pjax_template_name`` class variable if
you want a specific template used for PJAX responses:

.. code:: python

    from django.views.generic import View
    from djpjax import PJAXResponseMixin

    class MyView(PJAXResponseMixin, View):
        template_name = "template.html"
        pjax_template_name = "pjax.html"

        def get(self, request):
            return self.render_to_response({'my': 'context'})

That's it!

Using Template Extensions
-------------------------

If the content in your ``template-pjax.html`` file is very similar to
your ``template.html`` an alternative method of operation is to use the
decorator ``pjaxtend``, as follows:

.. code:: python

    from djpjax import pjaxtend

    @pjaxtend
    def my_view(request):
        return TemplateResponse(request, "template.html", {'my': 'context'})

Then, in your ``template.html`` file you can do the following::

    {% extends parent %}
    ...
    ...

Note that the template will extend ``base.html`` unless its a pjax
request in which case it will extend ``pjax.html``.

If you want to define the parent for a standard http or pjax request,
you can do so as follows:

.. code:: python

    from djpjax import pjaxtend

    @pjaxtend('someapp/base.html', 'my-pjax-extension.html')
    def my_view(request):
        return TemplateResponse(request, "template.html", {'my': 'context'})

Using this approach you don't need to create many ``*-pjax.html`` files.

If you have a collision with the variable name ``parent`` you can
specify the context variable to use as the third parameter to pjaxtexd,
as follows:

.. code:: python

    from djpjax import pjaxtend

    @pjaxtend('someapp/base.html', 'my-pjax-extension.html', 'my_parent')
    def my_view(request):
        return TemplateResponse(request, "template.html", {'my': 'context'})

Which would require the following in your template::

    {% extends my_parent %}
    ...
    ...

Testing
-------

Install dependencies:

``pip install -r requirements.txt``

Run the tests:

``python tests.py``

.. |Build Status| image:: https://travis-ci.org/eventials/django-pjax.svg?branch=master
   :target: https://travis-ci.org/eventials/django-pjax
.. |Version| image:: https://img.shields.io/pypi/v/django-pjax.svg
   :target: https://pypi.python.org/pypi/django-pjax

.. _how to use jQuery-PJAX: https://github.com/defunkt/jquery-pjax
.. _AHAH: http://www.xfront.com/microformats/AHAH.html
.. _check out the one defunkt put together: http://pjax.heroku.com/
.. _TemplateResponse: http://django.me/TemplateResponse
.. _Django-PJAX: https://github.com/jacobian-archive/django-pjax
.. _Jacob Kaplan-Moss: http://jacobian.org/

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-pjax',
    version='1.5',
    description='Django-PJAX: The Django helper for jQuery-PJAX.',
    license='BSD',
    long_description=read('README.rst'),
    url='https://github.com/eventials/django-pjax',
    author='Jacob Kaplan-Moss',
    author_email='jacob@jacobian.org',
    maintainer='Alexandre Vicenzi',
    maintainer_email='vicenzi.alexandre@gmail.com',
    py_modules=['djpjax'],
    install_requires=['django>=1.3'],
    keywords=['django', 'PJAX', 'ajax', 'jQuery'],
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.4',
        'Framework :: Django :: 1.5',
        'Framework :: Django :: 1.6',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ),
)

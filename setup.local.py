
import platform
from setuptools import setup, find_packages
from binding_version import binding_version
from setuptools.dist import Distribution
from setuptools.extension import Extension


class BinaryDistribution(Distribution):
    def __init__(self, attrs=None):
        Distribution.__init__(self, attrs)
        # The values used for the name and sources in the Extension below are
        # not important, because we override the build_ext command above.
        # The normal C extension building logic is never invoked, and is
        # replaced with our own custom logic. However, ext_modules cannot be
        # empty, because this signals to other parts of distutils that our
        # package contains C extensions and thus needs to be built for
        # different platforms separately.
        self.ext_modules = [Extension('h3c', [])]


long_description = open('README.rst').read()

setup(
    name='h3',
    version=binding_version,
    description=
    'Python bindings for H3, a hierarchical hexagonal geospatial indexing system developed by Uber Technologies',
    long_description=long_description,
    author='Uber Technologies',
    author_email='Niel Hu <hu.niel92@gmail.com>',
    url='https://github.com/uber/h3-py.git',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=[],
    package_data={
        'h3':
        ['out/*.dylib' if platform.system() == 'Darwin' else (
            'out/*.dll' if platform.system() == 'Windows' else
            'out/*.so.*')]
    },
    license='Apache License 2.0')
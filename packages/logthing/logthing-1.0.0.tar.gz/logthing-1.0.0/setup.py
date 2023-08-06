import os, sys

from logthing import __version__

readme = os.path.join(os.path.dirname(__file__), 'README.rst')
long_description = open(readme).read()


SETUP_ARGS = dict(
    name='logthing',
    version=__version__,
    description=(('Size based rotating log handler and various log config '
        'tools ')),
    long_description=long_description,
    url='https://github.com/cltrudeau/logthing',
    author='Christopher Trudeau',
    author_email='ctrudeau+pypi@arsensa.com',
    license='MIT',
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='size rotating log handler,log configuration tools',
    test_suite='load_tests.get_suite',
    install_requires = [
        'portalocker>=1.7.0',
    ],
    tests_require=[
        'context_temp==0.10.0',
        'waelstow==0.10.1',
    ],
)

if __name__ == '__main__':
    from setuptools import setup, find_packages

    SETUP_ARGS['packages'] = find_packages()
    setup(**SETUP_ARGS)

from __future__ import print_function
import sys
import re
import unittest

try:
    # try setuptools first, to get access to build_sphinx and test commands
    from setuptools import setup

    using_setuptools = True
except ImportError:
    from distutils.core import setup

    using_setuptools = False


def pyro_test_suite():
    testloader = unittest.TestLoader()
    testsuite = testloader.discover("tests/PyroTests", pattern="test*.py")
    return testsuite


if __name__ == '__main__':
    with open("src/Pyro4/constants.py") as constants_file:
        # extract the VERSION definition from the Pyro4.constants module without importing it
        version_line = next(line for line in constants_file if line.startswith("VERSION"))
        pyro4_version = re.match("VERSION ?= ?['\"](.+)['\"]", version_line).group(1)
    print('Pyro version = %s' % pyro4_version)

    setup(
        name="Pyro4",
        version=pyro4_version,
        license="MIT",
        description="distributed object middleware for Python (RPC)",
        long_description="""Pyro means PYthon Remote Objects.
It is a library that enables you to build applications in which
objects can talk to eachother over the network, with minimal programming effort.
You can just use normal Python method calls, with almost every possible parameter
and return value type, and Pyro takes care of locating the right object on the right
computer to execute the method. It is designed to be very easy to use, and to
generally stay out of your way. But it also provides a set of powerful features that
enables you to build distributed applications rapidly and effortlessly.
Pyro is a pure Python library and runs on many different platforms and Python versions.

The source code repository is on Github: https://github.com/irmen/Pyro4

The documentation can be found here: http://pyro4.readthedocs.io
""",
        author="Irmen de Jong",
        author_email="irmen@razorvine.net",
        keywords=["distributed objects", "RPC", "remote method call", "IPC"],
        url="http://pyro4.readthedocs.io",
        package_dir={'': 'src'},
        packages=['Pyro4', 'Pyro4.socketserver', 'Pyro4.test', 'Pyro4.utils'],
        scripts=[],
        platforms="any",
        test_suite="setup.pyro_test_suite",
        install_requires=[
            "serpent>=1.27,<1.30 ; python_version<'3.2'",
            "serpent>=1.27 ; python_version>='3.2'",
        ],
        extras_require={
            ":python_version<'3.4'": ["selectors34"]
        },
        requires=["serpent"],
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Development Status :: 6 - Mature",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Natural Language :: Dutch",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Topic :: Software Development :: Object Brokering",
            "Topic :: System :: Distributed Computing",
            "Topic :: System :: Networking"
        ],
        entry_points={
            'console_scripts': [
                'pyro4-ns=Pyro4.naming:main',
                'pyro4-nsc=Pyro4.nsc:main',
                'pyro4-test-echoserver=Pyro4.test.echoserver:main',
                'pyro4-check-config=Pyro4.configuration:main',
                'pyro4-flameserver=Pyro4.utils.flameserver:main',
                'pyro4-httpgateway=Pyro4.utils.httpgateway:main'
            ]
        },
        options={"install": {"optimize": 0}}
    )

    if len(sys.argv) >= 2 and sys.argv[1].startswith("install"):
        print("\nOnly the Pyro library has been installed (version %s)." % pyro4_version)
        print("If you want to install the tests, the examples, and/or the manual,")
        print("you have to copy them manually to the desired location.")

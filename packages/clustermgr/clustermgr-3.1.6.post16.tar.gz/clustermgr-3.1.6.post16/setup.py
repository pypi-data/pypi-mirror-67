import codecs
import os
import re
from setuptools import setup
from setuptools import find_packages


def find_version(*file_paths):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *file_paths), 'r') as f:
        version_file = f.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='clustermgr',
    author="Gluu",
    author_email="support@gluu.org",
    url="https://github.com/GluuFederation/cluster-mgr/",
    description="Tool to facilitate LDAP replication, key management and log centralization for the Gluu Server",
    long_description="See project `README <https://github.com/GluuFederation/cluster-mgr>`_ for details.",
    version=find_version("clustermgr", "__init__.py"),
    packages=find_packages(exclude=["e2e", "tests"]),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "more_itertools==5.0.0",
        "vine==1.3.0",
        "MarkupSafe==1.1.1",
        "kombu==4.3",
        "billiard==3.5.0.5",
        "Jinja2==2.11.2",
        "email-validator==1.1.0",
        "cffi",
        "asn1crypto",
        "blinker",
        "pynacl",
        "pyasn1",
        "bcrypt",
        "alembic",
        "WTForms",
        "Flask==1.1.1",
        "Flask-WTF",
        "celery==4.2.2",
        "Flask-SQLAlchemy",
        "redis==3.2.0",
        "requests>=2.20.0",
        "Flask-Migrate",
        "ldap3",
        "paramiko==2.7.1",
        "pyOpenSSL==19.0.0",
        "Flask-Login",
        "Flask-Mail",
        "cryptography",
        "ipaddress",
        "enum34",
        "oxdpython",
        "influxdb==5.2.3",
        "gunicorn==19.10.0",
        "psutil==5.7.0",
    ],
    scripts=['clusterapp.py', 'clustermgr-cli'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: System Administrators',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: System :: Logging',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Systems Administration'
    ],
    license='All Rights Reserved',
)

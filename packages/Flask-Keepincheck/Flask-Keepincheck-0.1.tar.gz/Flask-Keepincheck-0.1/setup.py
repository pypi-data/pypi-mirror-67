"""
Flask-Keepincheck
-------------

Flask extension that implements healthchecks for application's upstream dependencies
"""
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name='Flask-Keepincheck',
    version='0.1',
    url='https://github.com/Shuttl-Tech/flask-keepincheck',
    license='MIT',
    author='Abhirag Awasthi',
    author_email='abhirag.awasthi@shuttl.com',
    description='Healthchecks for upstream dependencies of a Flask app',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['flask_keepincheck'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

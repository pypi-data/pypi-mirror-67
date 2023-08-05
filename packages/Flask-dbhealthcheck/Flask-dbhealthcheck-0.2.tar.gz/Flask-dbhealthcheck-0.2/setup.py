"""
Flask-dbhealthcheck
-------------

Flask extension that implements a database healthcheck for your application
"""
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name='Flask-dbhealthcheck',
    version='0.2',
    url='http://example.com/flask-dbhealthcheck/',
    license='MIT',
    author='Abhirag Awasthi',
    author_email='abhirag.awasthi@shuttl.com',
    description='Database healthcheck for your Flask app',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['flask_dbhealthcheck'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
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

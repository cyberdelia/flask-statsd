from setuptools import setup

setup(
    name='Flask-StatsD',
    version='0.1.0',
    url='https://github.com/cyberdelia/flask-statsd',
    license='BSD',
    author='Timothee Peignier',
    author_email='timothee.peignier@tryphon.org',
    description='Access to statsd in your app.',
    py_modules=['flask_statsd'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['Flask', 'statsd'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

Flask-StatsD
============

This is a simple Flask extension that allows to access statsd in your Flask application.


Installation
------------

To install it, simply: ::

    pip install Flask-StatsD


Usage
-----

You only need to import and initialize your app ::

    from flask import Flask
    from flask.ext.statsd import StatsD

    app = Flask(__name__)
    app.config['STATSD_HOST'] = 'statsd.local'
    statsd = StatsD(app)



from statsd import StatsClient


class StatsD(object):
    def __init__(self, app=None, config=None):
        self.config = None
        self.statsd = None
        if app is not None:
            self.init_app(self.app)
        else:
            self.app = None

    def init_app(self, app, config=None):
        if config is not None:
            self.config = config
        elif self.config is None:
            self.config = app.config

        self.config.setdefault('STATSD_HOST', 'localhost')
        self.config.setdefault('STATSD_PORT', 8125)
        self.config.setdefault('STATSD_PREFIX', None)

        self.app = app

        self.statsd = StatsClient(self.config['STATSD_HOST'],
            self.config['STATSD_PORT'], self.config['STATSD_PREFIX'])

    def timer(self, *args, **kwargs):
        return self.statsd.timer(*args, **kwargs)

    def timing(self, *args, **kwargs):
        return self.statsd.timing(*args, **kwargs)

    def incr(self, *args, **kwargs):
        return self.statsd.incr(*args, **kwargs)

    def decr(self, *args, **kwargs):
        return self.statsd.decr(*args, **kwargs)

    def gauge(self, *args, **kwargs):
        return self.statsd.gauge(*args, **kwargs)

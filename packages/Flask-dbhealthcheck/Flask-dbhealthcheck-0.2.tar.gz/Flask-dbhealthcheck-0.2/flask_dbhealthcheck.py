class DbHealthCheck(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self):
        app.add_url_rule('/dbhealthcheck', view_func=self.check_db)

    def check_db(self):
        return "Hello, world!"

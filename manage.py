import os
import sys
import unittest

from flask_script import Manager

from app import blueprint
from app.main import create_app

env_type = 'test' if 'test' in sys.argv else os.getenv('TANKS_ENV') or 'dev'

app = create_app(env_type)
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)


@manager.command
def run():
    app.run(port=8001)


@manager.command
@manager.option('--pattern', '-p', dest='pattern')
def test(pattern=None):
    """Runs the unit tests."""
    pattern = "test*%s*.py" % pattern if pattern else "test*.py"
    tests = unittest.TestLoader().discover('app/test', pattern=pattern)
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()

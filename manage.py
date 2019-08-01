import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_cors import CORS

from app import blueprint
from app.main import create_app, db
import uuid
import datetime
from app.main.model import user, blacklist, encarte


app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

CORS(app)

@manager.command
def run():
    app.run()

@manager.command
def seed():
    db.session.add(user.User(public_id=str(uuid.uuid4()),
            email='admin@admin.com',
            password='1234',
            registered_on=datetime.datetime.utcnow(),
            name='Admin',
            admin=True,
            document='00000000000'))
    db.session.commit()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()

from app import create_app,db
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand
from app.models import User

# @manager.shell
# def make_shell_context)():
#     return dict(app = app, db = db, User = User)


app = create_app('default')

manager = Manager(app)
migrate = Migrate('db', MigrateCommand)
manager.add_command('server', Server)

if __name__ == '__main__':
    app.secret_key = 'youwillsucceed'
    manager.run()


from flask_migrate import Migrate
from app import create_app, db
from app.models import User, Item, Variant, UserActivity


app = create_app()

migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Item=Item, Variant=Variant, UserActivity=UserActivity)

if __name__ == '__main__':
    app.run()

# flask-keepincheck
Flask extension that implements healthchecks for application's upstream dependencies

## Usage

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_keepincheck import HealthCheck

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ''
db = SQLAlchemy(app)
healthcheck = HealthCheck()
healthcheck.add_db_check(app=app, db=db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

After this your db's healthcheck can be found at `/dbhealth`

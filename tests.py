import email
import unittest

from sqlalchemy import true
from flaskbackend import create_app, db
from flaskbackend.models import User
from config import Config

class TestConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI="sqlite://"

class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_user_creation(self):
        u = User(username="foo", email="foo@bar.com")
        db.session.add(u)
        db.session.commit()
        self.assertEqual(u.username, "foo")
        self.assertEqual(u.email, "foo@bar.com")

if __name__ == '__main__':
    unittest.main(verbosity=2)


        
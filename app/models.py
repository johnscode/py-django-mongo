from bson import ObjectId
import bcrypt


class User:
    def __init__(self, username, email, password, _id=None):
        self._id = ObjectId(_id) if _id else ObjectId()
        self.username = username
        self.email = email
        self.password = make_password(password)  # never store plain text passwords!

    @classmethod
    def from_dict(cls, data):
        return cls(
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password'),
            _id=data.get('_id')
        )

    def to_dict(self):
        return {
            '_id': self._id,
            'username': self.username,
            'email': self.email,
            'password': self.password
        }

    def check_password(self, raw_pass: str):
        raw_bytes = raw_pass.encode('utf-8')
        return bcrypt.checkpw(raw_bytes, self.password)


def make_password(password : str):
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bytes, salt)

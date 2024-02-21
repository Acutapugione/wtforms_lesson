from flask import Flask
from uuid import uuid4


app = Flask(__name__)
WTF_CSRF_SECRET_KEY = str(uuid4())
app.secret_key = str(uuid4())
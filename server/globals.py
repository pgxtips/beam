from flask import Flask
app_server = Flask(__name__, static_folder="../client/build", static_url_path="")

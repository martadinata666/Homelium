from ctypes import addressof
from flask import Flask
import routes.mainpage

app = Flask(__name__)

app.add_url_rule("/", view_func=routes.mainpage.mainpage)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host = "0.0.0.0")
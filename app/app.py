from flask import Flask
from modules import dashboard, add

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.add_url_rule("/", view_func=dashboard.mainpage)
app.add_url_rule("/new", "new", view_func=add.mainpage)
app.add_url_rule("/add", "add", methods=["POST"], view_func=add.addApp)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host = "0.0.0.0")
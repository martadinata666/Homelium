from flask import render_template
import json

def mainpage():

    with open("app/config.json", 'r') as f:
        links_dict = json.load(f)

    return render_template("mainpage.html", links_dict = links_dict)
import json
from flask import redirect, render_template, request

def mainpage():
    return render_template("new.html")

def addApp():

    with open("app/config.json", 'r') as f:
        links_dict = json.load(f)

    counter = 0
    for group in links_dict:
        if group["name"] == request.form["group"]:
            links_dict[counter]["apps"].append({"name":request.form["name"], "image":request.form["image"], "url":request.form["url"]})

            with open("app/config.json", 'w', encoding='utf-8') as f:
                json.dump(links_dict, f, ensure_ascii=False, indent=4)

        counter += 1
    
    
    return redirect("/")
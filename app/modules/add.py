import json
from flask import redirect, render_template, request
import requests

def mainpage():
    return render_template("new.html")

def addApp():

    with open("app/config.json", 'r') as f:
        links_dict = json.load(f)

    response = requests.get(request.form["image"])

    file = open("app/static/img/" + request.form["name"] + ".png", "wb")
    file.write(response.content)
    file.close()

    counter = 0
    found = False
    for group in links_dict:
        if group["name"] == request.form["group"]:

            found = True

            links_dict[counter]["apps"].append({"name":request.form["name"], "image":"static/img/" + request.form["name"] + ".png", "url":request.form["url"]})

            with open("app/config.json", 'w', encoding='utf-8') as f:
                json.dump(links_dict, f, ensure_ascii=False, indent=4)

        counter += 1
    
    if found == False:
        links_dict.append({"name":request.form["group"], "apps":[]})
        links_dict[counter]["apps"].append({"name":request.form["name"], "image":"static/img/" + request.form["name"] + ".png", "url":request.form["url"]})
        
        with open("app/config.json", 'w', encoding='utf-8') as f:
            json.dump(links_dict, f, ensure_ascii=False, indent=4)
    
    return redirect("/")
from flask import Flask,jsonify,request

app = Flask(__name__)

contactList = []

@app.route("/add-data",methods = ["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data!"
        })

@app.route("/add-task",methods = ["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status" : "error",
            "message" : "please provide the data",
        },400)
    contact = {
        "id" : contactList[-1]["id"]+1,
        "name" : request.json["name"],
        "contact" : request.json.get("contact"),
        "done" : False
    }
    contactList.append(contact)
    return jsonify({
        "status" : "succes",
        "message" : "task added succesfully",
        })

if(__name__ == "__main__"):
    app.run(debug = True)
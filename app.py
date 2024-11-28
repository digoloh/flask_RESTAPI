# import the Flask class from the flask library
from flask import Flask, jsonify, request 
import json

# create an instance of the Flask class and assign to app
# __name__ refers to the default path of the package
app = Flask(__name__)

# decorator @ is used to determine path and trigger proceeding function
@app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get("/get-json")
def get_json():
    response = [{"forename":"Francis"},{"surname":"Morrissey"}]
    return jsonify (response)

@app.post("/post-json")
def post_json():
  data = request.get_json() # access data from POST request
  print(json.dumps(data,indent=4))
  return jsonify(data)
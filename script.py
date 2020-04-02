import json
import io
from flask import Flask, request
from flask_cors import CORS, cross_origin
import smtplib
from serve import initialize, send_email

app = Flask(__name__)
cors = CORS(app)

#Define the post method.
@app.route('/mail', methods=['POST'])
def send():
    """ 
    Takes in a json file, then sends the email.
    """
    
    # Data the user input
    input_data = request.json
    l = input_data["login"]
    p = input_data["pass"]
    f = input_data["from"]
    t = input_data["to"]
    m = input_data["message"]
    
    #API function
    conn = initialize(l,p)
    response = send_email(conn,f,t,m)

    return response
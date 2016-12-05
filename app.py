#!/usr/bin/env python
from flask import Flask, jsonify, render_template
from tin_app import *
import sys
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/check/<tin>')
def check_tin(tin):

    # Check if TIN number is valid
    result=check(tin)

    res = {}
   
    if result is False:
        res['valid'] = False
    else:
        res['valid'] = True

        # If TIN is valid, send url to access company info
        res['url'] = tincheck(result)

    return jsonify(res)
   


if __name__ == '__main__':
   app.run()
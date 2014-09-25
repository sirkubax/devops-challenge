#!/usr/bin/env python

from flask import Flask, request
app = Flask(__name__)
import redis


@app.route('/counter',  methods=['POST'])
def post_counter():
    incrBy = request.form['incrBy']
    try:
        if isinstance(int(incrBy), int):
            global rs
            rs.incr("counter", int(incrBy))
            return incrBy 
        else:
            return "NaN"
    except:
        return "NaN"


@app.route('/counter',  methods=['GET'])
def get_counter():
    global rs
    cv = rs.get("counter")
    return cv


def init():
    rs = redis.Redis()
    #rs.set("counter", 1)
    return rs

if __name__ == '__main__':
    print "Starting an app"
    global rs 
    rs = init()
    app.run(port = 8080)

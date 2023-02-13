import random
from flask import Flask 
from threading import Thread 

app = Flask('')
 
@app.route('/')
def home():
    return "Host 24/7 Free With UptimeRobot (Not Sponsored)"
 
def run():
  app.run(host='0.0.0.0',port=random.randint(1000, 9999))
 
def keep_alive():
    t = Thread(target=run)
    t.start()
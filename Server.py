from flask import Flask
app = Flask(__name___) 

@app.route("/")
def home():
  return "<h1>aman</h1>"

if __name__ =="__main__":
  app.run()
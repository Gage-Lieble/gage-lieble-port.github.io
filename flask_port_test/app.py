from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/sent", methods=['post'])
def sent():
    with open('contact.json', 'a') as contacts:
        cont_email = request.form["contact_email"]
        cont_desc = request.form["contact_description"]
        contacts.write('\n' + cont_email)
        contacts.write(' - Description:  ' + cont_desc)
    
    return render_template("contact_sub.html", cont_email=cont_email, cont_desc=cont_desc)


#-*- coding: utf-8 -*-
"""View."""
from flask import Blueprint, render_template, abort, redirect, url_for
from flask import request, session
from jinja2 import TemplateNotFound
import simplejson as json
import requests

bp_auth = Blueprint('users', __name__,
                        template_folder='templates')


@bp_auth.route('/',methods=['GET'])
def login():
	return render_template('login/index.html')


@bp_auth.route('/', methods=['POST'])
def login_callback():
	email = request.form.get("email") 
	password = request.form.get("password")
	headers = {'Content-Type': 'application/json'}
	payload = {"email": email, "password": password}
	response = requests.post("http://localhost:3000/auth", data=json.dumps(payload), headers=headers)
	if response.status_code == 200:
		token = response.json()['token']
		session['user_token'] = response.json()['token']
		return redirect("./users")
 


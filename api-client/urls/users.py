#-*- coding: utf-8 -*-
"""View."""
from flask import Blueprint, render_template, abort, redirect, url_for
from flask import request
from jinja2 import TemplateNotFound
import simplejson as json
import requests

bp_users = Blueprint('bp_users', __name__,
                        template_folder='templates')



@bp_users.route('/',methods=['GET'])
def list_users():
	result = requests.get("http://localhost:3000/users")
	context = {"users": result.json()}
	return render_template('users/index.html', **context), 200 
 

@bp_users.route('/add', methods=['GET'])
def insert_form():
	context = {"user":[]}
	return render_template('users/form.html', **context), 200 
 
@bp_users.route('/add', methods=['POST']) 
def insert_user():
	# session.get('user')
	# session['username'] = username
	# import ipdb; ipdb.set_trace()
	name = request.form.get("nome") 
	password = request.form.get("password") 
	email = request.form.get("email") 
	permission = request.form.get("permission") 
	payload = {
		'name': name, 
		'password': password,
		'email': email,
		'permission': permission
		}
	headers = {'Content-Type': 'application/json'}
	response = requests.post("http://localhost:3000/users", data=json.dumps(payload), headers=headers)
	if response.status_code == 200:
		return redirect(url_for('bp_users.list_users'))

@bp_users.route('/update/<int:id>', methods=['GET'])
def update_form(id):
	result = requests.get("http://localhost:3000/user/{id}".format(id=id))
	context = {"user": result.json()}
	return render_template('users/form.html', **context), 200 
 
@bp_users.route('/update/<int:id>', methods=['POST'])
def update_user(id):
	name = request.form.get("nome") 
	password = request.form.get("password") 
	email = request.form.get("email") 
	permission = request.form.get("permission")
	payload = {
		'name': name, 
		'email': email,
		'permission': permission
		}
	if password:
		payload['password'] = password

	headers = {'Content-Type': 'application/json'}
	response = requests.put("http://localhost:3000/user/{id}".format(id=id), data=json.dumps(payload), headers=headers)
	print response.status_code
	if response.status_code == 204:
		return redirect(url_for('bp_users.list_users'))

@bp_users.route('/delete/<int:id>', methods=['GET'])
def delete_user(id):
	headers = {'Content-Type': 'application/json'}
	response = requests.delete("http://localhost:3000/user/{id}".format(id=id))
	if response.status_code == 204:
		return redirect(url_for('bp_users.list_users'))
		
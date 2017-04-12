#-*- coding: utf-8 -*-
"""View."""
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import requests

bp_users = Blueprint('bp_users', __name__,
                        template_folder='templates')


@bp_users.route('/',methods=['GET'])
def list_users():
	r = requests.get('<MY_URI>',headers=('Authorization: TOK:<MY_TOKEN>'))
	r.json()
	return render_template('users/index.html') 
 

@bp_users.route('/add', methods=['GET'])
def insert_form():
	return render_template('users/form.html') 
 
@bp_users.route('/add', methods=['POST']) 
def insert_user():
	session.get('user')
	session['username'] = username
	name = request.values.get("name") 
	password = request.values.get("password") 
	email = request.values.get("email") 
	permission = request.values.get("permission") 
	data = {
		'name': name, 
		'password': password,
		'email': email,
		'permission': permission
		}
	r = requests.post("http://localhost:3000/user", data=data)
	print r.text
	return render_template('users/form.html') 
 


@bp_users.route('/update/<int:id>', methods=['GET'])
def update_form(id):
	result = requests.get("http://localhost:3000/user")
	return render_template('users/form.html', **result) 

@bp_users.route('/update/<int:id>', methods=['GET'])
def update_user():
	name = request.values.get("name") 
	password = request.values.get("password") 
	email = request.values.get("email") 
	permission = request.values.get("permission") 
	data = {
		'name': name, 
		'password': password,
		'email': email,
		'permission': permission
		}
	r = requests.put("http://localhost:3000/user/{id}".format(id=id), data=data)
	pass 

@bp_users.route('/delete/<int:id>', methods=['GET'])
def delete_user(id):
	r = requests.delete("http://localhost:3000/user/{id}".format(id=id), data=payload)
	pass 
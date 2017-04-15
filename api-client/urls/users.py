#-*- coding: utf-8 -*-
"""View."""
from flask import Blueprint, render_template, abort, redirect, url_for
from flask import request, session
from jinja2 import TemplateNotFound
import simplejson as json
import requests

bp_users = Blueprint('users', __name__,
                        template_folder='templates')

@bp_users.route('/',methods=['GET'])
def list_users():
	if 'user_token' not in session:
		return redirect(url_for('auth.login'))
	
	headers = {
		'Content-Type': 'application/json',
		'Authorization': 'JWT {token}'.format(token=session.get('user_token'))
	}
	result = requests.get("http://localhost:3000/user", headers=headers)
	context = {"users": result.json(), "permission": session.get("permission")}
	return render_template('users/index.html', **context), 200 


@bp_users.route('/all',methods=['GET'])
def list_all_users():
	if 'user_token' not in session:
		return redirect(url_for('auth.login'))
	
	headers = {
		'Content-Type': 'application/json',
		'Authorization': 'JWT {token}'.format(token=session.get('user_token'))
	}
	result = requests.get("http://localhost:3000/users/all", headers=headers)
	context = {"users": result.json(), "permission": session.get("permission")}
	return render_template('users/users.html', **context), 200 
 
 

@bp_users.route('/add', methods=['GET'])
def insert_form():
	if 'user_token' not in session:
		return redirect(url_for('auth.login'))
	
	context = {"user":[], "permission": session.get("permission")}
	return render_template('users/form.html', **context), 200 
 
@bp_users.route('/add', methods=['POST']) 
def insert_user():
	errors = ''
	name = request.form.get("nome").strip() 
	password = request.form.get("password").strip() 
	email = request.form.get("email").strip() 
	permission = request.form.get("permission")

	if not permission:
		permission = "false"

	if not name or not password or not email:
		errors = "Preencha todos os campos."

	if not errors:
		payload = {
			'name': name, 
			'password': password,
			'email': email,
			'permission': permission
			}

		headers = {
			'Content-Type': 'application/json',
			'Authorization': 'JWT {token}'.format(token=session.get('user_token'))
		}

		response = requests.post("http://localhost:3000/users", data=json.dumps(payload), headers=headers)
		if response.status_code == 200:
			if session.get("permission"):
				return redirect(url_for('users.list_all_users'))
			else:
				return redirect(url_for('users.list_users'))
	else:
		context = {"user": {"name": name, "email": email, "password": password, "permission": permission}, 
			"errors": errors, "permission": session.get("permission")}
		return render_template('users/form.html', **context), 200


@bp_users.route('/update/<int:id>', methods=['GET'])
def update_form(id):
	# import ipdb; ipdb.set_trace()
	if 'user_token' not in session:
		return redirect(url_for('auth.login'))
	
	headers = {
		'Content-Type': 'application/json',
		'Authorization': 'JWT {token}'.format(token=session.get('user_token'))
	}
	
	result = requests.get("http://localhost:3000/user/", headers=headers)
	context = {"user": result.json(), "permission": session.get("permission")}
	return render_template('users/form.html', **context), 200 
 
@bp_users.route('/update/<int:id>', methods=['POST'])
def update_user(id):
	errors = ''
	name = request.form.get("nome").strip() 
	password = request.form.get("password").strip() 
	email = request.form.get("email").strip() 
	permission = request.form.get("permission")

	if not permission:
		permission = "false"
	
	if not name or not email:
		errors = "Preencha todos os campos."

	if not errors:
		payload = {
			'name': name, 
			'email': email,
			'permission': permission
			}
		if password:
			payload['password'] = password

		headers = {
			'Content-Type': 'application/json',
			'Authorization': 'JWT {token}'.format(token=session.get('user_token'))
		}

		response = requests.put("http://localhost:3000/user/", data=json.dumps(payload), headers=headers)
		if response.status_code == 204:
			return redirect(url_for('users.list_users'))
	else:
		context = {"user": {"name": name, "email": email, "password": password, "permission": permission}, 
			"errors": errors, "permission": session.get("permission")}
		return render_template('users/form.html', **context), 200


@bp_users.route('/delete/<int:id>', methods=['GET'])
def delete_user(id):
	if 'user_token' not in session:
		return redirect(url_for('auth.login'))
	
	headers = {
		'Content-Type': 'application/json',
		'Authorization': 'JWT {token}'.format(token=session.get('user_token'))
	}

	response = requests.delete("http://localhost:3000/user/", headers=headers)
	if response.status_code == 204:
		return redirect(url_for('users.list_users'))
		
#-*- coding: utf-8 -*-
"""View."""
from flask import Blueprint, render_template, abort, redirect, url_for
from flask import request, session
from jinja2 import TemplateNotFound
from config import HOST_API
import simplejson as json
import requests
import re

bp_auth = Blueprint('auth', __name__,
                        template_folder='templates')


@bp_auth.route('',methods=['GET'])
def login():
	u"""Displays the home page"""
	context = {}
	if 'cadastro_sucesso' in session:
		context ={
			"sucesso": session.get('cadastro_sucesso')
		}
		session.clear()
	return render_template('login/index.html', **context)


@bp_auth.route('', methods=['POST'])
def login_callback():
	u"""Checks the user credentials"""
	errors = ''
	email = request.form.get("email").strip()
	password = request.form.get("password").strip()

	if not email or not password:
		errors = "Preencha todos os campos."		
	
	if not errors:
		headers = {'Content-Type': 'application/json'}
		payload = {"email": email, "password": password}
		response = requests.post("{host}auth".format(host=HOST_API), data=json.dumps(payload), headers=headers)
		if response.status_code == 200:
			token = response.json()['token']
			session['user_token'] = response.json()['token']
			session['permission'] = response.json()['permission']

			if session.get("permission"):
				return redirect("./bookmarks/all")
			else:
				return redirect("./bookmarks")
		else:
			context = {"errors": u"Usuário não cadastrado"}
			return render_template('login/index.html', **context)	
 
	else:
		context = {"errors": errors}
		return render_template('login/index.html', **context)	
 
@bp_auth.route('logout', methods=['GET'])
def logout():
	u"""user logout"""
	session.clear()
	return redirect("/")


@bp_auth.route('cadastro', methods=['GET'])
def insert_form():
	u"""loading the login form"""
	context = {"user":[]}
	return render_template('login/cadastro.html', **context), 200 
 
@bp_auth.route('cadastro', methods=['POST']) 
def insert_user():
	u"""Inserts a new user"""
	errors = ''
	name = request.form.get("nome").strip() 
	password = request.form.get("password").strip() 
	email = request.form.get("email").strip() 	

	if not name or not password or not email:
		errors = "Preencha todos os campos."

	if not errors:
		payload = {
			'name': name, 
			'password': password,
			'email': email,
			'permission': "false"
			}

		headers = {
			'Content-Type': 'application/json'
		}

		response = requests.post("{host}users".format(host=HOST_API), data=json.dumps(payload), headers=headers)
		if response.status_code == 200:
			session['cadastro_sucesso'] = "Cadastro realizado com sucesso."
			return redirect(url_for('auth.login'))
	else:
		context = {"user": {"name": name, "email": email, "password": password, "permission": permission}, 
			"errors": errors}
		return render_template('login/cadastro.html', **context), 200
 


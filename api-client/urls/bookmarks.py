#-*- coding: utf-8 -*-
"""View."""
from flask import Blueprint, render_template, abort, redirect, url_for
from flask import request, session
from jinja2 import TemplateNotFound
from config import HOST_API
import simplejson as json
import requests

bp_bookmarks = Blueprint('bookmarks', __name__,
                        template_folder='templates')

def autenticate():
	if 'user_token' not in session:
		return redirect(url_for('auth.login'))
	
@bp_bookmarks.route('/',methods=['GET'])
def list_bookmarks():
	u"""Lists a bookmark's details"""
	autenticate()

	headers = {
		'Content-Type': 'application/json',
		'Authorization': 'JWT {token}'.format(token=session.get('user_token'))
	}
	result = requests.get("{host}bookmarks".format(host=HOST_API), headers=headers)
	context = {"bookmarks": result.json(), "permission": session.get("permission")}
	return render_template('bookmarks/index.html', **context), 200 
 

@bp_bookmarks.route('/all',methods=['GET'])
def all_bookmarks():
	u"""List all bookmarks"""
	autenticate()

	headers = {
		'Content-Type': 'application/json',
		'Authorization': 'JWT {token}'.format(token=session.get('user_token'))
	}
	result = requests.get("{host}bookmarks/all".format(host=HOST_API), headers=headers)
	if result.status_code == 200:
		context = {"all_bookmarks": result.json(), "permission": session.get("permission")}
		return render_template('bookmarks/bookmarks.html', **context), 200
	else:
		return redirect(url_for('bookmarks.list_bookmarks'))


@bp_bookmarks.route('/add', methods=['GET'])
def insert_form():
	u"""Displays the bookmarks form"""
	autenticate()

	context = {"bookmark":[], "permission": session.get("permission")}
	return render_template('bookmarks/form.html', **context), 200 
 

@bp_bookmarks.route('/add', methods=['POST']) 
def insert_bookmark():
	u"""Save bookmarks data"""
	errors = ''
	name = request.form.get("nome").strip() 
	url = request.form.get("url").strip() 
	
	if not name or not url:
		errors = "Preencha todos os campos."
	
	if not errors:
		payload = {
			'name': name, 
			'url': url,
			}
		headers = {
			'Content-Type': 'application/json',
			'Authorization': 'JWT {token}'.format(token=session.get('user_token'))
		}
		response = requests.post("{host}bookmarks".format(host=HOST_API), data=json.dumps(payload), headers=headers)
		if response.status_code == 201:
			return redirect(url_for('bookmarks.list_bookmarks'))
	else:
		context = {"bookmark": {"name": name, "url": url}, "errors": errors, 
			"permission": session.get("permission")}
		return render_template('bookmarks/form.html', **context), 200 


@bp_bookmarks.route('/update/<int:id>', methods=['GET'])
def update_form(id):
	u"""Displays the bookmarks form"""
	autenticate()

	headers = {
		'Content-Type': 'application/json',
		'Authorization': 'JWT {token}'.format(token=session.get('user_token'))
	}
	result = requests.get("{host}bookmark/{id}".format(host=HOST_API, id=id), headers=headers)
	context = {"bookmark": result.json(), "permission": session.get("permission")}
	return render_template('bookmarks/form.html', **context), 200 
 

@bp_bookmarks.route('/update/<int:id>', methods=['POST'])
def update_bookmark(id):
	u"""Update bookmark data"""
	errors = ''
	name = request.form.get("nome").strip() 
	url = request.form.get("url").strip() 
	
	if not name or not url:
		errors = "Preencha todos os campos."
	
	if not errors:	
		payload = {
			'name': name, 
			'url': url,
			}
		headers = {
			'Content-Type': 'application/json',
			'Authorization': 'JWT {token}'.format(token=session.get('user_token'))
		}	
		response = requests.put("{host}bookmark/{id}".format(host=HOST_API, id=id), data=json.dumps(payload), headers=headers)
		if response.status_code == 204:
			return redirect(url_for('bookmarks.list_bookmarks'))
	else:
		context = {"bookmark": {"name": name, "url": url}, "errors": errors, 
			"permission": session.get("permission")}
		return render_template('bookmarks/form.html', **context), 200 


@bp_bookmarks.route('/delete/<int:id>', methods=['GET'])
def delete_bookmark(id):
	u"""Delete bookmark data"""
	autenticate()

	headers = {
		'Content-Type': 'application/json',
		'Authorization': 'JWT {token}'.format(token=session.get('user_token'))
	}
	response = requests.delete("{host}bookmark/{id}".format(host=HOST_API, id=id), headers=headers)
	if response.status_code == 204:
		return redirect(url_for('bookmarks.list_bookmarks'))
		
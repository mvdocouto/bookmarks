#-*- coding: utf-8 -*-
"""View."""
from flask import Blueprint, render_template, abort, redirect, url_for
from flask import request, session
from jinja2 import TemplateNotFound
import simplejson as json
import requests

bp_bookmarks = Blueprint('bookmarks', __name__,
                        template_folder='templates')

@bp_bookmarks.route('/',methods=['GET'])
def list_bookmarks():
	if 'user_token' not in session:
		return redirect(url_for('auth.login'))
	
	headers = {
		'Content-Type': 'application/json',
		'Authorization': 'JWT {token}'.format(token=session.get('user_token'))
	}
	result = requests.get("http://localhost:3000/bookmarks", headers=headers)
	context = {"bookmarks": result.json()}
	return render_template('bookmarks/index.html', **context), 200 
 

@bp_bookmarks.route('/all',methods=['GET'])
def all_bookmarks():
	if 'user_token' not in session:
		return redirect(url_for('auth.login'))

	headers = {
		'Content-Type': 'application/json',
		'Authorization': 'JWT {token}'.format(token=session.get('user_token'))
	}
	result = requests.get("http://localhost:3000/bookmarks/all", headers=headers)
	if result.status_code == 200:
		context = {"all_bookmarks": result.json()}
		return render_template('bookmarks/bookmarks.html', **context), 200
	else:
		return redirect(url_for('bookmarks.list_bookmarks'))


@bp_bookmarks.route('/add', methods=['GET'])
def insert_form():
	if 'user_token' not in session:
		return redirect(url_for('auth.login'))

	context = {"bookmark":[]}
	return render_template('bookmarks/form.html', **context), 200 
 

@bp_bookmarks.route('/add', methods=['POST']) 
def insert_bookmark():
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
		response = requests.post("http://localhost:3000/bookmarks", 
			data=json.dumps(payload), headers=headers)
		if response.status_code == 201:
			return redirect(url_for('bookmarks.list_bookmarks'))
	else:
		context = {"bookmark": {"name": name, "url": url}, "errors": errors}
		return render_template('bookmarks/form.html', **context), 200 


@bp_bookmarks.route('/update/<int:id>', methods=['GET'])
def update_form(id):
	import ipdb; ipdb.set_trace()
	if 'user_token' not in session:
		return redirect(url_for('auth.login'))
	
	headers = {
		'Content-Type': 'application/json',
		'Authorization': 'JWT {token}'.format(token=session.get('user_token'))
	}
	result = requests.get("http://localhost:3000/bookmark/{id}".format(id=id), headers=headers)
	context = {"bookmark": result.json()}
	print context
	return render_template('bookmarks/form.html', **context), 200 
 

@bp_bookmarks.route('/update/<int:id>', methods=['POST'])
def update_bookmark(id):
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
		response = requests.put("http://localhost:3000/bookmark/{id}".format(id=id), 
			data=json.dumps(payload), headers=headers)
		print response.status_code
		if response.status_code == 204:
			return redirect(url_for('bookmarks.list_bookmarks'))
	else:
		context = {"bookmark": {"name": name, "url": url}, "errors": errors}
		return render_template('bookmarks/form.html', **context), 200 


@bp_bookmarks.route('/delete/<int:id>', methods=['GET'])
def delete_bookmark(id):
	if 'user_token' not in session:
		return redirect(url_for('auth.login'))
	
	headers = {
		'Content-Type': 'application/json',
		'Authorization': 'JWT {token}'.format(token=session.get('user_token'))
	}
	response = requests.delete("http://localhost:3000/bookmark/{id}".format(id=id), headers=headers)
	if response.status_code == 204:
		return redirect(url_for('bookmarks.list_bookmarks'))
		
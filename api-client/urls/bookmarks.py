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
	headers = {
		'Content-Type': 'application/json',
		'Authorization': 'JWT {token}'.format(token=session.get('user_token'))
	}
	result = requests.get("http://localhost:3000/bookmarks", headers=headers)
	context = {"bookmarks": result.json()}
	return render_template('bookmarks/index.html', **context), 200 
 


@bp_bookmarks.route('/add', methods=['GET'])
def insert_form():
	context = {"bookmark":[]}
	return render_template('bookmarks/form.html', **context), 200 
 

@bp_bookmarks.route('/add', methods=['POST']) 
def insert_user():
	name = request.form.get("nome") 
	url = request.form.get("url") 
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


@bp_bookmarks.route('/update/<int:id>', methods=['GET'])
def update_form(id):
	headers = {
		'Content-Type': 'application/json',
		'Authorization': 'JWT {token}'.format(token=session.get('user_token'))
	}
	result = requests.get("http://localhost:3000/bookmark/{id}".format(id=id), headers=headers)
	context = {"bookmark": result.json()}
	return render_template('bookmarks/form.html', **context), 200 
 

@bp_bookmarks.route('/update/<int:id>', methods=['POST'])
def update_user(id):
	name = request.form.get("nome") 
	url = request.form.get("url") 
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


@bp_bookmarks.route('/delete/<int:id>', methods=['GET'])
def delete_user(id):
	headers = {
		'Content-Type': 'application/json',
		'Authorization': 'JWT {token}'.format(token=session.get('user_token'))
	}
	response = requests.delete("http://localhost:3000/bookmark/{id}".format(id=id), headers=headers)
	if response.status_code == 204:
		return redirect(url_for('bookmarks.list_bookmarks'))
		
#-*- coding: utf-8 -*-
"""View."""
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import requests

bp_bookmarks = Blueprint('bookmarks', __name__,
                        template_folder='templates')


@bp_bookmarks.route('/',methods=['GET'])
def list_bookmarks():
	return render_template('bookmarks/index.html') 

@bp_bookmarks.route('/add', methods=['GET'])
def view_bookmark_form():
	return render_template('bookmarks/form.html') 

@bp_bookmarks.route('/add', methods=['POST'])
def insert_bookmark():
	pass 


@bp_bookmarks.route('/update/<int:id>', methods=['GET'])
def update_bookmark():
	pass 

@bp_bookmarks.route('/delete/<int:id>', methods=['GET'])
def delete_bookmark():
	pass 
#-*- coding: utf-8 -*-
"""View."""
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import requests

bp_users = Blueprint('bp_users', __name__,
                        template_folder='templates/users')


@bp_users.route('/',methods=['GET'])
def list_users():
	pass 

@bp_users.route('/', methods=['POST'])
def insert_user():
	pass 

@bp_users.route('/update/<int:id>', methods=['GET'])
def update_user():
	pass 

@bp_users.route('/delete/<int:id>', methods=['GET'])
def delete_user():
	pass 
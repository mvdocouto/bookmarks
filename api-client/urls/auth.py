#-*- coding: utf-8 -*-
"""View."""
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import requests

bp_auth = Blueprint('users', __name__,
                        template_folder='templates')


@bp_auth.route('/',methods=['GET'])
def login():
	return render_template('login/index.html')


@bp_auth.route('/', methods=['POST'])
def login_callback():
	pass 


# -*- coding: utf-8 -*-
"""Rotas."""
from app import app
from urls.auth import bp_auth
from urls.users import bp_users
from urls.bookmarks import bp_bookmarks

app.register_blueprint(bp_auth, url_prefix='/login')
app.register_blueprint(bp_users, url_prefix='/users')
app.register_blueprint(bp_bookmarks, url_prefix='/bookmarks')
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
import mongoengine
from flask_mongoengine import MongoEngine

import itsdangerous
import passlib
import flask_babelex
import babel
import blinker
import flask.ext.wtf
import flask_wtf
import six
import flask
import wtforms
import redis
import arrow
import pygeoip
import regex
from werkzeug.contrib import cache
import simplekv
import flask_kvsession

from mongrey.web import settings
from mongrey.web.manager import main
from mongrey.web import extensions
from mongrey.storage.mongo import models

main()
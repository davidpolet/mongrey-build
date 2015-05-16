#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
import MySQLdb
import psycopg2
import peewee
import playhouse
import mongoengine

import blinker
import six
import flask
import arrow
import regex
import psutil
import redis
import pygeoip
from werkzeug.contrib import cache

import wtforms
import wtfpeewee
import flask.ext.wtf
import flask_wtf
from flask_mongoengine import MongoEngine

from mongrey.server.core import main as server_main
from mongrey.web import settings
from mongrey.web.manager import main as web_main
from mongrey.web import extensions

from mongrey.migration.core import main as migration_main

from mongrey.storage.sql import models as sql_models
from mongrey.storage.sql.policy import SqlPolicy

from mongrey.storage.mongo import models as mongo_models
from mongrey.storage.mongo.policy import MongoPolicy
from mongrey.storage.mongo.utils import create_mongo_connection

migration_main()
web_main()
server_main()

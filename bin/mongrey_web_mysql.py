#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

import itsdangerous
import passlib
import flask_babelex
import babel
import blinker
import six
import flask
import redis
import arrow
import pygeoip
import regex
from werkzeug.contrib import cache
import peewee
import playhouse
import wtforms
import wtfpeewee
import simplekv
import flask_kvsession

from mongrey.web import settings
from mongrey.web.manager import main
from mongrey.web import extensions
from mongrey.storage.sql import models

main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
import mongoengine

import six
import psutil
import redis
import arrow
import pygeoip
import regex
from werkzeug.contrib import cache

from mongrey.server.core import main
from mongrey.server import geventdaemon
from mongrey.storage.mongo.policy import MongoPolicy
from mongrey.storage.mongo.utils import create_mongo_connection
from mongrey.storage.mongo import models

main()
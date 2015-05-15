# -*- coding: utf-8 -*-

from PyInstaller.hooks.hookutils import collect_data_files

datas = collect_data_files('mongo_mail_web', subdir='static')
datas += collect_data_files('mongo_mail_web', subdir='templates')
datas += collect_data_files('mongo_mail_web', subdir='translations')
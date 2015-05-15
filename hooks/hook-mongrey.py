# -*- coding: utf-8 -*-

from PyInstaller.hooks.hookutils import collect_data_files

datas = collect_data_files('mongrey', subdir='translations')
datas += collect_data_files('mongrey', subdir='web/static')
datas += collect_data_files('mongrey', subdir='web/templates')
datas += collect_data_files('mongrey', subdir='ext')

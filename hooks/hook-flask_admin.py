# -*- coding: utf-8 -*-

import os
import glob

from PyInstaller.hooks.hookutils import collect_submodules, collect_data_files

hiddenimports = collect_submodules('flask_admin')

datas = collect_data_files('flask_admin', subdir='static')
datas += collect_data_files('flask_admin', subdir='templates')
datas += collect_data_files('flask_admin', subdir='translations')


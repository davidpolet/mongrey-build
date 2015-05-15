# -*- coding: utf-8 -*-

import os
import glob

from PyInstaller.hooks.hookutils import collect_submodules, collect_data_files

hiddenimports = collect_submodules('flask_mongoengine')
datas = collect_data_files('flask_mongoengine', subdir='templates')


# -*- coding: utf-8 -*-

from PyInstaller.hooks.hookutils import collect_submodules, collect_data_files

hiddenimports = collect_submodules('flask.ext')
hiddenimports += collect_submodules('flask_security')

datas = collect_data_files('flask_security', subdir='templates')


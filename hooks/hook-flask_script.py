# -*- coding: utf-8 -*-

from PyInstaller.hooks.hookutils import collect_submodules

hiddenimports = collect_submodules('flask_script')



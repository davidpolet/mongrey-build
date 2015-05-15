# -*- coding: utf-8 -*-

import os
import glob

from PyInstaller.hooks.hookutils import collect_submodules

hiddenimports = collect_submodules('passlib.handlers')


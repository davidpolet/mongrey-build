# -*- coding: utf-8 -*-

import os
import glob

from PyInstaller.hooks.hookutils import collect_data_files
datas = collect_data_files('geoip_data')

# coding=utf-8

"""
This file is part of OpenSesame.

OpenSesame is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OpenSesame is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OpenSesame.  If not, see <http://www.gnu.org/licenses/>.
"""

from libopensesame.py3compat import *
import os
from qtpy.QtCore import QTranslator, QCoreApplication
from libopensesame.oslogging import oslogger
from libqtopensesame.extensions import BaseExtension
from libqtopensesame.misc.translate import translation_context
_ = translation_context(u'RapunzelLocale', category=u'extension')


class RapunzelLocale(BaseExtension):

    def event_startup(self):

        try:
            qm_path = self.ext_resource(self.main_window.locale + u'.qm')
        except Exception as e:
            return
        oslogger.info('installing translator {}'.format(qm_path))
        self.main_window.translator.load(qm_path)

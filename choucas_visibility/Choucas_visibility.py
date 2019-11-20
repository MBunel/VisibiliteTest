# -*- coding: utf-8 -*-

"""
/***************************************************************************
 Choucas_visibility
                                 A QGIS plugin
 Calcul de visibilité et des incertitudes
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2019-07-08
        copyright            : (C) 2019 by Choucas
        email                : Mohssine.Kaouadji@ign.fr
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Choucas'
__date__ = '2019-07-08'
__copyright__ = '(C) 2019 by Choucas'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import sys
import inspect

from qgis.core import QgsProcessingAlgorithm, QgsApplication
from .Choucas_visibility_provider import Choucas_visibilityProvider

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


class Choucas_visibilityPlugin(object):

    def __init__(self):
        self.provider = None
		print("Premier test")

    def initProcessing(self):
        """Init Processing provider for QGIS >= 3.8."""
        self.provider = Choucas_visibilityProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)

    def initGui(self):
        self.initProcessing()

    def unload(self):
        QgsApplication.processingRegistry().removeProvider(self.provider)

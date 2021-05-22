# -*- coding: utf-8 -*-
from __future__ import print_function

__author__ = "Olek B"
__copyright__ = "Copyright 2020, Ortho"
__credits__ = []
__appname__='Ortho'
__license__ = "GPL"
__title__ = "Ortho"
__version__ = "0.1.0"
__maintainer__ = "Olek B"
__email__ = "oleksandr.buzunov@orthoclinicaldiagnostics.com"
__github__=	''
__status__ = "Development" 



import datetime
from pprint import pprint as pp
import wx
import wx.lib.inspection
import wx.lib.mixins.inspection

import json, codecs
import os, sys
from os.path import join, isfile

from ui_layer.utils import ex, format_stacktrace

from multiprocessing import freeze_support 

from ui_layer.StartFrame import StartFrame

        
class myApp(wx.App, wx.lib.mixins.inspection.InspectionMixin):

    def OnInit(self):

        self.InitInspection() 
        wx.SystemOptions.SetOption("mac.window-plain-transition", 1)
        self.SetAppName("Ortho")
        #sys.excepthook = self.MyExceptionHandler

        return True
    def MyExceptionHandler(self, type, value, trace_back):
        """Catch exceptions, log them to file and show error dialog
        """        
        ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')
        #timestamp = myTime.asctime(myTime.localtime(myTime.time()))
        #print('**** %s ****\n' % ts)
        raise


def main_ui(**kwargs):
    freeze_support()

    app 	= myApp(False)
    headless=kwargs.get('headless', False)
    sf 	= StartFrame(None, headless=headless)
    sf.Hide()
    app.MainLoop()
def headless_ui():
    freeze_support()

    app 	= myApp(False)
    
    sf 	= StartFrame(None, headless=True)
    sf.Hide()
    return app
    
if __name__ == "__main__":
    main_ui()
    
import wx
import os, re, sys, copy, string
from os.path import join
import json, shutil, glob

from datetime import datetime 
from copy import deepcopy
from pprint import pprint as pp
from ui.include.log_init import  info, debug
from ui.include.utils import  dict2, exception
from ui.include.common import *

e=sys.exit

import ui.config.ui_config as ui_config 
uic = ui_config.uic

from ui.include.Config import Config
from ui.include.Layout import Layout



class UiLayout(Config): 

    def __init__(self, pipeline):
 
        Config.__init__(self)
        self.cfg = None
        self.pref=None
        self.ppl=pipeline
        self.layout_dir=self.getLayoutDir()
        #self.build_loc = join(UI_TMP_DIR, BUILD_DIR, BUILD_FN )
        self.build_tmpl_loc = join(uic.root, UI_DIR, INCLUDE_DIR, BUILD_DIR, BUILD_TMPL_FN )
    @exception
    def loadLayout(self):
        global  cfg
        
        self.layout_fn = self.getLayoutFile()
        self.layout_name = self.getLayoutName()
   

        self.layout_loc= join(uic.root, self.layout_fn)

        assert os.path.isfile(self.layout_loc), 'UI layout does not exists\n%s\n%s' % (self.layout_loc,self.layout_fn)
        cfg=load_config(config_path = self.layout_loc)
        return cfg

    def getLayoutDir(self):

        
        out = join (os.getcwd(),UI_DIR,PIPELINE_DIR, self.ppl)

        assert out
        return out
        
        
    def getLayoutFile(self):

        
        out = join (os.getcwd(),UI_DIR,PIPELINE_DIR, self.ppl, self.getLayoutName())

        assert out
        return out
    def getLayoutName(self):
        
        out = self.ppl.split(os.path.sep)[-1]

        assert out
        return '%s.json' % out
        
    def getNode_LayoutRoot(self, nref, ntype):
        api = getattr(sbc, 'get%sRoot' % ntype)
        return os.path.join(api(nref),self.LAYOUT_DIR)
        
        
    def getAllLayouts(self, pref):
    

        out={}
        for k, ntype in self.ntypes.items():
            if k in pref: 
                out.update(self.getNode_LayoutList(pref, ntype))
        
        return out

    def getNode_LayoutList(self, pref, ntype):
        api = getattr(self,'get%sCopyRef' % ntype)
        nref =  api(pref)
        layout_root = self.getNode_LayoutRoot(nref, ntype)
        return {os.path.relpath(file,self.root):nref for file in glob.glob(os.path.join(layout_root, JSON_EXT))}



        
        
    def assertExists(self):
        assert os.path.isdir(self.cfg_root), 'Config root does not exists for app "%s"' % self.app_name
        assert os.path.isdir(self.layout_root), 'Layout root does not exists for app "%s"\n%s' % (self.app_name,self.layout_root)
        return self
 
        
    def getLayoutList(self):
        return [os.path.basename(file) for file in glob.glob(os.path.join(self.layout_root, JSON_EXT))]



        
    def get(self, key, default = None):	
        global cfg
        if not 'cfg' in globals():
            self.cfg=cfg=self.loadLayout()

            return self.cfg.get(key, default)
        
    def items(self):
        
        global cfg
        if not 'cfg' in globals():
            self.cfg=cfg=self.loadLayout()
            return [(k,v) for k, v in cfg.items() if not k.startswith('_')]

    def keys(self):
        
        global cfg
        if 'cfg' in globals():
            return cfg.keys()
        else:
            
            cfg=self.loadLayout()
            return cfg.keys()

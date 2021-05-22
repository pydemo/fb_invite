import os, sys

from os.path import join, isdir

from pprint import pprint as pp
from collections import OrderedDict

from cli_layer.common import TMP_DIR, load_config

e=sys.exit


class Config(object): 

    def __init__(self, **kwargs):
        
        self.setCfg(**kwargs)
        self.cfg_root = cfg_root= self.getCfgRoot()		
        if not isdir(cfg_root): os.makedirs(cfg_root)
        

        
        #self.layout_root = self.getShelfLayoutRoot(app_name)
        
        self.include_root = join(self.getRoot(), 'include')
        self.root= self.getRoot()
    def getConfigName(self):
        return self.config_name
    def getRoot(self):
        return os.getcwd()
    def getBuildRoot(self):
        return join(os.getcwd(), '_build')
    def getTemplateRoot(self):
        return join(self.getBuildRoot(), '_template')		
    def getCfgRoot(self):
        return join(TMP_DIR,'cli_config')
        
    def setCfg(self,**kwargs):
        if kwargs.get('quiet'):
            self.quietOn() 
        else:
            self.quietOff()

        
    def getToolsRoot(self):
        return join(self.getRoot(), 'tools')
        
    def LoadConfig(self, config_path, quiet=False):
        if not quiet:
            print('-'*80)
            print('Loading config: %s' % config_path)
        cfg =load_config(config_path=config_path)
        if not quiet:
            print('-'*80)
        return cfg
    def quietOn(self):
        global quiet
        self.quiet=quiet=True
    def quietOff(self):
        global quiet
        self.quiet=quiet=False
        
        

        
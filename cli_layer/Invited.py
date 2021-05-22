import os, re, sys, copy, codecs, string
from os.path import isfile, isdir, join, basename
import json
from datetime import datetime 
from copy import deepcopy
from pprint import pprint as pp
from cli_layer.Config import *
import shutil
import logging


e=sys.exit



class Invited(Config): 
    def __init__(self, **kwargs):
        Config.__init__(self,**kwargs)
        if 1:
            cfg_root =join('out', 'fb', 'invite')
            cfgfn = 'Invited.json'
            cfg_loc = join(cfg_root, cfgfn)

        self.inv_path=cfg_loc
        print(cfg_loc)
        if not isfile(cfg_loc):
            self.initCfgFile(path=cfg_loc)

    def savePage(self, pid,data):
        self.cfg[pid]=data
        self.saveConfig()
    def getLatestPage(self):
        #pp(self.cfg)
        return self.cfg[str(max([int(x) for x in self.cfg]))]
    def getHome(self):
        home=self.home
        assert home
        assert isdir(home)
        return home
        
    

    def setTs(self,ts):
        assert hasattr(self,'cfg')
        assert self.cfg
        self.cfg['lambda_ts']=ts
        self.saveConfig()
        assert hasattr(self,'cfg')
        assert self.cfg        
        self.load(quiet=True)
        assert hasattr(self,'cfg')
        assert self.cfg        
    def setLatest(self, fname, key, data):
        
        ts=self.getTs()
        assert ts, ts
        if fname not in self.cfg:
            self.cfg[fname]={}
            self.cfg[fname][key]={}
            self.cfg[fname][key][ts]=data
        elif key not in self.cfg[fname]:
            self.cfg[fname][key]={}
            self.cfg[fname][key][ts]=data
        else:
            assert not  ts in self.cfg[fname][key], f'APC:{fname}:{key}:ts "{ts}" is already in latest'
            
            self.cfg[fname][key][ts]=data
            
        self.saveConfig()
        self.load(quiet=True)
        #pp(self.cfg)
    def getLatest(self, fname, key):
        assert fname in self.cfg
        assert key in self.cfg[fname]
        ts=self.getTs()
        #pp(self.cfg[fname][key])
        #print(ts)
        assert ts in self.cfg[fname][key], f'APC:{fname}:{key}:ts record "{ts}" does not exists'
        return self.cfg[fname][key][ts]
    def getTs(self):
        return self.cfg.get('lambda_ts',self.ts)
    def saveConfig(self):
        
        #assert hasattr(self, 'cfg')
        assert isfile(self.inv_path)
        
        with open(self.inv_path, 'w') as fp:
            dump = json.dumps(self.cfg, indent='\t', separators=(',', ': '))
           
            new_data= re.sub('"\n[\t]+},', '"},', dump)

            fp.write(dump)
    def initCfgFile(self,path):
        
        if not isfile(path):
            with open(path, 'w') as fh: fh.write('{0={}}\n')
    def load(self, quiet=False):

        if not quiet: 
            print(self.inv_path)

        
        self.cfg = {} #self.LoadConfig(config_path=self.inv_path, quiet=quiet)
        #pp(self.cfg)

        
        with open(self.inv_path, encoding="utf-8") as fh:
            
            self.cfg = json.loads(fh.read())


    
        assert self.cfg
        return self
        
        
            
    def getPythonHome(self):
        cfg=self.cfg
        assert 'Python' in cfg
        assert 'home' in cfg['Python']
        return cfg['Python']['home']

    def getApcPath(self):
        return join(self.getCfgRoot(), self.APC_FILE_NAME )
    def getApcExecPath(self):
        return join(self.getCfgRoot(), self.EXEC_APC_FILE_NAME )
    def assertExists(self):
        assert isdir(self.cfg_root), 'Config root does not exists for app "%s"\n%s' % (self.app_name, self.cfg_root)
        assert isfile(self.apc_path), 'App config JSON file does not exists for app "%s"\n%s' % (self.app_name,self.apc_path)
        
        return self

    
    def createConfigRoot(self):
        if not os.path.isdir(self.cfg_root):
            os.makedirs(self.cfg_root, exist_ok=True)
        return self



    def validate(self):
        if not  os.path.isdir(self.cfg_root):
            raise Exception('Cfg root does not exists at " %s "' % ( self.cfg_root))
        if not isfile(self.apc_path):
            print('ERROR: App config does not exists at \n%s' % self.apc_path)
            
        return self


    def getAppName(self, layout_loc=None):
        if not layout_loc: return self.app_name
        else:
            return os.path.splitext(os.path.basename(layout_loc))[0]


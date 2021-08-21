import os, json, codecs
from os.path import join, isdir, isfile

CONFIG_DIR  = 'config'

_MAPPING_DIR= 'mapping'
LAYER_DIR   = 'cli_layer'
MOCK_DIR    = 'mock_data'
VA_VIEW     = 'vw_vendor_current_control_lots'
STACK_DIR   = 'stack' 
TMPL_DIR    = 'template'
PLAN_DIR    = 'plan'
QUERY_DIR   = 'query'
QC_QUERY_FN = 'qc_query.sql'
QC_DUMP_FN  = "qc_query_dump.csv"
TEST_EVENT_DIR = 'test_event'
IN_DIR      = 'in'
OUT_DIR     = 'out'
INCLUDE_DIR = 'include'
CODE_DIR    = 'code_staging'
SUCCESS = 0
FAILURE = 1
NODATA  = 3

FUNC_DIR = 'lambda_function'

assert 'ZZZ_STACK_NAME__' in os.environ
sn= os.environ['ZZZ_STACK_NAME__']
assert len(sn.split('.'))==2
prj, stack_name = sn.strip().split('.')


if os.name == 'nt':
    SLITE_LOC   = join (LAYER_DIR,'sqlite', 'nt', 'sqlite3.exe')
else:
    SLITE_LOC   = join (LAYER_DIR,'sqlite', 'posix', 'sqlite3')

is_nt=False
if os.name == "nt":
    is_nt=True
    TMP_DIR=join('C:\\','tmp','ortho_cli')
    OPT_DIR= ''
    PPL_DIR = join(LAYER_DIR, 'pipeline')
    PPL_DIR = join('pipeline')
    DOWN_DIR=join(TMP_DIR,'downloads')
    IMPLOG_DIR=join(TMP_DIR,'import_log')
else:
    TMP_DIR=join('/tmp','ortho_cli')
    OPT_DIR= join('/opt', 'python')
    PPL_DIR = join(OPT_DIR, LAYER_DIR, 'pipeline')
    DOWN_DIR=join(TMP_DIR,'downloads')
    IMPLOG_DIR=join(TMP_DIR,'import_log')
    
if not isdir(TMP_DIR): os.makedirs(TMP_DIR)

LAYER_ZIP_DIR=join(TMP_DIR,'layer_zip')
if not isdir(LAYER_ZIP_DIR): os.makedirs(LAYER_ZIP_DIR)
if 0:
    WSDL_URL = 'http://www.maslablink.com/OrthoAPI/OrthoAPIService.asmx?WSDL'
    WSDL_USER='90138COM'
    WSDL_PWD ='ORTHO_ECONNECT'

def load_config(config_path,  verify_version=True):
    from collections import OrderedDict
    with codecs.open(config_path, encoding="utf-8") as stream:
        data=stream.read()
        config = json.loads(data, object_pairs_hook=OrderedDict)

    return config

def perr(err):
    print('#'*80)
    print('#'*80)
    print('ERROR:', err)
    print('#'*80)
    print('#'*80)
    
class dict2(dict):                                                              

    def __init__(self, **kwargs):                                               
        super(dict2, self).__init__(kwargs)                                     

    def __setattr__(self, key, value):                                          
        self[key] = value                                                       

    def __dir__(self):                                                          
        return self.keys()                                                      

    def __getattr__(self, key):                                                 
        try:                                                                    
            return self[key]                                                    
        except KeyError:                                                        
            raise AttributeError(key)                                           

    def __setstate__(self, state):                                              
        pass 


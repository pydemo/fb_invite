import os, sys, csv, time, logging, json
import datetime as dt
from  datetime import datetime
import decimal
from os.path import split, join, isdir, basename, isfile
from pprint import pprint as pp
from cli_layer.include.utils import timer, get_err
from pathlib import Path
from cli_layer.include.common import *
from cli_layer.include.fmt import  pfmt, psql, pfmtd

import  cli_layer.include.wsdl as wsdl

import cli_layer.include.config.app_config as app_config 
apc = app_config.apc

e=sys.exit
log = logging.getLogger('cli')

SERVICE='VADataTransferMasQC_MTMS'


def get_params(**kwargs):
    params = kwargs['params']
    assert params, params
    cp=dict()
    if type(params) in [tuple]:
    
        cp = {pid:p for pid,p in enumerate(params)}
    else:
        assert type(params) in [str]
        cp[0]=params

    return cp, params
@timer (basename(__file__))
def main(**kwargs):
    """
    Reagent 
    Service Name: VADataTransferOrthoPV_MTMS
    File name: Ortho_LIMS_VA_API_export.csv
    """
    
    usage(**kwargs)
    cp, params=get_params(**kwargs)
    limit	= kwargs['lame_duck']
def check_pcount(params,pcount):
    
    if pcount == 1:
        assert params, 'Empty params.'
        assert type(params) in [str], params
        return
    
    assert len(params)==pcount, '%d - wrong parameter count (expecting %d)' % (len(params),pcount)
    
def usage(**kwargs):
    if not apc.quiet:
        pfmtd([kwargs], 'Kwargs.')

    cp, params=get_params(**kwargs)
    if not apc.quiet:
        pfmtd([cp], 'Params.')
    pcount=1
    try:
        if kwargs['help']:
            assert False, 'Show usage.'    
        check_pcount(params,pcount)
        
        
        
        slist = params.split('.')
        #pp(slist)
        assert len(slist) ==2, slist
        api, service= slist
        #print(api, service)
        #pp(SERVICES)
        assert api in SERVICES, 'API "%s" not in SERVICES %s' % (api, SERVICES.keys())
        apid = SERVICES[api]
        assert service in apid, 'Service "%s" not in SERVICES[api=%s]: %s' % (service, api, apid.keys())
        if 1:
            from os.path import isfile
            import sys

            from pysimplesoap.client import SoapClient

            #e=sys.exit
            trace=0
                
            
            #print(__name__)
            #e()
            #logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.ERROR)
            client = SoapClient(wsdl=WSDL_URL, ns="web", trace=trace)
            
            
            client['AuthHeaderElement'] = {'username': WSDL_USER, 'password': WSDL_PWD}

            #Discover operations
            list_of_services = [service for service in client.services]
            #Discover params
            method = client.services['OrthoAPIService']

            dic=method.items()
            #pp(dic)
            out={}
            #print(len(dic))
            for k, v in dic:
                #print(k)
                out[k]=v

            serv= out['ports']['OrthoAPIServiceSoap']

            ops =serv['operations']

            method='VADataTransferMasQC_MTMS'
            request='vaDataTransferMasQCMTMSrequest'
            assert method in ops
            op= ops[method]
            assert 'input' in op
            op= op['input']
            assert method in op
            op= op[method]
            assert request in op
            op= op[request]
            for k, v in op.items():
                op[k]=dict(wsdl_type="%s" % v)
            #pp(op)

            outj=json.dumps(op,sort_keys=True, indent=4)
            print(outj)
            if 0:
                for k in sorted(op):
                    print (k)

        

    except Exception as err:
        error=get_err()
        perr(error)
        pfmtd([dict(Usage=r"""
USAGE:

    python cli.py -nop 1 -r DEV -p utils\show\service\json -pa VA.Thermo
        
    Number of input paramenters [-nop]:
        "2" - count of pipeline params in "-pa" option.
        
    Runtime environment [-r]:
        "DEV" - runtime name (DEV/UAT/PROD)
        
    Pipeline name [-p]:
        "utils\show\service\json" - pipeline description.
    
    Pipeline parameters [-pa]:
        "service_name" - param 0
""")])

        raise



    
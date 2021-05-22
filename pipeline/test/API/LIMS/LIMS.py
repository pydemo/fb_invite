"""
python cli.py  -nop 2 -r DEV -p test\API\LIMS -pa cli_layer\in\test\API\LIMS\MAS_LIMS_VA_API_export.csv cli_layer\out\test\API\LIMS\out_MAS_LIMS_VA_API_export.csv
"""
import os, sys, csv, time, logging
import datetime as dt
from  datetime import datetime
import decimal
from os.path import split, join, isdir, basename, isfile, dirname
from pprint import pprint as pp
from cli_layer.include.utils import timer, get_err
from pathlib import Path
from cli_layer.include.common import *
from cli_layer.include.fmt import  pfmt, psql, pfmtd

import  cli_layer.include.wsdl as wsdl

e=sys.exit

log = logging.getLogger('cli')

"""
Thermo
    •   VADataTransferMasQC_MTMS
    •   VADataTransferMasQC_MW
    -Ortho
    •   VADataTransferOrthoPV_MTMS
    •   VADataTransferOrthoPV_MW

    rest- Data Point
    -Thermo
    •   MasQCDataTransfer_MTMS
    •   MasQCDataTransfer_MW
    -Ortho
    •   OrthoPVDataTransfer_MTMS
    •   OrthoPVDataTransfer_MW
"""
test=True
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
    infn_, outfn_ = params
    
    infn=join(infn_)
    outfn=join(TMP_DIR,outfn_)
    out_dir=dirname(outfn)
    if not isdir(out_dir):
        os.makedirs(out_dir)
    client = wsdl.get_client()
    done=[]
    print('*START*'*5)
    print(infn)
    

    import unicodecsv as csv
    with open(infn, mode="rb") as csvfile:
        reader = csv.DictReader(csvfile)
        if 0:
            t={'assayname': 'A1c',
             'bodyfluid': 'BLOOD',
             'control_expiration': '10/22/2022 12:00:00 AM',
             'control_level': '1',
             'control_lot': '',
             'control_lot_number': 'DBCL20091',
             'conv_unit': 'g/dL',
             'ismultitest': 'N',
             'lassaynumber': '539',
             'lower_limit': '0',
             'mean': '0.56',
             'producttype': 'MT',
             'reagent_expiration_date': '3/14/2021 12:00:00 AM',
             'reagent_intro_date': '8/27/2019 12:00:00 AM',
             'reagent_number': '20',
             'reagent_version': '1',
             'rundatetime': '12/22/2020 12:00:00 AM',
             'sd': '0',
             'upper_limit': '0',
             'vendor': 'Thermo Fisher'}
        lims_fn='LIMS.py'
        if 0:
            sj_dir=join(LAYER_DIR,CONFIG_DIR,'service','VA_Thermo')
            assert isdir(sj_dir)
            sj_floc=join(sj_dir, lims_fn)
            assert isfile(sj_floc)
            cfg=load_config(sj_floc)
            #pp(cfg)
            cols=[v['column'] for v in cfg.values()]

        for rid,row in enumerate(reader):
            
            #e()
            if 0:
                notin=[]
                
                for k in row:
                    
                    if k not in cols:
                        notin.append(k)
                pp(notin)


            if row['vendor']=='Thermo Fisher':

                SERVICE='VADataTransferMasQC_MTMS'
                
                try:
                    request={'AssayName':   row['assayname'],
                    'BodyFluid':            row['bodyfluid'],
                    'Credentials': {'Login': "90138COM", 'Password': "ORTHO_ECONNECT"},
                    'GenExpirationDate':    datetime.now() if test else row['reagent_expiration_date'],
                    'GenIntroductionDate':  datetime.now() if test else row['reagent_intro_date'],
                    'GenNumber':            row['reagent_number'],
                    'GenVersion':           row['reagent_version'],
                    'Level':                row['control_level'],
                    'LowerLimitRange':      row['lower_limit'],
                    'MASControlLot':        row['control_lot_number'],
                    'MASControlLotExpirationDate': datetime.now() if test else row['control_expiration'],
                    'MASControlLotNumber': row['control_lot_number'],
                    'Mean':                 row['mean'],
                     #'PVControlLot':         row['control_lot_number'],
                     #'PVControlLotExpirationDate': datetime.now() if test else row['control_expiration'],
                     #'PVControlLotNumber':   row['control_lot_number'],
                    'ProductType':          row['producttype'],
                        #'ReagentExpirationDate': datetime.now(),
                        #'ReagentIntroductionDate': datetime.now(),
                        #'ReagentNumber': row['reagent_number'],
                        #'ReagentVersion': row['reagent_version'],
                    'RunDateTime':          datetime.now(),
                    'Sd':                   row['sd'],
                    'SubLot':               row['reagent_number'],
                    'UnitName':             row['conv_unit'],
                    'UpperLimitRange':      row['upper_limit']
               }
                except: 
                    pp(row)
                    raise

            else:
                SERVICE='VADataTransferOrthoPV_MTMS'
                try:
                    request={'AssayName':   row['assayname'],
                    'BodyFluid':            row['bodyfluid'],
                    'Credentials': {'Login': "90138COM", 'Password': "ORTHO_ECONNECT"},
                    'GenExpirationDate':    datetime.now() if test else row['reagent_expiration_date'],
                    'GenIntroductionDate':  datetime.now() if test else row['reagent_intro_date'],
                    'GenNumber':            row['reagent_number'],
                    'GenVersion':           row['reagent_version'],
                    'Level':                row['control_level'],
                    'LowerLimitRange':      row['lower_limit'],
                    #'MASControlLot':        row['control_lot_number'],
                    #'MASControlLotExpirationDate': datetime.now() if test else row['control_expiration'],
                    #'MASControlLotNumber': row['control_lot_number'],
                    'Mean':                 row['mean'],
                     'PVControlLot':         row['control_lot_number'],
                     'PVControlLotExpirationDate': datetime.now() if test else row['control_expiration'],
                     'PVControlLotNumber':   row['control_lot_number'],
                    'ProductType':          row['producttype'],
                        #'ReagentExpirationDate': datetime.now(),
                        #'ReagentIntroductionDate': datetime.now(),
                        #'ReagentNumber': row['reagent_number'],
                        #'ReagentVersion': row['reagent_version'],
                    'RunDateTime':          datetime.now(),
                    'Sd':                   row['sd'],
                    'SubLot':               row['reagent_number'],
                    'UnitName':             row['conv_unit'],
                    'UpperLimitRange':      row['upper_limit']
               }
                except: 
                    pp(row)
                    raise                
                
            if 1:
                service=client.service
                api  = getattr(service, SERVICE)
                responce=api(request)
                
                if hasattr(responce,'ImportId'):
                    status=dict(Status= responce.Status,Errors= responce.Errors,ImportId=  hasattr(responce,'ImportId') if responce.ImportId else '')
                else:
                    status=dict(Status= responce.Status,Errors= responce.Errors)
            #pfmtd([status], 'status.')

            if 1:
                err=dict(ErrorCode='',ErrorMessage='')
                if status['Status'] in ['ERROR']:
                    assert status['Errors']
                    serr= status['Errors']['Error'][0]
                    err['ErrorCode']=serr['ErrorCode']
                    err['ErrorMessage']=serr['ErrorMessage']

                    
                preh='Status,ErrorCode,ErrorMessage'
                hdr=preh+','+','.join(reader.fieldnames)
                fmt='{%s}' % hdr.replace(',','},{')
                row['Status']=status['Status']
                #pp(err)
                pfmtd([err], 'err.')
                row.update(err)
                out=fmt.format(**row).strip().strip(',')
                if not done:
                    done.append(hdr)
                done.append(out)
                #print(len(done))
            if limit and rid+1>=limit: 
                log.info('Lame duck break [%d]' % limit)
                break


    if done:
        with open(outfn, 'w') as fh:
            fh.write('\n'.join(done))
        log.info('CSV log created at: %s' % outfn)
    else:
        log.warn('CSV log is empty.')
    

def check_pcount(params,pcount):
    
    if pcount == 1:
        assert params, 'Empty params.'
        assert type(params) in [str], params
        return
    
    assert len(params)==pcount, '%d - wrong parameter count (expecting %d)' % (len(params),pcount)
    
def usage(**kwargs):
    pfmtd([kwargs], 'Kwargs.')

    cp, params=get_params(**kwargs)
    pfmtd([cp], 'Params.')
    pcount=2
    try:
        if kwargs['help']:
            assert False, 'Show usage.'    
        check_pcount(params,pcount)
        
        #assert pcount==2+1 #remove
        
        infn, outfn = params
        assert isfile(infn), 'Input file "%s" does not exists.' % infn
        if isfile(outfn): os.remove(outfn); assert not isfile(outfn), 'Cannot delete existing output file "%s".' % outfn

        out_dir, outbn = split(outfn)
        if out_dir and not isdir(out_dir):
            os.makedirs(out_dir)
            assert isdir(out_dir), 'Cannot create output dir "%s"' % out_dir






    except Exception as err:
        error=get_err()
        perr(error)
        pfmtd([dict(Usage=r"""
USAGE:

    python cli.py -nop 1 -r DEV -p test\API\LIMS -pa in_file out_file
        
    Number of input paramenters [-nop]:
        "2" - count of pipeline params in "-pa" option.
        
    Runtime environment [-r]:
        "DEV" - runtime name (DEV/UAT/PROD)
        
    Pipeline name [-p]:
        "test\API\LIMS" - pipeline description.
    
    Pipeline parameters [-pa]:
        "in_file" - param 0
        "out_file" - param 1
""")])

        e(FAILURE)



    
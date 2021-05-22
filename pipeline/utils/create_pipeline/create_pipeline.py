import os, sys, csv, time, logging
import datetime, decimal
import subprocess
from os.path import split, join, isdir, basename, isfile
from pprint import pprint as pp
from cli_layer.utils import timer, get_err, os_path
from ui_layer.utils import edit_file
from pathlib import Path
from cli_layer.common import PPL_DIR, IN_DIR, OUT_DIR, perr, FAILURE, LAYER_DIR
from cli_layer.fmt import  pfmt, psql, pfmtd
e=sys.exit

TMPL = join(PPL_DIR, '_config','template','new_pipeline.txt')

def create_ppl(fn, ppl_body):
    if isfile(fn):
        over = input('\nPipeline "%s" exists. Overwrite? y/n: ' % fn)
        if over.lower() !='y':
            return
    with open(fn, 'w') as fh: fh.write(ppl_body)
        
def create_ppl_bat(fn, ppl_bat_body):
    if isfile(fn):
        over = input('\n"%s" file exists. Overwrite? y/n: ' % fn)
        if over.lower() !='y':
            return
    with open(fn, 'w') as fh: fh.write(ppl_bat_body)
    

def create_md(fn, ppl_body):
    if isfile(fn):
        over = input('\nMarkdown "%s" exists. Overwrite? y/n: ' % fn)
        if over.lower() !='y':
            return
    with open(fn, 'w') as fh: fh.write(ppl_body)
            
@timer (basename(__file__))
def main(**kwargs):
    
    usage(**kwargs)
    params = kwargs['params']
    pp(params)
    assert params, params
    cp = params.split()
    cp[1] = os_path(cp[1])
    if 1: #in
        pp(cp)
        #new_in_dir = join(LAYER_DIR,IN_DIR, os_path(cp[1]))
        new_in_dir = join(IN_DIR, cp[1])
        pp(new_in_dir)
        #e()
        if not isdir(new_in_dir):
            os.makedirs(new_in_dir)
    if 1: #out
        new_out_dir = join(LAYER_DIR, OUT_DIR, os_path(cp[1]))
        new_out_dir = join(OUT_DIR, cp[1])
        pp(new_out_dir)
        if not isdir(new_out_dir):
            os.makedirs(new_out_dir)
    #e()
    if 1:
        new_ppl_dir = join(PPL_DIR, cp[1])
        new_ppl = cp[1].split('\\')[-1]
        new_ppl_name='%s.py' % new_ppl
        #pp(new_ppl_name)
        new_ppl_nop = cp[0]
        new_ppl_params=' '.join(cp[2:])
        if 0:
            assert not isdir(new_ppl_dir)
        if not isdir(new_ppl_dir):
            os.makedirs(new_ppl_dir)
        new_loc=join(new_ppl_dir,new_ppl_name)
        #Path(new_loc).touch()
    assert isfile(TMPL), TMPL
    with open(TMPL, 'r') as fh: tmpl=fh.read()
    new_ppl_param_list = '\n'.join(['        "%s" - param %d' % (p, pid) for pid ,p in enumerate(cp[2:])])
    fmdict=dict(new_ppl_nop=new_ppl_nop,new_ppl_name=new_ppl_name, new_ppl_dir=cp[1],new_ppl_param_list=new_ppl_param_list, new_ppl_params=new_ppl_params)
    new_ppl_body = tmpl.format(**fmdict)
    create_ppl(new_loc, new_ppl_body)
    

    cmd='python cli.py  -nop {new_ppl_nop} -r DEV -p {new_ppl_dir} -pa {new_ppl_params}  %*'.format(**fmdict)
    pfmtd([dict(cmd = cmd)], 'New pipeline "%s".' % new_ppl_name)
    ppl_bat_fn= '%s.bat' % cp[1].replace('\\','.')
    create_ppl_bat(ppl_bat_fn, cmd+'\n')
    dir_1=cp[1].split(os.sep)[0]
    md_dir=join(PPL_DIR,'_docs', dir_1)
    if not isdir(md_dir): os.makedirs(md_dir)
    
    md_fn=join(md_dir, '%s.md' % cp[1].replace(os.sep,'.'))
    md_body="""```
%s
```""" % cmd.strip('%*')
    create_md(md_fn, md_body)
    if 1:
        edit_file(ppl_bat_fn)
        edit_file(md_fn)
        edit_file(new_loc)
    
def check_pcount(params,pcount):
    
    if pcount == 1:
        assert params, 'Empty params.'
        assert type(params) in [str], params
        return
    
    assert len(params)==pcount, '%d - wrong parameter count (expecting %d)' % (len(params),pcount)

def usage(**kwargs):
    pfmtd([kwargs], 'Kwargs.')

    params = kwargs['params']
    pcount=1
    
    try:
        if kwargs['help']:
            assert False, 'Show usage.'    
        check_pcount(params,pcount)
        #e()
    except Exception as err:
        error=get_err()
        perr(error)
        pfmtd([dict(Usage=r"""
USAGE:

    python cli.py -nop 1 -r DEV -p utils\create_pipeline -pa " 2 import_csv\3rd_party\Microwell in_file out_file"
        
    Number of input paramenters [-nop]:
        "1" - count of pipeline params in "-pa" option.
        
    Runtime environment [-r]:
        "DEV" - runtime name (DEV/UAT/PROD)
        
    Pipeline name [-p]:
        "import_csv\create_pipeline" - pipeline used to bootstrap new pipeline.
    
    Pipeline parameters [-pa]:
        "pipeline_name" - new pipeline name
        "param_cnt"  - param count (to new pipeline) 
        "param_1 ... param_n"  - param list (to would be new pipeline)
""")])

        e(FAILURE)



    
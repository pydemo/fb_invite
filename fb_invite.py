import os, sys,  random
from os.path import join, isdir, isfile, dirname
from  time import sleep
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from ui_layer.utils import  cli_exception
from pprint import pprint  as pp
e=sys.exit

chrome_options = Options()


import cli_layer.config.app_config as app_config 
if 1:
    app_config.init(**dict(quiet=False))
    apc = app_config.apc
    apc.validate().load()

import cli_layer.config.invited as invited
if 1:
    invited.init()
    inv = invited.inv
    inv.load()
    

options = Options()
options.add_argument("--log-level=3")
options.add_argument("--silent")
#options.add_argument("--disable-web-security")
mobile_emulation = {"deviceName": "Nexus 5"}
options.add_experimental_option("mobileEmulation", mobile_emulation)
options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')

if 0:
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    #options.add_argument("--disable-gpu")
    #options.add_argument("--disable-dev-shm-usage")
    #options.add_argument("--no-proxy-server")
    #options.add_argument("--disable-infobars")
    #options.add_argument("--disable-extensions")
    #options.add_argument("--disable-setuid-sandbox")
    options.add_argument('--remote-debugging-port=9222')
    

data_dir=r'C:\Users\alex_\mygit\fb_invite\chrome-data'

options.add_argument("--disable-logging")
options.add_argument("--mute-audio")
options.add_argument(f"--user-data-dir={data_dir}")


did=90
driverpath = r".\driver\nt\chromedriver_%d.exe" % did
if 0:
    data_dir=f'chrome-data-{did}'
    if not isdir(data_dir):
        #did=87
        data_dir=f'chrome-data-{did}'
    



    #assert isdir(data_dir), data_dir
    
    


def save_creds(fn, data):
    dn=dirname(fn)
    if not isdir(dn):
        os.makedirs(dn)
    if isfile(fn):
        os.remove(fn)
    with open(fn, 'w') as fh:
        fh.write(data)
@cli_exception  
def main(url):
    if 1:
        driver = webdriver.Chrome(executable_path=driverpath,options=options)
        options.add_argument(f"user-data-dir={data_dir}")
        
        
        driver.get(url)
        sleep(3) 
        
    if 1:
        
       
        
        url="https://m.facebook.com/pg/alexbuzunovart/posts/?ref=page_internal&mt_nav=0"
        driver.get(url)
        sleep(5) 
    if 1:
        
        dtl=['/html/body/div[1]/div/div[4]/div/div[1]/div/div[3]/div/div[3]/div/div/article/footer/div[1]/div[1]/a/div/div[1]/div',
        '/html/body/div[1]/div/div[4]/div/div[1]/div/div[3]/div/div[3]/div/div/article/footer/div[1]/div[1]/div[1]/a/div/div[1]/div']
        for path in dtl:
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
            sleep(1)
            try:
                print('Trying: Go to likes...')
                a=driver.find_element_by_xpath(path).click()
                print('Done: Go to likes')
                break
            except:
                print('Go to likes failed.')  
                sleep(1)

    sleep(2)   
    ol=['/html/body/div[1]/div/div[4]/div/div/div/div/div[2]/div/div/div[2]/a/div/div',
        '/html/body/div[1]/div/div[4]/div/div/div/div/div[2]/div/div/div[2]/a/div/div']
    for path in ol:
        try:
            print('Trying: Open likes...')
            a=driver.find_element_by_xpath(path).click()
            print('Done: Open likes')
            sleep(3)
            break
        except Exception as ex:
            print('Open failed.') 
            sleep(1)            
        
    try:
        print('Trying: Buttons ...')
        btns=browser.find_element_by_xpath('//button[text()="Invite"]')
        pp(btns)
        print(len(btns) )       
        print('Done: Buttons ')
        
  
    except Exception as ex:
        print('Buttons failed.') 
    
    
    try:
        print('Trying: normalize Buttons ...')
        btns=driver.find_element_by_xpath('//button[normalize-space()="Invite"]')  
        pp(btns)
        print(len(btns))
        print('Done: normalize Buttons ')
    except Exception as ex:
        print(str(ex))
        print('normalize Buttons failed.')      

 
    try:
        print('Trying: class Buttons ...')
        btns=driver.find_element_by_class_name('_54k8 _52jg _56bs _26vk _56bt')  
        pp(btns)
        print(len(btns))
        print('Done: class Buttons ')
    except Exception as ex:
        print(str(ex))
        print('class Buttons failed.') 


    try:
        print('Trying: type Buttons ...')
        btns=driver.find_elements_by_xpath("//button[@type='submit']")  
        pp(btns)
        print(111, len(btns))
        print('Done: type Buttons ')
        btn=btns[0] 
        pp(btn)
        #pp(dir(btn))        
        intv=30
        if 1:
            for i in range (7):
                driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
                sleep(1) 
        invited=[]
        if 1:
            btns=driver.find_elements_by_xpath("//button[@type='submit']") 
            print(222, len(btns))
            if 1:
                toinv=[btn for btn in btns if 'Invite' in btn.text]
                print('to_inv len: ', len(toinv))
                for bid, btn in enumerate(toinv):
                    #print(bid,'value', btn.value_of_css_property('value') ) 
                    if 1:
                        print(bid,'Button text', btn.text)
                        #print(bid,'location_once_scrolled_into_view', btn.location_once_scrolled_into_view)
                        #print(bid,'location', btn.location)
                        #print(bid,'tag_name', btn.tag_name)
                        #print(bid,'id', btn.id)  
                    if 'Invite' in btn.text:
                        try:
                            
                            btn.click()
                            invited.append(btn)
                            print(bid, 'Click button: DONE')
                            wait=random.randrange(intv,intv+10)
                            sleep(wait)
                        except Exception as ex:
                            print(ex)
                            print(bid, 'Click button FAILED')
            sleep(1)  
    
    except Exception as ex:
        print(str(ex))
        print('type Buttons failed.') 
    old=[]
    for p in range(0,150):
        see=None
        try:
            print(p, 'Trying: See more...')
            #see=driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div[2]/div[1]/div[3]/a/div/div/div/strong/div')
            see=driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div[2]/div[1]/div[3]/a')

            href=see.get_attribute("href")
            print(href)
            hid= href.split('ft_ent_identifier=')[1].split('&')[0]
            #print (href)
            print(hid)
            sids= href.split('shown_ids=')[1].split('&')[0]
            #print(sids)
            new=sids.split('%2C')
            print(707070, len(new), len(old), len(new)- len(old))
            #print('set:',  set(new)-set(old), set(old)-set(new))
            newids= list(set(new)-set(old))

            #print('NEW IDs count: ', len(newids))
            inv.savePage(p, newids)
            if 1:
                new_sids = '%2C'.join(newids)
                maxids= inv.getLatestPage()
                #print(2222, maxids)
                #break
                
                #new_sids = '%2C'.join(maxids)
                url= 'https://m.facebook.com/ufi/reaction/profile/browser/fetch/?limit=50&shown_ids=%s&total_count=2621&ft_ent_identifier=1764142307092985&ref=page_internal' % new_sids
                print('SET URL:' , url)
                driver.execute_script("arguments[0].setAttribute('href','%s')" % url, see)
                    
                    
            old=new
            
            print(p, 'See more... DONE')
        except Exception as ex:
            print(str(ex))
            print(p, 'See more... FAILED')
            #raise
        assert see
        if 0:
            print('see text', see.text)
            print('location_once_scrolled_into_view', see.location_once_scrolled_into_view)
            print('location', see.location)
            print('tag_name', see.tag_name)
            print('id', see.id)  
        see.click()
        print(p,'See click: DONE')
        
        sleep(5)

        if 1:
            for i in range (7):
                driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
                sleep(1) 
        btns=driver.find_elements_by_xpath("//button[@type='submit']") 
        print(p,'len(btns): ', len(btns))
        if 1:
            toinv=[btn for btn in btns if 'Invite' in btn.text and btn not in invited]
            print(p, 'invited len: ', len(invited))
            print(p, 'to_inv len: ', len(toinv))
            for bid, btn in enumerate(toinv):
                try:
                    if 'Invite' in btn.text:
                        try:
                            btn.click()
                            invited.append(btn)
                            wait=random.randrange(intv,intv+10)
                            print(bid, 'Click button 11: DONE', wait, 123)
                            
                            sleep(wait)
                        except Exception as ex:
                            print(ex)
                            print(bid, 'Click button FAILED') 
                except Exception as ex:
                    print(str(ex))
                    print('Button.text failed.')                             
                    break
            
    driver.quit()
if __name__=="__main__":
    url="https://m.facebook.com/alexbuzunovart"

    main(url)
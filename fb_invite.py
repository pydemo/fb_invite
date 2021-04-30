import os, sys
from os.path import join, isdir, isfile, dirname
from  time import sleep
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from pprint import pprint  as pp
e=sys.exit

chrome_options = Options()





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
    
    

url="https://m.facebook.com/alexbuzunovart"

def save_creds(fn, data):
    dn=dirname(fn)
    if not isdir(dn):
        os.makedirs(dn)
    if isfile(fn):
        os.remove(fn)
    with open(fn, 'w') as fh:
        fh.write(data)
    
if __name__=="__main__":
    if 1:
        driver = webdriver.Chrome(executable_path=driverpath,options=options)
        options.add_argument(f"user-data-dir={data_dir}")
        
        
        driver.get(url)
        sleep(3) 
        
    if 1:
        
       
        
        url="https://m.facebook.com/pg/alexbuzunovart/posts/?ref=page_internal&mt_nav=0"
        driver.get(url)
        sleep(5) 
    while True:
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        sleep(1)
        try:
            print('Trying: Go to likes...')
            a=driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[1]/div/div[3]/div/div[3]/div/div/article/footer/div[1]/div[1]/div[1]/a/div/div[1]/div').click()
            print('Done: Go to likes')
            break
            
            
            
        except:
            print('Go to likes failed.')  
            sleep(1)
    sleep(5)   
    try:
        print('Trying: Open likes...')
        a=driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div[2]/div/div/div[2]/a/div/div').click()
        print('Done: Open likes')
  
    except Exception as ex:
        print('Open failed.')  
        
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
                            sleep(2)
                        except Exception as ex:
                            print(ex)
                            print(bid, 'Click button FAILED')
            sleep(1)  
    
    except Exception as ex:
        print(str(ex))
        print('type Buttons failed.') 

    for p in range(150):
        see=None
        try:
            print(p, 'Trying: See more...')
            #see=driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div[2]/div[1]/div[3]/a/div/div/div/strong/div')
            see=driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div[2]/div[1]/div[3]/a')
            print (see, type(see))
            #pp(dir(see))
            print(p, 'See more... DONE')
        except:
            print(p, 'See more... FAILED')
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
                #print(bid,'value', btn.value_of_css_property('value') ) 
                #if 1:
                    #print(bid,'Button text', btn.text)
                    #print(bid,'location_once_scrolled_into_view', btn.location_once_scrolled_into_view)
                    #print(bid,'location', btn.location)
                    #print(bid,'tag_name', btn.tag_name)
                    #print(bid,'id', btn.id) 
                try:
                    if 'Invite' in btn.text:
                        try:
                            btn.click()
                            invited.append(btn)
                            print(bid, 'Click button: DONE')
                            sleep(2)
                        except Exception as ex:
                            print(ex)
                            print(bid, 'Click button FAILED') 
                except Exception as ex:
                    print(str(ex))
                    print('Button.text failed.')                             
    e()


    try:
        print('Trying: parent/child ...')
        div=driver.find_elements_by_xpath('//*[@id="reaction_profile_browser"]')  
        pp(div)
        print(888, len(div))
        child = div[0].find_elements_by_xpath('.//*')
        
        print(777, len(child))
        print('parent/child DONE.') 
    except Exception as ex:
        print(str(ex))
        print('parent/child FAILED.') 
        
        


    try:
        print('Trying: _4mo div  ...')
        btns=driver.find_elements_by_class_name("_4mo")  
        pp(btns)
        print(444, len(btns))
        print('Done: _4mo div ')
        #pp(btns[0])
        #pp(dir(btns[0]))
    except Exception as ex:
        print(str(ex))
        print('_4mo div failed.')         

    try:
        print('Trying: value Buttons ...')
        btns=driver.find_elements_by_xpath("//button[@value='Invite']")  
        pp(btns)
        print(222, len(btns))
        print('Done: value Buttons ')
    except Exception as ex:
        print(str(ex))
        print('value Buttons failed.') 
    try:
        print('Trying: xpath Buttons ...')
        btns=driver.find_elements_by_xpath("//*[@value='Invite']")  
        pp(btns)
        print(333, len(btns))
        print('Done: xpath Buttons ')
    except Exception as ex:
        print(str(ex))
        print('xpath Buttons failed.')    
        
    e()
    
    try:
        print('Trying: Pick an account...')
        a=driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/div/div[2]/div').click()
    except:
        print('Pick an account failed.')
    
    driver.set_window_size(1000, 1000)
    a=None
    while True:
        sleep(2)
        print('MS "All Apps"')
        try:
            a=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/a')
            break
        except:
            print('Trying...')
    assert a
    aws_url = a.get_attribute('href')
    print(aws_url)
    if 1:
        driver.get(aws_url)
        #sleep(2000)
    if 1:
        
        while True:
            sleep(2)
            print('Accounts')
            try:
            
                driver.find_element_by_xpath('/html/body/app/portal-ui/div/portal-dashboard/portal-application-list/portal-application').click() 
                break
            except:
                print('Trying...')
        sleep(0.5)
        

        if 1: 
            env='DEV'
            print(f'Trying "{env}"')
            driver.find_element_by_xpath('//*[@id="ins-6e94a0c3ed76b196"]/div/div/div/div[2]').click()
            sleep(0.5)
            print('Command line or programmatic access')
            driver.find_element_by_xpath('/html/body/app/portal-ui/div/portal-dashboard/portal-application-list/sso-expander/portal-instance-list/div[1]/portal-instance/div/sso-expander/portal-profile-list/div/portal-profile/span/span/span[2]/a').click()
            sleep(0.5)
            if 1: 
                print('"Windows" url')
                try:
                    driver.find_element_by_xpath('//*[@id="p-51c7c7674ed91244"]/sso-modal/div/div/div[2]/modal-content/div/div[3]/sso-tabs/ul/li[2]/a').click()
                except:
                    go = input("Continue?")
                    if go=='y':
                        pass
                    else:
                        raise
                sleep(0.5)
                print('Hove/Click/Copy')
                driver.find_element_by_xpath('/html/body/app/portal-ui/div/portal-dashboard/portal-application-list/sso-expander/portal-instance-list/div[1]/portal-instance/div/sso-expander/portal-profile-list/div/portal-profile/span/span/span[2]/creds-modal/sso-modal/div/div/div[2]/modal-content/div/div[3]/sso-tabs/sso-tab[2]/div/div/div[2]/hover-to-copy/div').click()
                sleep(0.5)
                print(env)
                data=pyperclip.paste()
                if 1:
                    fn=join('.creds',f'{env}.bat')
                    save_creds(fn, data)
                    print(f'"{env}" keys are save to "{fn}"')
                print('Close popup')
                driver.find_element_by_xpath('/html/body/app/portal-ui/div/portal-dashboard/portal-application-list/sso-expander/portal-instance-list/div[1]/portal-instance/div/sso-expander/portal-profile-list/div/portal-profile/span/span/span[2]/creds-modal/sso-modal/div/div/div[1]/span').click()
                sleep(0.5)
        
        if 1: 
            env='QA'
            print(f'Trying "{env}"')
            try:
                driver.find_element_by_xpath('/html/body/app/portal-ui/div/portal-dashboard/portal-application-list/sso-expander/portal-instance-list/div[2]/portal-instance/div/div/div/div[2]').click()
            except:
                driver.find_element_by_xpath('/html/body/app/portal-ui/div/portal-dashboard/portal-application-list/sso-expander/portal-instance-list/div[2]/portal-instance/div/div/div/div[2]').click()
            sleep(0.5)
            print('Command line or programmatic access')
            driver.find_element_by_xpath('/html/body/app/portal-ui/div/portal-dashboard/portal-application-list/sso-expander/portal-instance-list/div[2]/portal-instance/div/sso-expander/portal-profile-list/div/portal-profile/span/span/span[2]/a').click()
            sleep(0.5)
            if 1:
                print('"Windows" url')
                driver.find_element_by_xpath('/html/body/app/portal-ui/div/portal-dashboard/portal-application-list/sso-expander/portal-instance-list/div[2]/portal-instance/div/sso-expander/portal-profile-list/div/portal-profile/span/span/span[2]/creds-modal/sso-modal/div/div/div[2]/modal-content/div/div[3]/sso-tabs/ul/li[2]/a').click()
                sleep(0.5)
                print('Hove/Click/Copy')
                driver.find_element_by_xpath('/html/body/app/portal-ui/div/portal-dashboard/portal-application-list/sso-expander/portal-instance-list/div[2]/portal-instance/div/sso-expander/portal-profile-list/div/portal-profile/span/span/span[2]/creds-modal/sso-modal/div/div/div[2]/modal-content/div/div[3]/sso-tabs/sso-tab[2]/div/div/div[2]/hover-to-copy/div').click()
                sleep(0.5)
                print(env)
                data=pyperclip.paste()
                if 1:
                    fn=join('.creds',f'{env}.bat')
                    save_creds(fn, data)
                    print(f'"{env}" keys are save to "{fn}"')
            
    driver.quit()
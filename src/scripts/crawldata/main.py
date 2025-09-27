
from tqdm import tqdm
from selenium import  webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import csv
options= Options()
options.add_argument('--window-size=1920,1200')
devices=['samsung-inverter-multi-door-bespoke-648-lit-rf59cb66f8ssv',
                            'hisense-inverter-multi-door-519-lit-rs668n4ew-pu',
                            'aqua-inverter-410-lit-aqr-m466xagb',
                            'aqua-inverter-455-lit-aqr-t518fasl',
                            'samsung-inverter-583-lit-rs57dg400em9sv',
                            'toshiba-inverter-515-lit-gr-rf677wi-pgv22-xk',
                            'hisense-inverter-multi-door-609-lit-rq768n4ew-ku',
                            'sharp-inverter-multi-door-362-lit-sj-fx420vg-bk',
                            'aqua-inverter-328-lit-aqr-t380fasl',
                            'tu-lanh-panasonic-inverter-170l-nr-ba190ppvn',
                            'sharp-inverter-multi-door-401-lit-sj-fxp480vg-ch',
                            'hisense-inverter-424-lit-rt549n4ebu-mbu',
                            'aqua-inverter-236-lit-aqr-t260fafb',
                            'lg-inverter-374-lit-ltd37blm',
                            'toshiba-inverter-side-by-side-555-lit-gr-rs696wi-pmv60-ag',
                            'hisense-inverter-multi-door-427-lit-rq519n4ebu',
                            'lg-inverter-multi-door-474-lit-lfb47blg',
                            'lg-inverter-315-lit-gn-m312bl',
                            'panasonic-inverter-251-lit-nr-sp275cpav',
                            'aqua-inverter-469-lit-aqr-m536xagb',
                            'lg-inverter-459-lit-ltd46blma',
                            'toshiba-inverter-multi-door-gr-rf611wi-pgv22-xk',
                            'aqua-inverter-212-lit-aqr-t239fafb',
                            'lg-inverter-612-lit-lfd61blga',
                            'hisense-inverter-424-lit-rt549n4ew-mbu',
                            'toshiba-inverter-515-lit-gr-rf675wi-pmv06-mg',
                            'casper-95-lit-ro-95pg',
                            'sharp-inverter-197-lit-sj-x215v-dg',
                            'toshiba-inverter-312-lit-gr-rt416we-pmv58-mm',
                            'aqua-130-lit-aqr-t150fabs',
                            'aqua-inverter-490-lit-aqr-s552xacbc',
                            'tu-lanh-toshiba-inverter-409-lit-gr-rt535wea-pmv06-mg',
                            'samsung-inverter-382-lit-rt38cg6584b1sv',
                            'sharp-inverter-181-lit-sj-x198v-dg',
                            'lg-inverter-335-lit-lbb33blga',
                            'aqua-mini-mot-cua-50-lit-aqr-d60fabs',
                            'lg-inverter-side-by-side-519-lit-gr-b256bl',
                            'casper-inverter-430-lit-rm-d430gbs',
                            'toshiba-inverter-253-lit-gr-rt329we-pmv52',
                            'panasonic-inverter-234-lit-nr-tv261bpkv',
                            'sharp-inverter-multi-door-556-lit-sj-fx630v-st',
                            'samsung-inverter-488-lit-rf48a4010b4sv',
                            'lg-inverter-459-lit-ltd46svma',
                            'lg-inverter-474-lit-french-door-lfb47svm',
                            'lg-inverter-side-by-side-635-lit-gr-g257bl',
                            'aqua-130-lit-aqr-t160fabs',
                            'hisense-mini-mot-cua-94-lit-hr09db',
                            'hisense-mini-mot-cua-45-lit-hr05db',
                            'tu-lanh-casper-inverter-multi-door-430-lit-rm-430pb',
                            'casper-458-lit-rs-460pg',
                            'hisense-inverter-side-by-side-519-lit-hs56wbg',
                            'sharp-inverter-197-lit-sj-x215v-sl',
                            'samsung-inverter-208-lit-rt20har8dbusv',
                            'samsung-inverter-635-lit-side-by-side-rs70f65k2fsv',
                            'aqua-inverter-189-lit-aqr-t220fafb',
                            'hisense-inverter-205-lit-rt256n4ebn',
                            'lg-inverter-264-lit-gv-b262ps',
                            'lg-inverter-635-lit-gr-g257sv',
                            'sharp-inverter-330-lit-sj-xp352ae-sl',
                            'tu-lanh-casper-inverter-side-by-side-495-lit-rs-460pbw',
                            'lg-inverter-340-lit-lbb33bgmai',
                            'samsung-inverter-side-by-side-655-lit-rs62r5001b4sv',
                            'samsung-inverter-256-lit-rt25m4032busv',
                            'aqua-inverter-212-lit-aqr-t239fahb',
                            'lg-inverter-612-lit-lfd61blgai',
                            'lg-inverter-461-lit-ltb46blg',
                            'aqua-inverter-283-lit-aqr-t299fasl',
                            'lg-inverter-217-lit-gv-b212wb',
                            'samsung-inverter-634-lit-side-by-side-rs80f65j2bsv',
                            'samsung-inverter-615-lit-side-by-side-rs90f65d2fsv',
                            'samsung-inverter-385-lit-rt38cb668412sv',
                            'lg-inverter-617-lit-lfb61blgai',
                            'toshiba-inverter-side-by-side-596-lit-gr-rs775wi-pmv06-mg',
                            'samsung-inverter-655-lit-side-by-side-rs70f65q3fsv',
                            'lg-inverter-side-by-side-519-lit-gr-b256jds',
                            'sharp-inverter-401-lit-sj-fxp480v-sl',
                            'aqua-mini-mot-cua-90-lit-aqr-d100fabs',
                            'samsung-inverter-345-lit-rt35cg5544b1sv',
                            'sharp-inverter-181-lit-sj-x198v-sl',
                            'lg-inverter-340-lit-lbb33blmai',
                            'samsung-inverter-multi-door-488-lit-rf48a4010m9sv',
                            'panasonic-inverter-multi-door-550-lit-nr-dz601vgkv',
                            'hisense-mini-mot-cua-82-lit-hr08dw',
                            'aqua-mini-mot-cua-90-lit-aqr-d99fa-bs',
                            'samsung-inverter-multi-door-488-lit-rf48a4000b4sv',
                            'sharp-inverter-side-by-side-530-lit-sj-sbx530wd-dg',
                            'toshiba-194-lit-gr-rt252we-pmv52']
url='https://fptshop.com.vn/tu-lanh/'
DRIVER_PATH='D:\\BTL_NLP\\src\\scripts\\crawldata\\chromedriver.exe'
def get_data(ur,cmts):
    dr=webdriver.Chrome(options=options)
    dr.get(ur)
    dr.implicitly_wait(20)
    html = dr.page_source
    soup = BeautifulSoup(html, 'html5lib')
    txt=soup.find('div',class_='my-4 text-left text-textOnWhitePrimary b2-semibold mb:hidden pc:h6-semibold').text
    nums=int(txt.split("Bình luận")[0].strip())
    i=0
    while i<nums:
        try:
            next_page=dr.find_element(By.CLASS_NAME,"Pagination_pagerItem__A7rPt.CustomPaginationComment_pagerItem__qYCnP.Pagination_pagerItemNext__N2sCi")
            dr.execute_script('arguments[0].click()', next_page)
            html = dr.page_source
            soup = BeautifulSoup(html, 'html5lib')
            for cmt in soup.find_all('span', class_='false break-all'):
             cmts.append(cmt.text)
            i+=6
            # print(next_page)
            # print(len(comments))
            # print(comments[len(comments)-1])
        except NoSuchElementException:
            print("No more page available")
            break
    dr.quit()
comments=[]
get_data(url+devices[3],comments)
with open('../svm/train_data/toxic1.csv','a',newline='',encoding='utf-8-sig') as f:
    writer=csv.writer(f,delimiter=',')
    writer.writerow(['Content','Label'])
    for comment in tqdm(comments):
        writer.writerow(['nontoxic',comment.rstrip()])


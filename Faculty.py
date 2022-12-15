from bs4 import BeautifulSoup
import requests
from csv import writer
import csv
import os
import pandas as pd
import re

d = os.getcwd()
#For the ECE dept
#For the ECE dept
#For the ECE dept
url_ece = ["http://ece.northsouth.edu/people/rajesh-palit/", "http://ece.northsouth.edu/people/m-rokonuzzaman/","http://ece.northsouth.edu/people/kazi-salam/","http://ece.northsouth.edu/people/rashedur-rahman/","http://ece.northsouth.edu/people/hafiz-rahman/","http://ece.northsouth.edu/people/shazzad-hosain/","http://ece.northsouth.edu/people/dr-mohammad-abdul-matin/","http://ece.northsouth.edu/people/nova-ahmed/","http://ece.northsouth.edu/people/atiqur-rahman/","http://ece.northsouth.edu/people/lamia-iftekhar/","http://ece.northsouth.edu/people/monirujjaman-khan/","http://ece.northsouth.edu/people/mahdy-rahman-chowdhury/","http://ece.northsouth.edu/people/dr-sifat-momen/","http://ece.northsouth.edu/people/dr-nabeel-mohammed/","http://ece.northsouth.edu/people/dr-ahsanur-rahman/","http://ece.northsouth.edu/people/dr-tanzilur-rahman-2/","http://ece.northsouth.edu/people/dr-shohana-rahman-deeba/","http://ece.northsouth.edu/people/dr-shahnewaz-siddique/","http://ece.northsouth.edu/people/dr-mohammad-ashrafuzzaman-khan/","http://ece.northsouth.edu/people/md-shahriar-karim/","http://ece.northsouth.edu/people/riasat-khan/","http://ece.northsouth.edu/people/dr-dihanmd-nuruddinhasan/","http://ece.northsouth.edu/people/dr-nafisa-noor/","http://ece.northsouth.edu/people/mr-shafin-rahman/","http://ece.northsouth.edu/people/dr-nadia-anam/","http://ece.northsouth.edu/people/dr-asm-jahid-hasan/","http://ece.northsouth.edu/people/dr-mohammad-abdul-qayum/","http://ece.northsouth.edu/people/iqbalur-rokon/","http://ece.northsouth.edu/people/lutfe-elahi/","http://ece.northsouth.edu/people/silvia-ahmed/","http://ece.northsouth.edu/people/md-naqib-imtiaz-hussain/","http://ece.northsouth.edu/people/tanjila-farah/","http://ece.northsouth.edu/people/ms-ashfia-binte-habib/","http://ece.northsouth.edu/people/md-shahriar-hussain/","http://ece.northsouth.edu/people/mr-tarek-ibne-mizan/","http://ece.northsouth.edu/people/abu-obaidah/","http://ece.northsouth.edu/people/syed-kastur/","http://ece.northsouth.edu/people/syeda-sarita-hassan/","http://ece.northsouth.edu/people/mr-intisar-tahmid-naheen/","http://ece.northsouth.edu/people/ms-tanzilah-noor-shabnam/","http://ece.northsouth.edu/people/ms-meem-tasfia-zaman/","http://ece.northsouth.edu/people/mr-rifat-ahmed-hassan/","http://ece.northsouth.edu/people/mr-muhammad-shafayat-oshman/","http://ece.northsouth.edu/people/azmeen-rahman/","http://ece.northsouth.edu/people/maksud-alam/","http://ece.northsouth.edu/people/rummana-rahman/","http://ece.northsouth.edu/people/ishtiaque-hossain/","http://ece.northsouth.edu/people/rashed-shelim/","http://ece.northsouth.edu/people/ms-tamanna-motahar/","http://ece.northsouth.edu/people/mounota-natasha/","http://ece.northsouth.edu/people/adnan-firoze/","http://ece.northsouth.edu/people/ms-wahida-taskin-bhuiyan/","http://ece.northsouth.edu/people/mr-abdullah-al-mamun/","http://ece.northsouth.edu/people/md-mizanur-rahman/","http://ece.northsouth.edu/people/abdullah-al-zubaer-imran/","http://ece.northsouth.edu/people/rishad-arfin/","http://ece.northsouth.edu/people/zunayeed-bin-zahir/","http://ece.northsouth.edu/people/ms-neethila-poddar/","http://ece.northsouth.edu/people/akm-bahalul-haque/","http://ece.northsouth.edu/people/md-mahfuzur-rahman/","http://ece.northsouth.edu/people/shaikh-shawon-arefin-shimon/","http://ece.northsouth.edu/people/mr-fahimul-haque/","http://ece.northsouth.edu/people/ahnaf-rashik-hassan/","http://ece.northsouth.edu/people/mr-ahmed-fahmin/"]
def get_ece_faculty_details(url_ece) :
    request_web_page = requests.get(url_ece)

    soup = BeautifulSoup(request_web_page.text , 'html.parser')
    #print(soup)

    name = soup.find_all('h1' , class_ = 'title title-large')
    faculty_name = name[0].text
    print(faculty_name)

    image = soup.find_all('img' , class_ = "staff-image" )
    x = str(image)
    link = x[31:-4]
    #making or directring to existing folder
    try:
        #Either you make a directory
        os.mkdir(os.path.join(os.getcwd(), 'Images'))
    except:
        pass
    #Or write to an existing one
    os.chdir(os.path.join(os.getcwd(), 'Images'))

    try:
        with open(faculty_name + '.jpeg', 'wb') as f:
            try:
                im = requests.get(link)
                f.write(im.content)
            except :
                pass
    except :
        pass

    number = soup.find_all('div' , class_ = 'staff-heading2 tel')
    try :
        faculty_numb = number[0].text[7:]
        print(faculty_numb)
    except:
        faculty_numb = str("NULL")
        pass


    email = soup.find_all('a' , class_ = 'email')
    faculty_email = email[0].text
    print(faculty_email)


    dept = "Electrical & Computer Engineering"

    return faculty_name , faculty_email ,faculty_numb ,dept


#For the Accounts & Finance Department
#For the Accounts & Finance Department
#For the Accounts & Finance Department
url_af = ["http://www.northsouth.edu/faculty-members/sbe/acc-fin/sharif.ahkam.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/dr.-mohammad-istiaq-azim.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/dr.-akm-waresul-karim.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/arif.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/dr.-md.-nurul-kabir.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/rma.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/dr.-fahim-faisal.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/dr.-samina-rahman.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/mr.-tanvir-nabi-khan.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/dr.-fj-mohaimen-fjm.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/mr.-mokhdum-morshed.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/ms.-shanila-taneem-snt.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/mr.-adnan-habib-anb.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/mzf.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/mr.-hasan-a.-mamun.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/mr.-kamrul-huda-talukdar-kht.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/ms.-afrin-rifat-ani.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/nahar.nazmun.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/mr.-muin-uddin-ahmed.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/muhammad-nasiruddin-mn.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/rubaiya-nadia-huda.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/mr.-ahsanur-rahim-arm.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/mr.abdullah-al-mamun-ahm.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/mr.-sheikh-mohammad-rabby-rby.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/mr.mohammed-golam-rabbani-mgr.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/shahid.ullah.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/wasi.abdul.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/syed.hossain.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/iftear-ahmed-chowdhury-iac.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/trisha.ahmed.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/asy.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/bushra-ferdous-khan-bfk.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/mohammad.rekabder.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/taskin.shakib.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/mr.-rezwanul-mumtahin-husain.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/sohanur-rahman.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/ms.-syeda-humayra-abedin.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/tanjina-shahjahan.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/humaira-haque.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/ms.-faria-islam-rista.html","http://www.northsouth.edu/faculty-members/sbe/acc-fin/hasan-mohammed-sami.html"]
def get_accounts_and_finance_faculty_details(url_af) :
    request_web_page = requests.get(url_af)

    soup = BeautifulSoup(request_web_page.text, 'html.parser')
    # print(soup)

    name = soup.find_all('h2', class_="title")
    faculty_name = name[0].text
    print(faculty_name)

    p = soup.find('div', class_="col-md-3")
    q = p.find_all('img')
    link = "http://www.northsouth.edu/" + q[0]['src'][0:]
    link2 = "http://www.northsouth.edu/" + q[0]['src'][0:]
    try:
        # Either you make a directory
        os.mkdir(os.path.join(os.getcwd(), 'Images'))
    except:
        pass
    # Or write to an existing one
    os.chdir(os.path.join(os.getcwd(), 'Images'))

    try:
        with open(faculty_name + '.jpeg', 'wb') as f:
            try:
                im = requests.get(link)
                f.write(im.content)
            except:
                im = requests.get(link2)
                f.write(im.content)
                pass
            try:
                im = requests.get(link3)
                f.write(im.content)
            except:
                pass
    except:
        pass

    email = soup.find("td")
    x = email.find_all("p")
    i = 0
    y = []
    for a in range(len(x)):
        j = x[i].text
        y.append(j)
        i = i + 1;
    y = str(y)

    # Regex generator link
    # https://regex-generator.olafneumann.org/?sampleText=%2B880-2-55668200%20Ext%3A%201072&flags=i
    faculty_email = str(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", y))[2:-2]
    print(faculty_email)

    faculty_numb = str(re.findall(r"\+880-\d-[0-9]+.*Ext.*\d\d\d\d", y))[2:28]
    faculty_numb = faculty_numb.replace("'", "")
    faculty_numb = faculty_numb.replace("]", "")
    print((faculty_numb))

    dept = "Accounts & Finance"

    return faculty_name, faculty_email, faculty_numb, dept


#For the Economics Department
#For the Economics Department
#For the Economics Department
url_eco = ["http://www.northsouth.edu/faculty-members/sbe/economics/dr.mismailhossain.html" , "http://www.northsouth.edu/faculty-members/sbe/economics/akm.atiqur.html" , "http://www.northsouth.edu/faculty-members/sbe/economics/grg.html" , "http://www.northsouth.edu/faculty-members/sbe/economics/ataur.html" , "http://www.northsouth.edu/faculty-members/sbe/economics/dr-helal-ahammad.html" , "http://www.northsouth.edu/faculty-members/sbe/economics/dr.mustafaabdurrahman.html" , "http://www.northsouth.edu/faculty-members/sbe/economics/dr.-sakib-bin-amin.html" , "http://www.northsouth.edu/faculty-members/sbe/economics/dr.-ahmed-tazmeen.html" , "http://www.northsouth.edu/faculty-members/sbe/economics/dr.-asad-karim-khan-priyo.html" , "http://www.northsouth.edu/faculty-members/sbe/economics/dr.-kanti-ananta-nuzhat.html" , "http://www.northsouth.edu/faculty-members/sbe/economics/dr.-mainul-islam-chowdhury.html" , "http://www.northsouth.edu/faculty-members/sbe/economics/dr.-syed-mortuza-asif-ehsan.html" , "http://www.northsouth.edu/faculty-members/sbe/economics/md.-syeed-uz-zaman-khan.html" , "http://www.northsouth.edu/faculty-members/sbe/economics/dr.-samiul-haque.html","http://www.northsouth.edu/faculty-members/sbe/economics/s-m-zahid-iqbal.html","http://www.northsouth.edu/faculty-members/sbe/economics/tapas-kumar-paul.html","http://www.northsouth.edu/faculty-members/sbe/economics/dr.-md.-javed-hossain.html","http://www.northsouth.edu/faculty-members/sbe/economics/syediftekharulhuq.html","http://www.northsouth.edu/faculty-members/sbe/economics/abdulmumit.html","http://www.northsouth.edu/faculty-members/sbe/economics/raisaafsana.html","http://www.northsouth.edu/faculty-members/sbe/economics/ms.-humaira-husain-hhn.html","http://www.northsouth.edu/faculty-members/sbe/economics/ms.-chowdhury-nawsheen-farooqui-cnq.html","http://www.northsouth.edu/faculty-members/sbe/economics/ms.-parisa-shakur-psk.html","http://www.northsouth.edu/faculty-members/sbe/economics/iqb.html","http://www.northsouth.edu/faculty-members/sbe/economics/ms.-nazneen-imam.html","http://www.northsouth.edu/faculty-members/sbe/economics/aba.html","http://www.northsouth.edu/faculty-members/sbe/economics/mr.-asif-chowdhury/","http://www.northsouth.edu/faculty-members/sbe/economics/ms.-aroni-kabita-porna.html","http://www.northsouth.edu/faculty-members/sbe/economics/nabeel.iqbal.html","http://www.northsouth.edu/faculty-members/sbe/economics/mr.-a.-m.-muhib-morshed.html","http://www.northsouth.edu/faculty-members/sbe/economics/ms.-mahnaz-aftabi-atique.html","http://www.northsouth.edu/faculty-members/sbe/economics/sayed-jubair-bin-hossain.html"]
def get_eco_faculty_details(url_eco) :
    request_web_page = requests.get(url_eco)
    soup = BeautifulSoup(request_web_page.text, 'html.parser')
    # print(soup)

    name = soup.find_all('h2', class_="title")
    faculty_name = name[0].text
    print(faculty_name)

    p = soup.find('div', class_="col-md-3")
    q = p.find_all('img')
    link = "http://www.northsouth.edu/" + q[0]['src'][0:]
    link2 = "http://www.northsouth.edu/" + q[0]['src'][0:]
    link3 = q[0]['src'][0:]
    try:
        # Either you make a directory
        os.mkdir(os.path.join(os.getcwd(), 'Images'))
    except:
        pass
    # Or write to an existing one
    os.chdir(os.path.join(os.getcwd(), 'Images'))

    try:
        with open(faculty_name + '.jpeg', 'wb') as f:
            try:
                im = requests.get(link)
                f.write(im.content)
            except:
                im = requests.get(link2)
                f.write(im.content)
                pass
            try:
                im = requests.get(link3)
                f.write(im.content)
            except:
                pass
    except:
        pass

    email = soup.find("td")
    x = email.find_all("p")
    i = 0
    y = []
    for a in range(len(x)):
        j = x[i].text
        y.append(j)
        i = i + 1;
    y = str(y)

    # Regex generator link
    # https://regex-generator.olafneumann.org/?sampleText=%2B880-2-55668200%20Ext%3A%201072&flags=i
    faculty_email = str(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", y))[2:-2]
    print(faculty_email)
    faculty_numb = str(re.findall(r"\+880-\d-[0-9]+.*Ext.*\d\d\d\d", y))[2:28]
    faculty_numb = faculty_numb.replace("'","")
    faculty_numb = faculty_numb.replace("]", "")
    #e = str(len(faculty_numb))
    #print("type of " + type(e))
#
    #if e > 26 :
    #    print("e = " + e)
    #    faculty_numb = faculty_numb[0:26]
    print((faculty_numb))

    dept = "Economics"

    return faculty_name, faculty_email, faculty_numb, dept


#For the Management Department
#For the Management Department
#For the Management Department
url_manage = ["http://www.northsouth.edu/faculty-members/sbe/mgt/dr.-abdul-hannan-chowdhury.html","http://www.northsouth.edu/faculty-members/sbe/mgt/dr.-m.-khasro-miah.html","http://www.northsouth.edu/faculty-members/sbe/mgt/mds.html","http://www.northsouth.edu/faculty-members/sbe/mgt/jashim.ahmed.html","http://www.northsouth.edu/faculty-members/sbe/mgt/nazlee-siddiqui.html","http://www.northsouth.edu/faculty-members/sbe/mgt/atikur-rahman-khan.html","http://www.northsouth.edu/faculty-members/sbe/mgt/s.-s.-m.-sadrul-huda.html","http://www.northsouth.edu/faculty-members/sbe/mgt/ziaul-haq-adnan.html","http://www.northsouth.edu/faculty-members/sbe/mgt/ummaha.hazra.html","http://www.northsouth.edu/faculty-members/sbe/mgt/zmu.html","http://www.northsouth.edu/faculty-members/sbe/mgt/dr.-mehe-z.-rahman.html","http://www.northsouth.edu/faculty-members/sbe/mgt/shl.html","http://www.northsouth.edu/faculty-members/sbe/mgt/dr.-zulkarin-jahangir.html","http://www.northsouth.edu/faculty-members/sbe/mgt/alima-aktar.html","http://www.northsouth.edu/faculty-members/sbe/mgt/dr.-md.-shamim-talukder.html","http://www.northsouth.edu/faculty-members/sbe/mgt/hannan.miah.html","http://www.northsouth.edu/faculty-members/sbe/mgt/shahid.hossain.html","http://www.northsouth.edu/faculty-members/sbe/mgt/mr.-ashik-imran-khan.html","http://www.northsouth.edu/faculty-members/sbe/mgt/fsw.html","http://www.northsouth.edu/faculty-members/sbe/mgt/md.-al-amin.html","http://www.northsouth.edu/faculty-members/sbe/mgt/nwa.html","http://www.northsouth.edu/faculty-members/sbe/mgt/ms.-niza-talukder-tkn.html","http://www.northsouth.edu/faculty-members/sbe/mgt/shafquat.alam.html","http://www.northsouth.edu/faculty-members/sbe/mgt/quazitafsir.html","http://www.northsouth.edu/faculty-members/sbe/mgt/bobby-hajjaj.html","http://www.northsouth.edu/faculty-members/sbe/mgt/shabnin-rahman-shorna-srs2.html","http://www.northsouth.edu/faculty-members/sbe/mgt/tua.html","http://www.northsouth.edu/faculty-members/sbe/mgt/afnaan.ahmed.html","http://www.northsouth.edu/faculty-members/sbe/mgt/adeyl-khan.html","http://www.northsouth.edu/faculty-members/sbe/mgt/mr.-shah-iftekhar-hossain-ift.html","http://www.northsouth.edu/faculty-members/sbe/mgt/israt.laila.html","http://www.northsouth.edu/faculty-members/sbe/mgt/rahnuma.sanjana.html","http://www.northsouth.edu/faculty-members/sbe/mgt/mof.html","http://www.northsouth.edu/faculty-members/sbe/mgt/tasnuva.chaudhury.html","http://www.northsouth.edu/faculty-members/sbe/mgt/kabid-md-surid.html","http://www.northsouth.edu/faculty-members/sbe/mgt/samuel-mursalin.html","http://www.northsouth.edu/faculty-members/sbe/mgt/tanya-ahmed/","http://www.northsouth.edu/faculty-members/sbe/mgt/rumana.luva.html","http://www.northsouth.edu/faculty-members/sbe/mgt/faseeha-zabir.html","http://www.northsouth.edu/faculty-members/sbe/mgt/mohammad-asif-gazi.html","http://www.northsouth.edu/faculty-members/sbe/mgt/md-asif-hossain.html","http://www.northsouth.edu/faculty-members/sbe/mgt/md-kamrul-hasan.html","http://www.northsouth.edu/faculty-members/sbe/mgt/tasnim-tarannum.html","http://www.northsouth.edu/faculty-members/sbe/mgt/umama-rahman.html","http://www.northsouth.edu/faculty-members/sbe/mgt/tasfia-mazid.html","http://www.northsouth.edu/faculty-members/sbe/mgt/asma-azad-akhi.html","http://www.northsouth.edu/faculty-members/sbe/mgt/looksina-khan.html","http://www.northsouth.edu/faculty-members/sbe/mgt/hamida-mosharraf-moniea.html","http://www.northsouth.edu/faculty-members/sbe/mgt/syed-imamuzzaman.html","http://www.northsouth.edu/faculty-members/sbe/mgt/umme-hani-meem.html","http://www.northsouth.edu/faculty-members/sbe/mgt/shabab-absarul-islam.html","http://www.northsouth.edu/faculty-members/sbe/mgt/meshbaul-hassan-chowdhury.html","http://www.northsouth.edu/faculty-members/sbe/mgt/yasir-arefin.html","http://www.northsouth.edu/faculty-members/sbe/mgt/yasir-arefin-yar.html" ]
def get_management_faculty_details(url_manage):
    request_web_page = requests.get(url_manage)

    soup = BeautifulSoup(request_web_page.text, 'html.parser')
    # print(soup)

    name = soup.find_all('h2', class_="title")
    faculty_name = name[0].text
    print(faculty_name)

    p = soup.find('div', class_="col-md-3")
    q = p.find_all('img')
    link = "http://www.northsouth.edu/" + q[0]['src'][0:]
    link2 = "http://www.northsouth.edu/" + q[0]['src'][0:]
    link3 = q[0]['src'][0:]
    try:
        # Either you make a directory
        os.mkdir(os.path.join(os.getcwd(), 'Images'))
    except:
        pass
    # Or write to an existing one
    os.chdir(os.path.join(os.getcwd(), 'Images'))

    try:
        with open(faculty_name + '.jpeg', 'wb') as f:
            try:
                im = requests.get(link)
                f.write(im.content)
            except:
                pass
            try:
                im = requests.get(link2)
                f.write(im.content)
            except:
                pass
            try:
                im = requests.get(link3)
                f.write(im.content)
            except:
                pass

    except:
        pass

    email = soup.find("td")
    try:
        x = email.find_all("p")
    except:
        x = ""
        pass

    i = 0
    y = []
    for a in range(len(x)):
        j = x[i].text
        y.append(j)
        i = i + 1;
    y = str(y)

    # Regex generator link
    # https://regex-generator.olafneumann.org/?sampleText=%2B880-2-55668200%20Ext%3A%201072&flags=i
    faculty_email = str(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", y))[2:-2]
    print(faculty_email)

    faculty_numb = str(re.findall(r"\+880-\d-[0-9]+.*Ext.*\d\d\d\d", y))[2:28]
    faculty_numb = faculty_numb.replace("'", "")
    faculty_numb = faculty_numb.replace("]", "")
    faculty_numb = faculty_numb.replace('/', "")


    print((faculty_numb))

    dept = "Management"

    return faculty_name, faculty_email, faculty_numb, dept


#For the Marketing and International Department
#For the Marketing and International Department
#For the Marketing and International Department
url_m_and_i = ["http://www.northsouth.edu/faculty-members/sbe/marketing-ib/dr.-tamgid-ahmed-chowdhury.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/dr.-muhammad-sabbir-rahman-dsr.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/dr.-mohammad-tayeenul-hoque.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/mahmud-hassan.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/farzana-nahid.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/khandker-md.-nahin-mamun.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/dr.-mehree-iqbal-mei.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/mr.-syed-kamrul-islam-ski.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/ztk.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/ishrat.synthia.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/mhz.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/rafsan.elahi.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/mr.-afnan-hossain.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/ms.-sherina-idrish-seh.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/ms.-narmin-tartila-banu-ntb.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/ms.-shahneela-naheed-sne.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/mahafuz.mannan.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/mev.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/mr.-mohammad-sakif-amin-skf.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/ms.-farzana-choudhury-fzy.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/mr.-omar-nasif-abdullah-onf.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/mahtab-muntazeri-mbt.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/mr.-faiz-hossain.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/farhana.tabassum.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/ehfaz.nowman.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/ms.-fairuze-chowdhury.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/farhana.zinnia.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/ms.-tilka-farzana.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/fdf.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/shadman-sahir-ahmed.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/tasneem-binte-morshed.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/saima-siddiqui.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/mr.ujal-ibrahim-ujb.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/nilufer-yasmin-munni.html","http://www.northsouth.edu/faculty-members/sbe/marketing-ib/afrida-mashnoon.html"]
def get_m_and_i_faculty_details(url_m_and_i):
    request_web_page = requests.get(url_m_and_i)

    soup = BeautifulSoup(request_web_page.text, 'html.parser')
    # print(soup)

    name = soup.find_all('h2', class_="title")
    faculty_name = name[0].text
    print(faculty_name)

    p = soup.find('div', class_="col-md-3")
    q = p.find_all('img')
    link = "http://www.northsouth.edu/" + q[0]['src'][0:]
    link2 = "http://www.northsouth.edu/" + q[0]['src'][0:]
    link3 = q[0]['src'][0:]
    try:
        # Either you make a directory
        os.mkdir(os.path.join(os.getcwd(), 'Images'))
    except:
        pass
    # Or write to an existing one
    os.chdir(os.path.join(os.getcwd(), 'Images'))

    try:
        with open(faculty_name + '.jpeg', 'wb') as f:
            try:
                im = requests.get(link)
                f.write(im.content)
            except:
                im = requests.get(link2)
                f.write(im.content)
                pass
            try:
                im = requests.get(link3)
                f.write(im.content)
            except:
                pass
    except:
        pass

    email = soup.find("td")
    email = soup.find("td")
    try:
        x = email.find_all("p")
    except:
        x = ""
        pass
    i = 0
    y = []
    for a in range(len(x)):
        j = x[i].text
        y.append(j)
        i = i + 1;
    y = str(y)

    # Regex generator link
    # https://regex-generator.olafneumann.org/?sampleText=%2B880-2-55668200%20Ext%3A%201072&flags=i
    faculty_email = str(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", y))[2:-2]
    print(faculty_email)

    faculty_numb = str(re.findall(r"\+880-\d-[0-9]+.*Ext.*\d\d\d\d", y))[2:28]
    faculty_numb = faculty_numb.replace("'", "")
    faculty_numb = faculty_numb.replace("]", "")
    faculty_numb = faculty_numb.replace("/", "")
    print((faculty_numb))

    dept = "Marketing and International"

    return faculty_name, faculty_email, faculty_numb, dept


#For the Architecture Department
#For the Architecture Department
#For the Architecture Department
url_archi = ["http://www.northsouth.edu/faculty-members/seps/architecture/hur.html","http://www.northsouth.edu/faculty-members/seps/architecture/mujtaba-ahsan.html","http://www.northsouth.edu/faculty-members/seps/architecture/ms.-shaila-joarder.html","http://www.northsouth.edu/faculty-members/seps/architecture/dr.-saiful-islam.html","http://www.northsouth.edu/faculty-members/seps/architecture/dr.-nandini-awal.html","http://www.northsouth.edu/faculty-members/seps/architecture/mr.-shahriar-iqbal-raj.html","http://www.northsouth.edu/faculty-members/seps/architecture/ms.-ismat-hossain-ish.html","http://www.northsouth.edu/faculty-members/seps/architecture/mr.maruf-hossain.html","http://www.northsouth.edu/faculty-members/seps/architecture/sujaul-islam-khan.html","http://www.northsouth.edu/faculty-members/seps/architecture/mr.-adnan-hossain.html","http://www.northsouth.edu/faculty-members/seps/architecture/izk.html","http://www.northsouth.edu/faculty-members/seps/architecture/shanjida.shamma.html","http://www.northsouth.edu/faculty-members/seps/architecture/amity-kundu.html","http://www.northsouth.edu/faculty-members/seps/architecture/mehnaj-tabassum.html", "http://www.northsouth.edu/faculty-members/seps/architecture/aida-hassan.html" , "http://www.northsouth.edu/faculty-members/seps/architecture/rishaad-mohammad-yusuff.html"]
def get_archi_faculty_details(url_archi):
    request_web_page = requests.get(url_archi)

    soup = BeautifulSoup(request_web_page.text, 'html.parser')
    # print(soup)

    name = soup.find_all('h2', class_="title")
    faculty_name = name[0].text
    print(faculty_name)

    p = soup.find('div', class_="col-md-3")
    try:
        q = p.find_all('img')
        link = "http://www.northsouth.edu" + q[0]['src'][0:]
        link2 = "http://www.northsouth.edu/" + q[0]['src'][0:]
        link3 = q[0]['src'][0:]
    except:
        link = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
        link2 = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
        link3 = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
    try:
        # Either you make a directory
        os.mkdir(os.path.join(os.getcwd(), 'Images'))
    except:
        pass
    # Or write to an existing one
    os.chdir(os.path.join(os.getcwd(), 'Images'))

    try:
        with open(faculty_name + '.jpeg', 'wb') as f:
            try:
                im = requests.get(link)
                f.write(im.content)
            except:
                im = requests.get(link2)
                f.write(im.content)
                pass
            try:
                im = requests.get(link3)
                f.write(im.content)
            except:
                pass
    except:
        pass

    email = soup.find("td")
    email = soup.find("td")
    try:
        x = email.find_all("p")
    except:
        x = ""
        pass
    i = 0
    y = []
    for a in range(len(x)):
        j = x[i].text
        y.append(j)
        i = i + 1;
    y = str(y)

    # Regex generator link
    # https://regex-generator.olafneumann.org/?sampleText=%2B880-2-55668200%20Ext%3A%201072&flags=i
    faculty_email = str(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", y))[2:-2]
    print(faculty_email)

    faculty_numb = str(re.findall(r"\+880-\d-[0-9]+.*Ext.*\d\d\d\d", y))[2:28]
    faculty_numb = faculty_numb.replace("'", "")
    faculty_numb = faculty_numb.replace("]", "")
    faculty_numb = faculty_numb.replace("/", "")
    print((faculty_numb))

    dept = "Architecture"

    return faculty_name, faculty_email, faculty_numb, dept


#For the Mathematics & Physics Department
#For the Mathematics & Physics Department
#For the Mathematics & Physics Department
url_m_and_p = ["http://www.northsouth.edu/faculty-members/seps/mathematics-physics/mla.html","http://www.northsouth.edu/faculty-members/seps/mathematics-physics/dr.-md.-sahadet-hossain-mth.html","http://www.northsouth.edu/faculty-members/seps/mathematics-physics/dr.-subir-chandra-ghosh.html","http://www.northsouth.edu/faculty-members/seps/mathematics-physics/dr.-muhammad-asad-uz-zaman.html","http://www.northsouth.edu/faculty-members/seps/mathematics-physics/hasina.akter.html","http://www.northsouth.edu/faculty-members/seps/mathematics-physics/dr.-mohammad-monir-uddin.html","http://www.northsouth.edu/faculty-members/seps/mathematics-physics/dr.-preetom-nag.html","http://www.northsouth.edu/faculty-members/seps/mathematics-physics/dr.-zaid-bin-mahbub-zbm.html","http://www.northsouth.edu/faculty-members/seps/mathematics-physics/dr.-md-harunur-rashid.html","http://www.northsouth.edu/faculty-members/seps/mathematics-physics/dr.-md.-shariful-islam.html","http://www.northsouth.edu/faculty-members/seps/mathematics-physics/dr.-mohammad-ali-nawaz.html","http://www.northsouth.edu/faculty-members/seps/mathematics-physics/dr.-atia-afroz.html","http://www.northsouth.edu/faculty-members/seps/mathematics-physics/mtm.html","http://www.northsouth.edu/faculty-members/seps/mathematics-physics/mahaboob-shaheen-ms1.html","http://www.northsouth.edu/faculty-members/seps/mathematics-physics/md.-zahangir-hossain-zhn.html","http://www.northsouth.edu/faculty-members/seps/mathematics-physics/mr.-zasim-u.-mazumder-zum.html","http://www.northsouth.edu/faculty-members/seps/mathematics-physics/mohammad-mahmud-hasan.html","http://www.northsouth.edu/faculty-members/seps/mathematics-physics/md-arifuzzaman-azm1.html","http://www.northsouth.edu/faculty-members/seps/mathematics-physics/sharmin-sultana.html","http://www.northsouth.edu/faculty-members/seps/mathematics-physics/mohammad-niaz-murshed.html","http://www.northsouth.edu/faculty-members/seps/mathematics-physics/mr.abu-naser-sarker.html","http://www.northsouth.edu/faculty-members/seps/mathematics-physics/md-salik-ahmed-ska2.html","http://www.northsouth.edu/faculty-members/seps/mathematics-physics/israt-jahan.html","http://www.northsouth.edu/faculty-members/seps/mathematics-physics/saquib-musavi-hassan.html","http://www.northsouth.edu/faculty-members/seps/mathematics-physics/afroja-parvin.html","http://www.northsouth.edu/faculty-members/seps/mathematics-physics/muhammad-sohel-rana.html"]
def get_m_and_p_faculty_details(url_m_and_p):
    request_web_page = requests.get(url_m_and_p)

    soup = BeautifulSoup(request_web_page.text, 'html.parser')
    # print(soup)

    name = soup.find_all('h2', class_="title")
    faculty_name = name[0].text
    print(faculty_name)

    p = soup.find('div', class_="col-md-3")
    try:
        q = p.find_all('img')
        link = "http://www.northsouth.edu" + q[0]['src'][0:]
        link2 = "http://www.northsouth.edu/" + q[0]['src'][0:]
        link3 = q[0]['src'][0:]
    except:
        link = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
        link2 = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
        link3 = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
    try:
        # Either you make a directory
        os.mkdir(os.path.join(os.getcwd(), 'Images'))
    except:
        pass
    # Or write to an existing one
    os.chdir(os.path.join(os.getcwd(), 'Images'))

    try:
        with open(faculty_name + '.jpeg', 'wb') as f:
            try:
                im = requests.get(link)
                f.write(im.content)
            except:
                im = requests.get(link2)
                f.write(im.content)
                pass
            try:
                im = requests.get(link3)
                f.write(im.content)
            except:
                pass
    except:
        pass

    email = soup.find("td")
    email = soup.find("td")
    try:
        x = email.find_all("p")
    except:
        x = ""
        pass
    i = 0
    y = []
    for a in range(len(x)):
        j = x[i].text
        y.append(j)
        i = i + 1;
    y = str(y)

    # Regex generator link
    # https://regex-generator.olafneumann.org/?sampleText=%2B880-2-55668200%20Ext%3A%201072&flags=i
    faculty_email = str(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", y))[2:-2]
    print(faculty_email)

    faculty_numb = str(re.findall(r"\+880-\d-[0-9]+.*Ext.*\d\d\d\d", y))[2:28]
    faculty_numb = faculty_numb.replace("'", "")
    faculty_numb = faculty_numb.replace("]", "")
    faculty_numb = faculty_numb.replace("/", "")
    print((faculty_numb))

    dept = "Mathematics & Physics Department"

    return faculty_name, faculty_email, faculty_numb, dept


#For the English & Modern Languages Department
#For the English & Modern Languages Department
#For the English & Modern Languages Department
url_e_and_ml =["http://www.northsouth.edu/faculty-members/shss/eml/rahman.bhuiyan.html","http://www.northsouth.edu/faculty-members/shss/eml/mohammad.shamsuzzaman.html","http://www.northsouth.edu/faculty-members/shss/eml/mr.shahedulhaque.html","http://www.northsouth.edu/faculty-members/shss/eml/katherine.li.html","http://www.northsouth.edu/faculty-members/shss/eml/shakila-nur.html","http://www.northsouth.edu/faculty-members/shss/eml/sukanto-roy.html","http://www.northsouth.edu/faculty-members/shss/eml/shapla.parveen.html","http://www.northsouth.edu/faculty-members/shss/eml/nazia.manzoor.html","http://www.northsouth.edu/faculty-members/shss/eml/nasrin-jabin.html","http://www.northsouth.edu/faculty-members/shss/eml/nasreen.rahman.html","http://www.northsouth.edu/faculty-members/shss/eml/sakiba.ferdousy.html","http://www.northsouth.edu/faculty-members/shss/eml/ms.-noora-shamsi-bahar.html","http://www.northsouth.edu/faculty-members/shss/eml/nasrin.pervin.html","http://www.northsouth.edu/faculty-members/shss/eml/michelle.draper.html","http://www.northsouth.edu/faculty-members/shss/eml/musharrat.hossain.html","http://www.northsouth.edu/faculty-members/shss/eml/samira.aziz.html","http://www.northsouth.edu/faculty-members/shss/eml/shakhaowat.hossain.html","http://www.northsouth.edu/faculty-members/shss/eml/sabeeha.saleque.html","http://www.northsouth.edu/faculty-members/shss/eml/sameya.priom.html","http://www.northsouth.edu/faculty-members/shss/eml/nausheen.siraj.html","http://www.northsouth.edu/faculty-members/shss/eml/ms.-tania-rahman.html","http://www.northsouth.edu/faculty-members/shss/eml/mehedi.hasan.html","http://www.northsouth.edu/faculty-members/shss/eml/sheikh-zobaer.html","http://www.northsouth.edu/faculty-members/shss/eml/shafayat.rasul.html","http://www.northsouth.edu/faculty-members/shss/eml/shahneela-tasmin-sharmi.html","http://www.northsouth.edu/faculty-members/shss/eml/shafqat.chaudhury.html","http://www.northsouth.edu/faculty-members/shss/eml/farzana.mohsin.html","http://www.northsouth.edu/faculty-members/shss/eml/nasreen.sultana.html","http://www.northsouth.edu/faculty-members/shss/eml/saleheen.ahmed.html","http://www.northsouth.edu/faculty-members/shss/eml/naveed.islam.html","http://www.northsouth.edu/faculty-members/shss/eml/s.m.-rubyat-rbt.html","http://www.northsouth.edu/faculty-members/shss/eml/rumana.aktar.html","http://www.northsouth.edu/faculty-members/shss/eml/atanu.bhuiyan.html","http://www.northsouth.edu/faculty-members/shss/eml/sumaiya-tasneem-haque.html","http://www.northsouth.edu/faculty-members/shss/eml/ashrafun-nahar.html","http://www.northsouth.edu/faculty-members/shss/eml/sarah.zaman.html","http://www.northsouth.edu/faculty-members/shss/eml/munira.khan.html","http://www.northsouth.edu/faculty-members/shss/eml/sayma.ahmed.html","http://www.northsouth.edu/faculty-members/shss/eml/tareq-arafat.html","http://www.northsouth.edu/faculty-members/shss/eml/ms.-shahnaz-sultana-kaiser.html","http://www.northsouth.edu/faculty-members/shss/eml/ms.-fariah-hassan.html"]
def get_e_and_ml_faculty_details(url_e_and_ml):
    request_web_page = requests.get(url_e_and_ml)

    soup = BeautifulSoup(request_web_page.text, 'html.parser')
    # print(soup)

    name = soup.find_all('h2', class_="title")
    faculty_name = name[0].text
    print(faculty_name)

    p = soup.find('div', class_="col-md-3")
    try:
        q = p.find_all('img')
        link = "http://www.northsouth.edu" + q[0]['src'][0:]
        link2 = "http://www.northsouth.edu/" + q[0]['src'][0:]
        link3 = q[0]['src'][0:]
    except:
        link = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
        link2 = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
        link3 = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
    try:
        # Either you make a directory
        os.mkdir(os.path.join(os.getcwd(), 'Images'))
    except:
        pass
    # Or write to an existing one
    os.chdir(os.path.join(os.getcwd(), 'Images'))

    try:
        with open(faculty_name + '.jpeg', 'wb') as f:
            try:
                im = requests.get(link)
                f.write(im.content)
            except:
                im = requests.get(link2)
                f.write(im.content)
                pass
            try:
                im = requests.get(link3)
                f.write(im.content)
            except:
                pass
    except:
        pass

    email = soup.find("td")
    try:
        x = email.find_all("p")
    except:
        x = ""
        pass

    i = 0
    y = []
    for a in range(len(x)):
        j = x[i].text
        y.append(j)
        i = i + 1;
    y = str(y)

    # Regex generator link
    # https://regex-generator.olafneumann.org/?sampleText=%2B880-2-55668200%20Ext%3A%201072&flags=i
    faculty_email = str(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", y))[2:-2]
    print(faculty_email)

    faculty_numb = str(re.findall(r"\+880-\d-[0-9]+.*Ext.*\d\d\d\d", y))[2:28]
    faculty_numb = faculty_numb.replace("'", "")
    faculty_numb = faculty_numb.replace("]", "")
    faculty_numb = faculty_numb.replace("/", "")
    print((faculty_numb))

    if faculty_numb == "" :
        if faculty_email == "" :
            email = soup.find_all("td")
            try:
                x = email[3].find_all("strong")
            except:
                x = ""
                pass

            i = 0
            y = []
            for a in range(len(x)):
                j = x[i].text
                y.append(j)
                i = i + 1;
            y = str(y)

            # Regex generator link
            # https://regex-generator.olafneumann.org/?sampleText=%2B880-2-55668200%20Ext%3A%201072&flags=i
            faculty_email = str(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", y))[2:-2]
            print(faculty_email)

            faculty_numb = str(re.findall(r"\+880-\d-[0-9]+.*Ext.*\d\d\d\d", y))[2:28]
            faculty_numb = faculty_numb.replace("'", "")
            faculty_numb = faculty_numb.replace("]", "")
            faculty_numb = faculty_numb.replace("/", "")
            print((faculty_numb))


    dept = "English & Modern Languages"

    return faculty_name, faculty_email, faculty_numb, dept


#For the Political Science and Sociology Department
#For the Political Science and Sociology Department
#For the Political Science and Sociology Department
url_p_and_s = ["http://www.northsouth.edu/faculty-members/shss/pss/abdur.khan.html","http://www.northsouth.edu/faculty-members/shss/pss/emdadul.haq.html","http://www.northsouth.edu/faculty-members/shss/pss/tawfique.haque.html","http://www.northsouth.edu/faculty-members/shss/pss/mahbubur.rahman.html","http://www.northsouth.edu/faculty-members/shss/pss/dr.-helal-mohd.-mohiuddin.html","http://www.northsouth.edu/faculty-members/shss/pss/mohammad-nuruzzaman.html","http://www.northsouth.edu/faculty-members/shss/pss/mohammad.siddiqi.html","http://www.northsouth.edu/faculty-members/shss/pss/jashim.uddin.html","http://www.northsouth.edu/faculty-members/shss/pss/dr.-rizwan-khair.html","http://www.northsouth.edu/faculty-members/shss/pss/s.m-rezwan-ul-alam.html","http://www.northsouth.edu/faculty-members/shss/pss/dr.-harisur-rahman.html","http://www.northsouth.edu/faculty-members/shss/pss/heinz-scheifinger.html","http://www.northsouth.edu/faculty-members/shss/pss/cynthia.mckinney.html","http://www.northsouth.edu/faculty-members/shss/pss/mahmudur-rahman-bhuiyan.html","http://www.northsouth.edu/faculty-members/shss/pss/mubashar.hasan.html","http://www.northsouth.edu/faculty-members/shss/pss/dr.-ishrat-zakia-sultana-izs.html","http://www.northsouth.edu/faculty-members/shss/pss/dr.-abdul-wohab.html","http://www.northsouth.edu/faculty-members/shss/pss/dr.-hasan-muhammad-baniamin.html","http://www.northsouth.edu/faculty-members/shss/pss/dr.-mohammad-jalal-uddin-sikder.html","http://www.northsouth.edu/faculty-members/shss/pss/raymond-kwun-sun-lau.html","http://www.northsouth.edu/faculty-members/shss/pss/md.-towfique-e-elahi.html","http://www.northsouth.edu/faculty-members/shss/pss/md-akram-hossain.html","http://www.northsouth.edu/faculty-members/shss/pss/tata.zafar.html","http://www.northsouth.edu/faculty-members/shss/pss/moushumi.shabnam.html","http://www.northsouth.edu/faculty-members/shss/pss/saimum.parveznorthsouth.edu.html","http://www.northsouth.edu/faculty-members/shss/pss/md.sabur.html","http://www.northsouth.edu/faculty-members/shss/pss/mizanur.rahman.html","http://www.northsouth.edu/faculty-members/shss/pss/tauhid.kashem.html","http://www.northsouth.edu/faculty-members/shss/pss/shams.quader.html","http://www.northsouth.edu/faculty-members/shss/pss/saidur.rahman02.html","http://www.northsouth.edu/faculty-members/shss/pss/parboti-roy-pbr.html","http://www.northsouth.edu/faculty-members/shss/pss/nur-newaz-khan-nn.html","http://www.northsouth.edu/faculty-members/shss/pss/ms.-tasmia-nower.html","http://www.northsouth.edu/faculty-members/shss/pss/asif-bin-ali.html","http://www.northsouth.edu/faculty-members/shss/pss/nzm.html","http://www.northsouth.edu/faculty-members/shss/pss/dr.-syeda-lasna-kabir.html","http://www.northsouth.edu/faculty-members/shss/pss/dr.-abul-kalam-azad.html","http://www.northsouth.edu/faculty-members/shss/pss/dr.-mohammad-nasir-uddin.html","http://www.northsouth.edu/faculty-members/shss/pss/mohammad-moniruzzaman-khan.html","http://www.northsouth.edu/faculty-members/shss/pss/dr.-naseem-akhter-hussain.html","http://www.northsouth.edu/faculty-members/shss/pss/dr.-ranjan-saha-partha.html","http://www.northsouth.edu/faculty-members/shss/pss/mofizur-rhaman.html","http://www.northsouth.edu/faculty-members/shss/pss/dr.-nurul-huda-sakib.html","http://www.northsouth.edu/faculty-members/shss/pss/dr.-mahfuzul-haque.html","http://www.northsouth.edu/faculty-members/shss/pss/saifuddin-ahmed.html","http://www.northsouth.edu/faculty-members/shss/pss/rezwana-karim-snigdha.html","http://www.northsouth.edu/faculty-members/shss/pss/dr.-kabir-m-ashraf-alam.html","http://www.northsouth.edu/faculty-members/shss/pss/shakil-ahmed.html","http://www.northsouth.edu/faculty-members/shss/pss/mohammad-ashraful-haque.html","http://www.northsouth.edu/faculty-members/shss/pss/kazi.-n.-h.-haque.html","http://www.northsouth.edu/faculty-members/shss/pss/azmat-ara-ahmad.html","http://www.northsouth.edu/faculty-members/shss/pss/farhana-sultana.html","http://www.northsouth.edu/faculty-members/shss/pss/shamir-shehab-ssb1.html","http://www.northsouth.edu/faculty-members/shss/pss/salman-haider.html","http://www.northsouth.edu/faculty-members/shss/pss/maroof-mohsin.html","http://www.northsouth.edu/faculty-members/shss/pss/shehreen-amin-bhuiyan.html","http://www.northsouth.edu/faculty-members/shss/pss/shahla-shahnaz-dyuti.html","http://www.northsouth.edu/faculty-members/shss/pss/ahnaf-ashiqur-rahman.html","http://www.northsouth.edu/faculty-members/shss/pss/farin-shabnam-ritu.html"]
def get_p_and_s_faculty_details(url_p_and_s):
    request_web_page = requests.get(url_p_and_s)

    soup = BeautifulSoup(request_web_page.text, 'html.parser')
    # print(soup)

    name = soup.find_all('h2', class_="title")
    faculty_name = name[0].text
    print(faculty_name)

    p = soup.find('div', class_="col-md-3")
    try:
        q = p.find_all('img')
        link = "http://www.northsouth.edu" + q[0]['src'][0:]
        link2 = "http://www.northsouth.edu/" + q[0]['src'][0:]
        link3 = q[0]['src'][0:]
    except:
        link = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
        link2 = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
        link3 = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
    try:
        # Either you make a directory
        os.mkdir(os.path.join(os.getcwd(), 'Images'))
    except:
        pass
    # Or write to an existing one
    os.chdir(os.path.join(os.getcwd(), 'Images'))

    try:
        with open(faculty_name + '.jpeg', 'wb') as f:
            try:
                im = requests.get(link)
                f.write(im.content)
            except:
                im = requests.get(link2)
                f.write(im.content)
                pass
            try:
                im = requests.get(link3)
                f.write(im.content)
            except:
                pass
    except:
        pass

    email = soup.find("td")
    try:
        x = email.find_all("p")
    except:
        x = ""
        pass

    i = 0
    y = []
    for a in range(len(x)):
        j = x[i].text
        y.append(j)
        i = i + 1;
    y = str(y)

    # Regex generator link
    # https://regex-generator.olafneumann.org/?sampleText=%2B880-2-55668200%20Ext%3A%201072&flags=i
    faculty_email = str(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", y))[2:-2]
    print(faculty_email)

    faculty_numb = str(re.findall(r"\+880-\d-[0-9]+.*Ext.*\d\d\d\d", y))[2:28]
    faculty_numb = faculty_numb.replace("'", "")
    faculty_numb = faculty_numb.replace("]", "")
    faculty_numb = faculty_numb.replace("/", "")
    print((faculty_numb))

    if faculty_numb == "" :
        if faculty_email == "" :
            email = soup.find_all("td")
            try:
                x = email[3].find_all("strong")
            except:
                x = ""
                pass

            i = 0
            y = []
            for a in range(len(x)):
                j = x[i].text
                y.append(j)
                i = i + 1;
            y = str(y)

            # Regex generator link
            # https://regex-generator.olafneumann.org/?sampleText=%2B880-2-55668200%20Ext%3A%201072&flags=i
            faculty_email = str(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", y))[2:-2]
            print(faculty_email)

            faculty_numb = str(re.findall(r"\+880-\d-[0-9]+.*Ext.*\d\d\d\d", y))[2:28]
            faculty_numb = faculty_numb.replace("'", "")
            faculty_numb = faculty_numb.replace("]", "")
            faculty_numb = faculty_numb.replace("/", "")
            print((faculty_numb))


    dept = "Political Science and Sociology"

    return faculty_name, faculty_email, faculty_numb, dept


#For the Law Department
#For the Law Department
#For the Law Department
url_Law = ["http://www.northsouth.edu/faculty-members/shss/law/dr.-md.-rizwanul-islam.html","http://www.northsouth.edu/faculty-members/shss/law/abu.ali.html","http://www.northsouth.edu/faculty-members/shss/law/ishtiaque.ahmed.html","http://www.northsouth.edu/faculty-members/shss/law/md.-rajab-ali.html","http://www.northsouth.edu/faculty-members/shss/law/arafat.khan.html","http://www.northsouth.edu/faculty-members/shss/law/nasmin-jabin-noor.html","http://www.northsouth.edu/faculty-members/shss/law/arf-2.html","http://www.northsouth.edu/faculty-members/shss/law/saquib.rahman.html","http://www.northsouth.edu/faculty-members/shss/law/sharaban.zaman.html","http://www.northsouth.edu/faculty-members/shss/law/nafiz-ahmed.html","http://www.northsouth.edu/faculty-members/shss/law/tasnim-hasan-saara.html","http://www.northsouth.edu/faculty-members/shss/law/md.-abdul-wahhab-miah.html","http://www.northsouth.edu/faculty-members/shss/law/dr-sarkar-ali-akkas.html","http://www.northsouth.edu/faculty-members/shss/law/dr.-mohammad-nakib-nasrullah.html","http://www.northsouth.edu/faculty-members/shss/law/k-m-shazzad-mohashin.html","http://www.northsouth.edu/faculty-members/shss/law/barrister-a.m.-masum.html","http://www.northsouth.edu/faculty-members/shss/law/abu-sufian-md.-noman.html","http://www.northsouth.edu/faculty-members/shss/law/tasnuva-tabassum-ratry.html","http://www.northsouth.edu/faculty-members/shss/law/barrister-kazi-tamrin-rashed.html","http://www.northsouth.edu/faculty-members/shss/law/effat-sharmin.html","http://www.northsouth.edu/faculty-members/shss/law/md.-mostafizur-rahman-mzr2.html","http://www.northsouth.edu/faculty-members/shss/law/antara-tasmeen-att.html","http://www.northsouth.edu/faculty-members/shss/law/barrister-ishtiak-abdullah-ibd.html","http://www.northsouth.edu/faculty-members/shss/law/meem-sanjana-shah.html"]
def get_law_faculty_details(url_Law):
    request_web_page = requests.get(url_Law)

    soup = BeautifulSoup(request_web_page.text, 'html.parser')
    # print(soup)

    name = soup.find_all('h2', class_="title")
    faculty_name = name[0].text
    print(faculty_name)

    p = soup.find('div', class_="col-md-3")
    try:
        q = p.find_all('img')
        link = "http://www.northsouth.edu" + q[0]['src'][0:]
        link2 = "http://www.northsouth.edu/" + q[0]['src'][0:]
        link3 = q[0]['src'][0:]
    except:
        link = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
        link2 = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
        link3 = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
    try:
        # Either you make a directory
        os.mkdir(os.path.join(os.getcwd(), 'Images'))
    except:
        pass
    # Or write to an existing one
    os.chdir(os.path.join(os.getcwd(), 'Images'))

    try:
        with open(faculty_name + '.jpeg', 'wb') as f:
            try:
                im = requests.get(link)
                f.write(im.content)
            except:
                im = requests.get(link2)
                f.write(im.content)
                pass
            try:
                im = requests.get(link3)
                f.write(im.content)
            except:
                pass
    except:
        pass

    email = soup.find("td")
    try:
        x = email.find_all("p")
    except:
        x = ""
        pass

    i = 0
    y = []
    for a in range(len(x)):
        j = x[i].text
        y.append(j)
        i = i + 1;
    y = str(y)

    # Regex generator link
    # https://regex-generator.olafneumann.org/?sampleText=%2B880-2-55668200%20Ext%3A%201072&flags=i
    faculty_email = str(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", y))[2:-2]
    print(faculty_email)

    faculty_numb = str(re.findall(r"\+880-\d-[0-9]+.*Ext.*\d\d\d\d", y))[2:28]
    faculty_numb = faculty_numb.replace("'", "")
    faculty_numb = faculty_numb.replace("]", "")
    faculty_numb = faculty_numb.replace("/", "")
    print((faculty_numb))

    if faculty_numb == "" :
        if faculty_email == "" :
            email = soup.find_all("td")
            try:
                x = email[3].find_all("strong")
            except:
                x = ""
                pass

            i = 0
            y = []
            for a in range(len(x)):
                j = x[i].text
                y.append(j)
                i = i + 1;
            y = str(y)

            # Regex generator link
            # https://regex-generator.olafneumann.org/?sampleText=%2B880-2-55668200%20Ext%3A%201072&flags=i
            faculty_email = str(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", y))[2:-2]
            print(faculty_email)

            faculty_numb = str(re.findall(r"\+880-\d-[0-9]+.*Ext.*\d\d\d\d", y))[2:28]
            faculty_numb = faculty_numb.replace("'", "")
            faculty_numb = faculty_numb.replace("]", "")
            faculty_numb = faculty_numb.replace("/", "")
            print((faculty_numb))


    dept = "Law"

    return faculty_name, faculty_email, faculty_numb, dept


#For the History and Philosophy Department
#For the History and Philosophy Department
#For the History and Philosophy Department
url_h_and_p = ["http://www.northsouth.edu/faculty-members/shss/history-philosophy/dr-emdadul.haq.html","http://www.northsouth.edu/faculty-members/shss/history-philosophy/sharifuddin.ahmed.html","http://www.northsouth.edu/faculty-members/shss/history-philosophy/norman.swazo.html","http://www.northsouth.edu/faculty-members/shss/history-philosophy/dr.-zerina-shabnaz-akkas.html","http://www.northsouth.edu/faculty-members/shss/history-philosophy/muhammad.basar.html","http://www.northsouth.edu/faculty-members/shss/history-philosophy/ashma-rahman.html","http://www.northsouth.edu/faculty-members/shss/history-philosophy/najiyah-afrin-khan.html","http://www.northsouth.edu/faculty-members/shss/history-philosophy/fahria-karim.html","http://www.northsouth.edu/faculty-members/shss/history-philosophy/md.-ezazul-karim.html","http://www.northsouth.edu/faculty-members/shss/history-philosophy/marzan-bintey-kamal.html"]
def get_h_and_p_faculty_details(url_h_and_p):
    request_web_page = requests.get(url_h_and_p)

    soup = BeautifulSoup(request_web_page.text, 'html.parser')
    # print(soup)

    name = soup.find_all('h2', class_="title")
    faculty_name = name[0].text
    print(faculty_name)

    p = soup.find('div', class_="col-md-3")
    try:
        q = p.find_all('img')
        link = "http://www.northsouth.edu" + q[0]['src'][0:]
        link2 = "http://www.northsouth.edu/" + q[0]['src'][0:]
        link3 = q[0]['src'][0:]
    except:
        link = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
        link2 = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
        link3 = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
    try:
        # Either you make a directory
        os.mkdir(os.path.join(os.getcwd(), 'Images'))
    except:
        pass
    # Or write to an existing one
    os.chdir(os.path.join(os.getcwd(), 'Images'))

    try:
        with open(faculty_name + '.jpeg', 'wb') as f:
            try:
                im = requests.get(link)
                f.write(im.content)
            except:
                im = requests.get(link2)
                f.write(im.content)
                pass
            try:
                im = requests.get(link3)
                f.write(im.content)
            except:
                pass
    except:
        pass

    email = soup.find("td")
    try:
        x = email.find_all("p")
    except:
        x = ""
        pass

    i = 0
    y = []
    for a in range(len(x)):
        j = x[i].text
        y.append(j)
        i = i + 1;
    y = str(y)

    # Regex generator link
    # https://regex-generator.olafneumann.org/?sampleText=%2B880-2-55668200%20Ext%3A%201072&flags=i
    faculty_email = str(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", y))[2:-2]
    print(faculty_email)

    faculty_numb = str(re.findall(r"\+880-\d-[0-9]+.*Ext.*\d\d\d\d", y))[2:28]
    faculty_numb = faculty_numb.replace("'", "")
    faculty_numb = faculty_numb.replace("]", "")
    faculty_numb = faculty_numb.replace("/", "")
    print((faculty_numb))

    if faculty_numb == "" :
        if faculty_email == "" :
            email = soup.find_all("td")
            try:
                x = email[3].find_all("strong")
            except:
                x = ""
                pass

            i = 0
            y = []
            for a in range(len(x)):
                j = x[i].text
                y.append(j)
                i = i + 1;
            y = str(y)

            # Regex generator link
            # https://regex-generator.olafneumann.org/?sampleText=%2B880-2-55668200%20Ext%3A%201072&flags=i
            faculty_email = str(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", y))[2:-2]
            print(faculty_email)

            faculty_numb = str(re.findall(r"\+880-\d-[0-9]+.*Ext.*\d\d\d\d", y))[2:28]
            faculty_numb = faculty_numb.replace("'", "")
            faculty_numb = faculty_numb.replace("]", "")
            faculty_numb = faculty_numb.replace("/", "")
            print((faculty_numb))


    dept = "History and Philosophy"

    return faculty_name, faculty_email, faculty_numb, dept



#For the Biochemistry and Microbiology Department
#For the Biochemistry and Microbiology Department
#For the Biochemistry and Microbiology Department
url_b_and_m = ["http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/klq.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/dr.-kazi-nadim-hasan-knh.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/sdl.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/dr.-nayeema-bulbul.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/jsj.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/muktadir-shahid-hossain.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/chaman.keya.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/dr.-md.-mainul-hossain-mh1.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/muhammad.maqsud.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/dr.-sabbir-rahman-shuvo.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/dr.-fariza-shams-fss1.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/ishrat.jabeen.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/md.-fakruddin.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/dr.-mohammed-kabir-uddin.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/sayad-md.-didarul-alam.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/dr.-s-m-bakhtiar-ul-islam.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/ahmed-ishtiaque.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/mahjabeen-hossain.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/fatimah-az-zahra.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/fahd-bin-zahed.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/kazi-fahmida-rahman.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/shafia-tasnim-khan.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/kazi-samia-pial.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/preyanka-nath.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/nusrat-zahan-rouf.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/dr.-s-m-mostafa-kamal-khan.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/zaied-ahmed-bhuyan.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/sfa2.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/muntahi-mourin.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/abhinandan.chowdhury.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/aurchie-rahman.html","http://www.northsouth.edu/faculty-members/shls/biochemistry-microbiology/habibur.rahaman.html"]
def get_b_and_m_faculty_details(url_b_and_m):
    request_web_page = requests.get(url_b_and_m)

    soup = BeautifulSoup(request_web_page.text, 'html.parser')
    # print(soup)

    name = soup.find_all('h2', class_="title")
    faculty_name = name[0].text
    print(faculty_name)

    p = soup.find('div', class_="col-md-3")
    try:
        q = p.find_all('img')
        link = "http://www.northsouth.edu" + q[0]['src'][0:]
        link2 = "http://www.northsouth.edu/" + q[0]['src'][0:]
        link3 = q[0]['src'][0:]
    except:
        link = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
        link2 = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
        link3 = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
    try:
        # Either you make a directory
        os.mkdir(os.path.join(os.getcwd(), 'Images'))
    except:
        pass
    # Or write to an existing one
    os.chdir(os.path.join(os.getcwd(), 'Images'))

    try:
        with open(faculty_name + '.jpeg', 'wb') as f:
            try:
                im = requests.get(link)
                f.write(im.content)
            except:
                im = requests.get(link2)
                f.write(im.content)
                pass
            try:
                im = requests.get(link3)
                f.write(im.content)
            except:
                pass
    except:
        pass

    email = soup.find("td")
    try:
        x = email.find_all("p")
    except:
        x = ""
        pass

    i = 0
    y = []
    for a in range(len(x)):
        j = x[i].text
        y.append(j)
        i = i + 1;
    y = str(y)

    # Regex generator link
    # https://regex-generator.olafneumann.org/?sampleText=%2B880-2-55668200%20Ext%3A%201072&flags=i
    faculty_email = str(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", y))[2:-2]
    print(faculty_email)

    faculty_numb = str(re.findall(r"\+880-\d-[0-9]+.*Ext.*\d\d\d\d", y))[2:28]
    faculty_numb = faculty_numb.replace("'", "")
    faculty_numb = faculty_numb.replace("]", "")
    faculty_numb = faculty_numb.replace("/", "")
    print((faculty_numb))

    if faculty_numb == "" :
        if faculty_email == "" :
            email = soup.find_all("td")
            try:
                x = email[3].find_all("strong")
            except:
                x = ""
                pass

            i = 0
            y = []
            for a in range(len(x)):
                j = x[i].text
                y.append(j)
                i = i + 1;
            y = str(y)

            # Regex generator link
            # https://regex-generator.olafneumann.org/?sampleText=%2B880-2-55668200%20Ext%3A%201072&flags=i
            faculty_email = str(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", y))[2:-2]
            print(faculty_email)

            faculty_numb = str(re.findall(r"\+880-\d-[0-9]+.*Ext.*\d\d\d\d", y))[2:28]
            faculty_numb = faculty_numb.replace("'", "")
            faculty_numb = faculty_numb.replace("]", "")
            faculty_numb = faculty_numb.replace("/", "")
            print((faculty_numb))


    dept = "Biochemistry and Microbiology"

    return faculty_name, faculty_email, faculty_numb, dept



#For the Environmental Science and Management Department
#For the Environmental Science and Management Department
#For the Environmental Science and Management Department
url_e_and_m = ["http://www.northsouth.edu/faculty-members/shls/esm/md.jakariya.html","http://www.northsouth.edu/faculty-members/shls/esm/biswas.farhana.html","http://www.northsouth.edu/faculty-members/shls/esm/nahar.kamrun.html","http://www.northsouth.edu/faculty-members/shls/esm/dr.-firoz-khan/","http://www.northsouth.edu/faculty-members/shls/esm/mdo.html","http://www.northsouth.edu/faculty-members/shls/esm/smo.html","http://www.northsouth.edu/faculty-members/shls/esm/dr.-mohammad-sujauddin-sud.html","http://www.northsouth.edu/faculty-members/shls/esm/md.-shawkatislam-sohel.html","http://www.northsouth.edu/faculty-members/shls/esm/tahmid-huq-easher-the.html","http://www.northsouth.edu/faculty-members/shls/esm/rbr.html","http://www.northsouth.edu/faculty-members/shls/esm/nnz2.html","http://www.northsouth.edu/faculty-members/shls/esm/haniyum-maria-khan.html","http://www.northsouth.edu/faculty-members/shls/esm/sheikh-samanin-tasnim.html"]
def get_e_and_m_faculty_details(url_e_and_m):
    request_web_page = requests.get(url_e_and_m)

    soup = BeautifulSoup(request_web_page.text, 'html.parser')
    # print(soup)

    name = soup.find_all('h2', class_="title")
    faculty_name = name[0].text
    print(faculty_name)

    p = soup.find('div', class_="col-md-3")
    try:
        q = p.find_all('img')
        link = "http://www.northsouth.edu" + q[0]['src'][0:]
        link2 = "http://www.northsouth.edu/" + q[0]['src'][0:]
        link3 = q[0]['src'][0:]
    except:
        link = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
        link2 = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
        link3 = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
    try:
        # Either you make a directory
        os.mkdir(os.path.join(os.getcwd(), 'Images'))
    except:
        pass
    # Or write to an existing one
    os.chdir(os.path.join(os.getcwd(), 'Images'))

    try:
        with open(faculty_name + '.jpeg', 'wb') as f:
            try:
                im = requests.get(link)
                f.write(im.content)
            except:
                im = requests.get(link2)
                f.write(im.content)
                pass
            try:
                im = requests.get(link3)
                f.write(im.content)
            except:
                pass
    except:
        pass

    email = soup.find("td")
    try:
        x = email.find_all("p")
    except:
        x = ""
        pass

    i = 0
    y = []
    for a in range(len(x)):
        j = x[i].text
        y.append(j)
        i = i + 1;
    y = str(y)

    # Regex generator link
    # https://regex-generator.olafneumann.org/?sampleText=%2B880-2-55668200%20Ext%3A%201072&flags=i
    faculty_email = str(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", y))[2:-2]
    print(faculty_email)

    faculty_numb = str(re.findall(r"\+880-\d-[0-9]+.*Ext.*\d\d\d\d", y))[2:28]
    faculty_numb = faculty_numb.replace("'", "")
    faculty_numb = faculty_numb.replace("]", "")
    faculty_numb = faculty_numb.replace("/", "")
    print((faculty_numb))

    if faculty_numb == "" :
        if faculty_email == "" :
            email = soup.find_all("td")
            try:
                x = email[3].find_all("strong")
            except:
                x = ""
                pass

            i = 0
            y = []
            for a in range(len(x)):
                j = x[i].text
                y.append(j)
                i = i + 1;
            y = str(y)

            # Regex generator link
            # https://regex-generator.olafneumann.org/?sampleText=%2B880-2-55668200%20Ext%3A%201072&flags=i
            faculty_email = str(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", y))[2:-2]
            print(faculty_email)

            faculty_numb = str(re.findall(r"\+880-\d-[0-9]+.*Ext.*\d\d\d\d", y))[2:28]
            faculty_numb = faculty_numb.replace("'", "")
            faculty_numb = faculty_numb.replace("]", "")
            faculty_numb = faculty_numb.replace("/", "")
            print((faculty_numb))


    dept = "Environmental Science and Management"

    return faculty_name, faculty_email, faculty_numb, dept


#For the Pharmaceutical Sciences Department
#For the Pharmaceutical Sciences Department
#For the Pharmaceutical Sciences Department
url_p = ["http://www.northsouth.edu/faculty-members/shls/pharmacy/dr.-hasan-mahmud-reza.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/preeti.jain.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/nurul.islam.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/mna.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/dr.-g.-m.-sayedur-rahman.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/asim.bepari.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/dr.-md.-ashraful-alam.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/mahbubur.rahman.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/murad.hossain.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/nusrat.subhan.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/khondker-ayesha-akter.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/manik-chandra-shill.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/ferdous-khan.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/sms3.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/ashrafur-rahman.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/dr.-md.-hasanuzzaman-shohag-mhs3.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/dr.-abdullah-al-masum-aas.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/rezwana-ahmed.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/mohammad.uddin.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/dr.-md-ariful-islam.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/md-shaki-mostaid.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/dr.-md.-mazharul-islam-chowdhury.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/tahmina.yasmin.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/adit.pavel.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/paromita-islam.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/nusrat-hossain.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/ms.-zarin-tasnim-gias-ztg.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/sadia-shabnam.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/sabrin-islam-khan.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/tabinda-islam.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/farah-ahmed.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/javed-ibne-hasan.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/md.-zahidul-islam-zahid.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/junayet-khan.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/sadia-kamal.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/anika-tabassum-bristy.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/rsw.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/a.-f.-m.-towheedur-rahman.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/isha.khan.html","http://www.northsouth.edu/faculty-members/shls/pharmacy/nadia-saffoon.html"]
def get_p_faculty_details(url_p):
    request_web_page = requests.get(url_p)

    soup = BeautifulSoup(request_web_page.text, 'html.parser')
    # print(soup)

    name = soup.find_all('h2', class_="title")
    faculty_name = name[0].text
    print(faculty_name)

    p = soup.find('div', class_="col-md-3")
    try:
        q = p.find_all('img')
        link = "http://www.northsouth.edu" + q[0]['src'][0:]
        link2 = "http://www.northsouth.edu/" + q[0]['src'][0:]
        link3 = q[0]['src'][0:]
    except:
        link = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
        link2 = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
        link3 = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
    try:
        # Either you make a directory
        os.mkdir(os.path.join(os.getcwd(), 'Images'))
    except:
        pass
    # Or write to an existing one
    os.chdir(os.path.join(os.getcwd(), 'Images'))

    try:
        with open(faculty_name + '.jpeg', 'wb') as f:
            try:
                im = requests.get(link)
                f.write(im.content)
            except:
                im = requests.get(link2)
                f.write(im.content)
                pass
            try:
                im = requests.get(link3)
                f.write(im.content)
            except:
                pass
    except:
        pass

    email = soup.find("td")
    try:
        x = email.find_all("p")
    except:
        x = ""
        pass

    i = 0
    y = []
    for a in range(len(x)):
        j = x[i].text
        y.append(j)
        i = i + 1;
    y = str(y)

    # Regex generator link
    # https://regex-generator.olafneumann.org/?sampleText=%2B880-2-55668200%20Ext%3A%201072&flags=i
    faculty_email = str(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", y))[2:-2]
    print(faculty_email)

    faculty_numb = str(re.findall(r"\+880-\d-[0-9]+.*Ext.*\d\d\d\d", y))[2:28]
    faculty_numb = faculty_numb.replace("'", "")
    faculty_numb = faculty_numb.replace("]", "")
    faculty_numb = faculty_numb.replace("/", "")
    print((faculty_numb))

    if faculty_numb == "" :
        if faculty_email == "" :
            email = soup.find_all("td")
            try:
                x = email[3].find_all("strong")
            except:
                x = ""
                pass

            i = 0
            y = []
            for a in range(len(x)):
                j = x[i].text
                y.append(j)
                i = i + 1;
            y = str(y)

            # Regex generator link
            # https://regex-generator.olafneumann.org/?sampleText=%2B880-2-55668200%20Ext%3A%201072&flags=i
            faculty_email = str(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", y))[2:-2]
            print(faculty_email)

            faculty_numb = str(re.findall(r"\+880-\d-[0-9]+.*Ext.*\d\d\d\d", y))[2:28]
            faculty_numb = faculty_numb.replace("'", "")
            faculty_numb = faculty_numb.replace("]", "")
            faculty_numb = faculty_numb.replace("/", "")
            print((faculty_numb))


    dept = "Pharmaceutical Sciences"

    return faculty_name, faculty_email, faculty_numb, dept


#For the Public Health Department
#For the Public Health Department
#For the Public Health Department
url_pbh = ["http://www.northsouth.edu/faculty-members/shls/pbh/gias.ahsan.html","http://www.northsouth.edu/faculty-members/shls/pbh/dr.-dipak-kumar-mitra.html","http://www.northsouth.edu/faculty-members/shls/pbh/dr.-ahmed-hossain.html","http://www.northsouth.edu/faculty-members/shls/pbh/mohammad-delwer-hossain-hawlader.html","http://www.northsouth.edu/faculty-members/shls/pbh/dr.-nadira-sultana-kakoly-nsk.html","http://www.northsouth.edu/faculty-members/shls/pbh/azaz-bin-sharif.html","http://www.northsouth.edu/faculty-members/shls/pbh/htn.html","http://www.northsouth.edu/faculty-members/shls/pbh/ms.-shahnaz-parveen.html","http://www.northsouth.edu/faculty-members/shls/pbh/dr.-afrin-ahmed-clara.html","http://www.northsouth.edu/faculty-members/shls/pbh/ms.-sadia-chowdhury-scw.html","http://www.northsouth.edu/faculty-members/shls/pbh/s-mahmud-mishu.html","http://www.northsouth.edu/faculty-members/shls/pbh/fouzia-khanam.html","http://www.northsouth.edu/faculty-members/shls/pbh/dr.-md.-imteaz-mahmud.html","http://www.northsouth.edu/faculty-members/shls/pbh/shaikh.salam.html","http://www.northsouth.edu/faculty-members/shls/pbh/nandeeta-samad.html","http://www.northsouth.edu/faculty-members/shls/pbh/arif.chowdhury.html","http://www.northsouth.edu/faculty-members/shls/pbh/yamin-tauseef-jahangir.html","http://www.northsouth.edu/faculty-members/shls/pbh/mr.-samiul-hossain.html","http://www.northsouth.edu/faculty-members/shls/pbh/ms.-segufta-dilshad.html","http://www.northsouth.edu/faculty-members/shls/pbh/juwel-rana.html","http://www.northsouth.edu/faculty-members/shls/pbh/sabrina-binte-haque.html"]
def get_pbh_faculty_details(url_pbh):
    request_web_page = requests.get(url_pbh)

    soup = BeautifulSoup(request_web_page.text, 'html.parser')
    # print(soup)

    name = soup.find_all('h2', class_="title")
    faculty_name = name[0].text
    print(faculty_name)

    p = soup.find('div', class_="col-md-3")
    try:
        q = p.find_all('img')
        link = "http://www.northsouth.edu" + q[0]['src'][0:]
        link2 = "http://www.northsouth.edu/" + q[0]['src'][0:]
        link3 = q[0]['src'][0:]
    except:
        link = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
        link2 = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
        link3 = "http://www.northsouth.edu/newassets/images/5-8524.female-faculty-image.jpg"
    try:
        # Either you make a directory
        os.mkdir(os.path.join(os.getcwd(), 'Images'))
    except:
        pass
    # Or write to an existing one
    os.chdir(os.path.join(os.getcwd(), 'Images'))

    try:
        with open(faculty_name + '.jpeg', 'wb') as f:
            try:
                im = requests.get(link)
                f.write(im.content)
            except:
                im = requests.get(link2)
                f.write(im.content)
                pass
            try:
                im = requests.get(link3)
                f.write(im.content)
            except:
                pass
    except:
        pass

    email = soup.find("td")
    try:
        x = email.find_all("p")
    except:
        x = ""
        pass

    i = 0
    y = []
    for a in range(len(x)):
        j = x[i].text
        y.append(j)
        i = i + 1;
    y = str(y)

    # Regex generator link
    # https://regex-generator.olafneumann.org/?sampleText=%2B880-2-55668200%20Ext%3A%201072&flags=i
    faculty_email = str(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", y))[2:-2]
    print(faculty_email)

    faculty_numb = str(re.findall(r"\+880-\d-[0-9]+.*Ext.*\d\d\d\d", y))[2:28]
    faculty_numb = faculty_numb.replace("'", "")
    faculty_numb = faculty_numb.replace("]", "")
    faculty_numb = faculty_numb.replace("/", "")
    print((faculty_numb))

    if faculty_numb == "" :
        if faculty_email == "" :
            email = soup.find_all("td")
            try:
                x = email[3].find_all("strong")
            except:
                x = ""
                pass

            i = 0
            y = []
            for a in range(len(x)):
                j = x[i].text
                y.append(j)
                i = i + 1;
            y = str(y)

            # Regex generator link
            # https://regex-generator.olafneumann.org/?sampleText=%2B880-2-55668200%20Ext%3A%201072&flags=i
            faculty_email = str(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", y))[2:-2]
            print(faculty_email)

            faculty_numb = str(re.findall(r"\+880-\d-[0-9]+.*Ext.*\d\d\d\d", y))[2:28]
            faculty_numb = faculty_numb.replace("'", "")
            faculty_numb = faculty_numb.replace("]", "")
            faculty_numb = faculty_numb.replace("/", "")
            print((faculty_numb))


    dept = "Public Health"

    return faculty_name, faculty_email, faculty_numb, dept



def write_data() :
    os.chdir(d)
    info = [faculty_name, faculty_email, faculty_numb, dept]
    thewriter.writerow(info)

with open('Faculty Database.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Name', 'Email' , 'Phone' , 'Department']
    thewriter.writerow(header)

    #For the ece department
    i = 0
    for x in range(len(url_ece)):
        faculty_name , faculty_email ,faculty_numb ,dept = get_ece_faculty_details(url_ece[i])
        print(i)
        i = i + 1;
        write_data()

    #For the Accounts and Finance Department
    i = 0
    for x in range(len(url_af)):
        faculty_name, faculty_email, faculty_numb, dept = get_accounts_and_finance_faculty_details(url_af[i])
        print(i)
        i = i + 1;
        write_data()

    ## For the Economics Department
    i = 0
    for x in range(len(url_eco)):
       faculty_name, faculty_email, faculty_numb, dept = get_eco_faculty_details(url_eco[i])
       print(i)
       i = i + 1;
       write_data()

    # For the Management Department
    i = 0
    for x in range(len(url_manage)):
        faculty_name, faculty_email, faculty_numb, dept = get_management_faculty_details(url_manage[i])
        print(i)
        i = i + 1;
        write_data()

    #For the Market and International Business Department
    i = 0
    for x in range(len(url_m_and_i)):
       faculty_name, faculty_email, faculty_numb, dept = get_m_and_i_faculty_details(url_m_and_i[i])
       print(i)
       i = i + 1;
       write_data()

    # For the Architecture Department
    i = 0
    for x in range(len(url_archi)):
        faculty_name, faculty_email, faculty_numb, dept = get_archi_faculty_details(url_archi[i])
        print(i)
        i = i + 1;
        write_data()

    # For the Mathematics and Physics Department
    i = 0
    for x in range(len(url_m_and_p)):
      faculty_name, faculty_email, faculty_numb, dept = get_m_and_p_faculty_details(url_m_and_p[i])
      print(i)
      i = i + 1;
      write_data()

    # For the English and Modern Language Department
    i = 0
    for x in range(len(url_e_and_ml)):
      faculty_name, faculty_email, faculty_numb, dept = get_e_and_ml_faculty_details(url_e_and_ml[i])
      print(i)
      i = i + 1;
      write_data()

    # For the Political Science and Sociology Department
    i = 0
    for x in range(len(url_p_and_s)):
      faculty_name, faculty_email, faculty_numb, dept = get_p_and_s_faculty_details(url_p_and_s[i])
      print(i)
      i = i + 1;
      write_data()

    # For the Law Department
    i = 0
    for x in range(len(url_Law)):
      faculty_name, faculty_email, faculty_numb, dept = get_law_faculty_details(url_Law[i])
      print(i)
      i = i + 1;
      write_data()

    # For the History and Philosophy Department
    i = 0
    for x in range(len(url_h_and_p)):
      faculty_name, faculty_email, faculty_numb, dept = get_h_and_p_faculty_details(url_h_and_p[i])
      print(i)
      i = i + 1;
      write_data()

    # For the Biochemistry and Microbiology Department
    i = 0
    for x in range(len(url_b_and_m)):
      faculty_name, faculty_email, faculty_numb, dept = get_b_and_m_faculty_details(url_b_and_m[i])
      print(i)
      i = i + 1;
      write_data()

    # For the Environmental Science and Management Department
    i = 0
    for x in range(len(url_e_and_m)):
      faculty_name, faculty_email, faculty_numb, dept = get_e_and_m_faculty_details(url_e_and_m[i])
      print(i)
      i = i + 1;
      write_data()

    # For the Pharmaceutical Sciences Department
    i = 0
    for x in range(len(url_p)):
      faculty_name, faculty_email, faculty_numb, dept = get_p_faculty_details(url_p[i])
      print(i)
      i = i + 1;
      write_data()

    # For the Public Health Department
    i = 0
    for x in range(len(url_pbh)):
      faculty_name, faculty_email, faculty_numb, dept = get_pbh_faculty_details(url_pbh[i])
      print(i)
      i = i + 1;
      write_data()


import Student











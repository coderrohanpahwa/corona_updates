from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
while True:
    def notifyMe(title,message):
        notification.notify(
            title=title,
            message=message,
            app_icon=None,
            timeout=9)
    def getData(url):
        r=requests.get(url)
        return r.text
    if __name__=="__main__":
        #notifyMe("Rohan","HI")
        myHtmlData=getData('https://www.mohfw.gov.in/')
        #print(myHtmlData)
        soup=BeautifulSoup(myHtmlData,'html.parser')
        #print(soup.prettify())   
        myDataStr=""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            #print(tr.get_text())
            myDataStr +=tr.get_text()
            
        myDataStr=myDataStr[1:]
        itemList=myDataStr.split("\n\n")
        states=[]
        a=int(input("Enter number of states you want to enquire in "))
        i=0
        print("Enter 1 for Andhra Pradesh")
        print("Enter 2 for Andaman and Nicobar Islands")
        print("Enter 3 for Arunachal Pradesh")
        print("Enter 4 for Assam")
        print("Enter 5 for Bihar")
        print("Enter 6 for Chandigarh")
        print("Enter 7 for Chhattisgarh")
        print("Enter 8 for Delhi")
        print("Enter 9 for Goa")
        print("Enter 10 for Gujarat")
        print("Enter 11 for Haryana")
        print("Enter 12 for Himachal Pradesh")
        print("Enter 13 for Jammu and Kashmir")
        print("Enter 14 for Jharkhand")
        print("Enter 15 for Karnataka")
        print("Enter 16 for Kerala")
        print("Enter 17 for Ladakh")
        print("Enter 18 for Madhya Pradesh")
        print("Enter 19 for Maharashtra")
        print("Enter 20 for Manipur")
        print("Enter 21 for Mizoram")
        print("Enter 22 for Odisha")
        print("Enter 23 for Puducherry")
        print("Enter 24 for Punjab")
        print("Enter 25 for Rajasthan")
        print("Enter 26 for Tamil Nadu")
        print("Enter 27 for Telengana")
        print("Enter 28 for Tripura")
        print("Enter 29 for Uttarakhand")
        print("Enter 30 for Uttar Pradesh")
        print("Enter 31 for West Bengal")
        
        while i<a:
                b=int(input("Enter choice : "))
                if b==1:
                    c="Andhra Pradesh"
                    states.append(c)
                elif b==2:
                    c="Andaman and Nicobar Islands"
                    states.append(c)
                elif b==3:
                    c="Arunachal Pradesh"
                    states.append(c)
                elif b==4:
                    c="Assam"
                    states.append(c)
                elif b==5:
                    c="Bihar"
                    states.append(c)
                elif b==6:
                    c="Chandigarh"
                    states.append(c)
                elif b==7:
                    c="Chhattisgarh"
                    states.append(c)
                elif b==8:
                    c="Delhi"
                    states.append(c)
                elif b==9:
                    c="Goa"
                    states.append(c)
                elif b==10:
                    c="Gujarat"
                    states.append(c)
                elif b==11:
                    c="Haryana"
                    states.append(c)
                elif b==12:
                    c="Himachal Pradesh"
                    states.append(c)
                elif b==13:
                    c="Jammu and Kashmir"
                    states.append(c)
                elif b==14:
                    c="Jharkhand"
                    states.append(c)
                elif b==15:
                    c="Karnataka"
                    states.append(c)
                elif b==16:
                    c="Kerala"
                    states.append(c)
                elif b==17:
                    c="Ladakh"
                    states.append(c)
                elif b==18:
                    c="Madhya Pradesh"
                    states.append(c)
                elif b==19:
                    c="Maharashtra"
                    states.append(c)
                elif b==20:
                    c="Manipur"
                    states.append(c)
                elif b==21:
                    c="Mizoram"
                    states.append(c)
                elif b==22:
                    c="Odisha"
                    states.append(c)
                elif b==23:
                    c="Puducherry"
                    states.append(c)
                elif b==24:
                    c="Punjab"
                    states.append(c)
                elif b==25:
                    c="Rajasthan"
                    states.append(c)
                elif b==26:
                    c="Tamil Nadu"
                    states.append(c)
                elif b==27:
                    c="Telengana"
                    states.append(c)
                elif b==28:
                    c="Tripura"
                    states.append(c)
                elif b==29:
                    c="Uttarakhand"
                    states.append(c)
                elif b==30:
                    c="Uttar Pradesh"
                    states.append(c)
                elif b==31:
                    c="West Bengal"
                    states.append(c)
                else :
                    print("You have entered a wrong input. Kindly enter again from 1 to 31")
                    i=i-1
                i=i+1
        for item in itemList[0:31]:
            dataList=item.split('\n')
            if dataList[1] in states:
               print(dataList)
               nTitle='Cases of COVID-19'
               nText=f"State : {dataList[1]} \nIndian cases : {dataList[2]} \nForeign : {dataList[3]} \nCured : {dataList[4]}"
               notifyMe(nTitle,nText)
               time.sleep(2)
        time.sleep(60*60)
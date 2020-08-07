from selenium import webdriver
from time import sleep
from pyvirtualdisplay import Display
import sys, os
from googlesearch import search 


class forex:
    def __init__(self):
        print("""\033[1;33;40m
__        _______ _     ____ ___  __  __ _____   _____ ___  
\ \      / / ____| |   / ___/ _ \|  \/  | ____| |_   _/ _ \ 
 \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|     | || | | |
  \ V  V / | |___| |__| |__| |_| | |  | | |___    | || |_| |
   \_/\_/  |_____|_____\____\___/|_|  |_|_____|   |_| \___/ 
                                                            
 _     _____     _______   _____ ___  ____  _______  __
| |   |_ _\ \   / / ____| |  ___/ _ \|  _ \| ____\ \/ /
| |    | | \ \ / /|  _|   | |_ | | | | |_) |  _|  \  / 
| |___ | |  \ V / | |___  |  _|| |_| |  _ <| |___ /  \ 
|_____|___|  \_/  |_____| |_|   \___/|_| \_\_____/_/\_\
                                                       
 """)
        inp = input("Would you like to see news?(y/n)")
        if(inp == 'y'):
            print("Wait a second...")
            self.getNews()
        elif(inp == 'n'):
            print("Ok...")
            pass
        else:
            print("There is no option '{inp}'.")

        self.dolar = 0
        self.euro = 0
        self.grGold = 0
        self.sterlin = 0
        self.oldDolar = self.dolar
        self.oldEuro = self.euro
        self.oldGrGold = self.grGold
        self.oldSterlin = self.sterlin
        
        self.display = Display(visible=0, size=(800,600))
        self.display.start()

        self.driver = webdriver.Firefox()
        self.driver.get("https://doviz.com")
        self.getData()

    def getNews(self):
        query = ["Dolar", "Euro", "Sterlin", "Gram Altın"]
        for i in range(len(query)):
            print(f"\033[1;36;40m\n\n ----- {query[i]} Haberleri -----")
            for j in search(query[i], tld="com", num=10, stop=10, pause=2, country="tr"): 
                print(j)
        print("\n\n\n\n\n\n")

    def getData(self):
        try:
            self.dolar = self.driver.find_elements_by_xpath("/html/body/header/div[2]/div/div/div[2]/a/span[2]")[0].text.replace(',','.')
            self.euro = self.driver.find_elements_by_xpath("/html/body/header/div[2]/div/div/div[3]/a/span[2]")[0].text.replace(',','.')
            self.grGold = self.driver.find_elements_by_xpath("/html/body/header/div[2]/div/div/div[1]/a/span[2]")[0].text.replace(',','.')
            self.sterlin = self.driver.find_elements_by_xpath("/html/body/header/div[2]/div/div/div[5]/a/span[2]")[0].text.replace(',','.')

            if(float(self.dolar) > float(self.oldDolar)):
                dolarS = "\033[1;32;40m Dolar: "+self.dolar
            elif(float(self.dolar) < float(self.oldDolar)):
                dolarS = "\033[1;31;40m Dolar: "+self.dolar
            else:
                dolarS = "\033[1;33;40m Dolar: "+self.dolar
            
            if(float(self.euro) > float(self.oldEuro)):
                euroS = "\033[1;32;40m Euro: "+self.euro
            elif(float(self.euro) < float(self.oldEuro)):
                euroS = "\033[1;31;40m Euro: "+self.euro
            else:
                euroS = "\033[1;33;40m Euro: "+self.euro
            
            if(float(self.grGold) > float(self.oldGrGold)):
                grGolds = "\033[1;32;40m GrGold: "+self.grGold
            elif(float(self.grGold) < float(self.oldGrGold)):
                grGolds = "\033[1;31;40m GrGold: "+self.grGold
            else:
                grGolds = "\033[1;33;40m GrGold: "+self.grGold

            if(float(self.sterlin) > float(self.oldSterlin)):
                sterlinS = "\033[1;32;40m Sterlin: "+self.sterlin
            elif(float(self.sterlin) < float(self.oldSterlin)):
                sterlinS = "\033[1;31;40m Sterlin: "+self.sterlin
            else:
                sterlinS = "\033[1;33;40m Sterlin: "+self.sterlin

            print(dolarS,"\t",euroS,"\t", sterlinS,"\t", grGolds, end='\r')
            self.oldDolar = self.dolar
            self.oldEuro = self.euro
            self.oldGrGold = self.grGold
            self.oldSterlin = self.sterlin
            sleep(5)


            self.getData()

        except KeyboardInterrupt:
            print("\nBye!")
            self.driver.quit()
            self.display.stop()
            sys.exit()
program = forex()
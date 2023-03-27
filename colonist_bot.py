"""
Creator - Sagiv Antebi
"""
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys

"""
* class name: MainBot
* class Operation: main class of the bot
"""
class MainBot():
    def __init__(self):
        #The chrome web driver path
        self.driver = webdriver.Chrome('C:\\Users\\sagiv\\Desktop\\CandK_Colonist\\chromedriver')
        print("\n-------------------------------------------------------------")
        print("""\nＳａｇｉｖ Ａｎｔｅｂｉ － Ａｌｌ Ｒｉｇｈｔｓ Ｒｅｓｅｒｖｅｄ\n""")
        print("-------------------------------------------------------------\n")

    """
    * Function name: startDownload
    * Function Operation: start the download process
    """
    def startSearch(self,url):
        self.driver.get(url)
        action = ActionChains(self.driver)
        lobby_btn = self.driver.find_element("xpath", "/html/body/header/div[1]/div[1]/a[2]")
        sleep(2)
        lobby_btn.click()
        lobby_btn.click()
        lobby_btn.click()
        lobby_btn.click()
        lobby_btn.click()
        sleep(2)
        refresh_btn = self.driver.find_element("xpath","/html/body/div[2]/div[5]/div[2]/div[2]/div[2]/div/table[1]/thead/tr/th[4]/img")

        first_row_name = "None"
        sleep(1)
        while self.driver.current_url == url:
            sleep(1)
            try:
                refresh_btn.click()
                refresh_btn.click()
                sleep(1)
                first_row_name = self.driver.find_element("xpath","/html/body/div[2]/div[5]/div[2]/div[2]/div[2]/div/table[1]/tbody/tr[1]/td[1]").text
                if "Cities & Knights" in first_row_name:
                    first_row_btn = self.driver.find_element("xpath","/html/body/div[2]/div[5]/div[2]/div[2]/div[2]/div/table[1]/tbody/tr[1]")
                    first_row_btn.click()
                    first_row_btn.click()
                    sleep(2)
                    input_box = self.driver.find_element("xpath", "/html/body/div[2]/div[5]/div[3]/div[3]/form/input")
                    msg = "I'm a 20/20 Karma Player - I have trouble entering my main account today, I know how to play :)"
                    input_box.send_keys(msg)
                    sleep(1)
                    snd_btn = self.driver.find_element("xpath", "/html/body/div[2]/div[5]/div[3]/div[3]/form/button")
                    snd_btn.click()
                    snd_btn.click()
                    snd_btn.click()

                    submit_btn = self.driver.find_element("xpath","/html/body/div[2]/div[5]/div[3]/div[2]/div[3]/div[1]/input")
                    submit_btn.click()

                    msg = "For real lol"
                    input_box.send_keys(msg)
                    sleep(1)
                    snd_btn = self.driver.find_element("xpath","/html/body/div[2]/div[5]/div[3]/div[3]/form/button")
                    snd_btn.click()
                    snd_btn.click()
                    snd_btn.click()
                    sleep(8)
            except Exception:
                first_row_name = "None"




def main():
    #creating copy of the bot
    bot = MainBot()
    #start command to search
    bot.startSearch('https://colonist.io/')
    print("""
██████╗░░█████╗░███╗░░██╗███████╗██╗
██╔══██╗██╔══██╗████╗░██║██╔════╝██║
██║░░██║██║░░██║██╔██╗██║█████╗░░██║
██║░░██║██║░░██║██║╚████║██╔══╝░░╚═╝
██████╔╝╚█████╔╝██║░╚███║███████╗██╗
╚═════╝░░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝""")
    print("\n-------------------------------------------------------------")
    print("""\nＳａｇｉｖ Ａｎｔｅｂｉ － Ａｌｌ Ｒｉｇｈｔｓ Ｒｅｓｅｒｖｅｄ\n""")
    print("-------------------------------------------------------------\n")
    sleep(50)
    input("Press enter to exit ;)")

if __name__ == "__main__":
    main()

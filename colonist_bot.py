"""
Creator - Sagiv Antebi
"""
from selenium import webdriver
from time import sleep


"""
* class name: MainBot
* class Operation: main class of the bot
"""
class MainBot():
    def __init__(self):
        # Setting The Chrome web driver
        self.driver = webdriver.Chrome('chromedriver')
        print("\n-------------------------------------------------------------")
        print("""\nＳａｇｉｖ Ａｎｔｅｂｉ － Ａｌｌ Ｒｉｇｈｔｓ Ｒｅｓｅｒｖｅｄ\n""")
        print("-------------------------------------------------------------\n")

    """
    * Function name: write_msg
    * Function Operation: writing msg into chat
    * Param: msg - The message to send
    """
    def write_msg(self, msg):
        input_box = self.driver.find_element("xpath", "/html/body/div[2]/div[5]/div[3]/div[3]/form/input")
        input_box.send_keys(msg)
        sleep(1)
        snd_btn = self.driver.find_element("xpath", "/html/body/div[2]/div[5]/div[3]/div[3]/form/button")
        snd_btn.click()
        snd_btn.click()
        snd_btn.click()

    """
    * Function name: start_search
    * Function Operation: starting the search for a room
    * Param: url - The colonist url
    """
    def start_search(self, url):
        self.driver.get(url)
        lobby_btn = self.driver.find_element("xpath", "/html/body/header/div[1]/div[1]/a[2]")
        sleep(2)
        lobby_btn.click()
        lobby_btn.click()
        lobby_btn.click()
        lobby_btn.click()
        lobby_btn.click()
        sleep(1)
        refresh_btn = self.driver.find_element("xpath","/html/body/div[2]/div[5]/div[2]/div[2]/div[2]/div/table[1]/thead/tr/th[4]/img")
        first_row_name = "None"
        sleep(1)
        # Loop while the url is still on  the lobby
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
                    sleep(1)

                    msg = "I'm a 20/20 Karma Player - I have trouble entering my main account today, I know how to play :)"
                    self.write_msg(msg)

                    # The READY button
                    submit_btn_ready = self.driver.find_element("xpath","/html/body/div[2]/div[5]/div[3]/div[2]/div[3]/div[1]/input")
                    submit_btn_ready.click()
                    sleep(1)

                    msg = "For real lol"
                    self.write_msg(msg)

                    sleep(8)
            except Exception:
                first_row_name = "None"




def main():
    bot = MainBot()
    # Start command to search
    bot.start_search('https://colonist.io/')
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

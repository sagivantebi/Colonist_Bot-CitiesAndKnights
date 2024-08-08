from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

class MainBot():
    def __init__(self):
        # Setting the Chrome web driver with correct options
        chrome_options = Options()
        # chrome_options.add_argument("--disable-extensions")
        # chrome_options.add_argument("--disable-gpu")
        # chrome_options.add_argument("--no-sandbox") 
        # chrome_options.add_argument("--headless")  # Uncomment this line if you want to run Chrome in headless mode

        # Replace 'path/to/chromedriver' with the actual path to the ChromeDriver executable
        service = Service('chromedriver.exe')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        print("\n-------------------------------------------------------------")
        print("""\nＳａｇｉｖ Ａｎｔｅｂｉ － Ａｌｌ Ｒｉｇｈｔｓ Ｒｅｓｅｒｖｅｄ\n""")
        print("-------------------------------------------------------------\n")
    
    def write_msg(self, msg):
        try:
            print("Finding input box...")
            input_box = self.driver.find_element(By.XPATH, '//*[@id="lobby_chat_input"]')
            print("Input box found. Sending message...")
            input_box.send_keys(msg)
            sleep(1)

            print("Finding send button...")
            snd_btn = self.driver.find_element(By.XPATH, '//*[@id="lobby_chat_button"]')
            print("Send button found. Clicking send button...")
            snd_btn.click()
            print("Message sent.")
            sleep(1)
        except Exception as e:
            print(f"An error occurred in write_msg: {e}")

    def ensure_ready_button_pushed(self):
            try:
                ready_btn = self.driver.find_element(By.ID, 'room_center_checkbox_ready')
                if not ready_btn.is_selected():
                    print("Clicking the ready button...")
                    ready_btn.click()
                else:
                    print("Ready button is already clicked.")

                while True:
                    sleep(1)
                    if not ready_btn.is_selected():
                        print("Ready button is not selected. Clicking again...")
                        ready_btn.click()
                    else:
                        print("Ready button is still selected.")
            except Exception as e:
                print(f"An error occurred while ensuring the ready button is pushed: {e}")

    def start_search(self, url):
        self.driver.get(url)
        lobby_btn = self.driver.find_element(By.XPATH, "/html/body/header/div[1]/div[1]/a[2]")
        sleep(2)
        lobby_btn.click()
        lobby_btn.click()
        lobby_btn.click()
        lobby_btn.click()
        lobby_btn.click()
        sleep(1)
        # refresh_btn = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[5]/div[2]/div[2]/div[2]/div/table[1]/thead/tr/th[4]/img")
        sleep(1)
        loby_url = self.driver.current_url
        while self.driver.current_url == url:
            sleep(1)
            try:
                
                rows = self.driver.find_elements(By.XPATH, '//*[@id="lobby_center_rooms_table_body"]/tr')
                for row in rows:
                    row_name = row.find_element(By.XPATH, 'td[1]').text


                    if "Cities & Knights" in row_name:
                        row.click()
                        sleep(1)
                        self.ensure_ready_button_pushed()
                        sleep(8)
                        if self.driver.current_url == loby_url:
                            continue
                        else:
                            return
            except Exception as e:
                print(f"An error occurred: {e}")

def main():
    bot = MainBot()
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

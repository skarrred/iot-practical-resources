import time, datetime
import RPi.GPIO as GPIO
import telepo6t
from telepot.loop import MessageLoop
green = 31
yellow = 33

now = datetime.datetime.now()
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#LED Yellow
GPIO.setup(yellow, GPIO.OUT)
GPIO.output(yellow, 0) #Off initially

#LED green
GPIO.setup(green, GPIO.OUT)
GPIO.output(green, 0) #Off initially
def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print ('Received: %s' % command)
    if 'on' in command:
         message = "on"
         
         if 'yellow' in command:
             message = message + "yellow "
             GPIO.output(yellow, 1)
         if 'green' in command:
             message = message + "green "
             GPIO.output(green, 1)
         if 'all' in command:
             message = message + "all "
             GPIO.output(yellow, 1)
             GPIO.output(green, 1)
             message = message + "light(s)"
             telegram_bot.sendMessage (chat_id, message)

    if 'off' in command:
        message = "off "
       
        if 'yellow' in command:
            message = message + "yellow "
            GPIO.output(yellow, 0)
        
        if 'green' in command:
            message = message + "green "
            GPIO.output(green, 0)
        if 'all' in command:
            message = message + "all "
            GPIO.output(yellow, 0)
            GPIO.output(green, 0)
            message = message + "light(s)"
            telegram_bot.sendMessage (chat_id, message)
    if command == 'file':
        telegram_bot.sendDocument(chat_id,document=open('/home/pi/telegram.py'))
telegram_bot = telepot.Bot('5834167228:AAEu7ImFqbyhrXGRNSOJLzC_JoA2zfCC78k') #CHANGE BOT TOKEN HERE !!!
print (telegram_bot.getMe())
MessageLoop(telegram_bot, action).run_as_thread()
print ('Up and Running....')
while 1:
    time.sleep(10)

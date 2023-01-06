import psutil
#from plyer import notification
import plyer
import time

while(True):
    battery = psutil.sensors_battery()
    percent = battery.percent
    charging = battery.power_plugged
    flag = False
    if percent > 60 :
        timer = 15
    elif 60 <= percent < 30:
        timer = 8
    else:
        timer = 3

    if not charging:
        notification = plyer.notification
        notification.notify(
            #app_name="Remembrall",
            title="Feed me",
            message=str(percent) + "% Battery remaining",
            timeout=15,
            app_icon="icon.ico"
        )
        flag = True
    elif charging:
        flag = False

    if flag:
        time.sleep(timer*60)
# after every 60 mins it will show the
# battery percentage
    #time.sleep(10*60)

    #continue
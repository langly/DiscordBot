
import requests

class LaMetric:
    def __init__(self, ip, key):
        self.ip     = ip
        self.key    = key


    def notify(self, icon, txt):
        s = "http://%s:8080/api/v2/device/notifications" %(self.ip)
        h = {"Content-Type" : "application/json"}
        b = '{ "model": { "frames" :[ { "icon":%d, "text":"%s"} ] } }' %(icon,txt)

        print(b)

        r = requests.post(s, headers=h, data=b, auth=('dev', self.key))

        print(r)

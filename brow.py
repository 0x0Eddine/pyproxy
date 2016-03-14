#proxy visitor by salah
#how to use: python script.py [starting number]

import sys
from selenium import webdriver

x = 0
n = int(sys.argv[1])

for x in range(n,6000):
	PROXYY = []
	with open('proxy.txt') as f:
        	PROXYY = f.read().splitlines()

	print PROXYY[x]
	PROXY = PROXYY[x]

	webdriver.DesiredCapabilities.FIREFOX['proxy']={
    		"httpProxy":PROXY,
    		"ftpProxy":PROXY,
    		"sslProxy":PROXY,
    		"noProxy":None,
    		"proxyType":"MANUAL",
    		"autodetect":False
		}
	firefoxProfile1 = webdriver.FirefoxProfile()
	#firefoxProfile1.set_preference('permissions.default.image', 2)
	#firefoxProfile1.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
	#firefoxProfile1.set_preference('permissions.default.stylesheet', 2)
    	
	driver = webdriver.Firefox(firefox_profile=firefoxProfile1)
	driver.set_window_size(400,500)
	driver.get('http://www.google.com/')
	x += 1
	driver.sleep(10000)
	driver.close()


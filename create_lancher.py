from os import getcwd, geteuid, popen

print("[+]Installing BruteCat.......")

def create_launcher():
    path = getcwd()
    lanchwrite = open("/usr/local/bin/brutecat", "w")
    lanchwrite.write("#!/bin/sh\ncd %s\npython brutecat.py" % (path))
    lanchwrite.close()
    popen("chmod +x /usr/local/bin/brutecat")

if geteuid() != 0:
    print("\n[!] This script must run as root. Please sudo it up! Exiting...")
    exit(0)

else:
	create_launcher()
	print("\n[*]Done ^_^")

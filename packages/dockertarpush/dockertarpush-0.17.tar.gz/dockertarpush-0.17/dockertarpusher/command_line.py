import dockertarpusher
import sys

def main():
    if(len(sys.argv) < 3):
        print("Arguments required: {REGISTRYURL} {TARPATH} [LOGIN] [PASSWORD] --noSslVerify")
        print("Example: http://localhost:5000 tests/busybox.tar")
        sys.exit(1)
    url = sys.argv[1]
    tarpath = sys.argv[2]
    login = None
    password = None
    if(len(sys.argv) > 3):
        login = sys.argv[3]
    if(len(sys.argv) > 4):
        password = sys.argv[4]
    verify = True
    if("--noSslVerify" in sys.argv):
        verify = False
    regClient = dockertarpusher.Registry(url, tarpath, stream = True, login = login, password = password, sslVerify = verify)
    regClient.processImage()
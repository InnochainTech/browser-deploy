#!/usr/bin/python3
# encoding: utf-8

import sys
import comm.check as commCheck
import comm.build as commBuild
def do():
    if len(sys.argv)==1:
        help()
        return
    param = sys.argv[1]
    if "installAll" == param:
        commCheck.do()
        commBuild.do()
    elif "startAll" == param:
        commBuild.start()
    elif "stopAll" == param:
        commBuild.end()
    elif "startServer" == param:
        commCheck.checkServerPort()
        commBuild.startServer()
    elif "stopServer" == param:
        commBuild.stopServer()
    elif "startWeb" == param:
        commCheck.checkWebPort()
        commBuild.startWeb()
    elif "stopWeb" == param:
        commBuild.stopWeb()
    elif "check"== param:
        commCheck.do()
    elif "help"== param:
        help()
    else:
        paramError()
    return

def help():
    helpMsg = '''
Usage: python deploy [Parameter]

Parameter:
    check : check the environment
    installAll : check the environment, deploy server and web
    startAll : start server and web
    stopAll : stop server and web
    startServer : start server
    stopServer : stop server
    startWeb : start web
    stopWeb : stop web
    
Attention:
    1. Need to install python3.6, jdk, mysql, PyMySQL first
    2. Need to ensure a smooth network
    3. You need to install git, wget, nginx; if it is not installed, the installation script will automatically install these components, but this may fail.
    '''
    print (helpMsg)
    return

def paramError():
    print ("")
    print ("Param error! Please check.")
    help()
    return

if __name__ == '__main__':
    do()
    pass
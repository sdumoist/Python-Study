from numpy import *
import itchat
from threading import Timer

def get_userName():
    itchat.auto_login(hotReload=True)
    friend=itchat.search_friends(name="微信名")
    print(friend)
    userName = friend[0]['UserName']
    return userName

def send_msg():
    userName = get_userName()
    itchat.send("你好", toUserName=userName)
    t = Timer(3600, send_msg)  #Timer的时间单位是秒
    t.start()
send_msg()

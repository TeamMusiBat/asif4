# -*-coding: utf-8 -*-

import VIPRO
from VIPRO.lib.curve.ttypes import *	
from datetime import datetime	
import io,os,re,ast,six,sys,glob,json,time,timeit,codecs,random,shutil,urllib,urllib2,urllib3,goslate,html5lib,requests,threading,wikipedia,subprocess,googletrans	,pytz
from gtts import gTTS	
from random import randint	
from time import sleep	
from urllib import urlopen, urlretrieve, urlencode	
from io import StringIO	
from bs4 import BeautifulSoup	
from threading import Thread	
from googletrans import Translator	
#==============================================================================#
botStart = time.time()

owner = VIPRG.LINE() #Akun Utama
owner.login(token="EFZ3xmI5Rh3XbLhhlBx1.0ebIDL8RGQxkHth5NCOfKq.z+ccjbj83ySLLIysdgnSzYJhkYePGSdZsCpYN18fdIs=")
owner.loginResult()
    
vipro = VIPRG.LINE()
vipro.login(token="EFnAL0njFzd0FaTaJUnc.WviproY5FFJePoiRXXaqUm+xa.4NnWPDdd9ZcFthwNXRZGFIQHbGX/UR89bl0Dmki2f3k=")
vipro.loginResult()

ki = VIPRG.LINE()
ki.login(token="EF8amXy5UtGoKsq1PLv9.Occn7DpcjDD71RtM3JikIq.wh9Bfva8nKbHN28D2sMxs7XFmdaDtflagRKCQJSJvh4=")
ki.loginResult()

ki2 = VIPRG.LINE()
ki2.login(token="EFZjRzhdIk8eBXMK9wK5.OZR85ZKJXI58DSjU51V8Dq.hBe/V5qv7r2+GWhsse3o/xYPAZDPF9UFsQ5SyxvGOk4=")
ki2.loginResult()

print("すべてログインしました!!")



oepoll = OEPoll(owner)
#==============================================================================#
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
banOpen = codecs.open("ban.json","r","utf-8")

read = json.load(readOpen)
settings = json.load(settingsOpen)
ban = json.load(banOpen)

msg_dict = {}
bl = [""]

#==============================================================================#
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    python = sys.executable
    os.exevipro(python, python, *sys.argv)
def logError(text):
    vipro.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        vipro.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def helpmessage():
    helpMessage = """╔══════════════
╠♥ ✿✿✿ 荒らし ✿✿✿ ♥
║
╠══✪〘 Help Message 〙✪═══
╠➥ help  コマンド一覧を出します。
╠()
╠➥ ログアウト ログアウトします。
╠()
╠➥ 荒らせ!! 全蹴りをします。
╚═〘 Created By: 😜😜😜😜〙"""
    return helpMessage

wait = {
    "myProfile": {
    "displayName": "",
    "coverId": "",
    "pictureStatus": "",
    "statusMessage": ""
    },
}
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}
setTime = {}
setTime = wait2['setTime']

KAC=[vipro,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
DEF=[vipro,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
mid = vipro.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid

Smid = owner.getProfile().mid
Bots=[mid,kimid,ki2mid,Smid,"uda936836a9869eb86ec8ab992a4e8979"]
admin=[mid,kimid,ki2mid,Smid,"uda936836a9869eb86ec8ab992a4e8979","ue4e13b0a41d848845489374e671c6861","ub21eb3d440e0dfd640eef9f2fb5ce02d","u782cdf7a9fd2545c84a0cd86f418e9f7","u799da4e06d50e1775cfcff1f3e59df03"]
creator=["uda936836a9869eb86ec8ab992a4e8979"]
admsa=["uda936836a9869eb86ec8ab992a4e8979"]

wait["myProfile"]["displayName"] = viproProfile.displayName
wait["myProfile"]["statusMessage"] = viproProfile.statusMessage
wait["myProfile"]["pictureStatus"] = viproProfile.pictureStatus
coverId = vipro.getProfileDetail()["result"]["objectId"]
wait["myProfile"]["coverId"] = coverId

readOpen = codecs.open("st2__b.json","r","utf-8")
read = json.load(readOpen)

contact = vipro.getProfile()
restoreprofile = vipro.getProfile()
restoreprofile.displayName = contact.displayName
restoreprofile.statusMessage = contact.statusMessage                        
restoreprofile.pictureStatus = contact.pictureStatus

contact = vipro.getProfile()
backup = vipro.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup = ki.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki2.getProfile()
backup = ki2.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))

admin =['ubdfdbe777c1ef100e4e51485c42cb5e5',viproMID]
owners = [""]
#if viproMID not in owners:
#    python = sys.executable
#    os.exevipro(python, python, *sys.argv)
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                vipro.findAndAddContactsByMid(op.param1)
                vipro.sendMessage(op.param1, " ".format(str(vipro.getContact(op.param1).displayName)))
        if op.type == 11:
            group = vipro.getGroup(op.param1)
            contact = vipro.getContact(op.param2)
            if settings["qrprotect"] == True:
                if op.param2 in admin or op.param2 in ban["bots"]:
                    pass
                else:
                    gs = vipro.getGroup(op.param1)
                    vipro.kickoutFromGroup(op.param1,[op.param2])
                    gs.preventJoinByTicket = True
                    vipro.updateGroup(gs)
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE GROUP")
            if viproMID in op.param3:
                group = vipro.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    vipro.acceptGroupInvitation(op.param1)
            elif settings["invprotect"] == True:
                if op.param2 in admin or op.param2 in ban["bots"]:
                    pass
                else:
                    vipro.cancelGroupInvitation(op.param1,[op.param3])
        if op.type == 24:
            print ("[ 24 ] NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                vipro.leaveRoom(op.param1)
        if op.type == 25 or op.type == 26:
            K0 = admin
            msg = op.message
            if settings["share"] == True:
                K0 = msg._from
            else:
                K0 = admin
#        if op.type == 25 :
#            if msg.toType ==2:
#                g = vipro.getGroup(op.message.to)
#                print ("sended:".format(str(g.name)) + str(msg.text))
#            else:
#                print ("sended:" + str(msg.text))
#        if op.type == 26:
#            msg =op.message
#            pop = vipro.getContact(msg._from)
#            print ("replay:"+pop.displayName + ":" + str(msg.text))
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != vipro.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
            if sender in K0 or sender in owners:
                if text.lower() == 'help':
                    helpMessage = helpmessage()
                    vipro.sendMessage(to, str(helpMessage))
                    
                elif text.lower() == 'bye':
                    vipro.sendMessage(to,"ByeBye")
                    vipro.leaveGroup(msg.to)
#==============================================================================#
                elif text.lower() == 'ログアウト':
                    vipro.sendMessage(to, "ログアウト中...")
                    time.sleep(5)
                    vipro.sendMessage(to, "ログアウトしました。\n再ログインしてください。")
                    restartBot()
#==============================================================================#
            elif "Nuke" in msg.text:
              if msg.from_ in creator:
                if msg.toType == 2:
                    print ("Nuke ok")
                    _name = msg.text.replace("Nuke","")
                    gs = vipro.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    gs = ki7.getGroup(msg.to)
                    gs = ki8.getGroup(msg.to)
                    gs = ki9.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        vipro.sendText(msg.to,"Limit gw njir..")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[vipro,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                pass
#==============================================================================#
        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                else:
                   pass
            except:
                pass
            try:
                if op.param1 in wait2['readPoint']:
                    Name = vipro.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n[※]" + Name
                        wait2['ROM'][op.param1][op.param2] = "[※]" + Name
                        print (time.time() + name)
                else:
                    pass
            except:
                pass
    except Exception as error:
        logError(error)
#==============================================================================#
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
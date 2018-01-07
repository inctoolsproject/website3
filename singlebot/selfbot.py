# -*- coding: utf-8 -*-
# kasem bot

import TCB
from TCB.lib.curve.ttypes import *
from multiprocessing import Pool
from googletrans import Translator
from threading import Thread
from urlparse import urlparse
from datetime import datetime
from urllib import urlopen
from gtts import gTTS
from bs4 import BeautifulSoup
from io import StringIO
import time, random, sys, re, os, json, threading, subprocess, string, codecs, requests, tweepy, ctypes, urllib, urllib2, wikipedia,tempfile,glob,shutil,unicodedata,urllib3,urlparse
mulai = time.time()
#==================BAGIAN LOGIN AKUN BOT====================================================================================================================================
#your account
saya = AYANA.LINE()
saya.login(token="your token LINE")
saya.loginResult()
print "succes login"

#==================BAGIAN VARIABLE UNTUK BOT=====================================================================================
print "self bot"
reload(sys)
sys.setdefaultencoding('utf-8')

meme = {
    "meme1":"buzz",
    "meme2":"patrick",
    "meme3":"wonka",
    "meme4":"sparta",
    "meme5":"older",
    "meme6":"noidea",
    "meme7":"aag",
    "meme8":"fetch",
    "meme9":"dodgson",
    "meme10":"rollsafe"
    }
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True, "members":2},
    'leaveRoom':False,
    'timeline':True,
    'autoAdd':False,
    'message':"Thanks for add Me",
    "lang":"JP",
    "comment":"auto like by me:)",
    "welmsg":"welcome to group",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "status":False,
    "kickmention":False,
    "likeOn":False,
    "autorein":True,
    "pname":False,
    "pelaku":False,
    "detectmention":False,
    "listmention":"don't tag me please'_'",
    "header":{},
    "blacklist":{},
    "whitelist":{},
    "spam":False,
    "wblacklist":False,
    "dblacklist":False,
    "qr":False,
    "welcomemsg":False,
    "pap":{},
    "squad":{},
    "Backup":False,
    "protectionOn":False,
    "adm":False,
    "unadm":False,
    "own":False,
    "unown":False,
    "stff":False,
    "unstff":False,
    "mod":False,
    "unmod":False,
    "bot":False,
    "unbot":False,
    "winvite":False,
    "tamper":False,
    "steal":False,
    "giftcontact":False,
    "cpp":False,
    "alwaysread":True,
    "linkticket":False,
    "atjointicket":True,
    "protectall":True,
    "post":True,
    "pnharfbot":{},
    "pname":{},
    "pro_name":{}
    }
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
settings = {
    "simiSimi":{}
    }
res = {
    'num':{},
    'us':{},
    'au':{}
}


#========================BAGIAN DATA RECORD BOT================================================================================================

mid = saya.getProfile().mid
namasaya = saya.getProfile().displayName

protectname = []
protecturl = []
protectall = {}
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
Bots=[mid]

setTime = {}
setTime = wait2['setTime']

contact = saya.getProfile()
backup = saya.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

settingsOpen = codecs.open("temp.json","r","utf-8")
sett = json.load(settingsOpen)
#=============BAGIAN DEFENISI SCRIPT===================================================================================================================================
def command(text):
    pesan = text.lower()
    if pesan.startswith(char["keyCommand"]):
        cmd = pesan.replace(char["keyCommand"],"")
    else:
        cmd = "Undefined command"
    return cmd
def helpbot():
    key = char["#"]
    key = key.title()
    helpMessage = "╔══[ Help Message ]" + "\n" + \
                  "╠ Use [" + key + "] for the Prefix" + "\n" + \
                  "╠ " + key + "Help" + "\n" + \
                  "╠ " + key + "Me" + "\n" + \
                  "╠ " + key + "Restart" + "\n" + \
                  "╠ " + key + "Speed" + "\n" + \
                  "╠ " + key + "Leave" + "\n" + \
                  "╠ " + key + "Stealpict 「」" + "\n" + \
                  "╠ " + key + "Kickout 「@」" + "\n" + \
                  "╠ " + key + "Stealmid 「@」" + "\n" + \
                  "╠ " + key + "Stealname 「@」" + "\n" + \
                  "╠ " + key + "Stealbio 「@」" + "\n" + \
                  "╠ " + key + "Link open" + "\n" + \
                  "╠ " + key + "Link close" + "\n" + \
                  "╠ " + key + "Gurl" + "\n" + \
                  "╠ " + key + "Mention" + "\n" + \
                  "╠ " + key + "Group icon" + "\n" + \
                  "╠ " + key + "Mybio:「text」" + "\n" + \
                  "╠ " + key + "Myname:「text」" + "\n" + \
                  "╠ " + key + "Gbroadcast 「text」" + "\n" + \
                  "╠ " + key + "Broadcast 「text」" + "\n" + \
                  "╠ " + key + "Grouplist" + "\n" + \
                  "╠ " + key + "Rejectall" + "\n" + \
                  "╠ " + key + "Recover" + "\n" + \
                  "╠ " + key + "Removechat" + "\n" + \
                  "╠ " + key + "Changekey:「new key」" + "\n" + \
                  "╠ Mykey" + "\n" + \
                  "╠ " + key + "Runtime" + "\n" + \
                  "╠ " + key + "Time" + "\n" + \
                  "╠══[ Asisst Command ]\n" + \
                  "╠ " + key + "Come in" + "\n" + \
                  "╠ " + key + "Come out" + "\n" + \
                  "╠ " + key + "Cleanse" + "\n" + \
                  "╠ " + key + "Bot1 rename:「txt」" + "\n" + \
                  "╠ " + key + "Bot2 rename:「txt」" + "\n" + \
                  "╠ " + key + "Bot1 out" + "\n" + \
                  "╠ " + key + "Bot2 out" + "\n" + \
                  "╠ " + key + "Bot1 clone@" + "\n" + \
                  "╠ " + key + "Bot2 clone@" + "\n" + \
                  "╠ " + key + "Bot1 refresh" + "\n" + \
                  "╠ " + key + "Bot2 refresh" + "\n" + \
                  "╠ " + key + "Bot1 say 「txt」" + "\n" + \
                  "╠ " + key + "Bot2 say 「txt」" + "\n" + \
                  "╠ " + key + "Bot1 gift" + "\n" + \
                  "╠ " + key + "Bot2 gift" + "\n" + \
                  "╠══[ Cctv Command ]\n" + \
                  "╠ " + key + "Lurk on" + "\n" + \
                  "╠ " + key + "Lurk off" + "\n" + \
                  "╠ " + key + "Lurk result" + "\n" + \
                  "╠══[ Remote Command ]\n" + \
                  "╠ " + key + "Autoread on" + "\n" + \
                  "╠ " + key + "Autoread off" + "\n" + \
                  "╠ " + key + "Autochat on" + "\n" + \
                  "╠ " + key + "Autochat off" + "\n" + \
                  "╠ " + key + "Autojoin on" + "\n" + \
                  "╠ " + key + "Autojoin off" + "\n" + \
                  "╠ " + key + "Autowelcome on" + "\n" + \
                  "╠ " + key + "Autowelcome off" + "\n" + \
                  "╠══[ Fun Command ]\n" + \
                  "╠ " + key + "Instagram 「query」" + "\n" + \
                  "╠ " + key + "Voice-id 「txt1」" + "\n" + \
                  "╠ " + key + "Voice-en 「txt1」" + "\n" + \
                  "╠ " + key + "Voice-jp 「txt1」" + "\n" + \
                  "╠ " + key + "Meme1-10 「txt1」 「txt2」" + "\n" + \
                  "╠ " + key + "Wikipedia 「query」" + "\n" + \
                  "╠ " + key + "Youtube 「query」" + "\n" + \
                  "╠ " + key + "Image 「query」" + "\n" + \
                  "╠ " + key + "Liststicker" + "\n" + \
                  "╠ " + key + "Spamsticker 「no」 「X」" + "\n" + \
                  "╠ " + key + "Praytime 「X」" + "\n" + \
                  "╠ " + key + "Weather 「X」" + "\n" + \
                  "╠ " + key + "location 「X」" + "\n" + \
                  "╚══[ SELFBOT:"+wait["header"].title()+"]"
    return helpMessage
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.01)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items


def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()



def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d hour %02d minute %02d seconds' % (hours, mins, secs)

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error
def sendMessage(self, messageObject):
        return self.Talk.client.sendMessage(0,messageObject)

def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

        return self.Talk.client.sendMessage(0, msg)
def sendImage(self, to_, path):
        M = Message(to=to_,contentType = 1)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self._client.sendMessage(M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'image',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self._client.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        #r.content
        return True


def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1


def NOTIFIED_READ_MESSAGE(op):
    print op
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name + datetime.now().strftime(' [%d - %H:%M:%S]')
                wait2['ROM'][op.param1][op.param2] = "・" + Name + " ツ"
        else:
            pass
    except:
        pass
def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait2['readPoint']:
                    if msg.from_ in wait2["ROM"][msg.to]:
                        del wait2["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
          
    except KeyboardInterrupt:
				sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return
def clientBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return

        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                saya.findAndAddContactsByMid(op.param1)
            saya.sendMessage(op.param1, "Halo {} terimakasih telah menambahkan saya sebagai teman :3".format(str(client.getContact(op.param1).displayName)))
            arg = "   New Friend : {}".format(str(client.getContact(op.param1).displayName))
            print (arg)

        if op.type == 11:
            print ("[ 11 ] NOTIFIED UPDATE GROUP")
            if op.param3 == "1":
                group = client.getGroup(op.param1)
                contact = client.getContact(op.param2)
                arg = "   Changed : Group Name"
                arg += "\n   New Group Name : {}".format(str(group.name))
                arg += "\n   Executor : {}".format(str(contact.displayName))
                print (arg)
            elif op.param3 == "4":
                group = saya.getGroup(op.param1)
                contact = saya.getContact(op.param2)
                if group.preventedJoinByTicket == False:
                    gQr = "Opened"
                else:
                    gQr = "Closed"
                arg = "   Changed : Group Qr"
                arg += "\n   Group Name : {}".format(str(group.name))
                arg += "\n   New Group Qr Status : {}".format(gQr)
                arg += "\n   Executor : {}".format(str(contact.displayName))
                print (arg)

        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE INTO GROUP")
            group = saya.getGroup(op.param1)
            contact = saya.getContact(op.param2)
            if wait["autoJoin"] == True:
                if wait["autoReject"]["status"] == True:
                    if len(group.members) > wait["autoReject"]["members"]:
                        saya.acceptGroupInvitation(op.param1)
                    else:
                        saya.rejectGroupInvitation(op.param1)
                else:
                    saya.acceptGroupInvitation(op.param1)
            gInviMids = []
            for z in group.invitee:
                if z.mid in op.param3:
                    gInviMids.append(z.mid)
            listContact = ""
            if gInviMids != []:
                for j in gInviMids:
                    name_ = client.getContact(j).displayName
                    listContact += "\n      + {}".format(str(name_))

            arg = "   Group Name : {}".format(str(group.name))
            arg += "\n   Executor : {}".format(str(contact.displayName))
            arg += "\n   List User Invited : {}".format(str(listContact))
            print (arg)

        if op.type == 17:
            print ("[ 17 ]  NOTIFIED ACCEPT GROUP INVITATION")
            group = saya.getGroup(op.param1)
            contact = saya.getContact(op.param2)
            arg = "   Group Name : {}".format(str(group.name))
            arg += "\n   User Join : {}".format(str(contact.displayName))
            print (arg)

        if op.type == 19:
            print ("[ 19 ] NOTIFIED KICKOUT FROM GROUP")
            group = saya.getGroup(op.param1)
            contact = saya.getContact(op.param2)
            victim = saya.getContact(op.param3)
            arg = "   Group Name : {}".format(str(group.name))
            arg += "\n   Executor : {}".format(str(contact.displayName))
            arg += "\n   Victim : {}".format(str(victim.displayName))
            print (arg)

        if op.type == 22:
            print ("[ 22 ] NOTIFIED INVITE INTO ROOM")
            if settings["autoLeave"] == True:
                saya.sendMessage(op.param1, "Goblok ngapain invite gw")
                saya.leaveRoom(op.param1)

        if op.type == 24:
            print ("[ 24 ] NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                saya.sendMessage(op.param1, "Goblok ngapain invite gw")
                saya.leaveRoom(op.param1)

        if op.type == 25:
            print ("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
#==================BAGIAN OPERATION TYPE UNTUK BOT==============================================================================================

       
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = sender
                elif msg.toType == 2:
                    to = receiver
                if settings["autoRead"] == True:
                    client.sendChatChecked(to, msg_id)
                if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to,data['result']['response'].encode('utf-8'))
#===========================================
        if op.type == 55:
            try:
				if op.param1 in wait2['readPoint']:
					Name = cl.getContact(op.param2).displayName
					if Name in wait2['readMember'][op.param1]:
						pass
					else:
						wait2['readMember'][op.param1] += "\n╠" + Name
						wait2['ROM'][op.param1][op.param2] = "╠" + Name
				else:
					cl.sendText
            except:
                pass
						
						
#------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True


def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()
    
while True:
    try:
        autoRestart()
        Ops = cl.fetchOps(cl.Poll.rev,  5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)

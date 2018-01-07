# -*-coding: utf-8 -*- 
# single bot
# inspirate kasem bot

import AYANA
from AYANA.lib.curve.ttypes import *
from multiprocessing import Pool
from googletrans import Translator
from threading import Thread
from datetime import datetime
from urllib import urlopen
from gtts import gTTS
from bs4 import BeautifulSoup
from io import StringIO
import time, random, sys, re, os, json, threading, subprocess, string, codecs, requests, tweepy, ctypes, urllib, urllib2, wikipedia,tempfile,glob,shutil,unicodedata,urllib3
mulai = time.time()
#==================BAGIAN LOGIN AKUN BOT====================================================================================================================================
#your account
cl = TCB.LINE()
cl.login(token="EoDdfcepQGRcHtWSMo7d.S9mM8bDFugfVB8yl2c1/3q.zXc35ICa7K2PAflGQN5/FE8j2UBDM2w6YMyyb0yla4Q=")
cl.loginResult()
print "succes login"

#==================BAGIAN VARIABLE UNTUK BOT=====================================================================================
print "ayana's bot"
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
    "key":cl.getProfile().displayName,
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

#===================BAGIAN LIST COMMAND UNTUK BOT==========================================================================================
helpMessage= "______________________\n"\
+" ☁STAFF COMMAND☁\n\n"\
+wait["key"].title()+" menu\n"\
+wait["key"].title()+" getmid @[name]\n"\
+wait["key"].title()+" getbio @[name]\n"\
+wait["key"].title()+" getname @[name]\n"\
+wait["key"].title()+" getcontact @[name]\n"\
+wait["key"].title()+" getpict @[name]\n"\
+wait["key"].title()+" getinfo[contact]\n"\
+wait["key"].title()+" gift1-3\n"\
+wait["key"].title()+" adminlist\n"\
+wait["key"].title()+" say [txt]\n"\
+wait["key"].title()+" lurk on\n"\
+wait["key"].title()+" lurk off\n"\
+wait["key"].title()+" lurkers\n"\
+wait["key"].title()+" date\n"\
+wait["key"].title()+" my picture\n"\
+wait["key"].title()+" my status\n"\
+wait["key"].title()+" my name\n"\
+wait["key"].title()+" mY Contact\n"\
+wait["key"].title()+" my mid\n"\
+wait["key"].title()+" instagram [txt]\n"\
+wait["key"].title()+" youtube [txt]\n"\
+wait["key"].title()+" wikipedia [txt]\n"\
+wait["key"].title()+" image [txt]\n"\
+wait["key"].title()+" twitter [txt]\n"\
+wait["key"].title()+" meme1-10 [txt] [txt]\n"\
+wait["key"].title()+" weather [txt]\n"\
+wait["key"].title()+" praytime [txt]\n"\
+wait["key"].title()+" location [txt]\n"\
+wait["key"].title()+" lyric [txt]\n"\
+wait["key"].title()+" music [txt]\n"\
+wait["key"].title()+" vn-id [txt]\n"\
+wait["key"].title()+" vn-en [txt]\n"\
+wait["key"].title()+" vn-jp [txt]\n"\
+wait["key"].title()+" tr-id [txt]\n"\
+wait["key"].title()+" tr-cn [txt]\n"\
+wait["key"].title()+" tr-ar [txt]\n"\
+wait["key"].title()+" tr-en [txt]\n"\
+wait["key"].title()+" tr-jp [txt]\n"\
+wait["key"].title()+" tr-ko [txt]\n"\
+wait["key"].title()+" tr-th [txt]\n"\
+"☁ADMIN COMMAND☁\n\n"\
+wait["key"].title()+" bye\n"\
+wait["key"].title()+" summon\n"\
+wait["key"].title()+" add all\n"\
+wait["key"].title()+" spam add:[txt]\n"\
+wait["key"].title()+" spam start:[num]\n"\
+wait["key"].title()+" group image\n"\
+wait["key"].title()+" system\n"\
+wait["key"].title()+" iconfig\n"\
+wait["key"].title()+" kernel\n"\
+wait["key"].title()+" cpu\n"\
+wait["key"].title()+" staff on[contact]\n"\
+wait["key"].title()+" staff on @[name]\n"\
+wait["key"].title()+" staff off @[name]\n"\
+wait["key"].title()+" staff off[contact]\n"\
+wait["key"].title()+" banlist\n"\
+wait["key"].title()+" bot on[contact]\n"\
+wait["key"].title()+" bot on @[name]\n"\
+wait["key"].title()+" bot off @[name]\n"\
+wait["key"].title()+" bot off[contact]\n"\
+wait["key"].title()+" mod on[contact]\n"\
+wait["key"].title()+" mod off[contact]\n"\
+wait["key"].title()+" mod on @name\n"\
+wait["key"].title()+" mod off @name\n"\
+wait["key"].title()+" speed\n"\
+wait["key"].title()+" notify on\n"\
+wait["key"].title()+" notify off\n"\
+wait["key"].title()+" chatbot on\n"\
+wait["key"].title()+" chatbot off\n"\
+wait["key"].title()+" protect on\n"\
+wait["key"].title()+" protect off\n"\
+wait["key"].title()+" mimic on\n"\
+wait["key"].title()+" mimic off\n"\
+wait["key"].title()+" welcome on\n"\
+wait["key"].title()+" welcome off\n"\
+wait["key"].title()+" check welcome\n"\
+wait["key"].title()+" settings\n"\
+wait["key"].title()+" memlist\n"\
+wait["key"].title()+" mimic add @[nme]\n"\
+wait["key"].title()+" mimic del @[name]\n"\
+wait["key"].title()+" mimic list\n"\
+wait["key"].title()+" gift [contact]\n"\
+wait["key"].title()+" ginfo\n"\
+wait["key"].title()+" invite [contact]\n"\
+wait["key"].title()+" gcreator\n"\
+wait["key"].title()+" glink open\n"\
+wait["key"].title()+" glink close\n"\
+wait["key"].title()+" gname:[txt]\n"\
+wait["key"].title()+" gurl\n"\
+wait["key"].title()+" runtime\n"\
+wait["key"].title()+" creator\n"\
+wait["key"].title()+" set welcome:[txt]\n"\
+wait["key"].title()+" check welcome\n"\
+wait["key"].title()+" pap set:[link image]\n"\
+wait["key"].title()+" pap\n"\
+wait["key"].title()+" ban @[name]\n"\
+wait["key"].title()+" banned [contact]\n"\
+wait["key"].title()+" unban @[name]\n"\
+wait["key"].title()+" unbanned [contact]\n"\
+wait["key"].title()+" vkick @[name]\n"\
+wait["key"].title()+" crash\n"\
+wait["key"].title()+" ulti @[name]\n"\
+wait["key"].title()+" cancel\n\n"\
+"☁OWNER COMMAND☁\n\n"\
+wait["key"].title()+" groupcast:[txt]\n"\
+wait["key"].title()+" broadcast:[txt]\n"\
+wait["key"].title()+" destroy\n"\
+wait["key"].title()+" backup run\n"\
+wait["key"].title()+" copy @[name]\n"\
+wait["key"].title()+" backup\n"\
+wait["key"].title()+" rename:[txt]\n"\
+wait["key"].title()+" bio:[txt]\n"\
+wait["key"].title()+" timeline:[txt]\n"\
+wait["key"].title()+" reject all\n"\
+wait["key"].title()+" remove chat\n"\
+wait["key"].title()+" restart\n"\
+wait["key"].title()+" spm invite[cntact]\n"\
+wait["key"].title()+" changepict\n"\
+wait["key"].title()+" join url\n"\
+wait["key"].title()+" grouplist\n"\
+wait["key"].title()+" blocklist\n"\
+wait["key"].title()+" friendlist\n"\
+wait["key"].title()+" contact banlist\n"\
+wait["key"].title()+" admin on @[name]\n"\
+wait["key"].title()+" admin off @[name]\n"\
+wait["key"].title()+" admin on[contact]\n"\
+wait["key"].title()+" admin off[contact]\n"\
+wait["key"].title()+" clear adminlist\n"\
+wait["key"].title()+" clear stafflist\n"\
+wait["key"].title()+" clear banlist\n"\
+wait["key"].title()+" clear botlist\n"\
+wait["key"].title()+" clear mimiclist\n"\

#========================BAGIAN DATA RECORD BOT================================================================================================

KAC=[cl]
mid = cl.getProfile().mid
koala = cl.getProfile().displayName

protectname = []
protecturl = []
protectall = {}
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
Bots=[mid]
pencipta = ["u832d6b22ecdb23a673a2ae6a8784f714"]
owner = ["u154441c3a17c0e9b3e4569fa9dcbac11"]
admin = ["uf87e2b4fdab8fa653c9afc42b78926f0"]
staff=["u50c3afb8bd7e815f9fe6493da96ca7e3"]
team=["u93b3c9ad72d83a795155ac4fe1019f03"]
moderator=["u6be3e3379b653eadf982dafa4e3b3c55"]

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

settingsOpen = codecs.open("temp.json","r","utf-8")
sett = json.load(settingsOpen)
#=============BAGIAN DEFENISI SCRIPT===================================================================================================================================

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
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

#==================BAGIAN OPERATION TYPE UNTUK BOT==============================================================================================

        if op.type == 11:
            if op.param3 == '1':
               if op.param1 in wait['pname']:
                 if wait["protectall"] == True:
                     try:
                         G = cl.getGroup(op.param1)
                     except:
                         pass
                     G.name = wait['pro_name'][op.param1]
                     if op.param2 in pencipta:
                     	pass
                     if op.param2 in owner:
                     	pass
                     if op.param2 in admin:
                     	pass
                     if op.param2 in staff:
                     	pass
                     if op.param2 in team:
                     	pass
                     if op.param2 in moderator:
                     	pass
                        cl.updateGroup(G)
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        targets = [op.param2]
                        for target in targets:
                            wait["blacklist"][target] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

        if op.type == 11:
           pelaku = op.param2
           korban = op.param3
           if wait["protectall"] == True:
              if pelaku in pencipta:
                 pass
              if pelaku in owner:
                 pass
              if pelaku in admin:
                 pass
              if pelaku in staff:
                 pass
              if pelaku in team:
                 pass
              if pelaku in moderator:
                 pass 
                 G = cl.getGroup(op.param1)
                 G.preventJoinByTicket = True
                 cl.kickoutFromGroup(op.param1,[op.param2]) 
                 X = cl.getGroup(op.param1)
                 X.preventJoinByTicket = True
                 cl.updateGroup(X)
                 targets = [op.param2]
                 for target in targets:
                     wait["blacklist"][target] = True
                     f=codecs.open('st2__b.json','w','utf-8')
                     json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

#===================================================================================================================================
#NOTIFIED_LEAVE_GROUP                          
        if op.type == 15:
           pelaku = op.param2
           korban = op.param3
           if pelaku in pencipta:
              cl.getGroup(op.param1)
              cl.findAndAddContactsByMid(op.param2)
              cl.inviteIntoGroup(op.param1,[op.param2])
        if op.type == 15:
           pelaku = op.param2
           korban = op.param3
           if pelaku in owner:
              cl.getGroup(op.param1)
              cl.findAndAddContactsByMid(op.param2)
              cl.inviteIntoGroup(op.param1,[op.param2])
        if op.type == 15:
           pelaku = op.param2
           korban = op.param3
           if pelaku in admin:
              cl.getGroup(op.param1)
              cl.findAndAddContactsByMid(op.param2)
              cl.inviteIntoGroup(op.param1,[op.param2])
#===================================================================================================================================
#NOTIFIED_CANCEL_INVITATION_GROUP
        if op.type == 32:
           pelaku = op.param2
           korban = op.param3
           if wait["protectall"] == True:
           	 if pelaku in pencipta:
           	  	 pass
           	 if pelaku in owner:
           	  	 pass
          	 if pelaku in admin:
           	  	 pass
             if pelaku in staff:
           	  	 pass
           	 if pelaku in team:
           	  	 pass
         	 if pelaku in moderator:
           	  	 pass
                 cl.getGroup(op.param1)
                 cl.kickoutFromGroup(op.param1,[op.param2])
                 cl.inviteIntoGroup(op.param1,[op.param3])
                 targets = [op.param2]
                 for target in targets:
                     wait["blacklist"][target] = True
                     f=codecs.open('st2__b.json','w','utf-8')
                     json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
        if op.type == 32:
           pelaku = op.param2
           korban = op.param3
           if korban in pencipta:
           	 if pelaku in team:
           	  	 pass
             cl.getGroup(op.param1)
             cl.kickoutFromGroup(op.param1,[op.param2])
             cl.inviteIntoGroup(op.param1,[op.param3])
             targets = [op.param2]
             for target in targets:
                     wait["blacklist"][target] = True
                     f=codecs.open('st2__b.json','w','utf-8')
                     json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
        if op.type == 32:
           pelaku = op.param2
           korban = op.param3
           if korban in owner:
           	 if pelaku in pencipta:
           	  	 pass
           	 if pelaku in team:
           	  	 pass
           	 cl.getGroup(op.param1)
             cl.kickoutFromGroup(op.param1,[op.param2])
             cl.inviteIntoGroup(op.param1,[op.param3])
             targets = [op.param2]
             for target in targets:
                     wait["blacklist"][target] = True
                     f=codecs.open('st2__b.json','w','utf-8')
                     json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
        if op.type == 32:
           pelaku = op.param2
           korban = op.param3
           if korban in admin:
                 if pelaku in pencipta:
              	      pass
                 if pelaku in owner:
              	      pass
                 if pelaku in team:
              	      pass
                 cl.getGroup(op.param1)
                 cl.kickoutFromGroup(op.param1,[op.param2])
                 cl.inviteIntoGroup(op.param1,[op.param3])
                 targets = [op.param2]
                 for target in targets:
                     wait["blacklist"][target] = True
                     f=codecs.open('st2__b.json','w','utf-8')
                     json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
        if op.type == 32:
           pelaku = op.param2
           korban = op.param3
           if korban in staff:
           	 if pelaku in pencipta:
           	  	 pass
           	 if pelaku in owner:
           	  	 pass
           	 if pelaku in admin:
           	  	 pass
           	 if pelaku in team:
           	  	 pass
           	 cl.getGroup(op.param1)
             cl.kickoutFromGroup(op.param1,[op.param2])
             cl.inviteIntoGroup(op.param1,[op.param3])
             targets = [op.param2]
             for target in targets:
                     wait["blacklist"][target] = True
                     f=codecs.open('st2__b.json','w','utf-8')
                     json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

#=====================================================================================================================================
#NOTIFIED_INVITE_INTO_GROUP
        if op.type == 13:
            pelaku = op.param2
            korban = op.param3
            if korban in mid:
             	if pelaku not in pencipta:
            	   pass
            	if pelaku not in owner:
            	   pass
            	if pelaku not in admin:
            	   pass
            	if pelaku not in staff:
            	   pass
            	if pelaku not in team:
            	   pass
           	    cl.getGroup(op.param1)
                cl.acceptGroupInvitation(op.param1)
                cl.sendText(op.param1,"thanks for invite me :)")

        if op.type == 13:
        	pelaku = op.param2
        	korban = op.param3
        	if wait["protectall"] == True:
        	   if pelaku in pencipta:
        		   pass
               if pelaku in owner:
        		   pass
        	   if pelaku in admin:
        		   pass
        	   if pelaku in staff:
        		   pass
               if pelaku in team:
        		   pass
               if pelaku in moderator:
        		   pass
        	   cl.getGroup(op.param1)
               cl.kickoutFromGroup(op.param1,[op.param2])
               cl.cancelGroupInvitation(op.param1,[op.param3])
               cl.cancelGroupInvitation(op.param1,[op.param2])
               cl.kickoutFromGroup(op.param1,[op.param3])
               targets = [op.param2]
               for target in targets:
                       wait["blacklist"][target] = True
                       f=codecs.open('st2__b.json','w','utf-8')
                       json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#=====================================================================================================================================
#NOTIFIED_ACCEPT_GROUP_INVITATION
        if op.type == 17:
            if op.param3 in wait["blacklist"]:
               if op.param3 in pencipta:
               	  pass
               if op.param3 in owner:
               	  pass
               if op.param3 in admin:
               	  pass
               if op.param3 in staff:
               	  pass
               if op.param3 in team:
               	  pass
               cl.kickoutFromGroup(op.param1,[op.param3])
               cl.cancelGroupInvitation(op.param1,[op.param3])
               cl.sendText(op.param1,"blacklist user detected-_-")

        if op.type == 17:
        	pelaku = op.param2
        	korban = op.param3
        	if mid in korban:
        	   groupp = cl.getGroup(msg.to)
        	   gMembMids = [contact.mid for contact in groupp.members]
        	   matched_list = []
        	   for tag in wait["blacklist"]:
        	       matched_list+= filter(lambda str: str == tag, gMembMids)
        	   if matched_list == []:
        	       cl.sendText(msg.to,"there was no blacklist user detected")
        	       return
        	   for jj in matched_list:
        	       cl.kickoutFromGroup(msg.to,[jj])
        	   cl.sendText(msg.to,"blacklist user is flushing is complete")
  
        if op.type == 17:
          if wait["welcomemsg"] == True:
              if op.param2 not in team:
                 ginfo = cl.getGroup(op.param1)
                 cl.sendText(op.param1,cl.getContact(op.param2).displayName +"\n"+ wait["welmsg"])


#========================================================================================================================
#NOTIFIED_KICKOUT_FROM_GROUP
        
        if op.type == 19:
           pelaku = op.param2
           korban = op.param3
           if team in korban:
           	 if pelaku in pencipta:
           	  	 pass
           	 if pelaku in owner:
           	  	 pass
           	 if pelaku in admin:
           	  	 pass
           	 if pelaku in team:
           	  	 pass
           	 cl.kickoutFromGroup(op.param1,[op.param2])
             cl.inviteIntoGroup(op.param1,[op.param3])
             targets = [op.param2]
             for target in targets:
                     wait["blacklist"][target] = True
                     f=codecs.open('st2__b.json','w','utf-8')
                     json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
        if op.type == 19:
           pelaku = op.param2
           korban = op.param3
           if pencipta in korban:
           	  if pelaku in team:
           	     pass
              cl.kickoutFromGroup(op.param1,[op.param2])
           	  cl.inviteIntoGroup(op.param1,[op.param3])
           	  targets = [op.param2]
                  for target in targets:
                     wait["blacklist"][target] = True
                     f=codecs.open('st2__b.json','w','utf-8')
                     json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
        if op.type == 19:
           pelaku = op.param2
           korban = op.param3
           if owner in korban:
           	  if pelaku in pencipta:
           	  	 pass
           	  if pelaku in team:
           	  	 pass
           	  cl.kickoutFromGroup(op.param1,[op.param2])
           	  cl.inviteIntoGroup(op.param1,[op.param3])
           	  targets = [op.param2]
              for target in targets:
                     wait["blacklist"][target] = True
                     f=codecs.open('st2__b.json','w','utf-8')
                     json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
        if op.type == 19:
           pelaku = op.param2
           korban = op.param3
           if admin in korban:
           	  if pelaku in pencipta:
           	  	 pass
           	  if pelaku in owner:
           	  	 pass
           	  if pelaku in team:
           	  	 pass
           	  cl.kickoutFromGroup(op.param1,[op.param2])
           	  cl.inviteIntoGroup(op.param1,[op.param3])
           	  targets = [op.param2]
              for target in targets:
                     wait["blacklist"][target] = True
                     f=codecs.open('st2__b.json','w','utf-8')
                     json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
        if op.type == 19:
           pelaku = op.param2
           korban = op.param3
           if staff in korban:
           	  if pelaku in pencipta:
           	  	 pass
           	  if pelaku in owner:
           	  	 pass
           	  if pelaku in admin:
           	  	 pass
           	  if pelaku in team:
           	  	 pass
           	  cl.kickoutFromGroup(op.param1,[op.param2])
           	  cl.inviteIntoGroup(op.param1,[op.param3])
              targets = [op.param2]
              for target in targets:
                     wait["blacklist"][target] = True
                     f=codecs.open('st2__b.json','w','utf-8')
                     json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#=====================================================================================================================================
                

    
#=================================================================================================================================
        if op.param3 == "1":
            if op.param1 in protectname:
                group = cl.getGroup(op.param1)
                try:
					group.name = wait["pro_name"][op.param1]
					cl.updateGroup(group)
					cl.sendText(op.param1, "Groupname protect now")
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except Exception as e:
                    print e
                    pass
#------------------------------------------------------------------------------------
      
#===========================================
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n╠" + op.param2
                        wait2['ROM'][op.param1][op.param2] = "╠" +op.param2
                else:
                    pass
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
        Ops = cl.fetchOps(cl.Poll.rev,  5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)

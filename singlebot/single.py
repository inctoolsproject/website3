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
cl = AYANA.LINE()
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
    "responMention":False,
    "reply":"don't tag me please'_'",
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
    "squad":"koala",
    "Backup":False,
    "protectionOn":False,
    "team":False,
    "unteam":False,
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


#========================BAGIAN DATA RECORD BOT================================================================================================

KAC=[cl]
mid = cl.getProfile().mid
koala = cl.getProfile().displayName
squad = wait["squad"]
protectname = []
protecturl = []
protectall = {}
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
Bots=[mid]
pencipta=["u832d6b22ecdb23a673a2ae6a8784f714"]
team=["u832d6b22ecdb23a673a2ae6a8784f714"]


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
def helpMessage():
    keyhelp = wait["key"]
    keyhelp = keyhelp.title()
    helpMessage = "______________________\n"\
                  +"COMMAND BOT\n\n"\
                  +keyhelp+" menu\n"\
                  +keyhelp+" getmid @[name]\n"\
                  +keyhelp+" getbio @[name]\n"\
                  +keyhelp+" getname @[name]\n"\
                  +keyhelp+" getcontact @[name]\n"\
                  +keyhelp+" getpict @[name]\n"\
                  +keyhelp+" getinfo[contact]\n"\
                  +keyhelp+" gift1-3\n"\
                  +keyhelp+" teamlist\n"\
                  +keyhelp+" say [txt]\n"\
                  +keyhelp+" lurk on\n"\
                  +keyhelp+" lurk off\n"\
                  +keyhelp+" lurking\n"\
                  +keyhelp+" date\n"\
                  +keyhelp+" my picture\n"\
                  +keyhelp+" my status\n"\
                  +keyhelp+" my name\n"\
                  +keyhelp+" my contact\n"\
                  +keyhelp+" my mid\n"\
                  +keyhelp+" instagram [txt]\n"\
                  +keyhelp+" youtube [txt]\n"\
                  +keyhelp+" youtubedl [txt]\n"\
                  +keyhelp+" wikipedia [txt]\n"\
                  +keyhelp+" image [txt]\n"\
                  +keyhelp+" twitter [txt]\n"\
                  +keyhelp+" meme1-10 [txt] [txt]\n"\
                  +keyhelp+" weather [txt]\n"\
                  +keyhelp+" praytime [txt]\n"\
                  +keyhelp+" location [txt]\n"\
                  +keyhelp+" lyric [txt]\n"\
                  +keyhelp+" music [txt]\n"\
                  +keyhelp+" vn-id [txt]\n"\
                  +keyhelp+" vn-en [txt]\n"\
                  +keyhelp+" vn-jp [txt]\n"\
                  +keyhelp+" tr-id [txt]\n"\
                  +keyhelp+" tr-cn [txt]\n"\
                  +keyhelp+" tr-ar [txt]\n"\
                  +keyhelp+" tr-en [txt]\n"\
                  +keyhelp+" tr-jp [txt]\n"\
                  +keyhelp+" tr-ko [txt]\n"\
                  +keyhelp+" tr-th [txt]\n"\
                  +keyhelp+" bye\n"\
                  +keyhelp+" summon\n"\
                  +keyhelp+" invite me\n"\
                  +keyhelp+" add all\n"\
                  +keyhelp+" add all\n"\
                  +keyhelp+" spam add:[txt]\n"\
                  +keyhelp+" spam start:[num]\n"\
                  +keyhelp+" group image\n"\
                  +keyhelp+" system\n"\
                  +keyhelp+" iconfig\n"\
                  +keyhelp+" kernel\n"\
                  +keyhelp+" cpu\n"\
                  +keyhelp+" banlist\n"\
                  +keyhelp+" recover\n"\
                  +keyhelp+" team on[contact]\n"\
                  +keyhelp+" team on @[name]\n"\
                  +keyhelp+" team off @[name]\n"\
                  +keyhelp+" team off[contact]\n"\
                  +keyhelp+" speed\n"\
                  +keyhelp+" respown on\n"\
                  +keyhelp+" respown off\n"\
                  +keyhelp+" notify on\n"\
                  +keyhelp+" notify off\n"\
                  +keyhelp+" chatbot on\n"\
                  +keyhelp+" chatbot off\n"\
                  +keyhelp+" protect on\n"\
                  +keyhelp+" protect off\n"\
                  +keyhelp+" mimic on\n"\
                  +keyhelp+" mimic off\n"\
                  +keyhelp+" welcome on\n"\
                  +keyhelp+" welcome off\n"\
                  +keyhelp+" check welcome\n"\
                  +keyhelp+" settings\n"\
                  +keyhelp+" memlist\n"\
                  +keyhelp+" mimic add @[nme]\n"\
                  +keyhelp+" mimic del @[name]\n"\
                  +keyhelp+" mimic list\n"\
                  +keyhelp+" gift [contact]\n"\
                  +keyhelp+" ginfo\n"\
                  +keyhelp+" invite [contact]\n"\
                  +keyhelp+" gcreator\n"\
                  +keyhelp+" glink open\n"\
                  +keyhelp+" glink close\n"\
                  +keyhelp+" gname:[txt]\n"\
                  +keyhelp+" gurl\n"\
                  +keyhelp+" runtime\n"\
                  +keyhelp+" creator\n"\
                  +keyhelp+" set welcome:[txt]\n"\
                  +keyhelp+" check welcome\n"\
                  +keyhelp+" pap set:[link image]\n"\
                  +keyhelp+" pap\n"\
                  +keyhelp+" ban @[name]\n"\
                  +keyhelp+" banned [contact]\n"\
                  +keyhelp+" unban @[name]\n"\
                  +keyhelp+" unbanned [contact]\n"\
                  +keyhelp+" vkick @[name]\n"\
                  +keyhelp+" purge\n"\
                  +keyhelp+" crash\n"\
                  +keyhelp+" ulti @[name]\n"\
                  +keyhelp+" cancel\n"\
                  +keyhelp+" groupcast:[txt]\n"\
                  +keyhelp+" broadcast:[txt]\n"\
                  +keyhelp+" destroy\n"\
                  +keyhelp+" backup run\n"\
                  +keyhelp+" copy @[name]\n"\
                  +keyhelp+" backup\n"\
                  +keyhelp+" rename:[txt]\n"\
                  +keyhelp+" squad name:[txt]\n"\
                  +keyhelp+" bio:[txt]\n"\
                  +keyhelp+" timeline:[txt]\n"\
                  +keyhelp+" reject all\n"\
                  +keyhelp+" remove chat\n"\
                  +keyhelp+" restart\n"\
                  +keyhelp+" spm invite[cntact]\n"\
                  +keyhelp+" changepict\n"\
                  +keyhelp+" join url\n"\
                  +keyhelp+" grouplist\n"\
                  +keyhelp+" blocklist\n"\
                  +keyhelp+" friendlist\n"\
                  +keyhelp+" contact banlist\n"\
                  +keyhelp+" clear banlist\n"\
                  +keyhelp+" clear mimiclist"
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
                     if op.param2 not in team:
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
              if pelaku not in team:
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
           if pelaku in team:
              cl.getGroup(op.param1)
              cl.findAndAddContactsByMid(op.param2)
              cl.inviteIntoGroup(op.param1,[op.param2])

#===================================================================================================================================
#NOTIFIED_CANCEL_INVITATION_GROUP
        if op.type == 32:
           pelaku = op.param2
           korban = op.param3
           if wait["protectall"] == True:
              if pelaku not in team:
                 cl.getGroup(op.param1)
                 cl.kickoutFromGroup(op.param1,[op.param2])
                 targets = [op.param2]
                 for target in targets:
                     wait["blacklist"][target] = True
                     f=codecs.open('st2__b.json','w','utf-8')
                     json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
        if op.type == 32:
           pelaku = op.param2
           korban = op.param3
           if korban in team:
             cl.getGroup(op.param1)
             cl.kickoutFromGroup(op.param1,[op.param2])
             cl.findAndAddContactsByMid(op.param3)
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
             	if pelaku in team:
           	   cl.getGroup(op.param1)
                   cl.acceptGroupInvitation(op.param1)



        if op.type == 13:
            if wait["protectall"] == True:
               if op.param2 not in team:
        	  cl.getGroup(op.param1)
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  cl.cancelGroupInvitation(op.param1,[op.param3])
                  targets = [op.param2]
                  for target in targets:
                       wait["blacklist"][target] = True
                       f=codecs.open('st2__b.json','w','utf-8')
                       json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#=====================================================================================================================================
#NOTIFIED_ACCEPT_GROUP_INVITATION
        if op.type == 17:
            if op.param3 in wait["blacklist"]:
               if op.param3 not in team:
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
                 contact = cl.getContact(op.param2)
                 cl.sendText(op.param1,cl.getContact(op.param2).displayName +"\n"+ wait["welmsg"])


#========================================================================================================================
#NOTIFIED_KICKOUT_FROM_GROUP
        
        if op.type == 19:
           if op.param3 in team:
              if op.param2 not in team:
                 cl.kickoutFromGroup(op.param1,[op.param2])
                 cl.inviteIntoGroup(op.param1,[op.param3])
              else:
                     cl.inviteIntoGroup(op.param1,[op.param3])
                     wait["blacklist"][op.param2] = True
                     f=codecs.open('st2__b.json','w','utf-8')
                     json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
        if op.type == 19:
           if wait["protectall"] == True:
              if op.param3 not in team:
              	 if op.param2 not in team:
                        cl.kickoutFromGroup(op.param1,[op.param2])
           	        cl.inviteIntoGroup(op.param1,[op.param3])
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)


#=====================================================================================================================================
                

        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if wait['alwaysread'] == True:
                msg = op.message
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)
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
                if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendText(msg.to,text)
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                  if wait["responMention"] == True:
                    names = re.findall(r'@(\w+)',msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        if mention['M'] in mid:
                            xname = cl.getContact(msg.from_).displayName
                            xlen = str(len(xname)+1)
                            msg.contentType = 0
                            balas = "@" + xname + " " + str(wait["reply"])
                            msg.text = balas
                            msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(msg.from_)+'}]}','EMTVER':'4'}
                            cl.sendMessage(msg)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == msg.to:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            cl.sendText(msg.to,"succes joined to group \n"+X.name)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)

        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")
                        
               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Deleted")
                        wait["dblack"] = False
                        
                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already in the blacklist")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"successfully load users into the blacklist")
                        
               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"successfully removed from the blacklist")
                        
                        wait["dblacklist"] = False
                        
                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = "http://dl.profile.line-cdn.net/" + (str(contact.pictureStatus))
                        try:
                            cl.sendImageWithURL(msg.to, str(path))
                        except:
                            pass
                        ret_ = "Details Contact"
                        ret_ += "\n\nNama: " + (str(contact.displayName))
                        ret_ += "\n\nMid : " + (str(msg.contentMetadata["mid"]))
                        ret_ += "\n\nBio : " + (str(contact.statusMessage))
                        ret_ += "\n\nLink: " + "http://dl.profile.line-cdn.net/" + (str(contact.pictureStatus))

                        cl.sendText(msg.to, str(ret_))
                        wait["contact"] = False
                    else:
                        cl.sendText(msg.to,"contact not found")
                        wait["contact"] = False
            elif msg.contentType == 1:
            	if msg.from_ in pencipta:
                     if wait["cpp"] == True:
                        path = cl.downloadObjectMsgId(msg.id)
                        wait["cpp"] = False
                        cl.updateProfilePictureee(path)
                        cl.sendText(msg.to, "success change profile picture")
     
            

            elif msg.contentType == 16:
                if wait["post"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL→\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            
  
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
            	if wait["winvite"] == True:
                     if msg.from_ in team:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 cl.sendText(msg.to,"use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         cl.findAndAddContactsByMid(invite)
                                         cl.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         cl.sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break
        if op.type == 26:                                 
            msg = op.message
            if msg.contentType == 13:
            	if wait["giftcontact"] == True:
                  if msg.from_ in team:
            		dodol = msg.contentMetadata["displayName"]
            		jeruk = msg.contentMetadata["mid"]
            		kumpulan = cl.getGroup(msg.to)
            		penunggu = kumpulan.invitee
            		targets = []
            		for kucing in kumpulan.members:
            			if dodol in kucing.displayName:
            				print "sukses gift target"
            				break
            			else:
            				targets.append(jeruk)
               	        if targets == []:
            	    	   pass
            	        else:
            	    	    for nanas in targets:
           
            	    			cl.sendText(msg.to,"gift to target succes")
            	    			msg.contentType = 9
            	    			msg.contentMetadata = {'PRDID':'9a076833-c2d3-4189-9653-2909e9bb6f58',
                                                      'PRDTYPE':'THEME',
                                                      'MSGTPL':'10'}
            	    			msg.to = nanas
            	    			msg.text = None
            	    			cl.sendMessage(msg)
            	    			wait["giftcontact"] = False
            	    			break
      
        if op.type == 26:                                 
            msg = op.message
            if msg.contentType == 13:
                if wait["spam"] == True:
                  if msg.from_ in pencipta:
                    dodol = msg.contentMetadata["displayName"]
                    jeruk = msg.contentMetadata["mid"]
                    kumpulan = cl.getGroup(msg.to)
                    penunggu = kumpulan.invitee
                    targets = []
                    for kucing in kumpulan.members:
                        if dodol in kucing.displayName:
                            print "sukses spam invite group"
                            break
                        else:
                            targets.append(jeruk)
                    if targets == []:
                        pass
                    else:
                        for nanas in targets:
                                ghost= str(nanas.mid)
                                cl.sendText(msg.to,"succes spam invite to target")
                                cl.findAndAddContactsByMid(ghost)
                                cl.createGroup("spammed1",nanas)
                                cl.createGroup("spammed2",nanas)
                                cl.createGroup("spammed3",nanas)
                                cl.createGroup("spammed4",nanas)
                                cl.createGroup("spammed5",nanas)
                                cl.createGroup("spammed6",nanas)
                                cl.createGroup("spammed7",nanas)
                                cl.createGroup("spammed8",nanas)
                                cl.createGroup("spammed9",nanas)
                                cl.createGroup("spammed10",nanas)
                                cl.createGroup("spammed11",nanas)
                                cl.createGroup("spammed12",nanas)
                                cl.createGroup("spammed13",nanas)
                                cl.createGroup("spammed14",nanas)
                                cl.createGroup("spammed15",nanas)
                                wait["spam"] = False
                                break
                
        
                  
#=====================================================================================================
#mendaftarkan sebagai admin
#===================================
        if op.type == 26:                                 
            msg = op.message           
            if msg.contentType == 13:
                if wait["team"] == True:
                  if msg.from_ in pencipta:
                      dodol = msg.contentMetadata["displayName"]
                      jeruk = msg.contentMetadata["mid"]
                      kumpulan = cl.getGroup(msg.to)
                      penunggu = kumpulan.invitee
                      targets = []
                      for kucing in kumpulan.members:
                          if dodol in kucing.displayName:
                              print "sukses add team"
                              break
                          else:
                              targets.append(jeruk)
                      if targets == []:
                          pass
                      else:
                          for nanas in targets:
                                 team.append(nanas)
                                 cl.sendText(msg.to,dodol + "\nhas been added as team")
                                 wait["team"] = False
                                 break
                 
        if op.type == 26:                                 
            msg = op.message           
            if msg.contentType == 13:
                if wait["unteam"] == True:
                  if msg.from_ in pencipta:
                      dodol = msg.contentMetadata["displayName"]
                      jeruk = msg.contentMetadata["mid"]
                      kumpulan = cl.getGroup(msg.to)
                      penunggu = kumpulan.invitee
                      targets = []
                      for kucing in kumpulan.members:
                          if dodol in kucing.displayName:
                              print "sukses demote team"
                              break
                          else:
                              targets.append(jeruk)
                      if targets == []:
                          pass
                      else:
                          for nanas in targets:
                                 team.remove(nanas)
                                 cl.sendText(msg.to,dodol + "\nhas been demote from team")
                                 wait["unteam"] = False
                                 break
    

#========================================you can edit from here===============================================================================================================
            elif msg.text.lower() == "responsename":
            	if msg.from_ in team:
                      profile = cl.getProfile()
                      text = profile.displayName
                      cl.sendText(msg.to, text)
#====================================================================================================
            elif msg.text.lower() == koala + " invite me":
                if msg.from_ in pencipta:
                	 cl.sendText(msg.to, "successfully invited you to all groups")
                         gid = cl.getGroupIdsJoined()
		         for i in gid:
			     cl.findAndAddContactsByMid(msg.from_)
                             cl.inviteIntoGroup(i,[msg.from_])
            elif msg.text.lower() == squad + " invite me":
                if msg.from_ in pencipta:
                	 cl.sendText(msg.to, "successfully invited you to all groups")
                         gid = cl.getGroupIdsJoined()
		         for i in gid:
			     cl.findAndAddContactsByMid(msg.from_)
                             cl.inviteIntoGroup(i,[msg.from_])
#=========================================================================================================================


            elif msg.text.lower() == koala + " menu":
            	if msg.from_ in team:
                      print "\nHelp pick up..."
                      if wait["lang"] == "JP":
                      	  gfd = helpMessage()
                          cl.sendText(msg.to,gfd)
                      else:
                          cl.sendText(msg.to,"eror")
            
#=============================================================================================================================
            elif koala + " getmid" in msg.text.lower():
            	if msg.from_ in team:
                      key = eval(msg.contentMetadata["MENTION"])
                      key1 = key["MENTIONEES"][0]["M"]
                      cl.sendText(msg.to, key1)
            
#==============================================================================================================================
            elif koala + " getbio" in msg.text.lower():
            	if msg.from_ in team:
                      key = eval(msg.contentMetadata["MENTION"])
                      key1 = key["MENTIONEES"][0]["M"]
                      contact = cl.getContact(key1)
                      try:
                          cl.sendText(msg.to, "[StatusMessage]\n" + contact.statusMessage)
                      except:
                          cl.sendText(msg.to, "[StatusMessage]\n" + contact.statusMessage)
           
#===============================================================================================================================
            elif koala + " getname" in msg.text.lower():
            	if msg.from_ in team:
                      key = eval(msg.contentMetadata["MENTION"])
                      key1 = key["MENTIONEES"][0]["M"]
                      contact = cl.getContact(key1)
                      try:
                          cl.sendText(msg.to, "[DisplayName]\n" + contact.displayName)
                      except:
                          cl.sendText(msg.to, "[DisplayName]\n" + contact.displayName)
            
#=============================================================================================================================

            elif koala + " getcontact" in msg.text.lower():
            	if msg.from_ in team:
                      key = eval(msg.contentMetadata["MENTION"])
                      key1 = key["MENTIONEES"][0]["M"]                
                      msg.contentType = 13
                      msg.contentMetadata = {"mid":key1}
                      cl.sendMessage(msg)
            
#================================================================================================================================

            elif koala + " getpict" in msg.text.lower():
            	if msg.from_ in team:
                      key = eval(msg.contentMetadata["MENTION"])
                      key1 = key["MENTIONEES"][0]["M"]
                      contact = cl.getContact(key1)
                      targets = []
                      targets.append(contact.mid)
                      if targets == []:
                          cl.sendText(msg.to,"Contact not found")
                      else:
                          for target in targets:
                              try:
                                  contact = cl.getContact(target)
                                  path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                  cl.sendImageWithURL(msg.to, path)
                              except Exception as e:
                                  raise e
            
#=========================================================================================================================


            elif msg.text.lower() == koala + " gift1":
            	if msg.from_ in team:
                      msg.contentType = 9
                      msg.contentMetadata={'PRDID': '9a076833-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '1'}
                      msg.text = None
                      cl.sendMessage(msg)
            
#========================================================================================================================

            elif msg.text.lower() == koala + " gift2":
            	if msg.from_ in team:
                      msg.contentType = 9
                      msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '2'}
                      msg.text = None
                      cl.sendMessage(msg)
            
#===============================================================================================================================

            elif msg.text.lower() == koala + " gift3":
            	if msg.from_ in team:
                      msg.contentType = 9
                      msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '3'}
                      msg.text = None
                      cl.sendMessage(msg)
            
 #==========================================================================================================================

            elif msg.text.lower() == koala + " getinfo":
                if msg.from_ in team:
                      wait["contact"] = True
                      cl.sendText(msg.to,"send a contact to getinfo")
            
#=========================================================================================================================

            elif koala + " say " in msg.text.lower():
            	if msg.from_ in team:
            		pisah = msg.text.split("say ")
            		isi = msg.text.replace(pisah[0]+"say ","")
            		cl.sendText(msg.to,isi)
            elif squad + " say " in msg.text.lower():
            	if msg.from_ in team:
            		pisah = msg.text.split("say ")
            		isi = msg.text.replace(pisah[0]+"say ","")
            		cl.sendText(msg.to,isi)
#=========================================================================================================================
   
            elif msg.text.lower() == koala + " teamlist":
            	if msg.from_ in team:
            	   	 	   	   cl.sendText(msg.to,"loading...........")
            	   	 	   	   ow = ""
            	   	 	   	   for mi_d in team:
            	   	 	   	   	   ow += "• " + cl.getContact(mi_d).displayName + "\n"
            	   	 	   	   cl.sendText(msg.to,"━━━━♚TEAM♚━━━━\n"+ow)
            elif msg.text.lower() == squad + " teamlist":
            	if msg.from_ in team:
            	   	 	   	   cl.sendText(msg.to,"loading...........")
            	   	 	   	   ow = ""
            	   	 	   	   for mi_d in team:
            	   	 	   	   	   ow += "• " + cl.getContact(mi_d).displayName + "\n"
            	   	 	   	   cl.sendText(msg.to,"━━━━♚TEAM♚━━━━\n"+ow)
     #======================================================================================================================
            elif msg.text.lower() == koala + " lurk on":
              if msg.from_ in team:
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        cl.sendText(msg.to,"Lurking already on")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    cl.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                    print wait2
            
#=======================================================================================================================
            elif msg.text.lower() == koala + " lurk off":
              if msg.from_ in team:
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to,"Lurking already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))
            
#===============================================================================================================================

            elif msg.text.lower() == koala + " lurking":
                if msg.from_ in team:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             cl.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to,"List Lurking\n\n%s\n\nLurking time: %s\nCurrent time: %s"%(wait2['readMember'][msg.to],wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S')))
            
#===========================================================================================================================
            elif msg.text.lower() == koala + " date":
            	if msg.from_ in team:
	    	      wait2['setTime'][msg.to] = datetime.today().strftime('date : %Y-%m-%d \nday : %A \ntime : %H:%M:%S')
	              cl.sendText(msg.to, "calendar\n\n" + (wait2['setTime'][msg.to]))

#=========================================================================================================================
            elif msg.text.lower() == koala + " my picture":
            	if msg.from_ in team:
                    h = cl.getContact(msg.from_)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            
#=======================================================================================================================
            elif msg.text.lower() == koala + " my status":
                if msg.from_ in team:
                    h = cl.getContact(msg.from_)
                    cl.sendText(msg.to,"[Status Message]\n" + h.statusMessage)
            
#====================================================================================================================
            elif msg.text.lower() == koala + " my name":
            	if msg.from_ in team:
                    h = cl.getContact(msg.from_)
                    cl.sendText(msg.to,"[Display Name]\n" + h.displayName)
            
#====================================================================================================================
            elif msg.text.lower() == koala + " my contact":
				if msg.from_ in team:
					msg.contentType = 13
					msg.contentMetadata = {'mid': msg.from_}
					cl.sendMessage(msg)
            
#========================================================================================================================
            elif msg.text.lower() == koala + " my mid":
            	if msg.from_ in team:
            		cl.sendText(msg.to,msg.from_)
            
#=====================================================================================================================
            elif koala + " instagram " in msg.text.lower():
                if msg.from_ in team:
                   try:
                       pisah = msg.text.split("m ")
                       instagram = msg.text.replace(pisah[0]+"m ","")
                       response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                       data = response.json()
                       namaUSER = str(data['user']['full_name'])
                       bioUSER = str(data['user']['biography'])
                       media = str(data['user']['media']['count'])
                       verifIG = str(data['user']['is_verified'])
                       username = str(data['user']['username'])
                       follower = str(data['user']['followed_by']['count'])
                       profile = data['user']['profile_pic_url_hd']
                       private = str(data['user']['is_private'])
                       followIG = str(data['user']['follows']['count'])
                       link = "Title: " + "https://www.instagram.com/" + instagram
                       text = "\n\nName: " + namaUSER
                       text +="\n\nUsername: " + username
                       text +="\n\n\nBiography: " + bioUSER
                       text +="\n\nFollower: " + follower
                       text +="\n\nFollowing: " + followIG
                       text +="\n\nPost: " + media
                       text +="\n\nVerified: " + verifIG
                       text +="\n\nPrivate: " + private
                       text +="\n\nURL: " + link
                       cl.sendImageWithURL(msg.to, profile)
                       cl.sendText(msg.to, str(text))
                   except Exception as e:
                       cl.sendText(msg.to, str(e))
            
#=============================================================================================================
            elif koala + " wikipedia " in msg.text.lower():
                if msg.from_ in team:
                      pisah = msg.text.split("a ")
                      wiki = msg.text.replace(pisah[0]+"a ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+="\nOver Text limit! please click link"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                      
            
#===============================================================================================================================
            elif koala + " youtube " in msg.text.lower():
                if msg.from_ in team:
                   query = msg.text.split("e ")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))
#=================================================================================================================
            elif koala + " youtubedl " in msg.text.lower():
            	if msg.from_ in team:
            		pisah = msg.text.split("youtubedl ")
            		bahan = msg.text.replace(pisah[0]+"youtubedl ","")
            		vid = pafy.new(bahan)
                        stream = vid.streams
                        for s in stream:
                            vin = vid.title + "\n\nLink Download" + s.url
                        cl.sendText(msg.to,vin)
                                  
#==========================================================================================================================
            elif koala + " image " in msg.text.lower():
                if msg.from_ in team:
                    pisah = msg.text.split("e ")
            	    search = msg.text.replace(pisah[0]+"e ","")
                    url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                    raw_html = (download_page(url))
                    items = []
                    items = items + (_images_get_all_items(raw_html))
                    path = random.choice(items)
                    print path
                    try:
                        cl.sendImageWithURL(msg.to,path)
                    except:
                        pass
            
                                
#=====================================================================================================================
            elif koala + " meme1" in msg.text:
            	if msg.from_ in team:
            		pisah = msg.text.split(" ")
            		bahann = ("https://memegen.link/" + meme["meme1"] + "/" + str(pisah[2]) + "/" + str(pisah[3]) + ".jpg")
            		cl.sendImageWithURL(msg.to,bahann)
            
#===============================================================================================================
	    elif koala + " meme2" in msg.text.lower():
            	if msg.from_ in team:
            		pisah = msg.text.split(" ")
            		bahann = ("https://memegen.link/" + meme["meme2"] + "/" + str(pisah[2]) + "/" + str(pisah[3]) + ".jpg")
            		cl.sendImageWithURL(msg.to,bahann)
            
#=============================================================================================================
            elif koala + " meme3" in msg.text.lower():
            	if msg.from_ in team:
            		pisah = msg.text.split(" ")
            		bahann = ("https://memegen.link/" + meme["meme3"] + "/" + str(pisah[2]) + "/" + str(pisah[3]) + ".jpg")
            		cl.sendImageWithURL(msg.to,bahann)
            
#==============================================================================================================
            elif koala + " meme4" in msg.text.lower():
            	if msg.from_ in team:
            		pisah = msg.text.split(" ")
            		bahann = ("https://memegen.link/" + meme["meme4"] + "/" + str(pisah[2]) + "/" + str(pisah[3]) + ".jpg")
            		cl.sendImageWithURL(msg.to,bahann)
            
#=============================================================================================================
            elif koala + " meme5" in msg.text.lower():
            	if msg.from_ in team:
            		pisah = msg.text.split(" ")
            		bahann = ("https://memegen.link/" + meme["meme5"] + "/" + str(pisah[2]) + "/" + str(pisah[3]) + ".jpg")
            		cl.sendImageWithURL(msg.to,bahann)
            
#================================================================================================================
            elif koala + " meme6" in msg.text.lower():
            	if msg.from_ in team:
            		pisah = msg.text.split(" ")
            		bahann = ("https://memegen.link/" + meme["meme6"] + "/" + str(pisah[2]) + "/" + str(pisah[3]) + ".jpg")
            		cl.sendImageWithURL(msg.to,bahann)
            
#==========================================================================================================
            elif koala + " meme7" in msg.text.lower():
            	if msg.from_ in team:
            		pisah = msg.text.split(" ")
            		bahann = ("https://memegen.link/" + meme["meme7"] + "/" + str(pisah[2]) + "/" + str(pisah[3]) + ".jpg")
            		cl.sendImageWithURL(msg.to,bahann)
            
#==============================================================================================================
            elif koala + " meme8" in msg.text.lower():
            	if msg.from_ in team:
            		pisah = msg.text.split(" ")
            		bahann = ("https://memegen.link/" + meme["meme8"] + "/" + str(pisah[2]) + "/" + str(pisah[3]) + ".jpg")
            		cl.sendImageWithURL(msg.to,bahann)
            
#=======================================================================================================
            elif koala + " meme9" in msg.text.lower():
            	if msg.from_ in team:
            		pisah = msg.text.split(" ")
            		bahann = ("https://memegen.link/" + meme["meme9"] + "/" + str(pisah[2]) + "/" + str(pisah[3]) + ".jpg")
            		cl.sendImageWithURL(msg.to,bahann)
            
#==========================================================================================================
            elif koala + " meme10" in msg.text.lower():
            	if msg.from_ in team:
            		pisah = msg.text.split(" ")
            		bahann = ("https://memegen.link/" + meme["meme10"] + "/" + str(pisah[2]) + "/" + str(pisah[3]) + ".jpg")
            		cl.sendImageWithURL(msg.to,bahann)
            
#==================================================================================================================

            elif koala + " location " in msg.text.lower():
            	if msg.from_ in team:
                            pisah = msg.text.split("n ")
                            location = msg.text.replace(pisah[0]+"n ","")
                            params = {'lokasi':location}
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(sett["userAgent"])
                                r = requests.get("http://api.corrykalam.net/apiloc.php?"+ urllib.urlencode(params))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "[ Details Location ]"
                                    ret_ += "\n\nLocation : " + data[0]
                                    ret_ += "\nGoogle Maps : " + link
                                else:
                                    ret_ = "[ Details Location ] Error : Location not found"
                                cl.sendText(msg.to, str(ret_))
                                                                    
#===================================================================================================================

            elif koala + " weather " in msg.text.lower():
            	if msg.from_ in team:
                            pisah = msg.text.split("r ")
                            location = msg.text.replace(pisah[0]+"r ","")
                            params = {'kota':location}
                            with requests.session() as web:
                            	web.headers["user-agent"] = random.choice(sett["userAgent"])
                                r = requests.get("http://api.corrykalam.net/apicuaca.php?" + urllib.urlencode(params))
                                data = r.text
                                data = json.loads(data)
                                if "result" not in data:
                                    ret_ = "[ Weather Status ]"
                                    ret_ += "\n\nLocation: " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\nTemperature: " + data[1].replace("Suhu : ","")
                                    ret_ += "\nHumidity: " + data[2].replace("Kelembaban : ","")
                                    ret_ += "\nAir pressure: " + data[3].replace("Tekanan udara : ","")
                                    ret_ += "\nWind velocity: " + data[4].replace("Kecepatan angin : ","")
                                else:
                                    ret_ = "[ Weather Status ] Error : Location not found"
                                cl.sendText(msg.to, str(ret_))
                                                                        
#=================================================================================================================
            elif koala + " praytime " in msg.text.lower():
            	if msg.from_ in team:
                            pisah = msg.text.split("e ")
                            location = msg.text.replace(pisah[0]+"e ","")
                            params = {'lokasi':location}
                            with requests.session() as web:
                                r = requests.get("http://api.corrykalam.net/apisholat.php?" + urllib.urlencode(params))
                                data = r.text
                                data = json.loads(data)
                                if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashr : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                    ret_ = "[ Prayer Schedule ]"
                                    ret_ += "\n\nLocation : " + data[0]
                                    ret_ += "\n" + data[1]
                                    ret_ += "\n" + data[2]
                                    ret_ += "\n" + data[3]
                                    ret_ += "\n" + data[4]
                                    ret_ += "\n" + data[5]
                                else:
                                    ret_ = "[ Prayer Schedule ] Error : Location not found" 
                                cl.sendText(msg.to, str(ret_))
                                                    
#==========================================================================================================================
            elif koala + " lyric " in msg.text.lower():
                if msg.from_ in team:
                   try:
                           pisah = msg.text.split("lyric ")
                           songname = msg.text.replace(pisah[0]+"lyric ","")
                           params = {'songname': songname}
                           r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                           data = r.text
                           data = json.loads(data)
                           for song in data:
                               hasil = 'Song Lyrics ('
                               hasil += song[0]
                               hasil += ')\n\n'
                               hasil += song[5]
                               cl.sendText(msg.to, hasil)
                   except Exception as wak:
                               cl.sendText(msg.to, str(wak))
                
#=================================================================================================================

            elif koala + " music " in msg.text.lower():
                if msg.from_ in team:
                    pisah = msg.text.split("c ")
                    songname = msg.text.replace(pisah[0]+"c ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Title: ' + song[0]
                        hasil += '\nDuration: ' + song[1]
                        hasil += '\nDownload Link: ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
              
            
                
#================================================================================================================
            elif koala + " vn-id " in msg.text.lower():
            	if msg.from_ in team:
            		pisah = msg.text.split("d ")
            		psn = msg.text.replace(pisah[0]+"d ","")
            		tts = gTTS(psn, lang='id', slow=False)
            		tts.save('tts.mp3')
            		cl.sendAudio(msg.to, 'tts.mp3')
            
#==================================================================================================================
            elif koala + " vn-en " in msg.text.lower():
            	if msg.from_ in team:
            		pisah = msg.text.split("n ")
            		psn = msg.text.replace(pisah[0]+"n ","")
            		tts = gTTS(psn, lang='en', slow=False)
            		tts.save('tts.mp3')
            		cl.sendAudio(msg.to, 'tts.mp3')
            
#=========================================================================================================
            elif koala + " vn-jp " in msg.text.lower():
            	if msg.from_ in team:
            		pisah = msg.text.split("p ")
            		psn = msg.text.replace(pisah[0]+"p ","")
            		tts = gTTS(psn, lang='ja', slow=False)
            		tts.save('tts.mp3')
            		cl.sendAudio(msg.to, 'tts.mp3')
            
#================================================================================================
            elif koala + " tr-id " in msg.text.lower():
            	if msg.from_ in team:
            		  pisah = msg.text.split("tr-id ")
            		  gtgt = msg.text.replace(pisah[0]+ "tr-id ","")
            		  try:
            		      translator = Translator()
            		      trs = translator.translate(gtgt,'id')
            		      A = trs.text
            		      A = A.encode('utf-8')
            		      cl.sendText(msg.to,A)
            		  except:
            		  	     cl.sendText(msg.to,"eror")
#=================================================================================================================
            elif koala + " tr-en " in msg.text.lower():
            	if msg.from_ in team:
            		  pisah = msg.text.split("tr-en ")
            		  gtgt = msg.text.replace(pisah[0]+ "tr-en ","")
            		  try:
            		      translator = Translator()
            		      trs = translator.translate(gtgt,'en')
            		      A = trs.text
            		      A = A.encode('utf-8')
            		      cl.sendText(msg.to,A)
            		  except:
            		  	     cl.sendText(msg.to,"eror")
            
#===========================================================================================================
            elif koala + " tr-ar " in msg.text.lower():
            	if msg.from_ in team:
            		  pisah = msg.text.split("tr-ar ")
            		  gtgt = msg.text.replace(pisah[0]+ "tr-ar ","")
            		  try:
            		      translator = Translator()
            		      trs = translator.translate(gtgt,'ar')
            		      A = trs.text
            		      A = A.encode('utf-8')
            		      cl.sendText(msg.to,A)
            		  except:
            		  	     cl.sendText(msg.to,"eror")
            
#==================================================================================================================
            elif koala + " tr-ko " in msg.text.lower():
            	if msg.from_ in team:
            		  pisah = msg.text.split("tr-ko ")
            		  gtgt = msg.text.replace(pisah[0]+ "tr-ko ","")
            		  try:
            		      translator = Translator()
            		      trs = translator.translate(gtgt,'ko')
            		      A = trs.text
            		      A = A.encode('utf-8')
            		      cl.sendText(msg.to,A)
            		  except:
            		  	     cl.sendText(msg.to,"eror")
            
#==================================================================================================================
            elif koala + " tr-th " in msg.text.lower():
            	if msg.from_ in team:
            		  pisah = msg.text.split("tr-th ")
            		  gtgt = msg.text.replace(pisah[0]+ "tr-th ","")
            		  try:
            		      translator = Translator()
            		      trs = translator.translate(gtgt,'th')
            		      A = trs.text
            		      A = A.encode('utf-8')
            		      cl.sendText(msg.to,A)
            		  except:
            		  	     cl.sendText(msg.to,"eror")
            
#=============================================================================================================
            elif koala + " tr-cn " in msg.text.lower():
            	if msg.from_ in team:
            		  pisah = msg.text.split("tr-cn ")
            		  gtgt = msg.text.replace(pisah[0]+ "tr-cn ","")
            		  try:
            		      translator = Translator()
            		      trs = translator.translate(gtgt,'zh-cn')
            		      A = trs.text
            		      A = A.encode('utf-8')
            		      cl.sendText(msg.to,A)
            		  except:
            		  	     cl.sendText(msg.to,"eror")
            
#===================================================================================================================
            elif koala + " tr-jp " in msg.text.lower():
            	if msg.from_ in team:
            		  pisah = msg.text.split("tr-jp ")
            		  gtgt = msg.text.replace(pisah[0]+ "tr-jp ","")
            		  try:
            		      translator = Translator()
            		      trs = translator.translate(gtgt,'ja')
            		      A = trs.text
            		      A = A.encode('utf-8')
            		      cl.sendText(msg.to,A)
            		  except:
            		  	     cl.sendText(msg.to,"eror")
            
#===========command for admin only================================================================================================
            elif msg.text.lower() == koala + " bye":
            	if msg.from_ in team:
            		cl.getGroup(msg.to)
            		cl.sendText(msg.to,"see you later")
            		cl.leaveGroup(msg.to)
            
#======================================================================================================================
            elif msg.text.lower() == koala + " summon":
              if msg.from_ in team:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 100:
                    mention(msg.to, nama)
                if jml > 100 and jml < 200:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, len(nama)):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                if jml > 200 and jml < 300:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                if jml > 300 and jml < 400:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                if jml > 400 and jml < 500:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, 400):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                    for h in range(401, len(nama)):
                        nm5 += [nama[h]]
                    mention(msg.to, nm5)
                if jml > 500:
                    print "pickup mention command"
                cnt = Message()
                cnt.text = "total mention: "+str(jml)
                cnt.to = msg.to
                cl.sendMessage(cnt)
            
#======================================================================================================================
            elif msg.text.lower() == koala + " add all":
                if msg.from_ in team:
                   thisgroup = cl.getGroup(msg.to)
                   Mids = [contact.mid for contact in thisgroup[0].members]
                   cl.findAndAddContactsByMids(Mids)
                   cl.sendText(msg.to,"Success Add all")
            
#===================================================================================================================
            elif koala + " spam add:" in msg.text.lower():
            	if msg.from_ in team:
            	   pisah = msg.text.split(":")
                   wait["spam"] = msg.text.replace(pisah[0]+":","")
                   cl.sendText(msg.to,"spam changed")
            elif koala + " squad name:" in msg.text.lower():
            	if msg.from_ in pencipta:
            	   pisah = msg.text.split(":")
                   wait["squad"] = msg.text.replace(pisah[0]+":","")
                   cl.sendText(msg.to,"name squad changed")
#=============================================================================================================
            elif msg.text.lower() == koala + " spam start:":
            	if msg.from_ in team:
                   pisah = msg.text.split(":")
                   strnum = msg.text.replace(pisah[0]+":","")
                   num = int(strnum)
                   for var in range(0,num):
                       cl.sendText(msg.to, wait["spam"])
            
#==================================================================================================================
            elif msg.text.lower() == koala + " group image":
            	if msg.from_ in team:
                   group = cl.getGroup(msg.to)
                   path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                   cl.sendImageWithURL(msg.to,path)
            
#=====================================================================================================================
            elif msg.text.lower() == koala + " system":
            	if msg.from_ in team:
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n==SERVER INFO SYSTEM==")
            
#==============================================================================================================
            elif msg.text.lower() == koala + " iconfig":
            	if msg.from_ in team:
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n==SERVER INFO NetStat==")
            
#=======================================================================================================================
            elif msg.text.lower() == koala + " kernel":
            	if msg.from_ in team:
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n==SERVER INFO KERNEL==")
            
#===================================================================================================================

            elif msg.text.lower() == koala + " cpu":
            	if msg.from_ in team:
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n==SERVER INFO CPU==")
            
#=======================================================================================================================
            elif msg.text.lower() == koala + " team on":
                if msg.from_ in pencipta:
                      wait["team"] = True
                      cl.sendText(msg.to,"send a contact to make team")
                else:
                	 cl.sendText(msg.to,"command denied")
                	 cl.sendText(msg.to,"creator permission recuired")
            elif msg.text.lower() == squad + " team on":
                if msg.from_ in pencipta:
                      wait["team"] = True
                      cl.sendText(msg.to,"send a contact to make team")
                else:
                	 cl.sendText(msg.to,"command denied")
                	 cl.sendText(msg.to,"creator permission recuired")
#=========================================================================================================================
            elif msg.text.lower() == koala + " team off":
                if msg.from_ in pencipta:
                      wait["unteam"] = True
                      cl.sendText(msg.to,"send a contact to demote")
                else:
                	 cl.sendText(msg.to,"command denied")
                	 cl.sendText(msg.to,"creator permission recuired")
            elif msg.text.lower() == squad + " team off":
                if msg.from_ in pencipta:
                      wait["unteam"] = True
                      cl.sendText(msg.to,"send a contact to demote")
                else:
                	 cl.sendText(msg.to,"command denied")
                	 cl.sendText(msg.to,"creator permission recuired")
#===============================================================================================================
            elif koala + " team on" in msg.text.lower():
                   if msg.from_ in pencipta:
                      key = eval(msg.contentMetadata["MENTION"])
                      key1 = key["MENTIONEES"][0]["M"]
                      contact = cl.getContact(key1)
                      targets = []
                      targets.append(contact.mid)
                      if targets == []:
                          cl.sendText(msg.to,"Contact not found")
                      else:
                          for target in targets:
                              try:
                                  team.append(target)
                                  cl.sendText(msg.to, contact.displayName + "\nhas been added as team")
                              except:
                                pass
                   else:
                        cl.sendText(msg.to,"contact not found")
            elif squad + " team on" in msg.text.lower():
                   if msg.from_ in pencipta:
                      key = eval(msg.contentMetadata["MENTION"])
                      key1 = key["MENTIONEES"][0]["M"]
                      contact = cl.getContact(key1)
                      targets = []
                      targets.append(contact.mid)
                      if targets == []:
                          cl.sendText(msg.to,"Contact not found")
                      else:
                          for target in targets:
                              try:
                                  team.append(target)
                                  cl.sendText(msg.to, contact.displayName + "\nhas been added as team")
                              except:
                                pass
                   else:
                        cl.sendText(msg.to,"contact not found")
            
#===================================================================================================================
            elif koala + " team off" in msg.text.lower():
                   if msg.from_ in pencipta:
                      key = eval(msg.contentMetadata["MENTION"])
                      key1 = key["MENTIONEES"][0]["M"]
                      contact = cl.getContact(key1)
                      targets = []
                      targets.append(contact.mid)
                      if targets == []:
                          cl.sendText(msg.to,"Contact not found")
                      else:
                          for target in targets:
                              try:
                                  team.remove(target)
                                  cl.sendText(msg.to, contact.displayName + "\nhas been demote from team")
                              except:
                                pass
                   else:
                	 cl.sendText(msg.to,"command denied")
                	 cl.sendText(msg.to,"creator permission recuired")
            elif squad + " team off" in msg.text.lower():
                   if msg.from_ in pencipta:
                      key = eval(msg.contentMetadata["MENTION"])
                      key1 = key["MENTIONEES"][0]["M"]
                      contact = cl.getContact(key1)
                      targets = []
                      targets.append(contact.mid)
                      if targets == []:
                          cl.sendText(msg.to,"Contact not found")
                      else:
                          for target in targets:
                              try:
                                  team.remove(target)
                                  cl.sendText(msg.to, contact.displayName + "\nhas been demote from team")
                              except:
                                pass
                   else:
                	 cl.sendText(msg.to,"command denied")
                	 cl.sendText(msg.to,"creator permission recuired")
            
#=================================================================================================================
            
#===================================================================================================================
            elif msg.text.lower() == koala + " speed":
                if msg.from_ in team:
                   start = time.time()
                   time.sleep(0.1)
                   cl.sendText(msg.to, "loading.............")
                   elapsed_time = time.time() - start
                   cl.sendText(msg.to, "%sseconds" % (elapsed_time))
            elif msg.text.lower() == squad + " speed":
                if msg.from_ in team:
                   start = time.time()
                   time.sleep(0.1)
                   cl.sendText(msg.to, "loading.............")
                   elapsed_time = time.time() - start
                   cl.sendText(msg.to, "%sseconds" % (elapsed_time))
#===================================================================================================================
            elif msg.text.lower() == koala + " notify on":
                if msg.from_ in team:
                      settings["post"] = True
                      cl.sendText(msg.to,"notification has been enabled")
            
#======================================================================================================================
            elif msg.text.lower() == koala + " notify off":
                if msg.from_ in team:
                      settings["post"] = False
                      cl.sendText(msg.to,"notification has been disabled")
            
#=================================================================================================================
            elif msg.text.lower() == koala + " welcome on":
                if msg.from_ in team:
                      settings["welcomemsg"] = True
                      cl.sendText(msg.to,"welcome message has been enabled")
            
#=================================================================================================================
            elif msg.text.lower() == koala + " welcome off":
                if msg.from_ in team:
                      settings["welcomemsg"] = False
                      cl.sendText(msg.to,"welcome message has been disabled")
            
#=============================================================================================================
            elif msg.text.lower() == koala + " chatbot on":
                if msg.from_ in team:
                      settings["simiSimi"][msg.to] = True
                      cl.sendText(msg.to,"chatbot has been enabled")
#============================================================================================================
            elif msg.text.lower() == koala + " respown on":
                if msg.from_ in team:
                      wait["responMention"] = True
                      cl.sendText(msg.to,"responMention has been enabled")
#====================================================================================================
            elif msg.text.lower() == koala + " respown off":
                if msg.from_ in team:
                      wait["responMention"] = False
                      cl.sendText(msg.to,"responMention has been disabled")
            
#====================================================================================================================
            elif msg.text.lower() == koala + " chatbot off":
                if msg.from_ in team:
                      settings["simiSimi"][msg.to] = False
                      cl.sendText(msg.to,"chatbot has been disabled")
            
#====================================================================================================================
            elif msg.text.lower() == koala + " protect on":
                if msg.from_ in team:
                      wait["protectall"] = True
                      cl.sendText(msg.to,"protect has been enabled")
            elif msg.text.lower() == squad + " protect on":
                if msg.from_ in team:
                      wait["protectall"] = True
                      cl.sendText(msg.to,"protect has been enabled")
#================================================================================================================
            elif msg.text.lower() == koala + " protect off":
                if msg.from_ in team:
                      wait["protectall"] = False
                      cl.sendText(msg.to,"protect has been disabled")
            elif msg.text.lower() == squad + " protect off":
                if msg.from_ in team:
                      wait["protectall"] = False
                      cl.sendText(msg.to,"protect has been disabled")
#=======================================================================================================================
            elif koala + " mimic " in msg.text.lower():
            	if msg.from_ in team:
                          pisah = msg.text.split("c ")
               		  cmd = msg.text.replace(pisah[0]+"c ","")
            		  if cmd == "on":
            			  if mimic["status"] == False:
            				  mimic["status"] = True
            				  cl.sendText(msg.to,"turning on mimic")
            				
            			  else:
            				  cl.sendText(msg.to,"mimic have been enable")
            				
            		  elif cmd == "off":
            			  if mimic["status"] == True:
            				  mimic["status"] = False
            				  cl.sendText(msg.to,"turning off mimic")
            				
            			  else:
            				  cl.sendText(msg.to,"Mimic have been desable")
            
#=======================================================================================================================
            elif msg.text.lower() == koala + " check welcome":
                if msg.from_ in team:
                       if wait["lang"] == "JP":
                            cl.sendText(msg.to,"welcome  message is\n\n" + wait["welmsg"])
                       else:
                            cl.sendText(msg.to,"The automatic welcome message is set as on")
            
#======================================================================================================================
            elif msg.text.lower() == koala + " settings":
                if msg.from_ in team:
                      print "Setting pick up..."
                      yhg=cl.getProfile().displayName
                      ghj=cl.getContact(msg.from_).displayName
                      md="Bot Status: work\n"
                      md+="Bot Name: " + str(yhg)
                      md+="\nUser name: " + str(ghj) 
                      md+="\nSquad Name: " + str(wait["squad"])
                      if wait["alwaysread"] == True: md+="\n🔵 always read\n"
                      else:md+="\n🔴 always read\n"
                      if wait["responMention"] == True: md+="🔵 responMention\n"
                      else:md+="🔴 responMention\n"
                      if wait["welcomemsg"] == True: md+="🔵 welcome message\n"
                      else:md+="🔴 welcome message\n"
                      if wait["post"] == True: md+="🔵 notification\n"
                      else:md+="🔴 notification\n"
                      if mimic["copy"] == True: md+="🔵 Mimic\n"
                      else:md+="🔴 Mimic\n"
                      if wait["protectall"] == True: md+="🔵 Protection\n\n"+datetime.today().strftime('%H:%M:%S')
                      else:md+="🔴 Protection\n\n"+datetime.today().strftime('%H:%M:%S')
                      cl.sendText(msg.to,md)
            
#============================================================================================================================
            elif msg.text.lower() == koala + " memlist":
                if msg.from_ in team:  
                   kontak = cl.getGroup(msg.to)
                   group = kontak.members
                   num=1
                   msgs="═══List Member═══"
                   for ids in group:
                       msgs+="\n[%i] %s" % (num, ids.displayName)
                       num=(num+1)
                   msgs+="\n═══List Member═══\n\nTotal Members : %i" % len(group)
                   cl.sendText(msg.to, msgs)
            
#==================================================================================================================
            elif koala + " mimic add" in msg.text.lower():
                 if msg.from_ in team:
                    targets = []
                    mention = eval(msg.contentMetadata["MENTION"])
                    mention["MENTIONEES"][0]["M"]
                    for x in mention["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            mimic["target"][target] = True
                            cl.sendText(msg.to,"Target ditambahkan!")
                            break
                        except:
                            cl.sendText(msg.to,"Fail !")
                            break
            
#=========================================================================================================================
            elif koala + " mimic del" in msg.text.lower():
                 if msg.from_ in pencipta:
                    targets = []
                    mention = eval(msg.contentMetadata["MENTION"])
                    mention["MENTIONEES"][0]["M"]
                    for x in mention["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del mimic["target"][target]
                            cl.sendText(msg.to,"Target dihapuskan!")
                            break
                        except:
                            cl.sendText(msg.to,"Fail !")
                            break
            
#==================================================================================================================
            elif msg.text.lower() == koala + " mimic list":
                if msg.from_ in team:
                    if mimic["target"] == {}:
                        cl.sendText(msg.to,"nothing")
                    else:
                        mc = "═══════List Mimic═══════\n"
                        for mi_d in mimic["target"]:
                            mc += "╠ "+cl.getContact(mi_d).displayName + "\n"
                        cl.sendText(msg.to,mc + "\n═══════List Mimic═══════")
            
#===============================================================================================================

            elif msg.text.lower() == koala + " gift":
                if msg.from_ in team:
                      wait["giftcontact"] = True
                      cl.sendText(msg.to,"send a contact to gift")

#=====================================================================================================
            elif msg.text.lower() == koala + " recover":
            	 if msg.from_ in pencipta:
                 	    thisgroup = cl.getGroups([msg.to])
		            Mids = [contact.mid for contact in thisgroup[0].members]
		            mi_d = Mids[:333]
                            group = cl.getGroup(msg.to)
		            cl.createGroup(group.name, mi_d)
		            cl.sendText(msg.to,"Success recover")
                 else:
                 	cl.sendText(msg.to,"command denied")
                 	cl.sendText(msg.to,"creator permission recuired")
#============================================================================================================
            elif msg.text.lower() == koala + " ginfo":
            	if msg.from_ in team:
            	    group = cl.getGroup(msg.to)
            	    try:
            	    	gCreator = group.creator.displayName
            	    except:
            	    	gCreator = "not found"
            	    if group.invitee is None:
            	    	gPending = "0"
            	    else:
            	    	gPending = str(len(group.invitee))
            	    if group.preventJoinByTicket == True:
            	    	gQr = "closed"
            	    	gTicket = "nothing"
            	    else:
            	    	gQr = "opened"
            	    	gTicket = "https://line.me/R/ti/g/"+ str(cl.reissueGroupTicket(group.id))
            	    ret_ = "Group  Info"
            	    ret_ += "\n\nGroup name: " + group.name
            	    ret_ += "\n\nGroup ID: " + group.id
            	    ret_ += "\n\nGroup creator: " + gCreator
            	    ret_ += "\n\nGroup members: " + str(len(group.members))
            	    ret_ += "\n\nInvitation Pending: " + gPending
            	    ret_ += "\n\nGroup QR: " + gQr
            	    ret_ += "\n\nGroup URL: " + gTicket
            	    cl.sendText(msg.to, str(ret_))
            
#=====================================================================================================================
            elif msg.text.lower() == koala + " invite":
                if msg.from_ in team:
                   wait["winvite"] = True
                   cl.sendText(msg.to,"send a contact to invite")
            
#=======================================================================================================================
            elif msg.text.lower() == koala + " gcreator":
                if msg.from_ in team:
                   try:
                       group = cl.getGroup(msg.to)
                       GS = group.creator.mid
                       M = Message()
                       M.to = msg.to
                       M.contentType = 13
                       M.contentMetadata = {'mid': GS}
                       cl.sendMessage(M)
                   except:
                       W = group.members[0].mid
                       M = Message()
                       M.to = msg.to
                       M.contentType = 13
                       M.contentMetadata = {'mid': W}
                       cl.sendMessage(M)
                       cl.sendText(msg.to,"old user")
            
#==============================================================================================================
            elif msg.text.lower() == koala + " glink open":
                if msg.from_ in team:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL open")
                    else:
                        cl.sendText(msg.to,"URL open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than")
#================================================================================================================
            elif msg.text.lower() == koala + " glink close":
                if msg.from_ in team:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL close")
                    else:
                        cl.sendText(msg.to,"URL close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than")
            
#=========================================================================================================
            elif koala + " gname:" in msg.text.lower():
                if msg.from_ in team:
                   X = cl.getGroup(msg.to)
                   pisah = msg.text.split(":")
                   X.name = msg.text.replace(pisah[0]+":","")
                   cl.updateGroup(X)
                else:
                   cl.sendText(msg.to,"It can't be used besides the group.")
            
#===============================================================================================================
            
            elif msg.text.lower() == koala + " gurl":
                if msg.from_ in team:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            
#============================================================================================================
            elif msg.text.lower() == koala + " runtime":
                if msg.from_ in team:
                   eltime = time.time() - mulai
                   van = "Bot has been running for: "+ waktu(eltime)
                   cl.sendText(msg.to,van)
           
#==============================================================================================================
            elif msg.text.lower() == koala + " creator":
            	if msg.from_ in team:
				   msg.contentType = 13
				   msg.contentMetadata = {'mid': "u832d6b22ecdb23a673a2ae6a8784f714"}
				   cl.sendMessage(msg)
				   cl.sendText(msg.to,"My Creator")
	    
#===================================================================================================================
            elif koala + " set welcome:" in msg.text.lower():
                if msg.from_ in team:
            	  pisah = msg.text.split(":")
                  wait["welmsg"] = msg.text.replace(pisah[0]+":","")
                  cl.sendText(msg.to,"done")
            
#=====================================================================================================================
            elif msg.text.lower() == koala + " check welcome":
                if msg.from_ in team:
                   if wait["lang"] == "JP":
                       cl.sendText(msg.to,"welcome  message\n\n" + wait["welmsg"])
                   else:
                       cl.sendText(msg.to,"The automatic appending information is set as follows。\n\n" + wait["welmsg"])
            
#=======================================================================================================================
            elif koala + " pap set:" in msg.text.lower():
                if msg.from_ in team:
            	   pisah = msg.text.split("set:")
                   wait["pap"] = msg.text.replace(pisah[0]+"set:","")
                   cl.sendText(msg.to,"Pap Has Been changed")
           
#========================================================================================================================
            elif msg.text.lower() == koala + " pap":
            	if msg.from_ in team:
                   cl.sendImageWithURL(msg.to,wait["pap"])
           
#===========================================================================================================================
            elif msg.text.lower() == koala + " banned":
                if msg.from_ in team:
                   wait["wblacklist"] = True
                   cl.sendText(msg.to,"send contact to banned")
            
#==================================================================================================================
            elif msg.text.lower() == koala + " unbanned":
                if msg.from_ in team:
                   wait["dblacklist"] = True
                   cl.sendText(msg.to,"send contact to unbanned")
            
#============================================================================================================
            elif koala + " unban" in msg.text.lower():
                if msg.from_ in team:
                      key = eval(msg.contentMetadata["MENTION"])
                      key1 = key["MENTIONEES"][0]["M"]
                      contact = cl.getContact(key1)
                      targets = []
                      targets.append(contact.mid)
                      if targets == []:
                          cl.sendText(msg.to,"Contact not found")
                      else:
                          for target in targets:
                              try:
                                  del wait["blacklist"][target]
                                  f=codecs.open('st2__b.json','w','utf-8')
                                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                  cl.sendText(msg.to,"Succes")
                              except:
                                  cl.sendText(msg.to,"There was no blacklist user")
            
#================================================================================================================
            elif koala + " ban" in msg.text.lower():
                if msg.from_ in team:
                      key = eval(msg.contentMetadata["MENTION"])
                      key1 = key["MENTIONEES"][0]["M"]
                      contact = cl.getContact(key1)
                      targets = []
                      targets.append(contact.mid)
                      if targets == []:
                          cl.sendText(msg.to,"Contact not found")
                      else:
                          for target in targets:
                              try:
                                  wait["blacklist"][target] = True
                                  f=codecs.open('st2__b.json','w','utf-8')
                                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                  cl.sendText(msg.to,"Success ")
                              except:
                                  cl.sendText(msg.to,"Error")
            
#=====================================================================================================================================
            elif koala + " vkick" in msg.text.lower():
                if msg.from_ in team:
					targets = []
					key = eval(msg.contentMetadata["MENTION"])
					key["MENTIONEES"][0]["M"]
					for x in key["MENTIONEES"]:
						targets.append(x["M"])
					for target in targets:
						try:
							cl.kickoutFromGroup(msg.to,[target])
						except:
							cl.sendText(msg.to,"Error")
           
#===========================================================================================
            elif msg.text.lower() == koala + " banlist":
                if msg.from_ in team:
                   if wait["blacklist"] == {}:
                      random.choice(KAC).sendText(msg.to,"Tidak Ada")
                   else:
                      mc = ""
                      for mi_d in wait["blacklist"]:
                          mc += "->" +cl.getContact(mi_d).displayName + "\n"
                      cl.sendText(msg.to,"===[Blacklist User]===\n"+mc)
            
#==============================================================================================================
            elif msg.text.lower() == koala + " crash":
                if msg.from_ in team:
                   msg.contentType = 13
                   msg.contentMetadata = {'mid': "00000000000000000000000000000000',"}
                   cl.sendMessage(msg)
            
#=====================================================================================
            elif msg.text.lower() == koala + " cancel":
                if msg.from_ in team:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting。")
                        else:
                            cl.sendText(msg.to,"eror")
            
#===============================================================================================================
            elif koala + " ulti" in msg.text.lower():
                if msg.from_ in team:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                       	   cl.findAndAddContactsByMid(target)
                           cl.kickoutFromGroup(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            
#===========command owner only====================================================================================================

            elif koala + " groupcast " in msg.text.lower():
            	if msg.from_ in team:
                   pisah = msg.text.split("groupcast ")
                   bctxt = msg.text.replace(pisah[0]+"groupcast ", "")
                   n = cl.getGroupIdsJoined()
                   for manusia in n:
                       cl.sendText(manusia,(bctxt +"\n\nbroadcasted by:" + cl.getContact(msg.from_).displayName))
            
#====================================================================================================================

            elif koala + " teamcast " in msg.text.lower():
            	if msg.from_ in team:
                   pisah = msg.text.split("teamcast ")
                   bctxt = msg.text.replace(pisah[0]+"teamcast ", "")
                   t = cl.getAllContactIds()
                   for manusia in t:
                       cl.sendText(manusia,(bctxt +"\n\nbroadcasted by:" + cl.getContact(msg.from_).displayName))
            
#===================================================================================================================
            elif koala + " destroy" in msg.text:
                if msg.from_ in team:
                    print "ok cleanse"
                    _name = msg.text.replace(koala + " destroy","")
                    gs = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"Just some casual cleansing ")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"member not found")
                    else:
                        for target in targets:
                          if not target in team:
                               try:
                                   cl.kickoutFromGroup(msg.to,[target])
                                   print (msg.to,[g.mid])
                                   if targets == []:
                                      cl.sendText(msg.to,"group succes cleanse")
                               except:
                                   cl.sendText(msg.to,"bot have a limit kick")
#====================================================================================================================
            elif msg.text.lower() == koala + " backup run":
                if msg.from_ in team:
                    wek = cl.getContact(mid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('mydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('mysm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('myps.txt',"w")
                    u.write(a)
                    u.close()
                    cl.sendText(msg.to,"done")
                    print wek
                    print a
                    print r
                    print i
            
#========================================================================================================================
            elif koala + " copy" in msg.text.lower():
                if msg.from_ in team:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           contact = cl.getContact(target)
                           X = contact.displayName
                           profile = cl.getProfile()
                           profile.displayName = X
                           cl.updateProfile(profile)
                           #---------------------------------------
                           Y = contact.statusMessage
                           lol = cl.getProfile()
                           lol.statusMessage = Y
                           cl.updateProfile(lol)
                           #---------------------------------------
                           P = contact.pictureStatus
                           cl.updateProfilePicture(P)
                           cl.sendText(msg.to,"done")
                       except Exception as e:
                           print e
            
#=========================================================================================================
            elif msg.text.lower() == koala + " backup":
                if msg.from_ in team:
                        try:
                            h = open('mydn.txt',"r")
                            name = h.read()
                            h.close()
                            x = name
                            profile = cl.getProfile()
                            profile.displayName = x
                            cl.updateProfile(profile)
                            i = open('mysm.txt',"r")
                            sm = i.read()
                            i.close()
                            y = sm
                            cak = cl.getProfile()
                            cak.statusMessage = y
                            cl.updateProfile(cak)
                            j = open('myps.txt',"r")
                            ps = j.read()
                            j.close()
                            p = ps
                            cl.updateProfilePicture(p)
                            cl.sendText(msg.to, "Succes")
                        except Exception as e:
                            cl.sendText(msg.to,"failed !!")
                            print e
            
#====================================================================================================================
            elif koala + " rename:" in msg.text.lower():
            	if msg.from_ in team:
                      pisah = msg.text.split("rename:")
                      string = msg.text.replace(pisah[0]+"rename:","")
                      if len(string.decode('utf-8')) <= 50:
                          profile = cl.getProfile()
                          profile.displayName = string
                          cl.updateProfile(profile)
                          cl.sendText(msg.to,"change name: "+string+"\nsucces")
                          
            
#==========================================================================================================================
            elif koala + " bio:" in msg.text:
                if msg.from_ in team:
                   pisah = msg.text.split(":")
                   string = msg.text.replace(pisah[0]+":","")
                   if len(string.decode('utf-8')) <= 5000:
                       profile = cl.getProfile()
                       profile.statusMessage = string
                       cl.updateProfile(profile)
                       cl.sendText(msg.to,"successfully changed to: " + string)
            
#===================================================================================================================================
           
#===============================================================================================================================
            elif msg.text.lower() == koala + " reject all":
                if msg.from_ in team:
                   gid = cl.getGroupIdsInvited()
                   for i in gid:
                       cl.rejectGroupInvitation(i)
                   if wait["lang"] == "JP":
                       cl.sendText(msg.to,"done")
                   else:
                       cl.sendText(msg.to,"done")
           
#==================================================================================================================
            elif msg.text.lower() == koala + " remove chat":
                if msg.from_ in team:
                   cl.removeAllMessages(op.param2)
                   cl.sendText(msg.to,"done")
            

#================================================================================================================
            elif msg.text.lower() == koala + " spm invite":
                if msg.from_ in pencipta:
                      wait["spam"] = True
                      cl.sendText(msg.to,"send a contact to spam invite")
                else:
                	 cl.sendText(msg.to,"command denied")
                	 cl.sendText(msg.to,"creator permission recuired")
#==================================================================================================================

            elif msg.text.lower() == koala + " changepict":
                if msg.from_ in pencipta:
                   wait["cpp"] = True
                   cl.sendText(msg.to,"please send an image")
                else:
                	 cl.sendText(msg.to,"command denied")
                	 cl.sendText(msg.to,"creator permission recuired")
#============================================================================================================
            elif msg.text.lower() == koala + " join url":
                if msg.from_ in team:
                   wait["linkticket"] = True
                   cl.sendText(msg.to,"please send a link URL to me")
            
#=============================================================================================================

            elif "http://line.me/R/ti/g/" in msg.text.lower():
            	if msg.from_ in team:
                             if wait["linkticket"] == True:
                                    tiket = msg.text.replace("http://line.me/R/ti/g/","")
                                    bahan = "http://line.me/R/ti/g/" + tiket
                                    group = cl.findGroupByTicket(bahan)
                                    cl.acceptGroupInvitationByTicket(group.id,bahan)
                                    wait["linkticket"] = False
                                    cl.sendText(msg.to, "succes joined to group %s" % str(group.name))
#===================================================w=========================================================================

#====================================================================================================================
            elif msg.text.lower() == koala + " clear banlist":
                if msg.from_ in pencipta:
                   wait["blacklist"] = {}
                   cl.sendText(msg.to,"banlist has been clean")
            elif msg.text.lower() == koala + " clear banlist":
                if msg.from_ in owner:
                   wait["blacklist"] = {}
                   cl.sendText(msg.to,"banlist has been clean")
#====================================================================================================================

            elif msg.text.lower() == koala + " clear mimiclist":
                if msg.from_ in pencipta:
                   mimic["target"] = {}
                   cl.sendText(msg.to,"mimiclist has been clean")
            elif msg.text.lower() == koala + " clear mimiclist":
                if msg.from_ in owner:
                   mimic["target"] = {}
                   cl.sendText(msg.to,"mimiclist has been clean")
#=====================================================================================================================

            

            elif msg.text.lower() == koala + " contact banlist":
                if msg.from_ in team:
                   if wait["blacklist"] == {}:
                       cl.sendText(msg.to,"nothing")
                   else:
                       cl.sendText(msg.to,"Blacklist user")
                       h = ""
                       for i in wait["blacklist"]:
                           h = cl.getContact(i)
                           M = Message()
                           M.to = msg.to
                           M.contentType = 13
                           M.contentMetadata = {'mid': i}
                           cl.sendMessage(M)
           
#============================================================================================================================
            elif msg.text.lower() == koala + " friendlist":
                if msg.from_ in team:
                   contactlist = cl.getAllContactIds()
                   kontak = cl.getContacts(contactlist)
                   num=1
                   msgs="═════════List Friend═════════"
                   for ids in kontak:
                       msgs+="\n[%i] %s" % (num, ids.displayName)
                       num=(num+1)
                   msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                   cl.sendText(msg.to, msgs)
            

#========================================================================================================================
       
#======================================================================================================================

            elif msg.text.lower() == koala + " grouplist":
                if msg.from_ in pencipta:
                   gs = cl.getGroupIdsJoined()
                   L = "『 Groups List 』\n"
                   for i in gs:
                       L += "[≫] %s \n" % (cl.getGroup(i).name + " | [ " + str(len (cl.getGroup(i).members)) + " ]")
                   cl.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
                else:
                	 cl.sendText(msg.to,"command denied")
                	 cl.sendText(msg.to,"creator permission recuired")

            elif msg.text.lower() == koala + " purge":
            	if msg.from_ in team:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"blacklist user not found")
                        return
                    for jj in matched_list:
                        try:
                            cl.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            
#================================================================================================================
            elif koala +" twitter " in msg.text.lower():
            	if msg.from_ in team:
                   try:
                       pisah = msg.text.split("twitter ")
                       user = msg.text.replace(pisah[0]+"twitter ","")
                       with requests.session() as s: 
                            s.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0' 
                            url    = 'https://twitter.com/'+user
                            r    = s.get(url)
                            soup = BeautifulSoup(r.content, 'html5lib')
                            hasil = soup.select_one('.ProfileHeaderCard')
                            hasil = hasil.findAll(msg.text)
                            tweet = soup.find('span', class_ = 'ProfileNav-value').get_text()
                            fllwng = soup.find('li', class_ = 'ProfileNav-item ProfileNav-item--following').get_text()
                            fllwr = soup.find('li', class_ = 'ProfileNav-item ProfileNav-item--followers').get_text()
                            fav = soup.find('li', class_ = 'ProfileNav-item ProfileNav-item--favorites').get_text()
                            img = soup.find('img', class_ = 'ProfileAvatar-image')
                            cl.sendImageWithURL(msg.to,img['src'])
                            cl.sendMessage(msg.to,'Name: '+hasil[2]+'\nUsername: '+hasil[7]+hasil[8]+'\nBio: '+hasil[12]+hasil[13]+' '+hasil[15]+hasil[16]+'\nLoc: '+hasil[20]+'\nWeb: '+hasil[26]+'\nJoined: '+hasil[32]+'\nBorn: '+hasil[37])
                            cl.sendMessage(msg.to,'Tweets: '+tweet+'\nFollowing: '+fllwng.replace('Following','')+'\nFollowers: '+fllwr.replace('Followers','')+'\nLikes:'+fav.replace('Likes',''))
                   except Exception as njer:
                	   cl.sendText(msg.to, str(njer))

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
                    Name = cl.getContact(op.param2).displayName
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n●" + Name
                        wait2['ROM'][op.param1][op.param2] = "●" + Name
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

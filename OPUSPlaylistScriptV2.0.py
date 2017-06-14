import urllib, urllib2, string, base64, datetime, os, json, shutil, time, zipfile, re, stat, sys
from random import randint
print "Playlist Wilmaa and Wilmaa-OPUS by Albiii!"

#Input the Quality of the Channels

qual = raw_input("Type the Quality:\n 7:Low\n 17:Medium\n 32:High\n 97:Super-High\n ")

print 'Set quality to ',qual, 'and setting correct Bitrate...'
if qual == '7':
    bit = '540000'
    qual2 = '01'
elif qual == '17':
     bit = '2290000'
     qual2 = '02'
elif qual == '32':
     bit = '3305000'
     qual2 = '03'
elif qual == '97':
     bit = '4240000'
     qual2 = '04'
else:
      bit = '394000'
      qual2='01'

#Script OPUS-Token

print "Getting OPUS-Token..."
linktok1 = urllib.urlopen("http://racacaxtv.ga/mega.php?chn=VEYx&pls=RnJhbmNvcGhvbmVz")
pagetok1 = linktok1.read()
postoken11 = string.find(pagetok1,"wil/4BHu")
postoken21 = string.find(pagetok1,"/tf_1_hd/")
tokenopuscf = pagetok1[(postoken11+4):(postoken21)]


print "Got Tokens and Links, starting step 2..."

print "Reading origin file and copying it..."
originweb = urllib.urlopen("http://tvmaster.hol.es/liste/opus-final-1.txt")
dest = originweb.read()

print "Copied."

originweb.close()

#MAIN FUNCTIONS
#Opus Session Script 

def OpusProxyLink(chid,qual):
    a = str(randint(0,8))
    b = str(randint(0,256))
    c = str(randint(0,256))
    ip = str("85."+a+'.'+b+'.'+c)
    print "Random SwissCom-IP "+ip+" Generated for this channel."
    chlink64 = base64.b64encode('https://streams.wilmaa.com/m3u8/get?channelId='+chid+'&profile='+qual)
    link = urllib2.Request('http://surf.ahnungslos.ch/index.php?q='+chlink64+'%3D%3D&hl=3ed')
    link.add_header('User-Agent','Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')
    link.add_header('X-Forwarded-For=',ip)
    source = urllib2.urlopen(link)
    page = source.read()
    session1 = string.find(page,'session/')
    session2 = string.find(page,'6cexmz/')
    session = page[session1+7:session2]
    wilid = page[(session2+6):(session2+14)]
    server1 = string.find(page,'http://')
    server2 = string.find(page,':80')
    server = page[server1+7:server2+3]
    finallink = 'http://opus.cf/allfrtvstrm/tkn/wil/'+ tokenopuscf +'/'+server+ '/session'+session+'6cexmz'+wilid+bit+'/index'
    return str(finallink)

#Script France.TV
quality = ""
def FranceTVlink(ident,quality):
    if ident == "2":
        quality = "315"
    elif ident == "3":
        quality = "325"
    elif ident == "4":
        quality = "335"
    elif ident == "5":
        quality = "345"
    elif ident == "O":
        quality = "355"
    link = urllib.urlopen("http://www.mytvonline.org/minproxy.php/http://hdfauthftv-a.akamaihd.net/esi/TA?format=json&url=http%3A%2F%2Flive.francetv.fr%2Fsimulcast%2FFrance_"+ident+"%2Fhls_v1%2Findex.m3u8")
    page = link.read()
    postoke1 = string.find(page,ident+"/hls_v1/")
    postoke2 = string.find(page,"/index")
    postoke3 = string.find(page,"}")
    tokfra =page[(postoke1+9):(postoke2)]
    tokfrb =page[(postoke2+11):(postoke3-1)]
    stream = "http://www.mytvonline.org/minproxy.php/http://live.francetv.fr/simulcast/France_"+ident+"/hls_v1/" + tokfra + "/France_"+ident+"-video=1465200-audio_AACL_fra_65600_"+quality+"=65600.m3u8" + tokfrb
    return stream

#Choose France Stream

posfr = 0
pos8link = 0
lastchid = "O"
ident = ""
while ident != lastchid:
    posfr = dest.find('francetvch@', posfr + 1)
    pos8link = posfr
    pos8link = dest.find('.m3u8link', pos8link + 1)
    ident = dest[posfr+11:pos8link]
    print "France " + ident+ "..."
    finlink1 = FranceTVlink(ident,quality)
    dest = dest.replace("francetvch@"+ident+".m3u8link",finlink1+".m3u8")
    print "OK"

#RTS suisse channels on Opus

chopus0 = OpusProxyLink("orf_2_hd",qual)
chopus1 = chopus0
chopus2 = chopus0
print 'Setting up RTS Un...'
chopus1 = string.replace(chopus1,"/1/1011/","/2/2034/")
chopus1 = string.replace(chopus1,"index","index.m3u8")
print 'OK, now setting RTS Deux...'
chopus2 = string.replace(chopus2,"/1/1011/","/2/2035/")
chopus2 = string.replace(chopus2,"index","index.m3u8")
print 'RTS channels OK...'

#Script Change OPUS channels in m3u playlist
posopus = 0
poshd = 0
lastchid = "orf_2_hd"
chid = ""
while chid != "orf_2_hd":
    posopus = dest.find('chan@', posopus + 1)
    poshd = posopus
    poshd = dest.find('.m3u8link', poshd + 1)
    chid = dest[posopus+5:poshd]
    print chid
    finlink2 = OpusProxyLink(chid,qual)
    dest = dest.replace("chan@"+chid+".m3u8link",finlink2+".m3u8")

#Copying All in the final file.

print "Opening Copy and replacing strings..."
dest1 = file("play-weborigin-streams.m3u","w")
data = time.strftime("%d/%m")
dest = string.replace(dest,"datareplace",data)
dest = string.replace(dest,"tokenchange",tokenopuscf)
dest = string.replace(dest,"qual2",qual2)
dest = string.replace(dest,"qual",qual)
dest = string.replace(dest,"chopus1",chopus1)
dest = string.replace(dest,"chopus2",chopus2)

dest1.write(dest)

print "Writing last things..."

dest1.close()

print "OK, all done!"

#os.system("pause")

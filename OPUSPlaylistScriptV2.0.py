import urllib, urllib2, string, base64, datetime, os, json, shutil, time, zipfile, re, stat, sys
from random import randint

originweburl = "YUhSMGNEb3ZMM1IyYldGemRHVnlMbWh2YkM1bGN5OXNhWE4wWlM5dmNIVnpMWFJsYzNRdE15NTBlSFE9"

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

#Reading Origin File

print "Reading origin file and copying it..."
originweb = urllib.urlopen(base64.b64decode(base64.b64decode(originweburl)))
dest = originweb.read()

print "Copied."

originweb.close()


#Script OPUS-Token

def OpusCFToken(tipo):
    if tipo == "base": 
        print "Getting OPUS-Token V2..."
        linktok1 = urllib.urlopen("http://racacaxtv.ga/mega.php?chn=VEYx&pls=RnJhbmNvcGhvbmVz")
        pagetok1 = linktok1.read()
        postoken11 = string.find(pagetok1,"wil/4BHu")
        postoken21 = string.find(pagetok1,"/tf_1_hd/")
        tokenopuscf = pagetok1[(postoken11+4):(postoken21)]
        return tokenopuscf
    elif tipo == "sha":
        linktok1 = urllib.urlopen("http://opus.cf/allfrtvstrm/tkn/hd1/tok/i/weblive_1@90467/index_1240_av-b.m3u8")
        pagetok1 = link1.read()
        tokenopuscf = pagetok1[57:97]
        return tokenopuscf
    else:
        pass

tokenopuscf = OpusCFToken('base')

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

# TEST Selection
 
def Selection(index,lastchid,dest):
    lastchid = str(lastchid)
    posindex = 0
    pos8link = 0
    chidfin = ""
    posindexinfo = index+'@'
    u8link2 = '.m3u8link'
    posind2 = len(posindexinfo)+1
    while chidfin != lastchid:
        posindex = dest.find(posindexinfo, posindex + 1)
        print "Channel ID Start: "+str(posindex)
        pos8link = dest.find(u8link2, posindex + 1)
        print "Channel ID finish: "+str(pos8link)
        if posindexinfo == "francetvch@":
            chidfin = dest[(posindex+posind2)-1:(posindex+posind2)]
            print "             France "+chidfin
            finlink1 = FranceTVlink(chidfin,"")
        elif posindexinfo == "chan@":
            chidfin = dest[(posindex+posind2)-1:pos8link]
            print "             "+chidfin
            finlink1 = OpusProxyLink(chidfin,qual)
        dest = dest.replace(posindexinfo+chidfin+u8link2,finlink1+".m3u8")
        print "OK, done!"
    else:
        return dest

#Script OPUS RTS channels

def RTSCh(dest):
    chopus1 = OpusProxyLink("orf_2_hd",qual)
    chopus2 = chopus1
    print 'Setting up RTS Un...'
    chopus1 = string.replace(chopus1,"/1/1011/","/2/2034/")
    chopus1 = string.replace(chopus1,"index","index.m3u8")
    dest = string.replace(dest,"chopus1",chopus1)
    print 'OK, now setting RTS Deux...'
    chopus2 = string.replace(chopus2,"/1/1011/","/2/2035/")
    chopus2 = string.replace(chopus2,"index","index.m3u8")
    dest = string.replace(dest,"chopus2",chopus2)
    print 'RTS channels OK...'
    return dest

#Script RTBF

print "Starting RTBF Channels Token finder..."
def RTBF(opusurlid):
    opusurlid = base64.b64encode(opusurlid)
    linktokrtbf = urllib.urlopen("http://racacaxtv.ga/mega.php?chn="+opusurlid+"&pls=RnJhbmNvcGhvbmVz")
    pagetokrtbf = linktokrtbf.read()
    postokenbel1 = string.find(pagetokrtbf,"/open/")
    postokenbel2 = string.find(pagetokrtbf,"/la")
    tokenbel1=pagetokrtbf[postokenbel1+6:postokenbel2]
    return tokenbel1

#FrenchStream
    
indexfra = "francetvch"
lastfra = "O"
dest = Selection(indexfra,lastfra,dest)

#Wilmaa Streams

indexwil = "chan"
lastwil = "orf_2_hd"
dest = Selection(indexwil,lastwil,dest)

#RTBF La Une
print "Finding RTBF La Une Token and replacing it..."

rtbftoken = RTBF("RTBF La Une")
dest = dest.replace("launetok",rtbftoken)

#RTBF La Deux
print "Finding RTBF La Deux Token and replacing it..."

rtbftoken = RTBF("RTBF La Deux")
dest = dest.replace("ladeuxtok",rtbftoken)

#RTBF La Trois
print "Finding RTBF La Trois Token and replacing it..."

rtbftoken = RTBF("RTBF La Trois")
dest = dest.replace("latroistok",rtbftoken)

print "OK, RTBF Done!"

#RTS suisse channels on Opus

dest = RTSCh(dest)

#Step 2.

#Copying All in the final file.
print "Got Tokens and Links, starting step 2..."
print "Opening Copy and replacing strings..."
dest1 = file("play-weborigin-streams.m3u","w")
data = time.strftime("%d/%m")
dest = string.replace(dest,"datareplace",data)
dest = string.replace(dest,"tokenchange",tokenopuscf)
dest = string.replace(dest,"qual2",qual2)
dest = string.replace(dest,"qual",qual)

dest1.write(dest)

print "Writing last things..."

dest1.close()

print "OK, all done!"

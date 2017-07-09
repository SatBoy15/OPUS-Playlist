import urllib, urllib2, string, base64, time, datetime, os
import ftplib
from random import randint

def IPAdd():
    jsonip = urllib.urlopen("https://jsonip.com/")
    pageip=jsonip.read()
    jsonip.close()
    ippos1=pageip.find('"ip":"')
    ippos2=pageip.find('","about":"')
    ip=pageip[ippos1+6:ippos2]
    return ip

def OpusCFToken(tipo):
    if tipo == "base1":
        linktok1sce = urllib2.Request("http://opus.re/iptv-italia-tv-canale.php")
        linktok1sce.add_header('User-Agent','Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')
        linktok1=urllib2.urlopen(linktok1sce)
        pagetok1 = linktok1.read()
        postoken11 = string.find(pagetok1,"tkn/wil/")
        postoken21 = string.find(pagetok1,"/tele_ticino")
        tokenopuscf = pagetok1[(postoken11+8):(postoken21)]
        return tokenopuscf
    elif tipo == "base2":
        linktok1sce = urllib2.Request("https://racacaxtv.ga/mega.php?chn=Q2FuYWwgKyBDaW7DqW1h&pls=RnJhbmNvcGhvbmVz")
        linktok1sce.add_header('User-Agent','Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')
        linktok1=urllib2.urlopen(linktok1sce)
        pagetok1 = linktok1.read()
        postoken11 = string.find(pagetok1,"tvone/")
        postoken21 = string.find(pagetok1,'9/')
        tokenopuscf = pagetok1[(postoken11+6):(postoken21+1)]
        return tokenopuscf
    elif tipo == "sha":
        linktok1 = urllib.urlopen("http://racacaxtv.ga/tnt.php")
        pagetok1=linktok1.read()
        postok1=pagetok1.find("?token=")
        postok2=pagetok1.find("&chn=TF1")
        tokenopuscf=pagetok1[postok1+7:postok2]
        return tokenopuscf
    elif tipo == "baseshort":
        linktok1 = urllib.urlopen("http://racacaxtv.ga/mega.php?chn=Q2FuYWwgKw==&pls=RnJhbmNvcGhvbmVz")
        pagetok1 = linktok1.read()
        postoken11 = string.find(pagetok1,"artvecor/")
        postoken12 = string.find(pagetok1,'/canalplus/index.m3u8')
        tokenopuscf =pagetok1[postoken11+9:postoken12]
        return tokenopuscf
    else:
        pass

tokenopuscf = OpusCFToken('base1')
tokenopuscf0 = tokenopuscf
tokenopuscf3 = OpusCFToken('baseshort')
		
def OpusProxyLink(chid,qual):
    if qual == '7':
        bit = '540000'
        qual2 = '01'
    elif qual == '17':
        bit = '2290000'
        qual2 = '03'
    elif qual == '32':
        bit = '3305000'
        qual2 = '03'
    elif qual == '97':
        bit = '4240000'
        qual2 = '04'
    else:
        bit = '394000'
        qual2='01'
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

#Script OPUS RTS channels

def RTSCh(dest,qual):
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

#Script fluxies

def fluxies(chid,tokenopuscf3):
    print "Preparing fluxies url for "+chid+" channel..."
    fluxiesurl = "http://fluxies.ddns.net/artvecor/" + tokenopuscf3 + "/"+chid+"/index"
    print "Done"
    return fluxiesurl


#Script BeinSports

def Bein(opusurlid,qual2,tokenopuscf3):
    print "Finding correct Bein Sport Link and replacing..."
    if opusurlid < 3:
        opusurlid1 = base64.b64encode("beIn Sports "+opusurlid)
    else:
        opusurlid1 = base64.b64encode("beIn Sports MAX "+opusurlid)        
    linktokbein = urllib.urlopen("https://racacaxtv.ga/mega.php?chn="+opusurlid+"&pls=RnJhbmNvcGhvbmVz")
    pagetokbein = linktokbein.read()
    posservbein1 = string.find(pagetokbein,"http%3A%2F%2F")
    posservbein2 = string.find(pagetokbein,'.alwaysdata.net%2Fbtv')
    servbein1 = pagetokbein[posservbein1:posservbein2+19]
    beinlink = "http://racacax.remy-insitec.fr/btv/hls/beinsports"+opusurlid+"aes/index.m3u8?q="+qual2+"&token="+tokenopuscf3
    return beinlink
    

#Selection
def Selection(index,lastchid,dest,qual):
    if qual == '7':
        bit = '540000'
        qual2 = '01'
    elif qual == '17':
        bit = '2290000'
        qual2 = '03'
    elif qual == '32':
        bit = '3305000'
        qual2 = '03'
    elif qual == '97':
        bit = '4240000'
        qual2 = '04'
    else:
        bit = '394000'
        qual2='01'
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
            dest = dest.replace(posindexinfo+chidfin+u8link2,finlink1)
        elif posindexinfo == "chan@":
            chidfin = dest[(posindex+posind2)-1:pos8link]
            print "             "+chidfin
            finlink1 = OpusProxyLink(chidfin,qual)
        elif posindexinfo == "bein@":
            chidfin = dest[(posindex+posind2)-1:pos8link]
            print "             Bein Sports "+chidfin
            finlink1 = Bein(chidfin,qual2,tokenopuscf3)
            dest = dest.replace(posindexinfo+chidfin+u8link2,finlink1)
        elif posindexinfo == "fluxies@":
            chidfin = dest[(posindex+posind2)-1:pos8link]
            print "             Fluxies: "+chidfin
            finlink1 = fluxies(chidfin,tokenopuscf3)
        dest = dest.replace(posindexinfo+chidfin+u8link2,finlink1+".m3u8")
        print "OK, done!"
    else:
        return dest


#Status RTBF Script
def RTBFStat(urlid,dest,ptype):
    print "Checking status for RTBF "+urlid+" Channel..."
    if urlid == "1":
        url = urllib.urlopen("http://rtbf.l3.freecaster.net/live/rtbf/geo/open/25e004693ce49d226712769ae6a39d4f0782500f/laune-audio_1=128000-video=1152000.m3u8?token=0db0ad0d41931810f148c")
    elif urlid == "2":
        url = urllib.urlopen("http://rtbf.l3.freecaster.net/live/rtbf/geo/open/ce1a55335a3ded14921b12cd8cac1a6dd01bdc55/ladeux-audio_1=128000-video=1152000.m3u8?token=0f4d7af3370022aee98bf")
    elif urlid == "3":
        url = urllib.urlopen("http://rtbf.l3.freecaster.net/live/rtbf/geo/open/3a932b94370550225f6c82ce2d45c265af1cabc2/latrois-audio_1=128000-video=1152000.m3u8?token=00ed017e3c279a25b31fa")
    else:
        pass
    urlstat = url.read()
    if urlstat.find("../open/")>0:
        if ptype == "vlc":
            dest = dest.replace("stat"+urlid,"[ON]")
        else:
            dest = dest.replace("stat"+urlid,"[COLOR lime][ON]")
        print "Done"
    elif urlstat.find("../be/")>0:
        if ptype == "vlc":
            dest = dest.replace("stat"+urlid,"[OFF]")
        else:
            dest = dest.replace("stat"+urlid,"[COLOR red][OFF]")
        print "Done"
    elif urlstat.find("../rtbf/")>0:
        if ptype == "vlc":
            dest = dest.replace("stat"+urlid,"[OFF]")
        else:
            dest = dest.replace("stat"+urlid,"[COLOR red][OFF]")
        print "Done"
    else:
        pass
    return dest

hours1 = time.strftime("%H")
minutes1 = time.strftime("%M")
seconds1 = time.strftime("%S")
data = time.strftime("%d/%m")

def FileWriteReplace(fileorig,filename,qual):
    if qual == '7':
        bit = '540000'
        qual2 = '01'
    elif qual == '17':
        bit = '2290000'
        qual2 = '03'
    elif qual == '32':
        bit = '3305000'
        qual2 = '03'
    elif qual == '97':
        bit = '4240000'
        qual2 = '04'
    else:
        bit = '394000'
        qual2='01'
    fileorig = fileorig.replace("Hours1",hours1)
    fileorig = fileorig.replace("Minutes1",minutes1)
    fileorig = fileorig.replace("Seconds1",seconds1)
    fileorig = fileorig.replace("datareplace",data)
    fileorig = fileorig.replace("tokenchange",tokenopuscf)
    fileorig = fileorig.replace("qual2",qual2)
    fileorig = fileorig.replace("qual",qual)
    finalfile=file(filename,"w")
    finalfile.write(fileorig)
    finalfile.close()
    return "FileWriteReplace function for "+filename+" file is OK"

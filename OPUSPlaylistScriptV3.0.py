import urllib, urllib2, string, time, datetime, os, hashlib
import ftplib
from random import randint
#Importing LibAlbi
import libalbi
import libalbicrypt as albicrypt
tempo1 = time.time()

#Finding My IP

ip = libalbi.IPAdd()

print "\n------------------------------------------------\n"

print "Playlist Wilmaa and Wilmaa-OPUS by Albiii! V3.0\n"

print "Your IP: "+ip+"\n"

print "Today: "+time.strftime("%d/%m/%y")+"\n"

print "Hour :"+time.strftime("%H")+"     Minutes: "+time.strftime("%M")+"     Seconds: "+time.strftime("%S")

print "\n------------------------------------------------\n"

passw1 = raw_input("Please, type the password.\n----> ")

encpassw1 = hashlib.sha256(passw1).hexdigest()

if encpassw1 != "3ea94348d92b74fbc342a998022066557263a3f73ee58e7c3af158a544b56529":
    print "     Wrong Password...\n\n     Goodbye!"
    os.system('pause')
else:
    print "OK, Authentication Completed..."
    #Setting Sources

    kodiopt = raw_input("We'll make a Playable VLC playlist.\nDo you want the Kodi Playlist,too?(1:Yes, 0:No)--->")
    tokenfileopt= raw_input("Do you want also a \".txt\" file with all the tokens?(1:Yes, 0:No):")

    #Assigning Playlists Web URLs

    vlcblockurl= "lngjpnwvcxsvefefclnlmjkjklngjpnwvcxgjcdlngjpncxcfbdlngjpnwvcxzxlngjpnwvcxzxlngjpnwvcxzxaboplngjpncxcflnclnbxkvlkakvlncflklngjpncxcfbdkvjkclnbxeflngjpnwvcxsvbxkvghablngjpnwvcxpnoplngjpnwvcxzxclnefjkbxkvclnuijakvabnnijakvcdlngjpnwvcxpnlkefakvefK/135893"
    kodiblockurl= "anpnbdbdzxefefclnlmjkjkanpnbdbdpncdanpnbdgjsvanpnbdbdwvanpnbdbdwvanpnbdbdwvabopanpnbdgjgjclnbxkvlkakvlncflkanpnbdgjsvkvjkclnbxefanpnbdbdzxbxkvghabanpnbdbdanopanpnbdbdwvclnefjkbxkvclnuijakvabnnmnopbxkvanpnbdbdcxanpnbdbdwvlkefakvefK/75225"

    #Input the Quality of the Channels

    qual = raw_input("Type the Quality:\n-->7:Low\n-->17:Medium\n-->32:High\n-->97:Super-High\n----->")
    print 'Set quality to ',qual, 'and setting correct Bitrate...'
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
    
    #Reading Origin File

    print "Reading origin file and copying it..."

    #VLC
    originvlcweb = urllib.urlopen(albicrypt.Decode(vlcblockurl))
    destvlc = originvlcweb.read()
    originvlcweb.close()

    #Kodi (if selected)
    if kodiopt == "1":
        originkodiweb = urllib.urlopen(albicrypt.Decode(vlcblockurl))
        destkodi= originkodiweb.read()
        originkodiweb.close()
    else:
        originkodiweb = ""
        destkodi = originkodiweb

    print "Copied."


    #Script OPUS-Token

    tokenopuscf = libalbi.OpusCFToken('base1')
    tokenopuscf0 = tokenopuscf
    tokenopuscf1 = libalbi.OpusCFToken('base2')
    tokenopuscf2 = libalbi.OpusCFToken('sha')
    tokenopuscf3 = libalbi.OpusCFToken('baseshort')

    #Creating a file with all the tokens if tokenfileopt is "Yes"

    if tokenfileopt == "1":
        tokenfile1="\n------------------------------------------------\n\nFor IP: myip the OPUS-tokens are: \n--> Base1: tokenchange0\n\n--> Base2: tokenchange1\n\n--> SHA: tokenchange2\n\n--> Fluxies: tokenchange3\n\n------------------------------------------------\n"
        tokenfile1 = tokenfile1.replace("tokenchange0",tokenopuscf0)
        tokenfile1 = tokenfile1.replace("tokenchange1",tokenopuscf1)
        tokenfile1 = tokenfile1.replace("tokenchange2",tokenopuscf2)
        tokenfile1 = tokenfile1.replace("tokenchange3",tokenopuscf3)
        tokenfile1 = tokenfile1.replace("myip",ip)
        tokenfile = file("tokens.txt","w")
        tokenfile.write(tokenfile1)
        tokenfile.close()
        
    #Stuff for VLC Playlist
    #FrenchStream
        
    destvlc = libalbi.Selection("francetvch","O",destvlc,qual)

    #Wilmaa Streams

    destvlc = libalbi.Selection("chan","5_plus_hd",destvlc,qual)

    #Fluxies Streams

    destvlc = libalbi.Selection("fluxies","sfr_3",destvlc,qual)

    #Bein Streams

    destvlc = libalbi.Selection("bein","10",destvlc,qual)

    #RTBF Stream Stat

    destvlc = libalbi.RTBFStat("1",destvlc,"vlc")
    destvlc = libalbi.RTBFStat("2",destvlc,"vlc")
    destvlc = libalbi.RTBFStat("3",destvlc,"vlc")

    #RTS suisse channels on Opus

    destvlc = libalbi.RTSCh(destvlc,qual)

    #Doing The playlist for kodi if selected

    if kodiopt == "1":
        ptype = "kodi"
        destkodi = libalbi.Selection("francetvch","O",destkodi,qual)
        destkodi = libalbi.Selection("chan","5_plus_hd",destkodi,qual)
        destkodi = libalbi.Selection("fluxies","sfr_3",destkodi,qual)
        destkodi = libalbi.Selection("bein","10",destkodi,qual)
        destkodi = libalbi.RTBFStat("1",destkodi,"kodi")
        destkodi = libalbi.RTBFStat("2",destkodi,"kodi")
        destkodi = libalbi.RTBFStat("3",destkodi,"kodi")
        destkodi = libalbi.RTSCh(destkodi,qual)
        
    #Step 2.
    #Copying All in the final files.

    print "Got Tokens and Links, starting step 2..."
    print "Opening Copy and replacing strings..."
    libalbi.FileWriteReplace(destvlc,"play-vlc.m3u",qual)

    if kodiopt == "1":
        libalbi.FileWriteReplace(destkodi,"play-kodi.m3u",qual)

    #Finishing

    print "Writing last things..."
    print "OK, all done!"
    tempo2 = time.time()
    tempfin = tempo2-tempo1
    print "Running Time: "+str(tempfin)
    os.system('pause')

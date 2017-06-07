import urllib, urllib2, string, time
print "Playlist OPUS by Albiii!"
qual = raw_input("Type the Quality:\n 7:Low\n 17:Low/High\n 32:High\n 97:Super High\n ")
#qual = "17"
print "Setting quality to ",qual
print "Getting OPUS-Token..."
link = urllib.urlopen("http://racacaxtv.ga/mega.php?chn=VEYx&pls=RnJhbmNvcGhvbmVz")
page = link.read()
postoken = string.find(page,"wil/4BHu")
postoken2 = string.find(page,"/tf_1_hd/")
token = page[(postoken+4):(postoken2)]
#script francetv
print "Getting France.tv links and tokens and proxy..."
link2 = urllib.urlopen("http://www.mytvonline.org/minproxy.php/http://hdfauthftv-a.akamaihd.net/esi/TA?format=json&url=http%3A%2F%2Flive.francetv.fr%2Fsimulcast%2FFrance_2%2Fhls_v1%2Findex.m3u8")
link3 = urllib.urlopen("http://www.mytvonline.org/minproxy.php/http://hdfauthftv-a.akamaihd.net/esi/TA?format=json&url=http%3A%2F%2Flive.francetv.fr%2Fsimulcast%2FFrance_3%2Fhls_v1%2Findex.m3u8")
link4 = urllib.urlopen("http://www.mytvonline.org/minproxy.php/http://hdfauthftv-a.akamaihd.net/esi/TA?format=json&url=http%3A%2F%2Flive.francetv.fr%2Fsimulcast%2FFrance_4%2Fhls_v1%2Findex.m3u8")
link5 = urllib.urlopen("http://www.mytvonline.org/minproxy.php/http://hdfauthftv-a.akamaihd.net/esi/TA?format=json&url=http%3A%2F%2Flive.francetv.fr%2Fsimulcast%2FFrance_5%2Fhls_v1%2Findex.m3u8")
linkO = urllib.urlopen("http://www.mytvonline.org/minproxy.php/http://hdfauthftv-a.akamaihd.net/esi/TA?format=json&url=http%3A%2F%2Flive.francetv.fr%2Fsimulcast%2FFrance_O%2Fhls_v1%2Findex.m3u8")
page2 = link2.read()
page3 = link3.read()
page4 = link4.read()
page5 = link5.read()
pageO = linkO.read()
postoke21 = string.find(page2,"2/hls_v1/")
postoke22 = string.find(page2,"/index")
postoke23 = string.find(page2,"}")
postoke31 = string.find(page3,"3/hls_v1/")
postoke32 = string.find(page3,"/index")
postoke33 = string.find(page2,"}")
postoke41 = string.find(page4,"4/hls_v1/")
postoke42 = string.find(page4,"/index")
postoke43 = string.find(page2,"}")
postoke51 = string.find(page5,"5/hls_v1/")
postoke52 = string.find(page5,"/index")
postoke53 = string.find(page2,"}")
postokeO1 = string.find(pageO,"O/hls_v1/")
postokeO2 = string.find(pageO,"/index")
postokeO3 = string.find(page2,"}")
tokfr2a =page2[(postoke21+9):(postoke22)]
tokfr3a =page3[(postoke31+9):(postoke32)]
tokfr4a =page4[(postoke41+9):(postoke42)]
tokfr5a =page5[(postoke51+9):(postoke52)]
tokfrOa =pageO[(postokeO1+9):(postokeO2)]
tokfr2b =page2[(postoke22+11):(postoke23-1)]
tokfr3b =page3[(postoke32+11):(postoke33-1)]
tokfr4b =page4[(postoke42+11):(postoke43-1)]
tokfr5b =page5[(postoke52+11):(postoke53-1)]
tokfrOb =pageO[(postokeO2+11):(postokeO3-1)]
stream2 = "http://live.francetv.fr/simulcast/France_2/hls_v1/" + tokfr2a + "/France_2-video=1465200-audio_AACL_fra_65600_315=65600.m3u8" + tokfr2b
stream3 = "http://live.francetv.fr/simulcast/France_3/hls_v1/" + tokfr3a + "/France_3-video=1465200-audio_AACL_fra_65600_325=65600.m3u8" + tokfr3b
stream4 = "http://live.francetv.fr/simulcast/France_4/hls_v1/" + tokfr4a + "/France_4-video=1465200-audio_AACL_fra_65600_335=65600.m3u8" + tokfr4b
stream5 = "http://live.francetv.fr/simulcast/France_5/hls_v1/" + tokfr5a + "/France_5-video=1465200-audio_AACL_fra_65600_345=65600.m3u8" + tokfr5b
streamO = "http://live.francetv.fr/simulcast/France_O/hls_v1/" + tokfrOa + "/France_O-video=1465200-audio_AACL_fra_65600_355=65600.m3u8" + tokfrOb
print "Got Tokens and Links, starting step 2..."
#origin = file("origin.m3u","r")
print "Reading origin file and copying it..."
originweb = urllib.urlopen("http://tvmaster.hol.es/liste/origin.m3u")
dest = originweb.read()
print "Copied."
originweb.close()
#dest = origin.read()
#origin.close()
print "Opening Copy and replacing strings..."
dest1 = file("play-weborigin.m3u","w")
data = time.strftime("%d/%m")
dest = string.replace(dest,"datareplace",data)
dest = string.replace(dest,"tokenchange",token)
dest = string.replace(dest,"qual",qual)
dest = string.replace(dest,"stream2",stream2)
dest = string.replace(dest,"stream3",stream3)
dest = string.replace(dest,"stream4",stream4)
dest = string.replace(dest,"stream5",stream5)
dest = string.replace(dest,"streamO",streamO)
dest = string.replace(dest,"\n","")
dest1.write(dest)
print "Writing last things..."
dest1.close()
print "OK, all done!"
print "Fatto!"



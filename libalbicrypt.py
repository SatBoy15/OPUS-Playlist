import time,string,random
k="qr"
l="cd"
m="st"
n="gh"
o="yz"
p="c1"
q="mn"
r="op"
s="ab"
t="ef"
u="uv"
v="wx"
w="ij"
x="az"
y="bx"
z="kv"
aa="cf"
ab="ln"
ac="bd"
ad="gj"
ae="sv"
af="pn"
ag="zx"
ah="an"
ai="wv"
aj="cx"
sp="sp"
ak="lk"
al="jk"
am="lm"
tr="nn"

def Encode(word,key):
    a=str(0+key)
    b=str(9+key)
    c=str(2+key)
    d=str(4+key)
    e=str(8+key)
    f=str(6+key)
    g=str(7+key)
    h=str(1+key)
    i=str(3+key)
    j=str(5+key)
    text = word
    text = string.replace(text,"a",a)
    text = string.replace(text,"b",b)
    text = string.replace(text,"c",c)
    text = string.replace(text,"d",d)
    text = string.replace(text,"e",e)
    text = string.replace(text,"f",f)
    text = string.replace(text,"g",g)
    text = string.replace(text,"h",h)
    text = string.replace(text,"i",i)
    text = string.replace(text,"j",j)
    text = string.replace(text,"k",k)
    text = string.replace(text,"l",l)
    text = string.replace(text,"m",m)
    text = string.replace(text,"n",n)
    text = string.replace(text,"o",o)
    text = string.replace(text,"p",p)
    text = string.replace(text,"q",q)
    text = string.replace(text,"r",r)
    text = string.replace(text,"s",s)
    text = string.replace(text,"t",t)
    text = string.replace(text,"u",u)
    text = string.replace(text,"v",v)
    text = string.replace(text,"w",w)
    text = string.replace(text,"x",x)
    text = string.replace(text,"y",y)
    text = string.replace(text,"z",z)
    text = string.replace(text," ",sp)
    text = string.replace(text,"0",aa)
    text = string.replace(text,"1",ab)
    text = string.replace(text,"2",ac)
    text = string.replace(text,"3",ad)
    text = string.replace(text,"4",ae)
    text = string.replace(text,"5",af)
    text = string.replace(text,"6",ag)
    text = string.replace(text,"7",ah)
    text = string.replace(text,"8",ai)
    text = string.replace(text,"9",aj)
    text = string.replace(text,".",ak)
    text = string.replace(text,"/",al)
    text = string.replace(text,":",am)
    text = string.replace(text,"-",tr)
    return text + "K/"+str(key)

def Decode(word):
    text = word
    keypos = string.find(text,"K/")
    key = text[keypos+2:]
    keyreplace = text[keypos:]
    text = string.replace(text,keyreplace,"")
    text = string.replace(text,tr,"-")
    text = string.replace(text,am,":")
    text = string.replace(text,al,"/")
    text = string.replace(text,ak,".")
    text = string.replace(text,aj,"9")
    text = string.replace(text,ai,"8")
    text = string.replace(text,ah,"7")
    text = string.replace(text,ag,"6")
    text = string.replace(text,af,"5")
    text = string.replace(text,ae,"4")
    text = string.replace(text,ad,"3")
    text = string.replace(text,ac,"2")
    text = string.replace(text,ab,"1")
    text = string.replace(text,aa,"0")
    a=str(0+int(key))
    b=str(9+int(key))
    c=str(2+int(key))
    d=str(4+int(key))
    e=str(8+int(key))
    f=str(6+int(key))
    g=str(7+int(key))
    h=str(1+int(key))
    i=str(3+int(key))
    j=str(5+int(key))
    text = string.replace(text,sp," ")
    text = string.replace(text,z,"z")
    text = string.replace(text,y,"y")
    text = string.replace(text,x,"x")
    text = string.replace(text,w,"w")
    text = string.replace(text,v,"v")
    text = string.replace(text,u,"u")
    text = string.replace(text,t,"t")
    text = string.replace(text,s,"s")
    text = string.replace(text,r,"r")
    text = string.replace(text,q,"q")
    text = string.replace(text,p,"p")
    text = string.replace(text,o,"o")
    text = string.replace(text,n,"n")
    text = string.replace(text,m,"m")
    text = string.replace(text,l,"l")
    text = string.replace(text,k,"k")
    text = string.replace(text,j,"j")
    text = string.replace(text,i,"i")
    text = string.replace(text,h,"h")
    text = string.replace(text,g,"g")
    text = string.replace(text,f,"f")
    text = string.replace(text,e,"e")
    text = string.replace(text,d,"d")
    text = string.replace(text,c,"c")
    text = string.replace(text,b,"b")
    text = string.replace(text,a,"a")
    return text

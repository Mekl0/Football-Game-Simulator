import time
import random
#txt.dosyalarımızdaki verileri programımıza listeler yardımıyla aldık
def Oyunculist(OY,K,D,A):
    def listal (lial) :
        ok=True
        ListO=[]
        try :
            tut=open(lial,"r")
            ListO=tut.readlines()
            tut.close()
        except:
                print(tut, " dosyası okuma hatası...!")
                ok = False
        return ListO,ok
    OYlist=[]
    Kalelist=[]
    Defanslist=[]
    Ataklist=[]
    OYlist,ok=listal(OY)
    if ok:
        Kalelist,ok=listal(K)
        if ok:
            Defanslist,ok=listal(D)
            if ok:
                Ataklist,ok=listal(A)
    return OYlist,Kalelist,Defanslist,Ataklist
#kullanıcıdan kadrosunu kurmasını istiyoruz 11 tane oyuncu seçtiriyoruz ve kadroyu(11 oyuncu) bir listede return ediyoruz
def verial(Tip):
    icerde=False

    used=[]
    def kontrol(icerde):

        oyuncu=""
        while icerde==False:
                if oyuncu in used or oyuncu not in Players :
                    oyuncu= input("Yukarıdaki listeden bir Oyuncu girmediniz veya daha önce kadronuza eklediğiniz bir oyuncu girdiniz.Lütfen listenin içinden ve daha önce kadronuza ekelemediğiniz bir oyuncu seçiniz :")
                    if oyuncu not in used and oyuncu in Players:

                        icerde=True
        return oyuncu,used


    if Tip.upper()=="A" :
        for i in range(len(Players)-1):
             print((Players[i]+"   ATAK GÜCÜ  :"+str(ATAKCILAR[i])+"   DEFANS GÜCÜ :"+str(DEFANSCILAR[i])+"   KALE GÜCÜ  :"+(KALECILER[i])))


        kaleci=input("Kaleci seçiniz :")
        if kaleci not in (Players) or kaleci  in used:
            kaleci=kontrol(icerde)
        used.append(kaleci)
        defans1=input("1.defans oyuncunuzu seçiniz :")
        if defans1 not in (Players)or defans1  in used:
            defans1=kontrol(icerde)
        used.append(defans1)
        defans2=input("2.defans oyuncunuzu seçiniz :")
        if defans2 not in (Players)or defans2  in used:
           defans2=kontrol(icerde)
        used.append(defans2)
        defans3=input("3.defans oyuncunuzu seçiniz :")
        if defans3 not in (Players)or defans3  in used:
            defans3=kontrol(icerde)
        used.append(defans3)
        defans4=input("4.defans oyuncunuzu seçiniz :")
        if defans4 not in (Players)or defans4  in used:
            defans4=kontrol(icerde)
        used.append(defans4)
        ortasaha1=input("1. ortasaha oyuncunuzu seçiniz :")
        if ortasaha1 not in (Players)or ortasaha1  in used:
            ortasaha1=kontrol(icerde)
        used.append(ortasaha1)
        ortasaha2=input("2. ortasaha oyuncunuzu seçiniz :")
        if ortasaha2 not in (Players)or ortasaha2  in used:
            ortasaha2=kontrol(icerde)
        used.append(ortasaha2)
        ortasaha3=input("3. ortasaha oyuncunuzu seçiniz :")
        if ortasaha3 not in (Players)or ortasaha3  in used:
            ortasaha3=kontrol(icerde)
        used.append(ortasaha3)
        forvet1=input("1.forvet oyuncunuzu seçiniz :")
        if forvet1 not in (Players)or forvet1  in used:
            forvet1=kontrol(icerde)
        used.append(forvet1)
        forvet2=input("2.forvet oyuncunuzu seçiniz :")
        if forvet2 not in (Players)or forvet2  in used:
            forvet2=kontrol(icerde)
        used.append(forvet2)
        forvet3=input("3.forvet oyuncunuzu seçiniz :")
        if forvet3 not in (Players) or forvet3  in used:
            forvet3=kontrol(icerde)
        used.append(forvet3)
        Kadro=[kaleci,defans1,defans2,defans3,defans4,ortasaha1,ortasaha2,ortasaha3,forvet1,forvet2,forvet3]
    elif Tip.upper()=="B":
         for i in range(len(Players)):
             print((Players[i]+"   ATAK GÜCÜ  :"+str(ATAKCILAR[i])+"   DEFANS GÜCÜ :"+str(DEFANSCILAR[i])+"   KALE GÜCÜ  :"+(KALECILER[i])))
         kaleci=input("Kaleci seçiniz :")
         if kaleci not in (Players) or kaleci  in used:
            kaleci=kontrol(icerde)
         used.append(kaleci)
         defans1=input("1.defans oyuncunuzu seçiniz :")
         if defans1 not in (Players) or defans1  in used:
            defans1=kontrol(icerde)
         used.append(defans1)
         defans2=input("2.defans oyuncunuzu seçiniz :")
         if defans2 not in (Players)  or defans2  in used:
            defans2=kontrol(icerde)
         used.append(defans2)
         defans3=input("3.defans oyuncunuzu seçiniz :")
         if defans3 not in (Players)  or defans3  in used:
            defans3=kontrol(icerde)
         used.append(defans3)
         defans4=input("4.defans oyuncunuzu seçiniz :")
         if defans4 not in (Players) or defans4  in used:
            defans4=kontrol(icerde)
         used.append(defans4)
         ortasaha1=input("1. ortasaha oyuncunuzu seçiniz :")
         if ortasaha1 not in (Players) or ortasaha1  in used:
            ortasaha1=kontrol(icerde)
         used.append(ortasaha1)
         ortasaha2=input("2. ortasaha oyuncunuzu seçiniz :")
         if ortasaha2 not in (Players) or ortasaha2  in used:
            ortasaha2=kontrol(icerde)
         used.append(ortasaha2)
         ortasaha3=input("3. ortasaha oyuncunuzu seçiniz :")
         if ortasaha3 not in (Players) or ortasaha3  in used:
            ortasaha3=kontrol(icerde)
         used.append(ortasaha3)
         ortasaha4=input("4.ortasaha oyuncunuzu seçiniz :")
         if ortasaha4 not in (Players) or ortasaha4  in used:
            ortasaha4=kontrol(icerde)
         used.append(ortasaha4)
         forvet1=input("1.forvet oyuncunuzu seçiniz :")
         if forvet1 not in (Players)  or forvet1  in used:
            forvet1=kontrol(icerde)
         used.append(forvet1)
         forvet2=input("2.forvet oyuncunuzu seçiniz :")
         if forvet2 not in (Players) or forvet2  in used:
            forvet2=kontrol(icerde)
         used.append(forvet2)

         Kadro=[kaleci,defans1,defans2,defans3,defans4,ortasaha1,ortasaha2,ortasaha3,ortasaha4,forvet1,forvet2]
    elif Tip.upper()=="C":
         for i in range(len(Players)):
             print((Players[i]+"   ATAK GÜCÜ  :"+str(ATAKCILAR[i])+"   DEFANS GÜCÜ :"+str(DEFANSCILAR[i])+"   KALE GÜCÜ  :"+(KALECILER[i])))
         kaleci=input("Kaleci seçiniz :")
         if kaleci not in (Players) or kaleci  in used:
            kaleci=kontrol(icerde)
         used.append(kaleci)
         defans1=input("1.defans oyuncunuzu seçiniz :")
         if defans1 not in (Players) or defans1  in used:
            defans1=kontrol(icerde)
         used.append(defans1)
         defans2=input("2.defans oyuncunuzu seçiniz :")
         if defans2 not in (Players)  or defans2  in used:
            defans2=kontrol(icerde)
         used.append(defans2)
         defans3=input("3.defans oyuncunuzu seçiniz :")
         if defans3 not in (Players) or defans3  in used:
            defans3=kontrol(icerde)
         used.append(defans3)
         ortasaha1=input("1. ortasaha oyuncunuzu seçiniz :")
         if ortasaha1 not in (Players) or ortasaha1  in used:
            ortasaha1=kontrol(icerde)
         used.append(ortasaha1)
         ortasaha2=input("2. ortasaha oyuncunuzu seçiniz :")
         if ortasaha2 not in (Players) or ortasaha2  in used:
            ortasaha2=kontrol(icerde)
         used.append(ortasaha2)
         ortasaha3=input("3. ortasaha oyuncunuzu seçiniz :")
         if ortasaha3 not in (Players) or ortasaha3  in used:
            ortasaha3=kontrol(icerde)
         used.append(ortasaha3)
         ortasaha4=input("4.ortasaha oyuncunuzu seçiniz :")
         if ortasaha4 not in (Players) or ortasaha4  in used:
            ortasaha4=kontrol(icerde)
         used.append(ortasaha4)
         ortasaha5=input("5.ortasaha oyuncunuzu seçiniz :")
         if ortasaha5 not in (Players) or ortasaha5  in used:
            ortasaha5=kontrol(icerde)
         used.append(ortasaha5)
         forvet1=input("1.forvet oyuncunuzu seçiniz :")
         if forvet1 not in (Players) or forvet1  in used:
            forvet1=kontrol(icerde)
         used.append(forvet1)
         forvet2=input("2.forvet oyuncunuzu seçiniz :")
         if forvet2 not in (Players) or forvet2  in used:
            forvet2=kontrol(icerde)
         used.append(forvet2)
         Kadro=[kaleci,defans1,defans2,defans3,ortasaha1,ortasaha2,ortasaha3,ortasaha4,ortasaha5,forvet1,forvet2]

    else:
            print("Lütfen tanımlı bir formasyon seçiniz !")
            check=False
            while check==False:
                Tip=input("Hangi formasyonu oynamak istiyorsunuz 4-3-3 için A 4-4-2 için B 3-5-2 için C yazınız :" )

                if Tip.upper() =="A" or Tip.upper() =="B" or Tip.upper()=="C":
                    check=True
                    Kadro=verial(Tip)
    return Kadro

def mevki(Kadro):

    #kullanıcının seçtiği oyuncuların güçlerini kullanıcının takımına yüklüyoruz
    def gucbelirle(index,Kalelist,Defanslist,Ataklist,taypee):
        atak=0
        defans=0
        kale=0
        de=int(Defanslist[index])
        at=int(Ataklist[index])
        ka=int(Kalelist[index])
        if taypee=="A" :
            atak=atak+at
            defans=defans+(de*(0.1))
            kale=kale

        if taypee=="D":
            atak=atak+(at*(0.1))
            defans=defans+de
            kale=kale
        if taypee=="K":
            atak=atak+0
            defans=defans+(ka*3)
            kale=kale+ka

        if taypee=="O":
            atak=at*(0.5)
            defans=de*(0.5)
            kale=kale

        return atak,defans,kale
    #kullanıcının seçtiği oyuncunun kaçıncı satırda olduğu bilgisini alıyoruz ilerde kullanabilmek için
    def ara(aranan,Players):
            index=-1
            found=False
            for i in range(len(Players)):
               dogrukis=Players[i]
               dogrukisi = dogrukis.rstrip("\n")
               if dogrukisi==aranan:
                    index=i
                    found=True
                    break
            return index,found
    atakgucu=0
    defansgucu=0
    kalegucu=0
    for i in range(len(Kadro)):
        index,found=ara(Kadro[i],Players)
        if found:
            if Tip.upper()=="A" :
                if i <1 :
                    type="K"
                if i>=1 and i<5:
                    type="D"
                if i>=5 and i<8 :
                    type="O"
                if i>=8 and i<11:
                    type="A"
            elif Tip.upper()=="B":
                if i <1 :
                    type="K"
                if i>=1 and i<5:
                    type="D"
                if i>=5 and i<9 :
                    type="O"
                if i>=9 and i<11:
                    type="A"
            elif Tip.upper()=="C":
                if i <1 :
                    type="K"
                if i>=1 and i<4:
                    type="D"
                if i>=4 and i<9 :
                    type="O"
                if i>=9 and i<11:
                    type="A"
            atak,defans,kale=gucbelirle(index,KALECILER,DEFANSCILAR,ATAKCILAR,type)
            atakgucu=atakgucu+atak
            defansgucu=defansgucu+defans
            kalegucu=kalegucu+kale
            i+=1
    return atakgucu,defansgucu,kalegucu
def kapistir(takimadi,atakgucu,defansgucu,rakiptakimadi,rakipatak,rakipdefans):
    gc=(rakipdefans/atakgucu)*100
    gc=round(gc,0)
    egc=(defansgucu/rakipatak)*100
    egc=round(egc,0)
    team1=0
    team2=0
    print("MAÇ BAŞLADI")
    for i in range(90):
        s=random.randint(0,gc)
        a=random.randint(0,egc)
        if s==1:
            team1=team1+1
            print( takimadi+" GOL ATTI dakika :"+str(i))
        if a==1:
            team2=team2+1
            print(rakiptakimadi+" GOL ATTI dakika :"+str(i))
        time.sleep(0.2)
    if team1>team2:
        print("Kazandınız")

        print((takimadi)+"  "+str(team1)+"-"+str(team2)+rakiptakimadi)
        KAZANAN=True
    elif team2>team1:
        print("KAYBETTİNİZ")
        KAZANAN=False
        print((takimadi)+"  "+str(team1)+"-"+str(team2)+rakiptakimadi)
    elif team1==team2:
        print("90 DAKİKA SONUCUNDA EŞİTLİK BOZULMADI KAZANAN PENALTILARDA BELİRLENECEK")
        time.sleep(3)
        print((takimadi)+"  "+str(team1)+"-"+str(team2)+rakiptakimadi)
        x=random.randint(1,2)
        if x==1:
            KAZANAN=True
            print("PENALTILAR SONUCU "+takimadi+" KAZANDI")
        else:
            print("PENALTILAR SONUCU" +takimadi+" KAZANDI")
            KAZANAN=False
    return KAZANAN
#turnuva modundu başlatmak için bu fonksıyonu kullanıyoruz
def turnuva():
    Rakipler=["REAL MADRID","BARCELONA","MANCHESTER UNITED","MANCHESTER CITY","LIVERPOOL","ARSENAL","CHEALSEA","ATLETICO MADRID","BENFICA","INTER","MILAN","JUVENTUS","NAPOLI","BAYERN MUNICH","BORISSIA DORTMUND"]
    Rakipsaldırı=[550,450,425,580,550,500,525,400,450,375,385,410,150,550,50]
    Rakipdefans= [150,150,125,150,125,125,175,200,125,150,150,125,120,130,140]
    used=[]
    def takimsec():



        index=random.randint(0,14)
        if index  in used:
            while index  in used:
                index=random.randint(0,14)


        Rakiptakim=Rakipler[index]
        Rakiptakimatak=Rakipsaldırı[index]
        Rakiptakimdefans=Rakipdefans[index]
        return Rakiptakim,Rakiptakimatak,Rakiptakimdefans,index
    Rakiptakim,Rakiptakimatak,Rakiptakimdefans,index= takimsec()
    used.append(index)

    print("SON 16 TURU MAÇINIZ BAŞLIYOR RAKİBİNİZ :"+Rakiptakim)

    KAZANAN=kapistir(ad1,atakgucu,defansgucu,Rakiptakim,Rakiptakimatak,Rakiptakimdefans)
    if KAZANAN:
        print("TEBRİKLER ÇEYREK FİNALLERDESİNİZ")

        Rakiptakim,Rakiptakimatak,Rakiptakimdefans,index= takimsec()
        used.append(index)
        print("ÇEYREK FİNAL MAÇINIZ BAŞLIYOR RAKİBİNİZ :"+Rakiptakim)
        KAZANAN=kapistir(ad1,atakgucu,defansgucu,Rakiptakim,Rakiptakimatak,Rakiptakimdefans)
        if KAZANAN:
            print("YARI FİNALLERDESİNİZ")
            Rakiptakim,Rakiptakimatak,Rakiptakimdefans,index= takimsec()
            used.append(index)

            print("YARI FİNAL MAÇINIZ BAŞLIYOR RAKİBİNİZ :"+Rakiptakim)
            KAZANAN=kapistir(ad1,atakgucu,defansgucu,Rakiptakim,Rakiptakimatak,Rakiptakimdefans)

            if KAZANAN:
                print("TEBRİKLER FİNALLERDESİNİZ")
                Rakiptakim,Rakiptakimatak,Rakiptakimdefans,index= takimsec()
                used.append(index)
                print(" FİNAL MAÇINIZ BAŞLIYOR RAKİBİNİZ :"+Rakiptakim)
                KAZANAN=kapistir(ad1,atakgucu,defansgucu,Rakiptakim,Rakiptakimatak,Rakiptakimdefans)
                if KAZANAN:
                    print("TEBRİKLER EFSANALER LİGİ ŞAMPİYONU OLDUNUZ")
                else:
                    print("FİNALLERDE ELENDİNİZ")
            else:
                print("YARI FİNALDE ELENDİNİZ")
        else:
            print("Çeyrek FİNALDE ELENDİNİZ")


    else:
        print("SON 16 da elendiniz")



OY="OYUNCULAR.txt"
K="KALE.txt"
D="DEFANS.txt"
A="ATAK.txt"
Playersa,KALECILERA,DEFANSCILARA,ATAKCILARA=Oyunculist(OY,K,D,A)
#bu kısımda /n diye  istemediğimiz bir şey oluyordu onu engellemek için böyle bir şey yaptık
Players=[]
for i in range(len(Playersa)):
    g=Playersa[i].rstrip("\n")
    Players.append(g)
DEFANSCILAR=[]
for i in range(len(DEFANSCILARA)):
    g=DEFANSCILARA[i].rstrip("\n")
    DEFANSCILAR.append(g)
ATAKCILAR=[]
for i in range(len(ATAKCILARA)):
    g=ATAKCILARA[i].rstrip("\n")
    ATAKCILAR.append(g)
KALECILER=[]
for i in range(len(KALECILERA)):
    g=KALECILERA[i].rstrip("\n")
    KALECILER.append(g)

print("EFSANELER LİGİNE HOŞ GELDİNİZ")
mod=input("Hangi modu oynamak istiyorsunuz 1v1 için '1v1'Turnuva için 'T'yazınız :")
if mod.upper()!="1V1" and mod.upper()!="T":
    mod=input("Tanımlı bir oyun modu girmediniz lütfen tanımlı bir oyun modu giriniz !!")
    while mod.upper() !="1V1" and mod.upper()!="T":

        mod=input("Tanımlı bir oyun modu girmediniz lütfen tanımlı bir oyun modu giriniz !!")


if mod.upper() =="T":
    ad1=input("TAKIMINIZIN ADINI GİRİNİZ :")
    Tip=input("Hangi formasyonu oynamak istiyorsunuz 4-3-3 için A 4-4-2 için B 3-5-2 için C yazınız :" )
    Kadro=verial(Tip)
    atakgucu,defansgucu,kalegucu=mevki(Kadro)
    turnuva()
elif mod.upper()=="1V1":
    ad1=input("TAKIMINIZIN ADINI GİRİNİZ :")
    Tip=input("Hangi formasyonu oynamak istiyorsunuz 4-3-3 için A 4-4-2 için B 3-5-2 için C yazınız :" )
    Kadro=verial(Tip)
    atakgucu5,defansgucu5,kalegucu5=mevki(Kadro)
    ad2=input("TAKIMINIZIN ADINI GİRİNİZ :")
    Tip=input("Hangi formasyonu oynamak istiyorsunuz 4-3-3 için A 4-4-2 için B 3-5-2 için C yazınız :" )
    Kadro2=verial(Tip)
    atakgucu2,defansgucu2,kalegucu2=mevki(Kadro2)
    kapistir(ad1,atakgucu5,defansgucu5,ad2,atakgucu2,defansgucu2)











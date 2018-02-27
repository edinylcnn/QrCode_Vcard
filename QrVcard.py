import urllib.parse
import urllib.request
import os
#kutuphaneleri ekledik

try:
    size = input("QR Size : ")
    ad = input("Ad : ")
    soyad= input("Soyad : ")
    title = input("Title : ")
    telefon = input("Telefon : ")
    email = input("Email : ")
    #QR kodun içine ekliceğimiz verileri kullanıcıdan aldık

    FileName = input("FileName") + ".png"
    #dosyanın hangi isimle kaydedilmesini istediğimizi kullanıcıya sorduk

    datas = {
           'FN:' : ad + " "+ soyad,
           'TITLE:' : title,
           'TEL;TYPE=WORK,VOICE:' : telefon,
           'EMAIL;TYPE=PREF,INTERNET:' : email
           }
    #Vcard için aldığımız verileri kodlarıyla eşleştirdik

    boyut = size + "x" + size
    #QR kodun olculerını gereklı formata cevırdık

    parametreler = urllib.parse.urlencode(datas)
    #aldığımız bütün verileri url formatına çevirdik

    yeni = parametreler.replace("&", "%0A")
    # dataların sonundaki " "(boşluk/space) verisini enter/newline verisine çevirdik
    sondata = yeni.replace("=","")
    #eşleştirme ile gelen fazlalık "=" verisini kaldırdık

    urlbas = "https://chart.googleapis.com/chart?cht=qr&chl=BEGIN%3AVCARD%0AVERSION%3A3.0%0A"
    urlson = "%0AEND%3AVCARD%0A&chs="+ boyut +"&choe=UTF-8&chld=L|2"
    #url yapısına göre sabit yerleri parçaladık

    print("\n")

    temizurl = urlbas + sondata + urlson
    #url ımızı birleştirdik
    print(temizurl)
    # ve url i yazdırdık
    print("\n")
    print("\n")

    urllib.request.urlretrieve(temizurl, FileName)
    #Dosyayı aldığımız isme göre kaydettirdik
    print("Success")
    print("\n")
    #bir hata ile karşılaşılmaz ise başarılı bilgisini verdi
    print(os.path.abspath(FileName))
    #Dosyayı kaydettiği yolu ekrana yazdırdı
except:
    print("Creation Failed")
    #Bir sorun ile karşılaştığında veya başarısız olduğunda hatayı verip durdurdu

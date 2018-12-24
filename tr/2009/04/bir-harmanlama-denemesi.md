# Bir Harmanlama Denemesi

Onceki yazida bahsettigimiz harmanlamanin bir ornek kodlamasini yapalim... Eglence olsun. Efendim; Python adli bir dilde, RSS verisini okuyarak (dilde beslemelerin okunabilmesini saglayan guzel ek paketleri ve esnek bir kullanimi vardir), icindeki ilgilendigimiz anahtar kelimeleri cekip cikartacagiz ve korelasyon bulmaya ugrasacagiz.

Hangi verileri okuyalim? Diyelim ki Amerikan hukumetinin RSS ile yayinladigi bazi ekonomik veriler. Usa.gov sitesinde bu yayini buluyoruz. Listede "veriler ve istatistikler (data and statistics)" diyen baglantiya tikliyoruz "isgucu istatistikleri (labor statistics) .." diyen alt baglantiya gidiyoruz. Listede pek cok besleme kaynagi yayini goruyoruz.

Hangi veri kaynaklarini harmanlayalim? Diyelim ki "Uretkenlik ve Maliyet Son Rakamlar (Productivity and Costs Latest Numbers)" RSS'i ile "Uretici Fiyat Endeksleri Son Rakamlar (Producer Price Indexes Latest Numbers)" RSS'i harmanlansin.

Bu iki kaynak icinde birincisinden "saat basina uretimde degisim" degerini, ikincisinde "tibbi ofis acilimlarinda degisim orani" degerlerini cekip cikartacagiz ve aralarinda artis/azalis korelasyonuna bakacagiz. Okuma yapmamizi saglayacak yardimci kodlarini suradan indirdikten sonra, analiz programini yazabiliriz.

```
import feedparser, re;

d = feedparser.parse("http://www.bls.gov/feed/lpc_latest.rss")
content = d['entries'][0]['summary_detail']['value']
regex = "Manufacturing.*?Output per Hour.*?(\+|\-)"+\
  "(\d*\.\d*).*?in\s(.*?)<"
  man_out = re.findall(regex, content, re.DOTALL)[0]

d = feedparser.parse("http://www.bls.gov/feed/ppi_latest.rss")
content = d['entries'][0]['summary_detail']['value']
regex = "Offices of physicians.*?(\+|\-)"+\
  "(\d*\.\d*).*?in\s(.*?)<"
  off_pys = re.findall(regex, content, re.DOTALL)[0]

if (man_out[0] != off_pys[0]):
  print "Negatif korelasyon bulundu"
  else:
    print "Pozitif korelasyon bulundu"

print man_out[0] + man_out[1] + " ve " + off_pys[0] + off_pys[1]
print "Zaman dilimi: " + man_out[2] + " ve " + off_pys[2]
```

Kodu islettikten sonra sonuc geliyor:

```
Negatif korelasyon bulundu
-4.0 ve +0.1
Zaman dilimi: 4th Qtr of 2008 ve Mar 2009
```

Demek ki bu iki rakam arasinda rapor edilen tarihlerde "ters" bir korelasyon varmis..

Bu arada, ustteki iki RSS kaynagini tamamen rasgele olarak sectik - ilgili alanda bilgisi (domain knowledge) olanlar, daha baska kaynaklar ve olcum noktalari secebilirler dogal olarak.

Imdi: Ustteki program diyelim ki her gun otonom bir sekilde isliyor (ve veri beslemesinin de hergun yeni veriler verdigini farz edelim), ve sonucu alip otomatik olarak bir yere gonderiyor, ya da bir Web sayfasinda listeliyor. Bu analize kim ihtiyac duyabilir? Bir sirketteki karar verici, normal vatandas, girisimci, vs. - envai turden insan olabilir.

Her halukarda, veri oradadir, isteyen onu istedigi sekilde isleyip, istedigi sekilde kullanabilir.

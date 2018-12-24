# Lending Club

Wired

Kevin Bartz adli doktora öğrencisinin araştırmaları onu LendingClub adli bir Web sitesine götürdü. Bu site borç vermek isteyenler ile borç almak isteyenleri birbirine eşleştiren bir şirketti [1]. LC, diğer kişiden kişiye borçları idare eden şirketler gibi borçlanmak isteyenlerin kişisel geçmişini doldurmalarını istiyordu ve, bu borcu niye istediklerini anlatmaları hakkında bir kompozisyon yazmalarını istiyordu. LC bu kişiler hakkında tabii kendi kredi kontrolünü [2] yapıyor; fakat LC'yi özel yapan tüm bu bilgiyi açık olarak "herkesle" paylaşması.

Bartz 4600 kayıt içeren bu veri tabanını indirdi ve kendini tekrarlayan bazı öğeleri (pattern) bulmaya çalıştı. Özellikle kompozisyonlara odaklandı, ve Bartz bazı kelimelerin geç ödemeler ile ilintili olduğunu farketti. Alarm zilleri çaldırması gereken kelimeler şunlardı: İhtiyaç, fatura, iş. Bu kelimeler herhalde o anda borç alan kişinin parasal zorluk içinde olduğunu gösteriyordu.

LC bilgiyi açık bir şekilde paylaşmasının yanında, potansiyel bir borç isteyene not vermek için kullandığı matematiksel formülün kaynak kodlarını da açık şekilde paylaşıyor (open source). Böylece Web'den herhangi biri bu formüle bakıp aklına gelen bazı iyileştirmeleri LC'ye gonderebiliyor.

--

[1] Buna sektörde "kişiden kişiye borç vermek (peer-to-peer lending)" deniyor. Bu çözüm 3. dalgaya uyumlu; borç merkezi, odaklı (ve gördüğümüz gibi patlayınca tüm sistemi yanında götürebilecek) bankalar tarafından değil, tekil kişiler arasında yapılıyor.

[2] Bu bir kişinin borçlanma tarihine bakılarak yapılır, borçlarını ödeyebilen insanların notu yüksektir, diğerlerinin düşüktür, vs.

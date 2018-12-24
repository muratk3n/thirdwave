# Senkron

Doğada, bir eylemi beraber gerçekleştirmeye dönük çoğu senkronizasyon için merkezi bir noktaya ihtiyaç olmadığı biliniyor. Bunun sebebi herhalde sağlam (robüst) ve optimal bir yapıya olan ihtiyaçtadır: Eğer merkez bir nokta olsaydı, bu noktanın ölmesi/yok olması sonucu tüm grubun işi tehlikeye girebilirdi. İlginçtir ki insanların kurduğu ve sağlam bir yapı olan Internet aynı şekilde düzenlenmiştir. Bu merkezsiz yapı, ayrıca, ağın optimal bir şekilde büyüyebilmesini de sağlar. Her yeni birim, ağa istediği noktadan katılabilir ve işe anında başlayabilir çünkü kimsenin merkezi bulmasına gerek yoktur.

Doğadan basit ve ilginç bir örnek, ateş böcekleri olabilir.

Guney Asya'da bir ateş böceği tipi toplu halde oldukları zaman aynı anda, senkronize bir şekilde yanıp sönme kabiliyetine sahiptir. Bunu, yakında gezmekte olan dışı ateş böceklerine mesaj verebilmek için erkek böcekler grubu yapar (yani bu senkronizasyonu gerçekleştirebilmek evrimsel bir avantajdır).

Bu senkronizasyonu gerçekleştirmek için hiçbir koordinatör karaktere ihtiyaç yoktur.

Gayet basit bir şekilde bir böcek kendine en yakın böceğin yanıp sönüşüne bakar. Eğer bu yanıp sönüş kendi frekasından daha fazla işe, o böcek kendi frekansını artırır. Yavaş ise yavaşlatır. Diğer böcekler aynı algoritmayı takip ederler. Bu ufak algoritmaların "kollektif" birleşimi ise, bir süre sonra aynı yanıp sönüşe doğru yaklaşır (converge). Bunu matematiksel olarak modelleyen Winfree, Kuramoto, Strogatz gibi bilim adamları bu sonucu analitik olarak ta ispatlamışlardır.

Ve bu sonuç, daha önce bahsettiğimiz "bütün, parçaların toplamından fazla" kavramını doğrulayan bir gözlemdir.

# InSAR notes

## InSAR - Bürgmann

### Absztrakt

* új módszer: glob. topo, deformáció feltérképezése
* radar képek különböző irányokból &rarr; méteres pontosságú DEM
* tektonikus és szeizmikus mozgások monitorozásának segítése
* deformáció: 10 méteres felbontás, cm pontosság elmozdulás

### Bevezetés

* InSAR elmélet és alkalmazás tanulmányok (Griffiths 1995, Gens & Vangenderen
1996, Bamler & Hartl 1998, Massonnet & Feigl 1998, Madsen & Zebker 1999,
Rosen et al 2000
* alkalmazások: tektonikus deformáció, vulkanizmus, felszín alatti vízáramlás
* óceáni áramlatok, vegetációs paraméterek, klasszifikáció, földcsuszamlások
(Rosen et al 2000, Massonett & Feigl 1998)

### SAR - Hogyan működik

* radar: céltárgy pásztázása mikrohullámokkal, visszavert hullám &rarr; infó
* amplitudó és két utas futásidő &rarr; távolság, sweep &rarr; 2D kép
* valós aperturájú radar: 5-10 km-es felbontás lenne, footprint és teljesítmény
limitál
* SAR: jelfeldolgozás technikák + mh. pályainfó &rarr; 10 m-es felbontás
* SAR feldolgozás jelentős felbontás javítás range és azimut irányban, nyers
radar echok fókuszálásával
* mozgó antenna és képpont: visszareflektált jel Doppler-tolás + két utas
futásidő segítségével pontok elválasztása az azimut irányban
* echok kombinálása &rarr; nagyobb antenna apertúra "szintetizálása"
* tipikus képpont (pixel): 20-100 m szélesség 100 km-es pászta esetén

### InSAR - Hogyan működik

* 2 SAR kép &rarr; radar interferogram: magasság vagy deformáció infó
* SAR fókuszálás után: 2D fázis és amplitudó eloszlás
    * aplitudó: célpont reflektivitása
    * felszíni változások és a célpont távolságával arányos tag
* InSAR fáziskülönbségek felhasználása két kép között &rarr; interferogram
* pályadatokat ismerve felhaználható a felszíni topo. térképezésére
* különböző időpontban, de ugyanazon helyen készült két felvétel alapján &rarr;
mm nagyságrendű felszíni deform.

#### Topográfia térképezése

* DEM: "topográfia grid"
* InSAR topo. vizsgálatra: ált. 2 antenna egy űreszközön
* egyik sugároz, mindkettő veszi a visszavert jelet
* pl. SRTM (Shuttle Radar Topography Mission)
* ha nincs két antenna: tandem (ERS-1, ERS-2) vagy "visszatérésre" várni
* Fig 1;
    * h-t keressük minden pontra
    * &lambda; - radar adata
    * H mh. magasság és **B** mh. pályákból
    * &rho;<sub>1</sub> radar echo idejéből
    * &Phi; fáziskülönbség
* feltételezés: nincs változás a felszíni tulajdonságokban, felszín magasságban
atmoszf.-ban a két felvétel között
* ha a visszaverő objektum nem változik akkor: &Phi; = 4 &pi; &frasl; &lambda;
(&rho;<sub>1</sub> &minus; &rho;<sub>2</sub>)
* ifg.: egyik szép összeszorozva a másik kép komplex konjugáltjával
* megjelenítés: szürke színskála - amplitúdó, színes skála - fázis
* fringe-ek 2 &pi; radián fázisugrás
* mh. pálya infó + ifg. = h; felszíni mahasság
* LOS vektor változása a felszínen &rarr; nagy fázisgrad. az ifg.-on,
"flattening"-el korrigálni: mekkora lenne a &Phi; egy gömb alakú Földön, ezt
kivonjuk
* pontok közötti fringe-ek, modulo 2 &pi; - fázis kicsomagolás
* h<sub>a</sub> = 2 &pi; &sdot; &part; h &frasl; &part; &Phi; = (&lambda; sin
&Theta;) &frasl; 2 B &sdot; cos(&Theta; - &alpha;) - magasság
"bizonytalansága"

#### Felszíni deformáció mérése

* repeat-track interfero. - felszíni elmozdulás esetén plusz fáziskomponens
* ha a második kép ugyanabból az antenna pozícióból &rarr; csak deformációs
komponens
* ált. eset: topo. + deform. - &Phi; &approx; 4 &pi; &frasl; &lambda; ( &minus;
(**B** &sdot; **l**<sub>1</sub>) + (**D** &sdot; **l**<sub>1</sub>))
**l**<sub>1</sub> range irányú egységvektor; feltételezés: B és D sokkal
kisebb, mint a range távolság
* &delta;&rho; = **D** &sdot; **l**<sub>1</sub> elmozdulás nagysága
* &delta;&rho; = &lambda;/2 egy fringe; ERS - C: 28 mm
* 3D elmozdulás vektor nem határozható meg; ASC + DESC irány &rarr; 2 komponens
* topo fázis kivonásához DEM kell

#### Ifg. készítése

* 2 SAR képből, komplex számok: ampl. + fázis: kétutas terjedés
fáziskésleltetése
* fázis minden pixel esetében kb. random
* Fig 2. (ancillary - kiesgítő, kiegészítő) első lépés:
    * 2 SAR kép, teljes felbontás, komplex forma
    * keig. adatok: idő referencia, képek kiterjedése, antenna feltételezett
    iránya
    * komplex kép beszerzése vagy készítése nyers adatokól
* második lépés:
    * 2 kép keresztkorrelációja, eltolások és torzítások kiküszübölése &larr;
    geometria, a rdsz. limitációi
    * kis bázisvonal esetén: topo.  variációja csak kicsit modulál, range hatás
    elhaynagolható
    * mh. sebesség különbség miatt kis torzítás azimut irányban, ki kell
    küszöbölni
    * koregisztráció (korreláció segítségével) megtörtént &rarr; egyik kép
    újramintavételezése a másikra
    * torzítás nem egyenletes &rarr; térbeli interpoláció
* harmadik lépés:
    * első komplex * második komplex konj. &rarr; ampl. keresztkorreláció,
    fázis: topo. + deform.
    * jól automtizálható, eddig a lépésig
* negyedik lépés:
    * ifg.-ból geofizikailag értelmezhető mennyiségek, többféle technika,
    szakértelem kell hozzá
    * kicsomagolás kritikus lépés: bármely konzisztens megoldás (bármely
    irányban integrálva ugyanazt kapjuk) a topo. és deform. egy "változata"
    * más infó. hiányában: kis-felb. DEM, radar kép fényesség (brightness),
    korreláció (**kereszt?**) &rarr; nem nagyon lehet hibamentes kicsomagolás
    * repeat-pass esetben a kicsomagolás nagy kihívás
* deform. megkapásához a topo fázist ki kell vonni
* eredetileg: második ifg-al, melyben nincs deform. jel
* második út: DEM és mh. pálya segítségével &rarr; csak topo ifg. szimulálása
majd kivonása
* deform. fázis (kisebb változások) kicsomagolása sokszor kevésbé nehezebb mint
a topo.-é
* ifg. deform. relatív infó. - abszolút elmozdulás?
    * vizsgált területen kívüli fázis zéró (vulkán esetében jó pl.)
    * GPS segítségével (két lemez határnál)

### Limitációk

* fő tényezők: fázis zaj (több tényező), magassági "zaj" **?**, geom. torzulás
* Table 1. hatások összegezve

#### Fázis hibák

* atmo. változó fénytörése, visszavert EM jel térbeli dekorrelációja,
  feldolgozás
* ezen zajforrások &rarr; topo. hiba, deform. hiba
* bizonyos tényezők random változnak pixelről pixelre, mások térben és időben
  trendszerűen változnak lassan, megint mások az adat fajtájától függnek

**Interferometrikus korreláció:**

* random folyamatok - hasonlóság mérése korrelációval &gamma; = | &lang; 
c<sub>1</sub> c<sub>2</sub><sup>\*</sup> &rang; | &frasl; (&lang; 
c<sub>1</sub> c<sub>1</sub><sup>\*</sup> &rang; &lang; c<sub>2</sub> 
c<sub>2</sub><sup>*</sup> &rang;)<sup>1&frasl;2</sup>
* &lang; &rang; - sokaságra átlagolás, c<sub>i</sub> - i.-ik antenna pozíció 
(i.-ik felvétel?)
* &lang; &rang; ált. területre átlagolással számítják: &phi;&#770; = arg
&sum;<sub>i = 1, j = 1</sub><sup>i = N, j = M</sup> c<sub>1</sub> (i, j)
c<sub>2</sub> (i, j) &frasl; NM
* ez a módszer túlbecsüli a korrelációt olyan területeken, ahol kicsi a
korreláció és az átlagos pontsűrűség kicsi
* Zebker & Villasenor (1992): fázisvariancia és korreláció között az össze
függés: &sigma;<sub>&Phi;</sub><sup>2</sup> = (1 &frasl; 2NM) (1 - &gamma;
<sup>2</sup> &frasl; &gamma;<sup>2</sup>)
* mivel &gamma;&#770; néhol túlbecsül, a fázisvart is túlbecsüli
* fázisvar. kiszámításával &rightarrow; statisztikai pontosság

**Statisztikai hibák:**

* stat. fázis hiba &leftarrow; termális és kvantálási hibák plusz statisztikai
különbségek a két interferometrikus megfigyelés szóró geometriáiban
* termális zaj: antenna hőm.-e nem zéró és "meleg" objeltumokat érzékel,
visszatérő echoval dekorrelált
* ifg.-ok készítésénél félreregisztrálás &rarr; + random zaj, jól ismert mh.
pálya esetén ez a hiba elhanyagolható
* digitalizálás &rarr; kvantálás: termális zajhoz hasonló random komponens,
radarok ált. megfelelően tervezettek &rarr; alacsony szinten tartják ezt a
komponenst
* véges számábrázolás, elhanyagolható
* néhány termális zajkomponens: EM mező korrelációk: ugyanazon pont más szögből
nézve - pixelen belüli szórópontok másképp adódnak össze - bázisvonallal
növekvő bázisvonal dekorreláció
* ha a fázis változás 2&pi; vagy nagyobb (pl. bázisvonal dekorr. miatt) nem
lehet ifg.-ot csinálni
* vegetáció/extrém módon érdes felszínek &rarr; gyorsabb dekorr. bázisvonal
növekedésével
* 2 felvétel közötti időbeli változás (vegetáció növ., erőzió,...) is okozhat
dekorr.-t (Zebker & Villasenor 1992)
* időbeli bázisvonal választása alkalmazásfüggő.
    * ms-s óc.-i áramlatok
    * napok - gleccsefolyás
    * évek - kéregdeform. vizsgálat
* csupasz alapkőzettel borított (sivatag, vulkán) és városi területek esetén
akár több év is lehet az ifg. párok között
* hull.hossz is befolyásol: pl. L-sáv áthatol a felszíni növényzeten

**Szisztematikus hibák**:

* radar vevő láncban lassú fázis instabilitások (Rosen et al 2000),
hullámterjedési hatások (Goldstein 1995, Fujiwara et al 1998a)
* hull.terj. seb.-e: atmoszf. szerkezetétől függ, + fázis tag az atmoszf.
inhomogenitásából - kétantennás rdsz.-ek esetében ez a tag elhanyagolható
* nagy offszetet okozhat a toposzf.-a víztartalma
* 20%-os nedvességváltozás &rarr; 10cm deform. hiba, 100m-es topo hiba
(Goldstein 1995, Rosen et al 1996, Tarayre & Massonmet 1996, Zebker et al 1997)
* nagy atmoszférikus artifaktokkal rendelkező felvételek kihagyása
* csökkentés: nagymennyiségű ifg. átlagolása &rarr; korrelálatlan atmo.
késleltetés kiesik (Zebker et al 1997, Fujiwara et al 1998a, Sandwell & Price
1998)
* lehetséges: GPS és más atmo. szenzorok adataival &rarr; modell kivonása
(Delacourt et al 1998, Williams et al 1998)

## StaMPS

IFG = interferogram

## Goldstein filter
- in a patch we have: $I(x,y)$ phase values
- $Z(u,v)=\mathfrak{F}\{I(x,y)\}$, Fourier-transformed phase values
- response filter: $H(u,v) = \left| Z(u,v)\right|^{\alpha}$
	- useful $\alpha$ range: 0.2 - 1
	- $\alpha = 0$ no filtering, $\alpha = 1$ strong filtering
	- for IFGs with low correlation: high $\alpha$ and large patch size

## CLAP
- Combined Low Pass and Adaptive Filter
- $H(u,v) = \left| Z(u,v)\right|$, $Z$ smoothed intensity of 2D FFT
- $H(x,y) = \mathfrak{F}^{-1}\{H(x,y)\}$
- smoothing: 7&#10005;7 pixel, Gaussian-window
- $L(x,y)$: 5th order Butterworth-filter, default cutoff wavelength = 800 m
- $\overline{H}(x,y) = \text{median}(H(x,y))$
- filter:
$$
G(x,y) = L(x,y) + \beta \left( \frac{H(,xy)}{\overline{H}(x,y)} -1 \right)^{\alpha}
$$

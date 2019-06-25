# Bevezető

## Klasszikus távérzékelés

Azt a folyamatot nevezzük távérzékelésnek, amikor a vizsgálandó tárgy és a
vizsgáló eszköz között jelentős a távolság.  Vagy nem nagy a távolság de van
egy közeg közöttük.  
- Vagy nem tudunk közel menni
- Vagy nem látom csak távolról

Az információt rögzíteni kell, majd feldolgozni és alkalmazni.  Ma az egyik
legtöbbet használt felhasználási módja a térképészet.

- 1984 - LANDSAT-TM: Tematic Mapper
- TIROS: kezdettől fogva ingyenes volt
- NOAA &rarr; AVHRR
-  - műholdfedélzeti eszköz elforgatható
- NIMBUS-KOSMOS -- kis felbontás, nagy látószög
- LANDSAT: 5&deg;-es látószög, kb. 180 km-es sáv &rarr; 16-18 napos visszatérés
- NOAA: 55&deg;-es látószög, 2100 km-es sáv, torzított kép
- 1988: IRS - India
- GeoEye &rarr; Google Earth
- ENVISAT: rengeteg információ &larr; komplex műholdak, kutató műhold
- katonai kémműholdak

## Elektromágneses hullám

- "egysávos" pánkromatikus - az amit szemmel mi is látnánk
- mikrohullám - radar
- visszatérési idő &sim; (felszíni felbontás)<sup>&minus;1</sup>

## Műholdcsaládok

- ugyanaz a típus
- kissé eltolt pálya, azonos magasság
- akár egy időpontban a teljes Föld

## DMC

- nemzetközi program
- vegyen az adott ország egy holdat
- az adott ország adja át és cserébe az ország is kap a többi műhold adataiból
- 2-3 ilyen műholdcsalád van
- kombinálja a klasszikus nagyfelbontású műholdakat a -al
- itt nem az eszközt, hanem az egész műholdat forgatják
- többé-kevésbé napszinkron pályán
- kicsi, egyszerű mozgatás, a Föld mágneses terét használják fel
- 3 tengely stabilizált műholdak, bárhol is legyen a pályáján, mindig "lefele"
  néz

## Cubesat

- távérzékelési műholdaknál még nincs

## Távérzékelés: történet

### (Légi)fotó

- Léggömb: Gaspard-Félix Tournachon (Nadar), Párizs 1858, 80m magasból
- Repülőgép
- műhold

### Műholdak
- 1929 -- Robert Goddard kísérlete; barométer rakétára &rarr; felsőlégkör
- 1944 Ballisztikus rakéták -- V-2
- 1957 első mesterséges hold -- Szputnyik-1
- 1959 Explorer
- 1960 első jelentős műholdsorozat TIROS (első polgári műhold); első darabja
  &rarr; prototípus sorozat többi tagja azon alapult
- 1961 napszinkron pálya
- 1962 NIMBUS, KOZMOSZ
- 1964 geostacionárius pálya
- 1972 ERTS-1 (Earth Resources Technological Satellite) &rarr; Landsat-1
- 1978 TIROS-N (AVHRR), NOAA műholdsorozat első tagja, meteorológiai cél
  rájöttek: felszín vizsgálatára is jó
- lehetőség a Föld felszín és a légkör folyamatos monitorozására; addig csak
  *in-situ* mérések voltak

### Négyes "evolúció"

térben (felbontás), frekvenciában, időben, módban

#### Térben

- kisfelbontású adatok &sim;1km, pl. NOAA AVHRR
- közepes felbontású adatok &sim;100m, pl. Terra/Aqua MODIS
- nagyfelbontású adatok &sim;10m, pl. LANDSAT TM
- nagyon nagy felbontású adatok &sim;1m, pl. IKONOS
- kémholdak &sim;10cm

#### Frekvenciában

A.

- “egysávos” - pankromatikus
- többsávos - multispektrális szkenner: 2-10 sáv a látható/infravörös
  tartományban
- soksávos - hiperspektrális szkenner: 16-256 sáv a látható/infravörös
  tartományban

B.
- látható fény
- infravörös fény
- ibolyántúli fény
- röntgen
- mikrohullám

#### Időben

- magas pálya (geostacioner) - pl. Meteosat – kis és torzított térbeli, nagy
  időbeli felbontás
- alacsony pálya (&sim;800km) - széles letapogatási szög: kis (és torzított)
  térbeli, közepes időbeli felbontás
- alacsony pálya (&sim;800km) - kis letapogatási szög: nagy térbeli, kis
  időbeli felbontás
- nagyon alacsony pálya (&sim;100km) - nagy térbeli és időbeni felbontás –
  rövid élettartam
- műhold “flották” - pl. Disaster Monitoring Constellation (DMC) vagy RapidEye:
  sok hasonló műhold

#### Térben

- magas pálya (geostacioner) - pl. Meteosat – kis és torzított térbeli, nagy
  időbeni felbontás
- alacsony pálya (&sim;800km) - széles letapogatási szög: kis (és torzított)
  térbeli, közepes időbeli felbontás
- alacsony pálya (&sim;800km) - kis letapogatási szög: nagy térbeli, kis
  időbeni felbontás
- nagyon alacsony pálya - nagy térbeli és időbeni felbontás – rövid élettartam
- műhold “flották” – pl. Disaster Monitoring Constellation (DMC) sok hasonló
  műhold

#### Módban

- Passzív érzékelők: az eddigiek
    - passzív antenna: több antenna, több fázis, sugárzás irányának mesterséges
      változtatása
- Aktív rendszerek (radar - mikrohullámú; dm-cm):
    - RADAR, LIDAR, SONAR
    - SLAR: Side-Looking RADAR
    - radar (SAR, JSAR)
    - RADARSAT, ENVISAT, ERS-1 stb.
    - lidar - aktív optikai (ICESat, Calipso)
    - mikrohullám felbontás: dm-cm;
    - hullámintenzitás, energia, polarizáció adatokkal érdemes dolgozni

## Távérzékelés: alkalmazások
- Plank-fv., mérünk hőmérsékleti és visszavert sugárzást optimálisan
  megválasztott csatornákon
- mit mérünk? felszín + légkör &larr; több réteg
- elnyelés alacsonyabb hőmérsékletre "tolja" a Plank-görbét
- hiperspektrális: sok kicsi csatorna sűrűn &rarr; légkörről minél több infót
  szerezzünk
- CO<sub>2</sub> + H<sub>2</sub>O &larr; fő elnyelési sávok
- reflektancia: telajminőségtől függ - nedves/száraz; mindenképpen hullámhossz
  függő
- vétel: fő kiolvasó állomások poláris területeken (poláris műholdak tuti
  elhaladnak felette) &rarr; direct read out
- sok műhold folyamatosan is tud sugározni, amit utoljára mér, azt leküldi
  csomagba
- "sepregető" szkennelés (whiskbroom), leképző szenzor soronként letapogat
  &rarr; egy képbe beteszi
- szondázó &rarr; vertikális profil
- LANDSAT-8: OLI szenzor, láthatóban (VIS) finomabb, IR-ben durvább felbontás
- ASTER: nagyon finom felbontás IR-ben is
- MODIS: TERRA, AQUA műholdon, tervezett élettartam 6 év (sokkal hosszabb az
  átlagosnál)
- MERIS: MODIS-hoz hasonló, ENVISAT-on de elveszett a műholddal a kapcsolat
- Vegetation: AVHRR-hez hasonló, Spot-4,5
- Suomi-NPP: áthidaló műhold a NOAA és az új sorozat között, JPSS
- AVHRR kontinuitás meglegyen: MetOp-A,B és C kb. 2018
- GOES: Imager
- NVIRI: Meteosat: 1-7 első generáció, MSG 1-4 Seviri 1-3 km
- pánkromatikus csatorna szélesebb tartomány lefed &rarr; finomabb felbontás
  &rarr; pánkromatikus élesítés
- SEM: elektromos töltöttség szenzor, SAR: search-and-rescue
- minél több bit annál nagyobb a radiometric accuracy
- AVHRR egyszerre 5 csatorna, de összesen 6 csatorna - egy csatoran osztott
- spektrális relatív válaszfv.: egy csatornán belül adott hullámhosszra
  mennyire érzékeny
- vertikális szondázás
- ATOVS műszercsoport. AMSU-A és B és a HIRS
- TERRA, AQUA: AIRS, MODIS, ASTER, szenzorok is
- műhold konstellációk &rarr; szenzorok több műholdra is elhelyezve
- Fengyun - kínai műhold
- MODIS - spec. szkennelési geometria, bowtie torzítás: egyszerre 10 sort mér
  &rarr; szélén kiszélesedik, 5 perces granulákban érkeznek az adatok
- MODIS rácson Magyarország: h19v04
- collections: különböző modellekkel lefuttatott feldolgozások
- ASTER fizetni kell az adatokért
- LANDSAT: napi változások monitorozására nem jó
- SLC-off LANDSAT-7!!!
- OLI 9-es csatornája felhőzet kiszűrése

1. Térképészeti alkalmazások - DEM (Ikonos sztereo)
2. Növénytakaró:
    - felszínborítottság, földhasználat - LANDSAT TM
    - termésbecslés, -előrejelzés
3. Természeti katasztrófák: árvíz, belvíz, tűz, stb.
    - 2006. április, MODIS
    - 2003. március DMC-UK
4. Meteorológia
5. Környezetvédelem
    - Légszennyezés: optikai mélység (LANDSAT-TM)
    - Tengeri olajszennyezés: LANDSAT 7
    - Talajszennyezés: radarkép (légi)+Ikonos

6. Régészet
    - Csőszhalom, M3
    - Angkor Wat, Kambodzsa

## Távérzékelés: túl a klasszikus távérzékelésen

- Földrengés Gujarat-ban (India), 2001. január 26. Hő anomália térkép, MODIS TIR
- Gravitációs anomália térkép, CHAMP műhold
- Tenger felszín – radar magasságmérés
- Földi villámgyakoriság-eloszlás OTD/LIS műhold, kisülés/km<sup>2</sup>
- Teljes mágneses tér, OERSTED műhold
- Szférák a Föld körül -- űr-időjárás
- Sugárzási övek:
    - Hullám-részecske kölcsönhatás - DEMETER műhold
    - E = 200keV elektron, DEMETER műhold
- Plazmaszféra:
    - IMAGE műhold Extreme Ultraviolet Imager &lambda;=30.4nm 2000.  május 24.,
      07:34UTC

## Távérzékelés: "inverz" távérzékelés

- Plazmaszféra:
    - Whistlerek: elektronsűrűség, erővonal (L-érték)
    - FLR: plazmasűrűség, erővonal (L-érték)
- Villámdetektálás, WWLLN, GLD-360

# Műholdas adatok előfeldolgozása

Tipikus (és súlyos) hiba: a műholdas adatok előfeldolgozás nélküli vagy
részlegesen feldolgozott állapotban alkalmazzák.

1. Kalibráció
2. Radiometriai korrekció
3. Geometriai korrekció
4. Légköri korrekció
5. Georektifikáció

- Légköri ablakokban mérünk
- OLI 9-es csatornája &rarr; légkör vízgőztartalma, Solar-View kalibrálás
- 8 bit = 1 bájt, DE NOAA AVHRR - 10 bit

## Kép eltárolásának módszere

- BIL: band interlined by line; sorok egymás után
    - ha egy adott sávban csak bizonyos csatornákra van szükségem, be kell
      olvasnom az egész fájlt
- BSQ: Band Sequential, adatok csatornánként eltárolva, de az egész területre
- BIP: Band by Pixel, egy pixelenként eltárolva, egy pixelben az összes
  csatorna benne van
- legtöbb szoftver engedi a felhasználó "beleszólását" &larr; saját scriptek

## Kalibráció

- lineáris közelítés
- preflight/fellövés alatt
- belső kalibráció belső standard fénysugárzóval
- fontos és értékes: időben hosszú adatsorok, melyeket változatlan eszközökkel
  mérnek
- külső kalibráció, földi "változatlan" terület, sivatagi terület pl. jó
    - nem mindig lehet látni
    - nem szokott felhő lenni

Cél: a mért beütés szám (Digital Count, DC) konvertálása fizikai mennyiséggé:

DC = G &sdot; L+B
- L a radiancia [W/(m<sup>2</sup> sr &mu;m)], ezt szeretnénk tudni
- G az erősítés és
- B az ofszet

Honnan ismerhetjük G-t és B-t?
- fellövés előtti kalibráció - minden műhold &rArr; öregedés
- repülés közbeni kalibráció belső - pl. LANDSAT TM, EO-1 ALI
- repülés közbeni külső kalibráció (Nap, Hold) - pl. LANDSAT 8 OLI, EO-1 ALI
- külső kalibráció földi “változatlan” területek felhasználásával (pl. líbiai
  sivatag) &rArr; légkör problémája -  pl. NOAA AVHRR

## Radiometriai korrekció

Hibaforrások:
- az érzékelősorok eltérő karakterisztikája, öregedése &rArr; csíkosság
- nem lehet két egyforma detektort/félvezetőt csinálni

## Geometriai korrekció

Hibaforrások:
- a pályamagasság eltérése a névlegestől &rArr; 1-2km &rarr; 1 pixelhez rendelt
  terület változni fog
- a műhold/műszer orientációs hibája, csak akkor korrigálható, ha pontosan
  ismert az orientációs történet &sim;10km(!)
    - Föld mágneses terének használata, giroszkópok, Nap/csillagszenzorok
    - csak a műholdat felbocsájtó társaság tudja korrigálni
- felvevő rendszerek geometriai/elektromechanikai torzításai &rarr; hőtágulás -
  Nap rásüt/nem süt, ne nagyon van rá jó korrekciós módszer
- a képsor letapogatása közben a műhold mozgása &rArr; &sim;1 pixel
- műhold mozgásának (sebességének) szabálytalanságai a pálya mentén &rArr;
  &sim;1.5km
- a Föld görbülete okozta torzulások &rArr; &sim;0.1km
- a Föld forgásából adódó sodródások szkennelési irányban nyugat felé &rarr;
  &sim;10km; Föld kifordul a műhold leképezési síkja alól
- a domborzat okozta perspektív torzulások
- vetületi torzítások - lásd később.

## Légköri korrekció

- kb. 800 km-es stabil pálya, de van légkör fékeződés
- sűrű légkör a Föld és a műhold között
    - Rayleigh(minden irányban - molekulák Brown- mozgása miatt) és Mie
      szórás(előre és hátra)
- A felület homogén
- A légkör optikai mélysége kicsi
- Nincs domborzat
- Nézzük csak a légkörben egyszer megtörő fény nyalábok eseteit
- mély tiszta víz kb. fekete test

L<sub>TOA</sub> = L<sub>é</sub>(&Omega;<sub>0</sub>, &Omega;<sub>s</sub>) \+ (
T(&Omega;<sub>0</sub>) T(&Omega;<sub>s</sub>) E<sub>0</sub>
cos(&Theta;<sub>0</sub>) &rho; ) &frasl; ( &pi; [1 - &rho; S] )

- TOA = Top of the Atmosphere
- S: légkör felfelé menő sugárzásra vonatkozó albedója
- &rho;: reflektancia, &rho; &isin; [0, 1], &rho; = &rho;(frekvencia, érdesség,
  struktúra,...) &rarr; BONYOLULT, %-ban is ki szokták fejezni
- ehelyett: &rho; = *const* &ne; &rho;(&Omega;<sub>0</sub>,
  &Omega;<sub>s</sub>); Lamberti felület, akkor jó, ha egyenletesen nem
  tükröződő felület érdes; pl. homok aszfalt, távérzékelési gyakorlatban ezt
  használják
- BRDF: Bidirectional Reflectance Distribution Factor/Function
- a &Omega;<sub>0</sub> és &Omega;<sub>s</sub> szögeket ki tudjuk számolni

Transzmissziós függvény vagy transzmittancia:  T(&Omega;) = e<sup>&minus;
&delta; &frasl; cos(&Omega;)</sup>, &delta;: optikai mélység, jól le lehet írni

Egyszerűbben:  L<sub>mi</sub> = (1 / &pi;) &rho;<sub>i</sub> E<sub>S,i</sub>
(&delta;<sub>i</sub>, &Theta;<sub>0</sub>) e<sup>&minus; &delta;<sub>i</sub>
&frasl; cos(&Omega;)</sup> \+ L<sub>P,i</sub>

Hol van a légkör ebben a formulában?
- E<sub>S,i</sub> - felszíni globális besugárzás
- &delta;<sub>i</sub> -optikai mélység
- L<sub>P,i</sub> - légkörfénylés

Miből állnak a szórócentrumok?
- N<sub>2</sub>, O<sub>2</sub>, H<sub>2</sub> (CO<sub>2</sub>, CH<sub>4</sub>,
  O<sub>3</sub>)
- + korom, por, Nitrogén-Oxidok &larr; aeroszolok + vízgőz
- fontos tényező az aeroszolok mennyisége
- tengerparton só elpárolog &rarr; aeroszol

Légköri korrekció számításához kell egy csomó információ
- légkörfénylés: tiszta sötét vizek feletti fénylés kihasználása
- DOS: dark object subtraction
- baj, ha nincs mély vízfelület és az időjárás 100 km-el arrébb más
- légkör modellezése először katonai fejlesztés
- 4-6 féle standard légkör: sivatag, óceán,...
- kétszer "ránézek" a területre &rarr; ki lehet ejteni a légkört

"Valódi" légköri korrekciós eljárások:
- mért transzmittancia/optikai mélység – újabb műholdak, pl. EO-1: a pálya
  mentén előre/hátra nézve kétszer tapogatja le ugyanazt a területet
- Légkörmodellek használata a sugárzásátviteli egyenletben – ATCOR, ACABA
- ACABA: légkör állapotából &rarr; paraméterek (Low Resolution Translation
  Function)
- ATCOR: be lehet tenni a paramétereket
- LOWTRAN, MODTRAN, 5S, 6S (Second Simulation of a Satellite Signal in the
  Solar Spectrum) – standard légkörmodellek: nyári/téli, közepes
  szélesség/trópusi, város/vidék, tenger/szárazföld, stb. &rArr; mindegyikhez
  kell valamilyen bemenő információ a légkör állapotáról, vízgőz, aeroszol
  tartalom, ózon, stb. - vagy vízszintes látótávolság
- hiperspektrális adatok – mérés a megfelelő csatornán

## Georektifikáció

- ha egynél több képünk van
- műhold koordinátarendszer folyamatosan változik &rarr; nem jó
- jól azonosítható pontok keresése, egyenletesen szétszórva

Ha a képi és a célkoordinátarendszer el van forgatva egymáshoz képest
&rarr; átlapolódó pixelek, melyik célpixelhez rendelem a képi pixelt?
- nearest neighbour, legközelebbi szomszéd
- 4 pixel súlyozott átlaga &rarr; térképi felbontásban pontosabb, de az
  eredeti pixelértéket elvesznek

A képi és a vetületi koordináták közötti transzformáció
- polinomiális átalakító függvények. Az átalakító függvények alakja:

u = F(x, y) = &sum;<sub>i=0</sub><sup>n</sup> &sum;<sub>j=0</sub><sup>i-n</sup>
a<sub>ij</sub> x<sup>i</sup> y<sup>j</sup>  
v = G(x, y) = &sum;<sub>i=0</sub><sup>n</sup> &sum;<sub>j=0</sub><sup>i-n</sup> b<sub>ij</sub> x<sup>i</sup> y<sup>j</sup>

ahol:
- x,y : a vetületi rendszer koordinátái
- u,v : a digitális kép képi koordinátái
- a<sub>ij</sub>, b<sub>ij</sub>  : az átalakító függvények együtthatói
- n : a polinomok fokszáma.

A függvények együtthatóinak meghatározása a digitális képen földi
illesztőpontok azonosításából és vetületi koordinátáinak megadásából indul ki.
U és V jelölje a pontok képi u, illetve v koordinátáinak vektorát, az M mátrix
pedig az egyes átalakító függvények x<sup>i</sup> y <sup>j</sup> tagjait. Az
a<sub>ij</sub> és b<sub>ij</sub> együtthatók A, illetve B vektorának
meghatározása a következő mátrixegyenletekkel történik:

A = (M<sup>T</sup> M)<sup>-1</sup> (M<sup>T</sup> U)  B
= (M<sup>T</sup> M)<sup>-1</sup> (M<sup>T</sup> V)

A, B, U, V - p elemszámú vektorok, M - t soros és p oszlopos mátrix, ahol
- p az illesztőpontok száma
- t: a polinomok tagjainak száma, t = (n+1)(n+2)/2


Az eljáráshoz egy újra-mintavételezési eljárásra (resampling) is szükség van,
mivel a kiszámolt képkoordináták leggyakrabban nem pixel-koordináták. Az
általánosan alkalmazott módszerek a következők:
- a leképezett pixel-koordináta (nem egész szám) amelyik pixelbe esik, annak az
  intenzitás-értékeit választjuk (nearest neighbour method)
- a környező négy pixel intenzitás-értékeit a távolság függvényében bilineáris
  interpolációval számítjuk (bilinear interpolation)
- kétváltozós, harmadfokú polinomot illesztünk a pont környezetére, és ezt,
  mint súlyfüggvényt használva kapjuk meg az eredménypixel intenzitását (cubic
  convolution).
- ortorektifikáció - képhelyesbítés - során a felvétel perspektivikus
  torzításait korrigáljuk.

A georektifikáció **minden** műholdas adatra alkalmazandó!

Ha rendelkezésünkre áll DEM a perspektivikus torzítások korrigálhatóak.

## Műholdas adatok feldolgozási szintjei

Level 0: nyers adatok  Level 1a: radiometriai és geometria korrekció  Level 1b:
kalibrált és georektifikált adatok  Level 2, 3,...: magasabb feldolgozottságú
termékek, közvetlen felhasználásra

# Műholdas adatok feldolgozása

**Cél**: az adatok átalakítása olyan formába, amely lehetővé teszi, hogy
felhasználjuk interaktív (emberi) vagy numerikus alkalmazásokban.

**Módszerek:**

**I.**
- kontraszt fokozása/csökkentése
- zajelnyomás
- élek kiemelése &rArr; lineáris és nemlineáris szűrés

**II.**
- sávkombinációk (indexek)
- osztályozás

## 2D Fourier transzformáció

f(m,n) diszkrét térbeli változó Fourier transzformáltja:

F(&omega;<sub>1</sub>, &omega;<sub>2</sub>) = &sum;<sub>m</sub>
&sum;<sub>n</sub> f(m,n) e<sup>&minus;j&omega;<sub>1</sub>m</sup>
e<sup>&minus;j&omega;<sub>2</sub>n</sup>

periodikus 2&pi;-vel, ezért csak a &minus;&pi; &le; &omega;<sub>1</sub>,
&omega;<sub>2</sub> &le; &pi; szakaszt érdemes használni

f(m, n) = (1 &frasl; 4 &pi;<sup>2</sup>) &int;<sup>&pi;</sup>
<sub>&omega;<sub>1</sub> = &minus; &pi;</sub> &int;<sup>&pi;</sup>
<sub>&omega;<sub>2</sub> = &minus; &pi;</sub> F(&omega;<sub>1</sub>,
&omega;<sub>2</sub>) e<sup>&minus;j&omega;<sub>1</sub>m</sup>
e<sup>&minus;j&omega;<sub>2</sub>n</sup> d&omega;<sub>1</sub>
d&omega;<sub>2</sub>

## 2D konvolúció

A konvolúció a jelfeldolgozás egyik legelemibb művelete. Ez a lineáris művelet
két függvényből állít elő egy harmadikat. Legegyszerűbben úgy szemléltethető a
konvolúció, mint egy adatsorozat (egyik függvényből vett minta) súlyozott mozgó
átlagának számítása egy adott súlyfüggvény (a másik függvényből vett minta)
alapján.  A g(x,y) és f(x,y) folytonos függvényeknek az (a,b; c,d) intervallum
feletti konvolúcióját az alábbi kifejezés definiálja kétdimmenziós esetben:

f(x, y) * g(x, y) = &int;<sup>b</sup><sub>&xi;=a</sub>
&int;<sup>d</sup><sub>&eta;=c</sub> f(x &minus; &xi;, y &minus; &eta;) &sdot;
g(&xi;, &eta;) d&xi; d&eta;

A gyakorlatban a konvolúciót a képmátrix szűrésére is szokták használni.
Legyen a szűrő mátrix dimenziója 2N+1, akkor a szűrt érték pixel a

<span style="text-decoration:overline">SZ</span><sub>x,y</sub> =
&sum;<sub>&xi;</sub> &sum;<sub>&eta;</sub> SZ<sub>x &minus; &xi;, y &minus;
&eta;</sub> &sdot; r <sub>N + 1 + &xi;, N + 1 + &eta;</sub>  (x = 1,2,...,n),
(y = 1,2,...,n)

Szűrés frekvenciatérben, mert  f(x, y) * g(x, y) &hArr; F(u, v) G(u, v)

## Gradiens operátor

A gradiensvektor (érintővektor) a kép első deriváltjaiból képezett:

G[f(x, y)] = (G<sub>x</sub>, G<sub>y</sub>)<sup>T</sup>

vektor, ahol G<sub>x</sub> = &part;f &frasl; &part;x, illetve G<sub>y</sub> =
&part;f &frasl; &part;y a gradiensvektor két komponense.  

A gradiensvektor hosszát (a gradiens nagyságát), illetve irányát euklideszi
módon definiáljuk, azaz

&#9474;G[f(x, y)]&#9474; = (G<sub>x</sub><sup>2</sup> +
G<sub>y</sub><sup>2</sup>) <sup>1 &frasl; 2</sup> illetve &ang;G =
tan<sup>&minus;1</sup> (G<sub>y</sub> &frasl; G<sub>x</sub>)

a gradiens nagysága, illetve szöge a &Theta; irányba eső változás gyorsaságát
mutatja

&Delta;f = G<sub>x</sub> cos&Theta; + G<sub>y</sub> sin&Theta;

Sobel operátor (a) ("klasszikus" gradiens képzés):

&#9474;G[f(x, y)]&#9474; = { [ f(x, y) &minus; f(x + 1, y) ]<sup>2</sup> + [
f(x, y) &minus; f(x, y + 1) ]<sup>2</sup> } <sup>1 &frasl; 2</sup>

Roberts operátor (b) (ha a változás nem x vagy y irányba esik):

&#9474;G[f(x, y)]&#9474; = { [ f(x, y) &minus; f(x + 1, y + 1) ]<sup>2</sup> +
[ f(x + 1, y) &minus; f(x, y + 1) ]<sup>2</sup> } <sup>1 &frasl; 2</sup>

## Laplace-Gauss operátor

Egy háromváltozós skalár függvényre alkalmazzuk a Laplace-operátort:

&nabla;<sup>2</sup>&Phi; = (&part;<sup>2</sup> &Phi; &frasl; &part;
x<sup>2</sup> \+ &part;<sup>2</sup> &Phi; &frasl; &part; y<sup>2</sup> \+
&part;<sup>2</sup> &Phi; &frasl; &part; z<sup>2</sup>)

Ez egy skalár, mely azt mutatja, hogy a függvény változása a vizsgált pont
környezetében növekszik-e vagy csökken. Ahol a függvény növekedésből
csökkenésbe vagy csökkenésből növekedésbe megy át, ott a fenti kifejezés
előjelet vált.

2D normális eloszlás vagy Gauss függvény - simítás:

f(x, y) = f(r) = (1 &frasl; 2 &pi; &sigma;<sup>2</sup>) &sdot; e <sup> - [
(x<sup>2</sup> + y<sup>2</sup>) &frasl; (2 &sigma;<sup>2</sup>) ]</sup> , ahol
r<sup>2</sup> = x<sup>2</sup> + y<sup>2</sup>

Deriváljuk a Gauss szűrő kifejezését x majd y szerint, az első deriváltak az
alábbiak lesznek:

f<sub>x</sub><sup>'</sup> = &minus;(x &frasl; 2 &pi; &sigma;<sup>4</sup>)
&sdot; e <sup>&minus;[ (x<sup>2</sup> + y<sup>2</sup>) &frasl; (2
&sigma;<sup>2</sup>) ]</sup>

f<sub>y</sub><sup>'</sup> = &minus;(y &frasl; 2 &pi; &sigma;<sup>4</sup>)
&sdot; e <sup>&minus;[ (x<sup>2</sup> + y<sup>2</sup>) &frasl; (2
&sigma;<sup>2</sup>) ]</sup>

Az x és y szerinti második deriváltak pedig a következő alakot veszik fel:

f<sub>x</sub><sup>''</sup> = &minus;( [x<sup>2</sup> &minus;
&sigma;<sup>2</sup>] &frasl; [2 &pi; &sigma;<sup>6</sup>] ) &sdot; e
<sup>&minus;[ (x<sup>2</sup> + y<sup>2</sup>) &frasl; (2 &sigma;<sup>2</sup>)
]</sup>

f<sub>y</sub><sup>''</sup> = &minus;( [y<sup>2</sup> &minus;
&sigma;<sup>2</sup>] &frasl; [2 &pi; &sigma;<sup>6</sup>] ) &sdot; e
<sup>&minus;[ (x<sup>2</sup> + y<sup>2</sup>) &frasl; (2 &sigma;<sup>2</sup>)
]</sup>

A Laplace operátort a két második derivált összegeként kapjuk azaz

**LoG** = &minus;( [ x<sup>2</sup> + y<sup>2</sup> &minus;
2&sigma;<sup>2</sup>] &frasl; [2 &pi; &sigma;<sup>6</sup>] ) &sdot;
e<sup>&minus;[ (x<sup>2</sup> + y<sup>2</sup>) &frasl; (2 &sigma;<sup>2</sup>)
]</sup>

Érzékeny arra, ami kettőt "röccen".

## Képelem keresése

Képkorreláció = konvolúció a 180 fokkal elfordított szűrővel = a 2D FFT képek
szorzása + 2D IFFT
- minták keresése legegyszerűbben korrelációval
- küszöbszint: efeletti korreláció &rarr; megtaláltuk a mintát a képben
- jelfeldolgozásban használatos módszer

## Élkiemelés, éldetektálás

- távérzékelt képeknél a határok fontosak

A gradiensoperátor eredménye; (a) eredeti kép, (b) Sobel gradiens, (c) Roberts
gradiens.

A LoG egy simítás+élkiemelés - néhol kettős élet ad.

A LoG operátor hatása; (a) eredeti kép, (b) 5&times;5-ös maszk esetén, (c)
13&times;13-as maszk esetén. &rarr; mekkora legyen a mátrix, amivel
korreláltatom a képet? (futásidő vs. felbontás)  
Kompromisszum kell: mi az, amit el akarok érni? milyen eszközeim vannak?  
pl. túlságosan érzékeny operátor olyat is kiemel, amire nem vagyok kiváncsi

<!-- kép -->

Éldetektálás 3 × 3 méretű maszkokkal; (a) eredeti kép, (b) vízszintes élek, (c)
függőleges élek, (d) a vízszintes és függőleges élképek átlaga

<!-- kép -->

Canny éldetektáló eljárás - kettős küszöb: felső és alsó

<!-- kép -->

## Hisztogram transzformáció

- Hisztogram kiegyenlítés - lineáris hisztogram
- szűk tartományban van adat &rarr; széthúzzuk a teljes tartományra, ez a
  hisztogram kiegyenlítés
- képfeldolgozásban ezt bizonyos csatornákra alkalmazva &rarr; kontrasztosít

<!-- kép -->

Multispektrális kép hisztogram-kiegyenlítése; (a) eredeti kép, (b) kiegyenlítés
komponensenkénti transzformációs függvényekkel, (c) kiegyenlítés a
transzformációs függvények átlagolásával

<!-- kép -->

## Zajelnyomás, simítás

Ugyanazt a műveletet lehet és célszerű sokszor megismételni

**Medián** szűrés (nemlineáris)

- A maszkválaszt nem a képtartomány és a maszkelemek konvolúciós szorzataként
  kapjuk.
- 3&times;3-as medián szűrésnél a vizsgált képtartomány pontjainak intenzitását
  (&times;1, (&times;2, ..., (&times;9 értékeket) növekvő sorba rendezzük, majd
  az így kapott sorozat középső elemét intenzitásértékként a centrális
  képponthoz rendeljük.
- 3&times;3: eltűnt a maszat, de életlenebb is lett &rarr; nagyobb mátrix és
  kiegészítő küszöb; pl. légköri maszat szűrése
- Alapötlete, hogy a kiugró intenzitásértékek (zajok) a sorba rendezéskor a
  sorozat széleire esnek.
- Előnye, hogy nem jelennek meg új intenzitásértékek ellentétben a környezeti
  átlagolással

<!-- kép -->

Medián szűrés hatása; (a) eredeti (15%-os fehér zajjal terhelt) kép, (b) a
medián szűrés eredménye 3&times;3-as maszk esetén, (c) a szűrés eredménye 10
iterációs lépés után, (d) 5&times;5-ös medián szűrés eredménye kiegészítő
küszöbölést használva

**Aluláteresztő**  szűrés
- A frekvenciatartomány magas frekvenciás részeit gyengítve (vagy akár teljesen
  kiszűrve) a képen elmosó hatást érhetünk el.
- Ideális aluláteresztő szűrőfüggvény (elés ugrás zajt tud behozni):

<!-- kép -->

ahol K küszöb (vágási frekvencia).

- Butterworth aluláteresztő szűrő:

<!-- kép -->

ahol K a vágási frekvencia, t pedig az átmenet sebességét szabályozó pozitív
paraméter.

**Aluláteresztő szűrés**

Az ideális aluláteresztő szűrő hatása; (a) eredeti kép, (b) szűrt kép K = 25
esetben, (c) szűrt kép K = 60 esetben

<!-- kép -->

A Butterworth aluláteresztő szűrő hatása; (a) eredeti kép, (b) szűrt kép t = 2
és K = 25 esetben, (c) szűrt kép t = 2 és K = 60 esetben

<!-- kép -->

Mi értelme az aluláteresztő szűrésnek? &rarr; homogénebb képeket/részeket
könnyebb besorolni.

**Felülteresztő szűrés**

- A nagy intenzitásátmenetek (zajok, élek) a kép Fourier transzformáltjának
  magasfrekvenciás összetevőiben jelennek meg.
- Az alacsony frekvenciás összetevőket szűrjük ki (frekvenciatartománybeli
  képélesítés).
- Ideális felülátersztő szűrőfüggvény

<!-- kép -->

ahol K megfelelő pozitív küszöb

- Butterworth felüláteresztő szűrő:

<!-- kép -->

ahol K a vágási küszöb, t pedig az átmenet paraméter sebességét szabályozó
pozitív paraméter.

**Felüláteresztő szűrés**

Az ideális felüláteresztő szűrő hatása; (a) eredeti kép, (b) szűrt kép K = 20
esetben, (c) szűrt kép K = 40 esetben

<!-- kép -->

A Butterworth felüláteresztő szűrő hatása; (a) eredeti kép, (b) szűrt kép t = 2
és K = 50 esetben, (c) szűrt kép t = 2 és K = 80 esetben

<!-- kép -->

Feldolgozási lépések nem feltétlenül a vizuális interpretációt segítik.

# Vegetációs Indexek

<!-- képek! -->

## Mit lát a műhold?

- csupasz talaj, VIS/NIR, kb. lineárisan nő a reflektanciája. ERŐSEN függ
  a nedvességtartalomtól
- hamis színes megjelenítés &rarr; bizonyos dolgok kiemelése

## Ortogonális indexek

**Tasseled cap** = bojtos sapka transzformáció

ATC<sub>i</sub>=&sum;<sup>n</sup><sub>j=1</sub> O<sub>ij</sub>
&rho;<sub>a,j</sub>

&rho;<sub>a,j</sub> = &pi; L<sub>mj</sub> &frasl; E<sub>00j</sub>
cos&Theta;<sub>0</sub>

**Brightness** &rarr; defined in the direction of soil reflectance variation.
Obtained from a weighted sum of all bands. i.e. urbanized and bare soil areas
are evident in this image. Talaj nedvességtartalma, növényzet és a talaj elkülönül

**Greenness** &rarr; defined in the direction of vegetation reflectance
variation.  Obtained from the contrast of the visible bands (high absorption)
with the infrared bands (high reflectance). i.e. the greater the biomass, the
brighter the pixel value in this image.

**Wetness** &rarr; information concerning the moisture status of the
environment (soil & plant moisture). Obtained from the contrast of the sum of
visible and near-infrared with the sum of longer- infrared bands. i.e. water
bodies are very bright – greater the moisture content = brighter response.

1. Talajvonal: talajvonal kiválaszt, v. talaj ellipszoid pontok kiválasztása
2. Növénypontok: talajvonaltól messzi pontok keresése, pl. növényzet
3. Gram-Schmidt ortogonalizálás: pontokra koordinátarendszert illeszteni
4. ...

TC 2. v. 3. csatorna kell

## Nemlineáris indexek

Ratio Vegetation Index  
RVI = (NIR &frasl; RED)

Noramlized Differentail Vegetation Index  
NDVI = (NIR - RED) &frasl; (NIR + RED)  
magas NDVI &rarr; vegetáció, de milyen? búza?, kukorica?

AVHRR és MODIS adatokból számolhatóak

# Tematikus osztályozás

**Elnevezések:**
- klasszifikáció (classification)
- térképezés (thematic mapping)
- klaszterezés (clustering)

Lényege: felszín/kép &rarr; csoportosítás bizonyos szempontok alapján  
növényzet felületén/környékén &rarr; más hőmérséklet, páratartalom FONTOS  
szikes/normális talaj megkülönböztetése fontos mezőgazdasági szempontból

## Az eljárások csoportosítása
- Ellenőrzött (supervised) felügyelt

- Nem-ellenőrzött (unsupervised)
    - nem felügyelt
    - automatikus
    - klaszterezés (clustering)

## Ellenőrzött osztályozás

Kérdés: egy kép pixeljei hogyan sorolhatók tematikus osztályokba? Másként: az
adott pixel mit ábrázol?
- valamilyen infó beszerzése a területről
- "betanítás" - táblák megadása &larr; búza, vízfelület, erdő, ...; majd
  teszt területen megnézni jó-e az algoritmus
- tanuló területnek reprezentatívnak kell lennnie térben és növényzetben
- egész vizsgált területet lefedje kb. a tanulóterület
- egy-egy pixel általában nem reprezentatív! vonal se! &rarr; célszerű
  teljes táblákat kiválasztani

Pl. őszi és tavaszi búza megkülönböztetése, ha sikerül oké, ha nem, össze
kell vonni a két osztályt &rarr; a búza
- osztályozást nem csak egy időpontban készült kép alapján csinálni
- időbeliség &rarr; őszi és tavaszi búza
- több időpontban felvétel, tudni kell mikor vetették le a terményt
- szerencse: rét, víz, legelő,... &rarr; különválik az "intenzitástérben"

Klasszifikáció n dimenziós térben zajlik
- bemenő infó
    - &rho;<sub>i,t</sub> reflektancia, i. sávban és a t. időpontban
    - GN<sub>i,t</sub>, BR<sub>i,t</sub>, HN<sub>i,t</sub> /
      &delta;<sub>i,t</sub> &larr; indexek

### Tanuló területek

- Ellenőrző adat = terepről gyűjtött információ (ground truth information)
    - 2 &frasl; 3 rész: „tanításra” (paraméterezésre)
    - 1 &frasl; 3 rész: tesztelésre

- Fajtái:
    - pontszerű (elszórt pixelek)
    - vonalszerű (lineáris elemek)
    - felületszerű (poligonok)

- Megoszlás:
    - egy tematikus osztály = egy tanuló terület
    - egy tematikus osztály = több tanuló terület

### Néhány ellenőrzött osztályozó

- Legközelebbi középpont módszer (minimum distance): pixel, mely osztály
  központjához van a legközelebb, baj ha átfednek v. ugyanakkora a távolság
- Legközelebbi elem osztályozás
- Hipertégla vagy Box-módszer (paralelepipedon): n dimenziós téglalap,
  gyorsabb, baj átfedésnel
- Legnagyobb valószínűség módszer (maximum likelihood)
- Hibrid módszerek
- Neurális hálózatok

### Legközelebbi középpont

Osztályjellemzés: átlagvektor

Döntésfüggvény:

d<sub>k</sub> = { &sum;<sup>n</sup><sub>i=1</sub> (x<sub>i</sub> -
a<sub>ki</sub>)<sup>2</sup> }<sup>1 &frasl; 2</sup>

d<sub>k</sub> = arg min(d<sub>k</sub>)

- Előnyök:
    - egyszerű osztályleírás
    - gyors számítás
- Hátrányok:
    - nehézségek azonos távolságok esetén
    - átfedő osztályok kezelhetetlensége

### Box-módszer

Osztályjellemzés: minimum és maximum vektor

Döntésfüggvény:

min<sub>i</sub> &le; x<sub>i</sub> &le; max<sub>i</sub> &larr; i = 1..n

- Előnyök:
    - pontosabb osztályleírás
    - gyors számítás

- Hátrányok:
    - átfedő részek
    - kívül eső részek

### Legnagyobb valószínűség

Osztályjellemzés: átlagvektor, kovariancia mátrix  
- nincs éles határ
- aránylag jó
- legbonyolultabb
- baj, ha egy pixelen belül egyenlő a valószínűség &rarr; átfedés, ennek
  az esélye csekély

p<sub>k</sub> = {(2&pi;)<sup>n &frasl; 2</sup> &sdot;
||C<sub>k</sub>||}<sup>&minus;1</sup> &sdot; exp {&minus; 0.5
(x&minus;a<sub>k</sub>)<sup>T</sup> &sdot;
C<sup>&minus;1</sup><sub>k</sub> &sdot; (x&minus;a<sub>k</sub>)}

||C<sub>k</sub>|| &ne; 0

c = arg max(p<sub>k</sub>)

C<sub>k</sub>: kovariancia mátrix

- Előnyök:
    - (gyakran) pontos osztályleírás
    - jó paraméterezhetőség
- Hátrányok:
    - bonyolult számítási eljárás
    - lassú számítás

### Változatok ML-módszerre

logaritmusos formula:

p<sub>k</sub> = &minus; (n &frasl; 2) &sdot; ln(2&pi;) &minus;
ln(||C<sub>k</sub>||) &minus; 0.5 &sdot;
(x&minus; a <sub>k</sub>)<sup>T</sup> &sdot;
C<sub>k</sub><sup>&minus;1</sup> &sdot; (x &minus; a <sub>k</sub>) =
*const*<sub>1</sub> &minus; *const*<sub>2</sub> &minus; 0.5 &sdot;
(x&minus;a<sub>k</sub>)<sup>T</sup> &sdot;
C<sub>k</sub><sup>&minus;1</sup> &sdot; (x&minus;a<sub>k</sub>)

Mahalanobis-távolság:

d<sub>Mk</sub> = (x&minus;a<sub>k</sub>)<sup>T</sup> &sdot;
C<sub>k</sub><sup>&minus;1</sup> &sdot; (x&minus;a<sub>k</sub>)

egyszerűbb számítás

### Hibrid módszerek

- Gyors és kellően pontos módszer érdekében
- Változatai:
    - Box + legközelebbi középpont
    - Box + legnagyobb valószínűség

### Neurális hálózatok

- emberi agy működésének mintázatára
- több réteg &rarr; kapcsolatok, döntési fa
- van visszacsatolás: kimenet &rarr; bemenetre
- ki lehet alakítani tanulóhálozatokat
- párhuzamosan bemenő infó, rácspontok: logikai döntések, súlyozni is lehet
- pl. &rho; &lt; 0.5 vagy GR &gt; 0.1,...
- tanulási folyamat lassú, osztályozás gyors
- "finom" döntéseket is lehet hozni
- döntések: hány réteget használok, súlyok megválasztása
- Eszköze:
    - backpropagation hálózat
- Tananyag:
    - közvetlenül a pixelek intenzitásértékeivel
- Előny:
    - bonyolult, összetett intenzitáshatár-képzés
    - részosztályok kezelhetősége
- Hátrányok:
    - „black-box” tulajdonság
    - szakértelmet igényel

- érdemes kipróbálni többféle módszert
- nem lehet előre tudni melyik osztályozási módszer lesz a legjobb
- jól kell kiválasztani a tanulóterületeket; térben és időben reprezentatívak
  legyenek
- több módszer, indexek belevétele, előfeldolgozott adatok &larr; légköri
  korrekció
- klasszifikálásnál ne keverjünk össze lényegesen eltérő területeket

## Nem-ellenőrzött osztályozás

- ha nincs infó az adott területről, pl. múltbéli felvételek, távoli
  területek, nincs elég idő &rarr; gyorsan kell csinálni
- én mondom meg hány osztályom legyen, kb. 15-18 tipikusan
- osztályozás után össze lehet vonni osztályokat
- túl sok osztály, sok átfedés &hArr; kevés, nem elég jó felbontás
- Nincs tematikus osztály
- Nincs tanulóterület (ground truth)
- Cél: csoportok (klaszterek) képzése lehetőleg automatikusan
- Alkalmazási példa: homogén területek keresése

### Nem-ellenőrzött osztályozók

- k-means
- ISODATA
- neurális hálózat

### K-means módszer

- kb. ugyanaz mint k-means, csak véletlenszerű a választás
- ha két osztály közel esik (én határozom meg a kritériumot) összevonom
- megvannak az osztályok &rarr; azonosítani kell őket &rarr;
  "visszavetíteni" a képre; pl. Balatonra, Velencei-tóra esnek a pixelek
  &rarr; vízfelület
- addig nem alkalmazom az algoritmust, amíg a teszt területet megfelelően nem
  azonosítja
- felhő árnyék "torzít"

Algoritmus:
1. *k* véletlenszerű kezdő "átlag"
2. minták besorolása *k* csoportba (a legközelebbi átlaghoz)
3. klaszterjellemzők számítása, ez lesz az új átlag
4. 2 és 3 ismétlése, amíg nem konvergál

arg min<sub>**s**</sub> &sum;<sup>k</sup><sub>i=1</sub> &sum;<sub>
**x**<sub>j</sub>&isin;**S**<sub>i</sub></sub>
||**x**<sub>j</sub>&minus;**&mu;**<sub>i</sub>||<sup>2</sup>

### ISODATA

Iterative Self-Organizing Data Analysis Technique

1. Kiválasztunk megfelelő számú középpontot az intenzitástérben egyenletesen
vagy más módszerrel.
2. Minden pixelt a hozzá legközelebbi középponthoz sorolunk.
3. Kiszámítjuk az új középpontokat (a besorolt pixelek átlagvektora).
4. Ha a két osztály közel esik egymáshoz, összevonjuk őket.
5. Megvizsgáljuk a középpontok mozgását, ha ez nagy, akkor folytatjuk a 2.
lépéssel.
5. Kialakultak a klaszterek.

### Neurális hálózatok

- versengő (competitive) hálózatok 
    - „winner-takes-all”-szabály

- önszerveződő leképezések (self-organizing maps – SOM)

# Termésbecslés, terméselőrejelzés

Termésbecslés: a teljes tenyészidőszak távérzékelt adatai alapján
Terméselőrejelzés: a tenyészidőszak egy részének távérzékelt adatai alapján
- kell: terméshozam adatok - Mo.-n KSH szolgáltatta; baj lassú &rarr;
  gyorsítás: tapsztalt szakemberek tudnak becslést adni, átlag terméshozamot
  becsülni
- össztermés = búzatábla terület &sdot; átlagos várható hozam 1 ha-on
    - Y<sub>búza</sub> = &sum;<sub>n</sub> T<sub>n</sub> &sdot;
      Y<sub>n</sub>
    - megyei szintre le lehet menni
- humán (szakértői) termésbecslés: nem tudja az egész táblát végigjárni
- ma: távérzékelt adatokból becslés
- termés előrejelzés: becslés és aratás között sokminden történhet
- termésátlag mértékegysége: kg/ha (Mo.-n tonna/ha) v. mázsa/ha &larr;
  tömeg/terület
- USA-ban: térfogat/terület - bu(véka = 400 l ?)/acre; termés
- nedvességtartalma befolyásolja a tömegét és térfogatát, tömegben
  5-10 % eltérést is adhat

Módszerek:  
- Közvetlen: Távérzékelt adat &hArr; termésátlag, "fekete doboz"
- Közvetett: Távérzékelt adat &hArr; Növényállapot jellemző (pl. LAI &hArr;
  termésátlag)
    - LAI termésátlag közötti kapcsolat &larr; agrológusok, biológusok
    - bonyolítás: agrármeteorológiai modellek &larr; hőmérséklet, csapadék;
      országos szinten nem lehet megvalósítani
    - nagyfelbontású kép esetén ha valóban jól működik, akkor pontosan tudok
      becsülni termést
    - hátrány: adott növényfajtára becslés

- nagyfelbontású: tábla/gazdaság szintű (LANDSAT TM, Spot, IRS adatokból)
- kisfelbontású („Robosztus): megye/régió/országos szintű (NOAA AVHRR, MODIS
  adatokból)

## AVHRR adatok

GN = &rho;<sub>2</sub>&minus;&rho;<sub>1</sub>, BR = &rho;<sub>2</sub> +
&rho;<sub>1</sub>  NDVI = GN/BR és RVI = &rho;<sub>2</sub> &frasl;
&rho;<sub>1</sub>

## Kettős Gauss-görbe

- AVHRR GN menet modellezése kettős Gaussal
- szárazság &rarr; kényszerérés: megpróbál előbb termést hozni

f(t) = A<sub>1</sub> exp{&minus;(t&minus;t<sub>01</sub>)<sup>2</sup> &frasl;
&Delta;t<sub>1</sub> } + A<sub>2</sub> exp{&minus;(t&minus;t<sub>02</sub>)
<sup>2</sup> &frasl; &Delta;t<sub>2</sub> } + (a &sdot; t + b)

## Előrejelzés

Előrejelzés kukoricára:

A 240. napon: GN<sub>240+5i</sub> = GN<sub>200&minus;240</sub> &minus; 0.0008
&sdot; (20 + 5i) &larr; i=1..6

A 210. napon:  GN<sub>210+5i</sub> = 1.03 &sdot; GN<sub>180&minus;210</sub>
&minus; 0.00075 &sdot; (15+5i) &larr; i=1..6  GN<sub>240+5i</sub> =
GN<sub>240</sub> &minus; 0.0009 &sdot; 5i &larr; i = 7..12

# A távérzékelt adatok interpretációja és alkalmazásai

## Archeológia

- Elsősorban vizuális interpretáció - megfelelő előkészítés után
- Infravörös (termális) felvéteke és légifotók is (terület nagyságától
  függően)
- ha a Föld felszínéről nem látszik

## Meteorológia

- időjárás rövid előrejelzés &larr; felszínhőmérséklet
- urban heat island
- természetes növényfelület párologtatással hűti magát

## Vízminőség

- víz reflektanciája kicsi, de lehet vizsgálni
- klorofill tartalom &rarr; szervesanyagtartalom, algák
- turbidity - örvényesség, kicsi szennyezőanyagok lerakódnak

## Növénytakaró

- felszínborítottság &larr; klasszifikáció
- növényállapot
- növényfejlődés
- termésbecslés
- terméselőrejelzés:
    - távérzékelt adatok &hArr; növényállapot
    - közvetlen vagy közvetett kapcsolata
    
## Talaj - szikesedés

- mezőgazdaság: víz mellett a talaj a másik kritikus tényező
- nedvességtartalom, eróziós vizsgálat &rarr; potenciálisan veszélyeztetett
  területek kijelölése
- szikesedés: felgyülemlik a nem oldható só a talajban &rarr;vezetőképesség
  változik &rarr; mérés + távérzékelés &rArr; klasszifikáció
- talajjavítási kísérletek monitorozása

## Geológia

- főérték transzformáció (&hArr; klasszifikáció) változások kiemelése
- hiperspektrális felvételek &rarr; talajterületek klasszifikációja;
  ábrázolás: hiperspektrális kocka

## Természeti katasztrófák

- árvíz, belvíz, erdőtűz veszélyeztetett területek felmérése
- hőmennyiség mérése &rarr; olvásnál várható-e árviz
- vulkánkitőrés savas esőt okozhat, perfelhő állapota, mozgása
- növénybetegségek

## Növénybetegségek

# Távérzékelés radarral

- A hullámtan ide vonatkozó részei (ismétlés, vázlat) -Retardált potenciálok
- Elemi sugárzók (dipól, körantenna(mágneses dipól), elemi felület
  (Huyghens-féle sugárzó) )
- Radar alapfogalmak (nyereség, hatásos felület, radar egyenlet, nem elemi
  sugárzók, reciprocitás), radarberendezések.
- Távérzékelési alkalmazások
    - radar altiméter
    - SAR szintetikus apertúrájú radar mérések
    - scattero-méter, felszíni szélsebesség mérés
    - meteorológiai felhőradar (cloud profiling)
- Radar távérzékelés a Naprendszerben
- L, S, C, X sávban; 1-12 GHz
- tengeráramlások a felszínt eltolják, hosszú radar altimetriai
  mérésekkel mérhető

Távérzékelés az EM spektrumban

<!-- kép -->

Radar, rádió és mikrohullám frekvenciatartományok

<!-- kép -->

Légköri abszorpció a MW tartományban

<!-- kép -->

## A radar távérzékelés sajátosságai

- Időjárásfüggetlen (egy adott frekvenciatartományban)
- Nem szükséges a Nap, aktív mérés
- Szükségesek lehetnek korrekciók (terjedési úton a sebesség(víztartalom), pl.
  GPS-nél is).
- A jellemző frekvenciákon van némi behatolása az EM hullámnak talajba,
  növényzetbe, hótakaróba...
- Nagyobb hullámhosszak, 100m, 1km behatolás 1-10MHz tartomány, (Mars, felszín
  alatti jég kutatása)

**Alkalmazások**

- Topográfia (DEM interferometriával)
- Oceanográfia (szélsebesség, áramlatok, hullámmagasság)
- Mezőgazdaság (osztályzás, talajnedvesség...)
- Erdészet (Biomassza becslés, erdőirtások... )
- Környezet monitorozás (olajfoltok, árvizek, települések, globális változások)
- Katonai felderítés, ellenőrzés.

## Maxwell egyenletek, áttérés a potenciálokra

a Maxwell egyenletek:  &nabla;&times;**H** = **j** + &part;<sub>t</sub>**D**
&nabla;&times;**E** = &minus;&part;<sub>t</sub>**B**  &nabla;**D** = &rho;
&nabla;**B** = 0

anyagi egyenletek:  **D** = &epsilon;**E**  **B** = &mu;**H**

A vektorpotenciál: **B** = &nabla;&times;**A**  A harmadik egyenletből:
&nabla;&times;(**E** + &part;<sub>t</sub>**A**) = 0 &rArr; **E** +
&part;<sub>t</sub>**A** = &minus;&nabla;&Phi; &rArr; **E** =
&minus;&nabla;&Phi;&minus;&part;<sub>t</sub>**A**

A térerősségek a potenciálok idő és tér szerinti deriváltjaiból képezhetők.  A
potenciálok határozatlanok mert a térerősségeket a deriváltjaik definiálják:

A mértéktranszformáció:  **A**<sup>'</sup> = **A** + &nabla;&chi;
&Phi;<sup>'</sup> = &Phi;&minus;&part;<sub>t</sub>&chi;  változatlanul hagyja a
térerősségeket

A Maxwell egyenleteket a potenciálokkal felírva, átrendezgetve:
&nabla;<sup>2</sup>**A** &minus; &epsilon;&mu; &part;<sub>t</sub><sup>2</sup>
**A** &minus; &nabla;(&nabla;**A**+&epsilon;&mu;&part;<sub>t</sub>&Phi;) =
&minus;&mu;**j**  &nabla;<sup>2</sup>&Phi; &minus; &epsilon;&mu;
&part;<sub>t</sub><sup>2</sup> &Phi; &minus;
&nabla;(&nabla;**A**+&epsilon;&mu;&part;<sub>t</sub>&Phi;) = &minus;&rho;
&frasl; &epsilon;

Ejtsük ki a (&nabla;**A**+&epsilon;&mu; &part;<sub>t</sub>&Phi;) tagokat.
Lorentz-feltétel (nincs fizikai jelentése):

&nabla;**A**+&epsilon;&mu; &part;<sub>t</sub>&Phi; =  0

A Lorentz feltétellel a következő d'Alembert típusú diff.egyenletet kapjuk:
&nabla;<sup>2</sup>**A** &minus; &epsilon;&mu; &part;<sub>t</sub><sup>2</sup>
**A** = &minus;&mu;**j**  &nabla;<sup>2</sup>&Phi; &minus; &epsilon;&mu;
&part;<sub>t</sub><sup>2</sup> &Phi; = &minus;&rho; &frasl; &epsilon;  a
megoldásuk, a retardált potenciálok, ezek egyben kielégítik a Lorentz-
feltételt.

Elemi sugárzók ( &lambda; >> sugárzó rendszer méret)

Sugárzási teljesítmény a távoltérben:  **S**<sub>0</sub> = 0.5 &sdot; {
    (I<sub>0</sub> k<sub>0</sub> l) &frasl; (4&pi;) } &sdot; **Z**<sub>00</sub>
    **S**<sub>k</sub> = S<sub>0</sub> &sdot; { sin&theta; &frasl; r
    }<sup>2</sup> &sdot; **e**<sub>r</sub>

Huyghens-sugárzó: **S** = 0.5 &sdot; { (E<sub>0</sub><sup>2</sup> A
<sup>2</sup>) &frasl; (4&pi;)<sup>2</sup> } &sdot; { &epsilon;<sub>0</sub>
&frasl; &mu;<sub>0</sub> }<sup>1 &frasl; 2</sup> &sdot; {
    k<sub>0</sub><sup>2</sup> &frasl; r<sup>2</sup> } &sdot; (1 +
    cos&theta;)<sup>2</sup> **e**<sub>r</sub>

Az elemi sugárzókra vonatkozó oldalak forrása: Ferencz Csaba: Elektromágneses
hullámterjedés c. Könyve (Akadémiai Kiadó, 1996)

## Radar technológia, alapfogalmak

Kisugárzott összteljesítmény:  P = &int;<sub>4&pi;</sub> **e**<sub>r</sub>
**S**(r, &Omega;) r<sup>2</sup> d&Omega;

Intenzitás:  I(&Omega;) = r<sup>2</sup> S(r, &Omega;)  I<sub>*izotróp*</sub> =
P &frasl; (4&pi;) izotróp intenzitás

Iránykarakterisztika:  G(&Omega;) = I(&Omega;) &frasl; I<sub>*izotróp*</sub>

Nyílásszög, szögfelbontás:  &Theta; = &lambda; &frasl; (antenna &perp; hossza)

A hatásos vételi felület (A<sub>h</sub>), egyetlen irányból (&Omega;) származó
jelre az antenna P<sub>v</sub> teljesítményt vesz fel.  P<sub>v</sub>(&Omega;)
= S &sdot; A<sub>h</sub>(&Omega;)

## Reciprocitás

Reciprocitás tétele: az antenna adó és vevő kerakterisztikája azonos.  A
reciprocitás feltétele: &epsilon;<sub>ij</sub> és &mu;<sub>ij</sub>
szimmetrikus tenzorok.

"A" antenna sugároz P<sub>A</sub> teljesítménnyel:  S = { P<sub>A</sub> &frasl;
(4&pi;r<sup>2</sup>) } &sdot; G<sub>A</sub>,  P<sub>A</sub> = S &sdot;
A<sub>HV</sub> = { P<sub>A</sub> &frasl; (4&pi;r<sup>2</sup>) } &sdot;
G<sub>A</sub> &sdot; A<sub>HV</sub>

"V" antenna sugároz P<sub>A</sub> teljesítménnyel:  P<sub>V</sub> = S &sdot;
A<sub>HV</sub> = { P<sub>A</sub> &frasl; (4&pi;r<sup>2</sup>) } &sdot;
G<sub>V</sub> &sdot; A<sub>HA</sub>

&dArr;

G<sub>A</sub> &frasl; A<sub>HA</sub> = G<sub>V</sub> &frasl; A<sub>HV</sub> = G
&frasl; A<sub>H</sub>

a hatásos felület, egy elemi dipólus sugárzóra könnyen kiszámolhatóan:  

A<sub>H</sub>(&Omega;) = { &lambda;<sup>2</sup> &frasl; (4&pi;) } &sdot;
G(&Omega;)

## Radaregyenlet

A kisugárzott jel lehet szinuszjel, vagy bonyolultabb, folyamatos vagy
impulzus-szerű:  P<sub>v0</sub> = P<sub>0</sub> &sdot; { G<sub>max</sub>
&frasl; (4&pi; R<sup>2</sup>) } &sdot; &sigma;(&minus;**e**<sub>0</sub>,
**e**<sub>0</sub>) &sdot; { A <sub>H max</sub> &frasl; (4&pi; R<sup>2</sup>) }
= P<sub>0</sub> &sdot; { &lambda;<sup>2</sup> &frasl; (4&pi;)<sup>3</sup> }
&sdot; { G<sub>max</sub><sup>2</sup> &frasl; R<sup>4</sup> }
&sigma;(&minus;**e**<sub>0</sub>, **e**<sub>0</sub>)

&sigma;(&minus;**e**<sub>0</sub>, **e**<sub>0</sub>): Visszaszórási
Keresztmetszet-sűrűség

A pontosabb leírás (v. bonyolítási lehetőségek):
- a főnyalábra való integrálással
- A közeg csillapodásával lehet számolni
- Adó vevő nem azonos
- Térfogati visszaszórás (nagy csillapítás a céltárgyban)

**A radar "felfedezése"**

## Radarberendezések

Adó - Vevő - Antenna

Antennák:
- dipólus, (egyszerű antennák, alacsony frekvenciákon, kis teljesítmény)
- Szarv antenna. A hullámvezető tölcséresen kiszélesedik
- Parabola antennák
- Fázisvezérelt antennarács (Phased Array, PESA(Passive Electronically Scanned
  Array))
- AESA (Active electronically Scanned Array), minden egyes adó/vevő elem külön
  szabályozható, programozható

Adó berendezések (transmitter), a mikrohullámú jel generálása

- Vákuum csövek, magnetron, klisztron és haladóhullámú elektroncső
    - Előnyben van: nagy teljesítményeknél és nagy frekvenciáknál
    - De drágább, nagyobb mint a félvezető
- Félvezető adó elemek, kisebb teljesítmény, de sok elfér kis helyen, külön
  szabályozhatók, 2007: 2.6&times;3.2 mm nagyságú chip-en 16 adó/vevő elem.

Vevő, ugyanaz a hardware mint az adó, de nem kell akkora teljesítményeket
kezelni mint az adó áramköröknek.

## Radar berendezések működési paraméterei

Folytonos kisugárzással dolgozó radarok (CW Continuous Wave)
- Nagy teljesítmény (ha távolra), egyszerű feldolgozás.
- Sebesség mérés, egyszerű közelség érzékelők,
- Rakétavédelmi rendszerek, légvédelmi rakéták...
- Lehet távolságmérésre is használni, ha frekvenciamodulált (magasságmérés
  repülőn)...

A távérzékelésben a legtöbb radar berendezés, a radar altiméterek, és a SAR
berendezések is rövid impulzusokkal dolgoznak.  Alapvető jellemzők

- működési frekvencia (MW tartomány 3-30cm, 1-10GHz)
- az impulzus hossza = n&times;10 μsec (műholdak)
- Az impulzus ismétlődési ideje vagy frekvenciája (Pulse Repetition
  Time|Frequency) -- 1-3 kHz
- A kisugárzott/vett jel polarizációja: HH,VV,HV,VH az első betű a vett, a
  második a kisugárzott jelre vonatkozik (H=horizontális (E vektor),
  V=vertikális)

## Hullámvezető és parabola antenna

Normál kábellel nem lehet mikrohullámú jelet továbbítani

Kisebb frekvenciákon jó a koaxiális kábel

Nagyobb frekvenciákon &gt;6GHz: Csak üreges négyzetesvagy kör keresztmetszetű
hullámvezetők jöhetnek szóba.

## Magnetron

- nagy sugárzó teljesítmény
- jó hatásfok
- nem teljesen pontos a jel frekvenciája, nem alkalmas koherens radarokban

## Radar mérések térbeli felbontása

(RAR, Real Aperture Radar, valós apertúrájú radar)

A távolságmérés, a felbontás a kibocsátott impulzus hosszától függ nem függ
direktben a távolságtól és a frekvenciától

A felbontás:  &delta; = 0.5 &sdot; c&tau;, &larr; &tau; -- pulzus hossza
&delta; = 0.5 &sdot; (c &frasl; &beta;), &larr; &beta; -- pulzus sávszélessége
&beta; = 10 Mhz &rarr; &tau; = 0.1 &mu;sec, &delta; = 15 m

Oldalirányú felbontás (a sugárnyaláb szélességéből) Angolul: "Azimuth" vagy
"Along-track"  &delta;<sub>*oldal*</sub> = ( &lambda; &frasl; D ) &sdot; R  R
-- távolság  D -- antennnaméret

## Tömörített radar impulzus

Lineáris (Chirp) és nem lineáris FM (frekvencia modulált) impulzusok.  A
sávszélességük jóval nagyobb lehet mit az 1 &frasl; &tau;.

A tömörített radar impulzusok tulajdonságai:
- Az adott sávszélességhez nem kell nagyon rövidnek lenni az impulzusnak,
  kisebb teljesítmény is elegendő. (&sim;századnyi teljesítmény igény)
- A visszavert jel felgolgozása komplikáltabb, FFT, illesztett-szűrés.
- A &delta;<sub>R</sub> =1.5m-es felbontáshoz 100MHz sávszélesség kell

## Radar altiméterek

- Rövid impulzusok: PRF &sim;1700/sec -Sokszor csak lefelé néző elrendezés, de
  hardware függően lehet "multi-beam" avagy pásztázó működésű (ld. A képen)
- Kombinálható SAR technológiával a felszín menti felbontás növelése érdekében
- A pontosabb távolságmérés érdekében figyelembe kell venni a terjedési úton a
  törésmutató változásokat, amelyek oka a légkör víztartalma vagy ionizáció
  lehetnek.

Felhasználásuk (a távérzékelésben)
- Óceán felszínek
    - dinamikus felszín - hullámmagasság...
    - tengerszint mérés, áramlatok, víz-levegő energia csere (hő+szél)
- Szárazföldön topográfiai térképezés, bolygóknál pl. a Vénusz felszíni
  topográfia.

**A SAR technológia kezdetei**

<!-- kép -->

## SAR (Synthetic Aperture Radar, szintetikus apertúrájú radar)

- Doppler-eltolódás miatt különböző frekvenciák &hArr; különböző felszíni
  pontok
- oldalra néző radar
- csak antennnamérettől függ
- Képalkotó (2D) radar, felhasználva a forrás mozgását, a felszíndarabokról
  visszavert jelek különböző Doppler eltolódásának kihasználásával megnöveli a
  radarberendezés azimut irányú felbontását (némi fáradságos
  jelfeldolgozással).
- Lényeges része a jelfeldolgozás, de egy ideig ez nem megy real-time, kb
  '86-tól realtime
- Oldalról ránézés, kihasználandó a radarok jó sugárirányú felbontását
- független a napsugárzástól

Jellemzői:
- A radar elektronika számára lényeges a stabil koherens jel gerjesztés és a
  fázishelyesen vett jel vagy időben pontosan elhelyezhető beérkező jelalak.
- A platform helyének és mozgásának pontos ismerete + felszín geometriája
  formája.
- Megfelelő feldolgozó kapacitás (on-board kb. 1986-tól)

**Történet**

- Az alapötlet: Doppler beam-sharpening (a Doppler effektus kihasználásával
  úgymond javítsuk a felbontást, bontsuk több részre a jelet)
- 1950-es évektől elindulnak a SAR kísérletek
- 1960-as évek (USA) repülőgépes kíérletek
- 1978 SEASAT az első polgári SAR műhold
- 1981 SIR-A (Shuttle|Spaceborne Imaging Radar), 1984 SIR-B
- 1990-es évektől megnőtt az űrbéli SAR műszerek száma:
    - 1990, Magellán, Vénusz
    - 1994 SIR-C (NASA + DLR)
    - ESA: ERS-1(1991), ERS-2(1995)
    - RADARSAT-1 (1991-2013), RADARSAT-2 (1995-2016) (Kanadai űrügynökség CSA)
    - 2002 SRTM (SIR-C + második antenna &rarr; magasság mérés)
    - 2002 ENVISAT(ESA) -2012.04.08 (Envisat-tal megszűnik a kapcsolat.)
    - 2007 TerraSAR-X (DLR, Német Űrügynökség) -- TanDEM-X
    - 2014(-2021) Sentinel-1A (ESA)
    - 2016(-2023) Sentinel-1B (ESA)

[Oscar Satellites](www.wmo-sat.info/oscar/satellites): műszerek,
paramétereikkel, felhasználhatóságukkal...

Heurisztikusan, ha a az antennaméretet az egy pixelre vonatkozó adat gyűjtése
alatt megtett úttal azonosítjuk

&delta;<sub>AT</sub> = { &lambda; &frasl; (2 L<sub>SA</sub>) } &sdot; R
L<sub>SA</sub> = ( &lambda; &frasl; D<sub>AT</sub> ) &sdot; R
&delta;<sub>AT</sub> = D<sub>AT</sub> &frasl; 2

**Gábor-Heisenberg féle határozatlansági reláció**

Két különböző frekvenciájú jel elkülöníthető egy T hosszúságú adatsorból, ha:
&delta;&nu;= 1 &frasl; T

A frekvencia különbség itt a dy távolságban elhelyezkedő pontok a műholdhoz
viszonyított eltérő sebességéből adódó különböző Doppler eltolódásból adódik.

A Doppler eltolódás EM jelekre:  &nu; = &nu;<sub>0</sub> {
    [1&minus;(V<sup>2</sup> &frasl; c<sup>2</sup>)]<sup>1 &frasl; 2</sup>
    &frasl; [1&minus;(V &frasl; c) &sdot; cos&alpha;] }

Az oda és visszajövő jelre a dupla Doppler:  &nu;<sub>1</sub> =
&nu;<sub>0</sub> &sdot; D(V, &alpha;);  &nu;<sub>2</sub> = &nu;<sub>1</sub>
&sdot; D(V, &alpha;);  &nu;<sub>2</sub> = &nu;<sub>0</sub> &sdot;
D<sup>2</sup>(V, &alpha;);  d&nu;<sub>2</sub> &frasl; dy = &nu;<sub>0</sub>
&sdot; 2 &sdot; d{D(V, &alpha;)} &frasl; dy  itt most a felbontás (&Delta;y) és
a &Delta;&mu; kapcsolata érdekes, V &frasl; c &lt;&lt; 1 és cos&alpha; "elég"
kicsi esetében

d&nu;<sub>2</sub> &frasl; dy = { [1&minus;(V<sup>2</sup> &frasl;
c<sup>2</sup>)]<sup>1 &frasl; 2</sup> &frasl; [1&minus;(V &frasl; c) &sdot;
cos&alpha;]<sup>2</sup> } &sdot; { sin&alpha; &frasl; (R sin&alpha;) } &sdot;
(V &frasl; c)  d&nu;<sub>2</sub> &frasl; dy |(y = 0) = &nu;<sub>0</sub> {
    1&minus;(V<sup>2</sup> &frasl; c<sup>2</sup>) }<sup>1 &frasl; 2</sup>
    &sdot; { V &frasl; (R<sub>0</sub> &sdot; c) } &cong; &nu;<sub>0</sub>
    &sdot; { V &frasl; (R<sub>0</sub> &sdot; c) } =  V &frasl; (R<sub>0</sub>
    &sdot; &lambda;) 

V &frasl; c &lt;&lt; 1 felhasználásával:  &Delta;&nu; = 1 &frasl; T; T =
R<sub>0</sub> &sdot; (&lambda; &frasl; D<sub>AT</sub> ) &sdot; (1 &frasl; V),
&Delta;&nu; = { (V &sdot; D<sub>AT</sub>) &frasl; (&lambda; R<sub>0</sub>) } =
2 &sdot; { V &frasl; (&lambda; R<sub>0</sub>) } &sdot; &Delta;y &rArr; &Delta;y
= D<sub>AT</sub> &frasl; 2

A pályamenti felbontás csak az antenna méretétől függ!

**Mi korlátozza a felbontás növelését?**

- D<sub>AT</sub> &frasl; 2 távolságonként kell impulzus &rarr; alsó határ PRF
  (Pulse Repetition Frequency)
- a pásztaszélesség szétnyújtja a visszavert jelet, nem lehet addig új
  imppulzus

V &frasl; &delta;<sub>AT</sub> &le; PRF &le; {2&tau; + 2(R<sub>f</sub>&minus;
R<sub>n</sub> ) &frasl; c }<sup>&minus;1</sup>  *pásztaszélesség korlát*

- Egyszerre több jel is úton van (az űreszközöknél), adás/vétel összehangolása
- adatáram, digitalizálás, tárolási korlátozások

A<sub>min</sub> = (4V&lambda;R &sdot; tan&phi;<sub>i</sub>) &frasl; c

- ezen túl az adatforgalom sebessége, a tárolási kapacitás is korlátozza a
  felbontást (adatmennyiséget)

Tényezők, amik bonyolítják a jelfeldolgozást:
- terjedési korrekciók (légköri víz, ionizáció az úton)
- gömbfelület
- a Föld forgása
- a műhold pálya excentricitása
- műhold állásszögeinek kis eltérései
- pixel geometria, egyenlő időkülönbségbekből növekvő pixelek a kép szélén

A radar visszaverődés mértékét meghatározza a hullámterjedést befolyásoló
dielektromos állandó (&epsilon;)  A természetes felszíneknél ez többnyire 3-8
közötti érték, víznél 80 Minél nagyobb az &epsilon; annál jobban veri vissza az
anyag a sugárzást (nagy törésmutaó, nagy visszaverődés) &rarr; talaj vagy
növényzet nedvességtartalmára információt hordoz a radar visszaverőképesség.  A
dolgot bonyolítja a felszíni geometria is...

- felszín alá behatol &rarr; hó és jég elkülöníthető
- &sim; 100 km-es pászták
- AIS &rarr; több felvételből áramlás sebessége

## Interferometric SAR (InSAR) technológia

- A SAR felvétel tartalmaz amplitudó (radar reflektancia) és fázisinformációt a
  felszínelemekről
- Két különböző helyről készített felvételek kombinálásából fáziskülönbség-kép
  készíthető, ebből távolságkülönbség vezethető le &rarr; a felszín
  topográfiája

### IFSAR SAR interferometria

IFSAR vagy InSAR, ugyanarról a teületről két SAR felvétel kombinálva, eredmény:
DTM (magasság felbontás &sim;méteres, de változó lehet töbször 10m is a hiba
hegyekben..)
- SRTM, két antennával, 60° szélességig, felbontás 90m
- Vagy ERS-2 és Envisat tandem konstellációban, 2km bázistávolsággal
- TerraSAR-X, TanDEM-X 12m-es felbontás az egész felszínről (2014) &sim;2500TB
  adat. pl. [worlddem](http://www.intelligence-airbusds.com/worlddem/)

**Persistent Scatterer Interferometry (PSI)**

Persistent scatterer: olyan visszaverő felület a föld felszínén, amely erősen
reflektál és minden évszakban megbízhatón ugyanolyan marad a visszaverő
tulajdonsága (általában ember alkotta felületek, háztetők, ...)

## SAR adatok felhasználási területei

- Térképezés
- Felszíni deformációk észlelése, INFSAR
- Tengeri és szárazföldi jég monitorozása
- Mezőgazdasági felhasználás, növényzet osztályozása, radar reflektanciákkal
- Erdészeti fedettségi térképezés
- Óceni áramlatok, hullámzás vizsgálata

## RadarSat (CSA) a jövőben

RadarSat Constellation Mission (RCM)
- 3 műhold, együttesen 90% napi lefedettség, C-sáv
- Az első fellövés: 2018 (2015.nov)
- 586-615km Napszinkron pálya, i=97.74°
- Kicsit kisebbek, egyszerűbbek (célratörőbbek) mint az elődök. Alacsonyabban
  keringenek (jobb felbontás).
- Kanadában különösen fontos az ország távoli, sokszor bejárhatatlan részeinek
  ellenőrzése

## TerraSAR-X (2007), TanDEM-X műholdak

- DLR (**Deutsche Zentrum für Luft- und Raumfahrt**), Német
- Űrügynökség+ EADS Astrium
- Utóda a SIR-C (1994) és SRTM (2000) misszióknak
- AIS - Along Track Interferometry. Automatikus forgalmi adatok (szárazföldi
- utakon 10-50m/s), Vízi áramlatok mérése.
- 5 éves névleges szolgálati időtartam (2012)
- INSAR a TAnDEM-X-szel, (Interferometric SAR), globális DEM (12x12m
- felbontás, vertikálisan 2m relatív, 4m abszolút), kulcsszó: WorldDEM, 2014-
  ben elkészült.
- Topográfiai térképezés
- Felszínfedettségi térkép
- Digitális terep és felszínmodellek
- Felületi mozgás monitorozása
- A műhold kereskedelmi célú is, lehet rendelni archívumból is ...

## ERS - ENVISAT (ESA) sorozat

utód: Sentinel-1A, -1B 2014-.., 2016-..

**Műszerek:**
- Képalkotó SAR, InSAR technikával nagyon pontos magasságok, tandem működtetés
  ERS-2 és ENVISAT (2007,2008)
- Radar altiméter
- Passzív MW radiométer (terjedési út-korrekció az altiméterhez)

**ENVISAT (2002)**  **RA-2** altiméter két frekvencián 13.575GHz (Ku) és 3.2GHz
(S) az ionoszferikus korrekció miatt, 4.5cm febontás, horizontálisan 19km,
hullámmagasságra &sim;25cm  **MWR**, passzív MW radiométer, terjedési út
korrekciók **ASAR**, C sávban (5.3cm), 30m-5km felbontás, 5 féle polarizáció

**Felhasználási területek:**  
- RA-2: Óceán topográfia, tengeri jég mérése  
- ASAR: hullám karakterisztika („monster waves”), óceáni frontok, tengerpart
  dinamikája, erózió, szennyeződés, hajózás, halászat nyomonkövetése,
  olajszennyeződés térképezése
- Tengeri jégtakaró nyomonkövetése, térképezés, földfelszíni deformációk
  érzékelése, termésbecslés, erdőtakaró térképezés.

**ESA: Sentinel-1 radar (SAR) műhold**

[Honlap](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/)

- Az ERS-1, ERS-2 és az ENVISAT utódaként
- Sentinel program: két hasonló pályán keringő műhold (Sentinel-1A|1B)
- 6-18 h Napszinkron pálya, 693km, 1A fellövése: 2014 ápr. 3. 1B &rarr;
  &ge;2016
- C-sáv, 5.4GHz, felbontás 4-80m, teljesítmény 4800W
- Globális lefedettség - 6 naponként

## QuikSCAT (1999-2009)

800km-es pálya **Seawinds radar műszer (JPL)**
- 13.4GHz, két nyalábbal, 6 fok távolságban, 4 adat a felszín egy pontjáról,
  napi visszatérés
- Forgó 1m-es antenna, 18rpm,
- PRF=189Hz
- 1800km-es pásztaszélesség,
- 400000 mérési pont naponta
- Szélmérés 3-20 m/s, +/- 2m/s, 20&deg; iránybeli pontosság

Tudomány:
- A szél keltette kapilláris-gravitációs hullámokról méri a visszaverődést
  (Bragg scattering), modell alapján számolja a szélsebességet a többirányú
  mérésekből.
- Másodlagos felhasználás: jégtípusok megkülönböztetése (friss, idős jég
  felület, sarkoknál a jégtakaró kiterjedése)
- Egyéb felhasználás: esőerdők állapotának vizsgálata

## Radar altiméterek

TOPEX/POSEIDON - Jason n (Poseidon n+1) sorozat, Ocean Surface Topography
Mission (OSTM) = Jason, 1, 2, 3 NASA-CNES közös program

Cél: elsősorban óceán felületi mérések  Pályamagasság: 1330km  Inklináció:
66&deg;  Globális lefedés: 10 naponként  
- 2 csatornás nadír irányú radarok, 5.3GHz (C sáv), 13.6GHz (Ku sáv) ionoszféra
  korrekció miatt előnyös
- 3 csatornás MW radiométer (passzív- termális sugárzás mérése:18,21,37GHz) a
  légkör terjedési útbéli víztartalmával való korrekcióhoz
- A pontos pozició meghatározáshoz 3 független követő rendszer (pontosság a
  magasságban 2cm) :
- NASA LRA (Laser Reflector Array), 10-15 földi állomással
- DORIS MW követő rendszer (all-weather) 40-50 földi állomással, +még egy tucat
  műholdon repült ilyen műszer. Eredmény: cm-es pontosság az International
  Terrestrial Reference Frame (ITRF)-hez képest.
- GPS

**Alkalmazások:**

Klimatológia, Hurrikán előrejelzés, El Nino, Hajózási, halászati
útvonaltervezés, Tengeri emlős tudomány, Korall-zátony vizsgálatok.
Csendes-óceáni szintváltozások, évi 2.85mm tengerszint változás az eltelt évek
alatt

**TOPEX/Poseidon NASA-CNES**  1992 Aug 10 – 2006 jan. Pálya: 1330km, inkl = 66
fok

Feladatok
- Óceán felszíni topográfia
- Felszín magasság 5cm-es pontossággal
- Óceáni áramlatok feltérképezése
- El Niño előrejelzése
- Addig legpontosabb árapály térkép
- Gravitációs kísérlet – a Föld gravitációs terének pontosítása.

Műszerek:
- Altiméter (C+Ku, Ku sávban)
- Mikrohullámú radiométer - víztartalom mérése, altiméter korrekcióra
  (18,21,37GHz)
- Pozícionáló műszerek: GPS, Lézer fényvisszaverő egység, Doppler követő
  antenna (CNES: Doppler Orbitography and Radiopositioning Integrated by
  Satellite, DORIS)

**TOPEX/Poseidon misszió folytatása, OSTM (Ocean Surface Topography Mission)**

**Jason-1** (NASA-CNES, TOPEX/Poseidon utód)  (Joint Altimetry Satellite
Oceanography Network)
- Felbocsátás: 2001, Dec. 7, EOL: 2013.júl.1
- A TOPEX/Poseidon időbeli kiterjesztése szinte ugyanazokkal a műszerekkel
  feladatokkal
- Tengerszint magasság 3.3cm-es pontossággal.  OSTM (Ocean Surface Topography
  Mission )/Jason-2 (NASA, NOAA, CNES, EUMETSAT)
- Felbocsátás: 2008 Jun. 15.

JASON-3
- elhalasztva (SpaceX sikertelen kilövés...), 2016. jan. 17 óta már működik
  (-2021)

**ESA: Mars Express (2003 -? 2014-ig tervezték)**
- Sub-Surface Sounding Radar Altimeter (**MARSIS**); a felszín alatti üledékek
  feltérképezése 3-4km mélységig,
- Mars Radio Science Experiment (**MaRS**); Mars légkör – napszél
  kölcsönhatások vizsgálata
- High Resolution Stereo Camera (**HRSC**); 2-10m-es felbontással az egész Mars
  felszín feltérképezése.
- Energetic Neutral Atoms Analyser (**ASPERA**); Felső légkör, napszél-légkör
  kcsh.
- Planetary Fourier Spectrometer (**PFS**); Légkör. Légköri molekula-abszorpció
  mérése az 1.2-45 &mu;m tartományban.
- Visible and Infra Red Mineralogical Mapping Spectrometer (**OMEGA**);
  Ásványtani térképezés 100m-es felbontással
- Ultraviolet and Infrared Atmospheric Spectrometer (**SPICAM**); Légkör.
- felszín alatti víz
- diplóantenna elég

**NASA MRO (Mars Reconnaisance Orbiter)**
- **High Resolution Imaging Science Experiment (HiRISE):** kamera, nagy
  felbontású képeket készít.
- **Context Imager (CTX):** kamera, kisebb felbontású képek készítése a HiRISE
  képeinek környezetéről.
- **Mars Color Imager (MARCI):** színes képalkotó berendezés, színes képek
  készítése és az időjárás vizsgálata.
- **Compact Reconnaissance Imaging Spectrometers for Mars (CRISM):**
  optikai/**infravörös spektrométer**, a felszín ásványtani térképezését végzi.
- **Mars Climate Sounder (MCS):** infravörös radiométer, méri a légkör
  különböző tulajdonságait (hőmérséklet, nyomás stb.).
- **Shallow Subsurface Radar (SHARAD): radar**, a Mars poláris sapkáinak
  szerkezetét határozza meg.
- **Gravity Field Investigation Package:** a gravitációs tér változásait méri.
- **Atmospheric Structure Investigation Accelerometers:** **légsűrűség**
  mérésére használható **akcelerométerek**.
- **Electra** UHF rádió – kapcsolattartás a Marsra lesszált egységekkel, erre
  redukálódott mostanra az űrszonda működése (2010 után)

felbocsátás 2005, élettartam &sim;2010-ig

SHARAD, (Shallow Radar), 10m-es dipól antenna 15-25MHz, 10MHz sávszélességű
"CHIRP" jelalak. PRF = 700Hz, pulzus hossz = 85&mu;sec. Horizontális felbontás:
0.3-3km (magasságtól függően) Vertikális felbontás: 15m Felszín alatti jég
térképezése Behatolási mélység &lt;1km

A MARSIS (ESA 2003) utódja, nagyobb frekvencia, kisebb behatolási mélység, de
nagyobb vertikális felbontás (15m)

- Az északi-sarki jégsapka térfogata ~30%-a a grönlandi jégtakarónak.  (SHARAD)
- Alátámasztja a sarki területeken a felszín alatti jégtömegek és
  gleccserformációk létezését (SHARAD)
- Új kráterek helyén idővel elszublimáló jégfoltok (spektrométer)

**Cassini - radar műszerek**

SAR - 13.78 GHz, 0.35-1.7km felszíni felbontás  Radar altiméter 13.78 GHz
24-27km horz., 90-150m vertikális felbontás  Cassini-Huygens  Kilövés 1997, az
ESA Huygens  szondájával (Titánra ereszkedés, 2005)  Cél: Szaturnusz rendszer
Enceladus és Titán holdak  2017-ig tervezik működtetni.

**SSR (Subsurface Sounding Radar) tervek 2020-2029**

SHARAD-hoz hasonló radar  FOV: 1-10km, 20-50Mhz, mélység &lt;5km,  függ.
Felbontás &sim;10m  Paraméterekkel...  

ESA/NASA, Europa Jupiter System Mission - Laplace (EJSM/Laplace)

Változott:  ESA, JUICE (JUpiter ICy moons Explorer) Zöld utat kapott (2014
Nov.) Indítás: 2022 &rarr; 2030 Jupiter

Műszerek:  **GALA** - GAnymede Laser Altimeter Felbontás: H: 20m, V: 0.1m
**RIME** - Radar for Icy Moons Exploration 16m antenna 9MHz, 1-3MHz
sávszélesség 9km behatolás, 30m vert. felbontás jégben.

# Lidar (LIght Detection And Ranging), alkalmazások

Alapja a lézer kibocsátás és detektálás.  LASER=Light Amplification by
Stimulated Emission Radiation
- Digitális felszínmodellek (DSM, DEM, DTM), repülőgépes Lidar (ALS), földi
  lézer- szkennerek
    - 3D városmodellezés (Dániban kész az első teljes főleg Lidar alapú
      "országmodell")
    - Épületmodellezés
    - Geológiai (geomorfológia), hidrológiai célú modellek, vízlefolyás
      előrejelzés, árvízveszély...
    - Erdészeti alkalmazások, biomassza ill. Fa-tömeg becslése
    - Katonai felderítés...
    - Önvezető autók...
- Sarki jégtakaró monitorozása ICEsat, GLAS
- Légköri aeroszol és felhők, magassági eloszlás (CALIPSO)
- DIAL (Differential Absorption Lidar), légköri összetevők azonosítása;
  finomhangolható két lézersugár
- nagyon pontos távolságmérés 100 m-es skála, mm-es pontosság; impulzusok
  kiadása
- szkennelő eszköz &rarr; repülőgépre vagy műholdra (nem annyira
  használható mint a radar)

## Lézer (laser) alapfogalmak

- LASER = Light Amplification by Stimulated Emission of Radiation
- Az első lézert az amerikai Theodore Harold Maiman fejlesztette ki 1960-ban.
- fény időben és térben koherens, a lézer által kibocsátott hullámok fázisa a
  sugár minden keresztmetszeténél azonos.
- A lézernyaláb keskeny és nagyon kis széttartású nyaláb. A lézerfény nagyrészt
  párhuzamos fénysugarakból áll, nagyon kis szóródási szöggel. Ezzel nagy
  energiasűrűség érhető el szűk sugárban, nagy távolságokban is. A széttartás
  nagyságrendje &lt;mrad (&lt; 3 szögperc)
- A lézerek fénye egyszínű. A lézersugár egy olyan elektromágneses hullám,
  amely közel egyetlen hullámhosszú összetevőből áll. (a látható tartományban
  0.002 nm sávszélesség) - könnyen azonosítható a detektálásnál


## Molekuláris (vagy atomi) abszorpció és emisszió, Az Einstein-együtthatók

dN<sub>1</sub> &frasl; d t = N<sub>2</sub>A<sub>21</sub> +
N<sub>2</sub>B<sub>21</sub>j &minus; N<sub>1</sub>B<sub>21</sub>j

j: spektrális energia/áramsűrűség

N<sub>i</sub> a populáció száma az i-edik energiaszinten, j a sugárzás
spektrális energiasűrűsége (hullám mérték-specifikus, hullámhossz, frekvencia
vagy hullámszám szerint) a frekvencia környékén.

Einstein együtthatók: A<sub>21</sub> , B<sub>12</sub>(stimulált emisszió) ,
B<sub>21</sub> nem függetlenek, elegendő egyet megadni (az A<sub>12</sub>-t
szokás)  A stimulált emissziónál a fázis és irány a bejövő sugárzáséval egyezik
meg, (koherencia) Termodinamikai egyensúlyban a Boltzmann eloszlásnak
megfelelően:

N<sub>2</sub> &frasl; N<sub>1</sub> =
exp{&minus;(E<sub>2</sub>&minus;E<sub>1</sub>) &frasl; (kT)}

## A lézer jel|sugárzás generálásának alapjai

A gerjesztő közeg szerint gáz-, festék-, félvzető- és szilárdtestlézerek  A
gerjesztés lehet kémiai, optikai (esetleg egy másik lézer)

## Szilárdtestlézerek

Pl. Nd:YAG (neodímiummal szennyezett ittrium-alumínium-gránát
(Y<sub>3</sub>Al<sub>5</sub> O<sub>12</sub> - YAG) Yttrium Alumínim garnet)
kristály: 1064 nm .. 532 nm, 355, 266 and 213 nm (frekvencia kettőződés,
többszöröződés), Vonalszélesség: 0.45nm (1064nm-en)

## Lézer felharmonikusok

frekvencia kettőződés 532 nm &rarr; 1064 nm

Nemlineáris közegben a gerjesztő sugárzás felharmonikusai is megjelennek

Az elektron nem szimmetrikus potenciálgödörben, harmonikus gerjesztéskor a
mozgása nem lesz harmonikus &rarr; felharmonikusok jelennek meg a sugárzásban

## Folyamatosan hangolható lézerek

- Vagy a vonalszélességen belül hangolható állítható, az interferencia elvén
  szelektáló optikai elemmel
- Vagy a gerjesztő közegnek van több közeli energia-átmenete.
- Vagy mint a festéklézereknél inkább energia sávok vannak mint diszkrét
  energia szintek, a hangolás optikai elemek távolságának, szögének áll0tásával
  végezhető el.

## Lidar jellemzők (légi és műholdas műszerek)

- UV-látható-NIR (250nm – 10 μm), kisebb sűrűségeknél veszíti el az áthatoló
  képességét (mint a MW)
- Általában a lézersugár nyílásszöge: &lt;1mrad
- Spektrális sávszélesség ~0.5nm
- Fix frekvenciák és többszöröseik, kivéve a hangolható lézereket, félvezető
  lézerek
- Repülőgépről (Airborne Laser Scanning, ALS), műholdról és a felszínről is
  használják
- Hullámforma és diszkrét visszaverődési pontok (waveform and discrete return)
- Nyers adat – Diszkrét pontfelhő – georeferencia a műszer pálya és állásszög
  alapján – feldolgozás TIN ( triangulated irregular network ), DEM – térképek
  (pl. erdőmagasság térkép)
- Légi LIDAR felbontása: 2-15cm függőlegesen, 25-100cm vízszintesen
- Működési paraméterek (ALS) 15000 pulzus/sec
- ALS a jövőben: 100000 pps, több hullámhossz, polarizáció - több információ a
  céltárgyról (anyagfajta azonosítás).

**Példa egy földi szkenner működési paramétereire (2016) - Egy hirdetésből:**
  
**Leica HDS P 40 Terrestrial Laser Scanner**
- Scan rate: Up to 1’000’000 points per second
- Range accuracy: 1.2mm + 10 ppm over full range
- Angular accuracy: 8′′ horizontal; 8′′ vertical (3.8E-5 rad)
- 3D position accuracy: 3 mm at 50 m; 6 mm at 100 m

**Cloudworx for AUTOCAD**  Software application that lets users take advantage
of rich 3D Point Clouds directly within CAD

## Légi Lidar mérések, Airborne Laser Scanning=ALS

Kétféle műszer használatos
1. Amely megőrzi a teljes jelalakot
2. Amely véges számú visszavert jelet rögzít

**A mérések főbb jellemzői:**  300-900m magasságból
- &sim;50000 impulzus/s
- 10cm/1000m körüli pontosság
- 10-40 pont/m<sup>2</sup>
- Gyorsan készíthető DTM

Feldolgozás:  3D pontfelhő szűrése, mi a földfelszíni pont, mi épület, fa...
Ezután háromszögháló a felszíni pontokból (TIN), ez a DTM alapja

**Felhasználások:**
- Topográfiai felmérések
- Lefolyási irányok meghatározása
- Geomorfológia
- Erdészeti alkalmazások, biomassza, faanyag-tömeg becslés
- Mezőgazdasági felhasználások, a DTM-ből kapható lejtőszögek, dőlésirányok és
  a vízmegtartó képesség becslésével (nincs lefolyás...)

### Erdészeti alkalmazások (Lidar)

- Meghatározható a szálmagasság, és a biomassza vertikális eloszlása
- A DTM az eróziót elkerülendő mérnöki munkákhoz ad segítséget, árkok, utak
- Az ágszerkezet vizsgálatával a száraz gallyak mennyisége is becsülhető lehet
  (tűzvédelem)

### DIAL, Differential Absorption Lidar

Két jel kibocsátása közeli frekvencián, egyik frekvencián nagyobb reflexió
&rarr; adott gáz elnyelési sávjában

Hangolható lézerrel az abszorpciós sávbeli és az azon kívüli visszavert jel
különbségéből becsülhető az iránymenti reflexió, ill a sűrűség.

Hangolható lézer:  Ti: Sapphire (Al2O3)  **Ti: Al<sub>2</sub>O<sub>3</sub>
lasers**  650-1100nm

Felhasználás:
- Légköri aeroszol és vízpára profilok  
- LASE kísérlet:
- 16-21km magasság
- 30, 40m felbontás, függ., vízsz.
- Nagy vízpára sűrűségnél már nem jó

### ICESat (Ice, Cloud, and Land Elevation Satellite) NASA, 2003-2009,
ICEsat-2: 2017

Geoscience Laser Altimeter System (GLAS)  Működése:
- 3 lézer berendezés egyszerre, 532nm és 1064nm. (az egyik nagyon korán
  tönkrement)
- 40 pulzus/sec, 70 m-es footprint 170m-enként.
- A felszín magasságának mérése + légköri profil a visszavert jelalakból.
- Pontos helymeghatározás: lézer reflektorok (LRA)
- Állásszög meghatározás: Csillag kamera (Star Tracker Reference system, SRS)

Feladat
- Elsősorban a sarki jégtakaró monitorozása
- Légköri aeroszol profilok

### Lidar-Radar közös v. egymást kiegészítő alkalmazások

- A légkörben az aeroszol, víz és jég részecskék eloszlása (Lidar kisebb
  sűrűségekre alkalmas), CALIPSO-CloudSat
- 3D terepmodellek (eltérő felbontás, és teljes terület nagyság)
- Mezőgazdasági, erdészeti alkalmazások, egyrészt DTM-lel kapcsolatban

### CALIPSO ÉS CLOUDSAT (kilövés: 2006.04.28) NASA (IIR: CNES)

#### CALIPSO nadír irányú műszerek
- CALIOP = Cloud-aerosol Lidar with Orthogonal Polarization: 1064nm és 532nm,
  az utóbbin kétféle polarizációval
- IIR: Képalkotó infravörös radiométer (CNES)
- Nagylátószögű kamera (MODIS 1 csatorna)

#### CloudSat CPR: Cloud Profiling Radar, mint a felszíni felhőradarok (94GHz)
- nadir irányú 1.85m-es antenna
- 94 GHz, mint a felszíni időjárási radarok
- 500m vertikális felbontás
- Felbontás 1.7km&times;1.4km (Along-,Cross track)
- PRF 4300Hz, pulzus-szélesség 3.3&mu;sec

Részei az A-Train-nek, más műholdakkal szoros konstellációban

**A-Train (Afternoon Train):** CALIPSO-Cloudsat-AQUA-AURA-PARASOL (15 percen
belül) CALIPSO-Cloudsat (15 másodpercen belül, 2012 &sim;1sec)

#### CALIPSO / CALIOP (Cloud-Aerosol LIdar with Orthogonal Polarization)

Nadír irányú műszerek
- Lidar: 1064nm és 532 nm, az utóbbin kétféle polarizációval
- Nd:YAG lézer (neodymium-doped yttrium aluminum garnet; Nd: Y<sub>3</sub>
  Al<sub>5</sub>O<sub>12</sub>)
- 0.45nm vonalszélesség
- +1 redundáns lézer transzmitter
- 1m-es vevő távcső
- FOV = 0.13mrad
- Felbontás 30-60m vertikális, 333m horizontális

**Tudományos célok:**  (adatgyűjtés az időjárás és klíma modellekhez)
- Az aeroszolok hatása a klímára és az időjárásra
- Az aeroszolok és felhők kölcsönhatása, csapadékképződés
- Milyen szerepük van az aeroszoloknak a légkör hőháztartásában?
- Mérés merőleges polarizációval &rarr; nem gömbszimmetrikus részecskék
  (jégkristályok) kimutatása

#### CLOUDSAT (JPL)

**CPR: Cloud Profiling Radar**
- nadir irányú 1.85m-es antenna
- 94 GHz, mint a felszíni időjárási radarok
- 500m vertikális felbontás
- Felbontás 1.7km&times;1.4km (Along-,Cross track)
- PRF 4300Hz, pulzus-szélesség 3.3μsec

**Tudományos célok:**
- Hogyan modellezhetők és milyen sugárzási tulajdonságai vannak a felhőknek
- Vertikális víz és jégeloszlás a felhőkben
- Csapadékképződés és a felhők viszonya
- Hóesés detektálása az űrből
- Az egyetlen műszer, amellyel megfigyelhető napi rendszerességgel a sarkok
  körüli csapadék

# Nem képalkotó bolygóvizsgálati módszerek

**Nem, vagy nem csak a felszín vizsgálata!**

## Elektromágneses hullámmérések

- Föld körüli űrtérség &rarr; geospace
- mérések/műholdak &rarr; mérési célokat tudni

### Felsőlégkör: a kezdet

Ionsűrűségek - Lunyik-2 (1959), in-situ  Elektronsűrűségek - whistlerek
(1957-58), távérzékelés

### ISEE 1 SFR

**International Sun-Earth Explorer 1: 1977**
- Epoch start: 1977-10-22 00:00:00 UTC
- Epoch stop: 1987-09-26 00:00:00 UTC
- Orbital Parameters
    - Periapsis: 1.0399999618530273 R<sub>E</sub>
    - Apoapsis: 23.0 RE
    - Period: 3556.800048828125 minutes
    - Inclination: 28.760000228881836&deg;
    - Eccentricity: 0.9100000262260437
- Regions Traversed
    - Bow shock
    - Magnetopause
    - Magnetotail
    - Plasmapause
    - Plasmasphere
    - Solar wind
    - Trapped particle belts
- SFR: 3 elektromos dipólantenna és egy 3 tengelyű search-coil keskenysávú vevő
  32 frekvencialépésben 5.62Hz-311kHz között

32 sec átlag
- UHR
- helyi plazmafrekvencia

UHR: ha &omega; &#8811; &omega;<sub>i</sub> és &omega; &#8811;
&omega;<sub>p</sub>  &omega;<sup>2</sup><sub>UH</sub> =
&omega;<sup>2</sup><sub>e</sub> + &omega;<sup>2</sup><sub>p</sub> &larr; *felső
hibridfrekvencia*  &omega;<sup>2</sup><sub>p</sub> = (n e<sup>2</sup>) &frasl;
(&epsilon; m)

&omega;<sub>UH</sub> &rarr; plazmaszféra modellek

### Polar PWI

Polar: 1996  1.8 - 9 R<sub>E</sub>; 86&deg; inklináció  n<sub>e</sub> =
n<sub>e0</sub> &sdot; { (*L* R<sub>E</sub>) &frasl; R }<sup>&alpha;</sup>

erővonal menti sűrűség modell, műhold kétszer metszett át egy erővonalat

### Image RPI

**Imager for Magnetopause-to-Aurora Global Exploration: 2000**
- 1.22 - 8.2 R<sub>E</sub> ; 89.42&deg; inklináció
- 854 perc keringési idő
- RPI: aktív kísérlet
- aktív EM jel kivocsájt &rarr; n<sub>e</sub> eloszlás mérése &rarr; modell

n<sub>e</sub>(*L*, &lambda;) = n<sub>e</sub>(*L*) {1 + &gamma; (&lambda;
&frasl; &lambda;<sub>inv</sub>) } &sdot; sec<sup>&beta;(*L*)</sup>(
(&pi;&alpha;&lambda;) &frasl; 2&lambda;<sub>inv</sub>)  n<sub>e</sub>(L) = A (B
&frasl; *L* &minus; 1)  &beta;(L) = C + D &sdot; *L*

### Image EUV

**Image EUV**  Nap EUV (30.4nm) sugárzásának  rezonáns szóródása a He + ionokon

EUV kép, egymás utáni képek &rarr; dinamika

30&times;84&deg; FOV 640&times;640km 8 R<sub>E</sub>-nél

### CLUSTER Wave Experiment Consortium

(Consortium = mérési csoportok)

Image: teljes magnetoszféra vizsgálata, Cluster: csak lokális vizsgálat

Cluster I - 1996. június 4.: Ariane-5 (Kouru), a 37. másodpercben felrobbant a
4 Cluster műholddal...  Cluster II. 2000. június 24. és július 16.: 2x
Szojuz-Fregat (Bajkonur): Salsa, Samba, Rumba és Tango  WEC: Wave Experiment
Consortium (DWP, EFW, STAFF, WBD, and WHISPER)

Diameter: 2.9 m  Height: 1.3 m  Mass: 1200 kg  (of which) Propellant: 650 kg
(of which) Scientific payload: 71 kg  Solar array power: 224 W  Spin rate: 15
rpm  Operational lifetime: 5 years (nominal)

*In- situ mérések!*  WBD: Wide Band Data – 25Hz-577kHz elektromos és mágneses
antennák  WHISPER (Waves of HIgh frequency and Sounder for Probing of Electron
density by Relaxation): 2- 80kHz elektromos antenna

**EDI Onboard CLUSTER**  EDI measures electric fields at the in situ spacecraft
location (Paschmann et al.  2001). Electronbeams with an energy of 1 keV (and
500 eV for a small number of cases) are emitted from two pairs of guns in the
direction perpendicular to the ambient magnetic field. Electron beams
subsequently experience cyclotron motion and drift motion, and fractions of the
beams return to two pairs of detectors. Drift motions include both
**E**&times;B and &nabla;**B** components, although the latter contribution is
much smaller at the above beam energies in the inner magnetosphere. CLUSTER EDI
actually measures drift step length during approximately one or multiple
gyroperiods by triangulation and/or time-of-flight methods. Here we try to
determine two perpendicular components of the electric field from this drift
step ength.


### GPS TEC

**Ionoszféra- plazmaszféra integrált elektronsűrűségek**

GPS jel &sim; 1 GHz, érzékeny &larr; milyen elektronsűrűségű tartományon
halad át &rarr; integrált n<sub>e</sub>-t tudok mondani

TEC = (1 &frasl; 40.3) &sdot; { (f<sub>1</sub> f<sub>2</sub>) &frasl;
(f<sub>1</sub>&minus;f<sub>2</sub>) } &sdot;
(P<sub>2</sub>&minus;P<sub>1</sub>)  TEC is measured in unit (TECU) of
10<sup>16</sup> electrons per m<sup>2</sup>  P<sub>2</sub>, P<sub>1</sub>:
pseudorange

### Radiation Belt Storm Probes Van Allen Probes

Mass: &sim;1500 kg for both

Orbital elements:  Inclination &sim;10&deg;  Apoapsis &sim;5.8 Earth Radii
Periapsis &sim;700 kilometers  Orbital period &sim;9 hours  

- Sugárzási övek nagyenergiájú részecskei (fluxus)
- plazmaszféra elektronsűrűségek
- mágneses tér

**EMFISIS Instrument Suite:** Tri-axial Magnetometer (MAG)  MAG is a tri-axial
fluxgate magnetometer: Vector B, DC-15 Hz, 0.1 nT accuracy, three sensors on
rigid boom.

WAVES, a tri-axial search coil magnetometer and sweep frequency receiver.
Waves Components:

**Magnetic field** - vector B  10 Hz-12 kHz  sensitivity: 3&times;10
<sup>&minus;11</sup> nT<sup>2</sup>Hz<sup>&minus;1</sup> @ 1 kHz  3 sensors on
rigid boom

**Electric field** - spin-plane E  10 Hz-12 kHz (vector)  10 kHz-400 kHz
(single channel)  sensitivity: 3&times;10-17 V<sup>2</sup>m
<sup>&minus;2</sup>Hz<sup>&minus;1</sup> @ 1 kHz  100m tip-to-tip (spin plane),
14m (spin axis)

### És ami kimaradt:


- DE-1, Active (SAS), Compas-2 (SAS-2), Magion, Geotail, CRRES, DEMETER
- magnetopauza, fejhullám
- stb.

## Részecske mérések

- a felsőlégkörben a dinamika nagy részét a részecskék adják 
- napszélből, kozmikus sugárzásból, gyorsítási folyamatokból
- Elsősorban: Ion (H<sup>+</sup>, He<sup>+</sup>, He<sup>++</sup>, és
  O<sup>+</sup> ... Ni), elektron +semleges részecskék (Kozmikus sugárzás,
  Napból származó ionok, a Föld magnetoszférájában a napszél-magnetoszféra
  kcsh.-ban résztvevő részecskék, plazmaösszetevők az ionoszférában (szeizmikus
  kapcsolat)
- Azonos részecskék energiaeloszlása, sebességi irányeloszlás, esetleg
  hőmérséklet
- Ionok tömeg szerinti eloszlása, könnyű és nehezebb ionok.
- töltött és semleges rész &rarr; energia és szögszerinti eloszlás

Példák mérésekre, műszerekre
- Cluster műholdak (ESA)
- SAMPEX (NASA)
- Demeter (CNES)
- Van Allen Probes (NASA)

**Girorádiusz függése az részecske kinetikus energiájától**

R = (mv) &frasl; (eB)  m = m<sub>0</sub> &frasl; {1&minus; (v<sup>2</sup>
&frasl; c<sup>2</sup>)}<sup>1 &frasl; 2</sup>  E = (m - m<sub>0</sub>) &sdot;
c<sup>2</sup> &larr; *kinetikus energia*  R = { ( (E &frasl; c<sup>2</sup>) +
m<sub>0</sub> ) &sdot; v } &frasl; (eB)  v &#8810; c &rarr; R&sim;E<sup>1
&frasl; 2</sup>  v &cong; c &rarr; R&sim;E

kT&asymp;0.5 eV, (T=6000K)

### A CLUSTER holdak Cluster-2 (2000)

- Holdak közötti távolságok néhány 100km-től több 1000km-ig beállíthatók
- Négy egyforma műhold: Samba, Salsa, Rumba, Tango (C1,C2,C3,C4)
- 20&times;120 ezer km a pálya, 57 óra periódusidő
- Forgás: 15 rpm (1 fordulat=4s)

Részecske kísérletek:
- CIS, CLUSTER ion spektroszkópia
- PEACE (**P**lasma **E**lectron **A**nd **C**urrent **E**xperiment)
- RAPID (**R**esearch with **A**daptive **P**article **I**maging **D**etectors)

A Cluster sikere után:  Magnetospheric Multiscale Mission (MMS) (NASA)
&sim;2014  Radiation Belt Storm Probes - Van Allen Probes (RBSP) 2012

**CIS, CLUSTER ionspektroszkópia kísérlet, mérések**

- 3D Ioneloszlás 4 másodpercenként (1 fordulat ideje)
- **HIA** ( Hot Ion Analyser ) 5 eV-32 keV
- **CODIF** (COmposition and DIstribution Function analyser) (H<sup>+</sup>,
  He<sup>+</sup>, He<sup>++</sup>, és O<sup>+</sup> ionokat észlel), 22.5&deg;
  szögeloszlásban
- +DPS rendszer a fedélzeti feldolgozáshoz

Tudományos célok:
- Időben és térben megfigyelni a napszél-magnetoszféra kölcsönhatás jelenségeit
- Magnetoszféra dinamikája
- A magnetopauza és a lökéshullám-front (fejhullám, bow shock) fizikai
  jelenségei
- Kis energiájú ionok az ionoszférából
- A napszél és földi mágneses tér kapcsolódási pontjai és a plazmaáramok
  körülötte

#### HIA, (Hot Ion Analyser)


Mérési tartomány: 5 eV/e-től 32 keV/e, csak ion energiát mér, fajtát nem
Elsődleges célja a napszélbeli ionáramlások vizsgálata  Dupla félgömb ion
deflektor, középen kör alakú nyílással  Bal oldalon csökkentett apertúra (arány
~25) a nagy fluxusok mérésére  Nagyfeszültségek alkalmazása sárga nyilaknál,
(sweep: 0.7-4800V, 64-szer fordulatonként)

MCP **(Microchannel plate detector)** - mikrocsatornás lemez

Úgy működik mint a fotoelektron-sokszorozó (PM Photo Multiplier) csövek
- A lemez anyaga szigetelő, a felületeken elektródák
- Gyors
- dupla lemezzel nagy erősítés érhető el ua. feszültséggel

#### HIA-2

napszél irányban jobb szögfelbontás

A HIA érzékelő anódok 2D szektorbeosztása  

Bal oldalon a nagyobb érzékenységű félkör kisebb szögfelbontással (11.25 &deg;)  

Azimut irányban 64 mintavétel készül fordulatonként (5.625&deg;)

Jobb oldalon a kis érzékenységű félkör, 45 fokos tartományon belül dupla
szögfelbontással a napszél plazmanyalábok tanulmányozására

#### A CODIF műszer

COmposition and DIstribution Function analyser  energiatartomány: 0.02eV-38
keV/töltés H<sup>+</sup>, He<sup>+</sup>, He<sup>++</sup>, és O<sup>+</sup>
Kétoldalt itt is különböző apertúra (100-as faktor)

RPA (Retarding Potential Analyser), speciális apertúraoptikával kiválasztja a
kis energiájú ionokat majd 100eV-tal gyorsítja őket, úgy a műszer megfelelő
méréstartományába kerülnek

TOF, time-of-flight  Spektrum egy adott energiaszinten

A beeső ionok a "C" fólián áthaladva elektront szabadítanak ki (energiájuk
némileg csökken), az elektron az erősítő bal oldalán áthaladva triggereli a
"start" jelet, az ion a jobb oldalon áthaladva triggereli a stop jelet.  Az
időkülönbségből számítható a sebesség és ebből visszaszámítható az eredeti
ionsebesség. Ebből és az energiából tömeg számolható.

#### Cluster, PEACE

- Alacsony és közepes energiájú elektronok irány szerinti vizsgálata (0.7eV-30
  keV)
- Két érzékelő (LEEA, HEEA, Low|High Energy Electron Analyser), a hold
  ellentétes oldalán, mindkettő teljestérszögben érzékel a forgás során
- Összesen 88 energiaszintet tudnak mérni.
- A Double Star (ESA-CNSA) misszió része is, a kínai holdakon (ekvatoriális és
  poláris holdak) is van PEACE
- Alap üzemmódban LEEA: 0.7eV-1keV, HEEA: 30eV-26keV
- Poláris szögfelbontás: 15&deg;
- Azimutálisan 3 lehetőség: 6,11,22&deg; a mért energiaszintek száma csökken a
  szögfelbontás javulásával

#### PEACE elektron spektrogramm

Magnetoszféra - mágneses burok átmenet a nappali oldalon, az előbbi ritkább, de
energikusabb elektronokat tartalmaz.

FTE-k (Flux Transfer Event) figyelhetők meg ahogy a holdak a lepel felé
tartanak.

MP- magnetopauza

#### RAPID (Research with Adaptive Particle Imaging Detectors)

- A KFKI részt vett a fejlesztésében
- 20 keV- 400keV elektron és 40keV-1.5 MeV ion energia, tömeg és szögeloszlás
- Két részből áll elektronok és ionok mérésére
- IIMS (imaging ion mass spectrometer), TOF (time of flight) és energia mérés
  adja a tömeget
- IES (imaging electron spectrometer)
- Képes nagyenergiájú neutrális részecskék detektálására is

MCP collimátorok  Köztük eltérítő feszültség (0-10kV), kizárandó a kis
energiájú ionokat és megkülönböztetendő a semleges részecskéket az ionoktól

### SAMPEX Solar Anomalous and Magnetospheric Particle EXplorer , NASA - Max
Planck Institute

- 1992, pálya: 512x687km (LEO=Low Earth Orbit), i=82&deg;
- 2004.06.30,
- 2012.11.13. megsemmisül az atmoszférában.
- LICA Low Energy Ion Composition (He-Ni) Analyser (0.5-5MeV, &lt;60AMU)
- HILT, Heavy Ion large Telescope (8 - 300MeV, He, C, O, Ne, Fe)
- MAST, MAss Spectrometer Telescope (Z=2..28, He-Ni, 10-n&times;100MeV/nukleon)
- PET, Proton-Electron Telescope, e<sup>&minus;</sup> : 0.5-30 MeV; H, He: 20 -
  200 MeV
- Kozmikus sugárzás (GCR, ACR, Galaktikus és Anomális kozmikus sugárzás)
- SEP, nagy energiájú részecskék a Napból (0.1-20 MeV/nuc)
- A napszélből befogott elektronok a magnetoszférában
- Magnetoszferikus vizsgálatok, nagy időbeli felbontás, a szélesség nagy
  tartományát bejárja a poláris pálya miatt

#### SAMPEX/LICA

(Low Energy Ion Composition Analyzer)

- Time-of-flight tömegspektrométer, iontömeg, -energia , beérkezési irány
  mérése
- 0.5-5MeV/nukleon energiatartományban (alacsony energiákon az összetétel
  pontosabban meghatározható, összetétel &rarr; ionok származási helye)
- Az MCP-k mögötti anódok megjegyzik az elektronfelhő kilépési helyét, ebből a
  fóliákon való áthaladások helye kalkulálható

#### SAMPEX MAST kísérlet

- Szilícium félvezető detektoros távcső, méri a részecske töltetését (Q)
  tömegét (M) és kinetikus energiáját (E)
- Izotópösszetétel (He-Ni, Z = 2-28)
- Napból származó nagy energiájú (15-250 MeV/nukleon) ionok (Z&gt;5) mérése \-
  korona összetétele

Nyugodt Nap esetén kozmikus sugárzás mérése: GCR + ACR

M1-M4, hely érzékeny detektorok, belőlük származik irány információ  Az
energiaveszteség-megtett távolság modellek alapján számolhatók az E,M,Q
paraméterek  Az pontosság M-ben &sim;0.2amu.

#### SAMPEX/PET

- Proton-Electron Telescope, e<sup>&minus;</sup>: 0.5-30 MeV, H,He: 20-200 MeV
- P1-P8 szilícium detektorok, vastagság 2-15mm
- A4-A8 gyűrű alakú szélső detektorrészek, amelyek az oldalfluxusokat kezelik
- Az egyes detektorokból és széldetektorokból jövő jelek kombinációjából és az
  elektron és az ionok távolság-energiaveszteségi karakterisztikáiból
  azonosíthatók a töltött részecskék (az elektronok nagyobb mélységbe képesek
  behatolni a detektorokba)
- Elsősorban könnyű ionok mérésére alkalmas, de nagyobb erősítéssel nehezebb
  ionok is észlelhetők
- 6 másodperces intervallumokban összegzi a különböző energiaszinteken a az
  események számát

### Demeter (Detection of Electro-Magnetic Emissions Transmitted from
Earthquake Regions)


- Fellövés: 2004 június, mikroműhold ~100kg 
- 2010 december
- 710km pálya, i=98&deg; (=napszinkron)
- Cél: ionoszferikus változások megfigyelése szeizmikus aktivitás illetve
  emberi tevékenységek nyomán
- Általában információgyűjtés a föld elektromágneses (és plazma) környezetéről

Részecske mérések:
- **IAP:** ionsűrűség, hőmérséklet és sebesség a főbb ionokra vonatkozóan:
  H<sup>+</sup>, He<sup>+</sup>, O<sup>+</sup>
- **IDP:** nagy energiájú elektronspektrum mérése( 70keV-2.5MeV). A belső
  sugárzási öv elektron energiaszerkezete, A VLF adók és a rezonáns
  elektronpopulációk kapcsolatát mutatta ki

#### Instrument d’Analyse du Plasma (IAP)

- Gyenge zavarok detektálása az ionoszférában a termális ionpopuláció
  folyamatos mérésével
- A plazma állapotának vizsgálata, hogy a hullámmérésekhez kiegészítő
  információval szolgáljon
- Két egyirányba, a műhold sebességvektora irányába néző műszer kombinációja:
  APR retardált potenciál műszer, energiát mérve változtatva a visszatartó
  potenciálját, a főbb ionokra sűrűséget, hőmérsékletet és apertúrairányú
  sebességet mér.
- ADV ion driftsebesség mérő

#### APR

- retardált potenciál &rarr; fékező potenciál, kisebb energiájú részecskék
  mérésére
- APR retardált potenciál műszer, energiát mérve változtatva a visszatartó
  potenciálját (VGR), a főbb ionokra (H+, He+, O+) sűrűséget, hőmérsékletet és
  apertúrairányú sebességet mér.
- G3-G4 feszültség változik (sweep), a felső határon visszatart minden iont és
  a háttérzaj becsülhető
- G6 visszatart kis energiájú elektronokat (foto elektronok, szupratermális
  elektronok)

#### IDP: nagy energiájú elektronspektrum mérése(> 70 keV).

- Elektronfluxus mérése a 70-2500keV energiatartományban
- A detektor a pályasíkra merőlegesen néz, 90&deg;-ban beeső elektronokat
  detektálja.
- A bejövő jelet 256 energiaosztályra bontja (10 keV felbontás)
- A detektorban elnyelt energia kb 800keV-ig azonos a részecske energiájával.
  Nagyobb energiáknál a hatásfok csökken, evvel korrigálni kell.
- Belső sugárzási övből kicsapódó elektronok, rezonanciacsúcsok földi VLF
  adókkal kapcsolatban

### Radiation Belt Storm Probes Van Allen Probes

- Sugárzási övek nagyenergiájú részecskei (fluxus)
- plazmaszféra elektronsűrűségek
- mágneses tér

# Villámok, RS technikák

**Sztratoszféra:**  A légköri kisülések / villám (-aktivitás)
- a semleges légkör meghatározó izikai jelensége,
- globális változás egyik direkt mérőszáma (Nap, földi sugárzási mérleg, hőm.
  és páratartalom, aeroszolok)
- összetett jelenségkör gyűjtőneve – több, mint a kisülés maga

elektromos kisülés &hArr; fény / hang / e.m. impulzus / kémiai reakciók / hő

## Miért észleljük, követjük, vizsgáljuk a villámokat?  pl.
- zivatarkövetés, extrém csapadék
- kiemelten repülésbiztonság (CN)
- biztosítók (épületkárok, erdészet)
- közmű-, inf.- hálózatok fenntartása
- **tud. alkalmazások**

Miért RS?  harangozók... B.Franklin, villámhárító

CG: stepped leader (elővillám, "előlépegető" villám),  CC: breakdown streamer
(csat. Ioniz.), **return stroke (lecsapó villám)**

detektálás: féynfelvillanás regisztrálása, OTD, LIS (felhő eltakarhatja)

*átlagos* jellemzők RS megigyelésekből:  
- vezető csatorna átmérő &sim;5 cm
    - ionizált gáz, izzó plazma
- hőmérséklet &sim;30 000 K
- áram &sim;30-200 kA
- teljesítmény 10<sup>8</sup> &sim; 10<sup>10</sup> W
- élettartam &lt; 100 &mu;s (cc: 1-2 s)
- kisülési csatorna hossz &sim; 3 km
- sebesség &sim; 0,1 C (30 000 km/s)
- energia &sim;6&times;10<sup>8</sup> J
- cellatérfogat &sim;3 000 km<sup>3</sup>

Trópusok: hőmérséklet különbség Szárazföldön alakul ki, kivéve pl.
Golf-áramlás; óceáni hőmérséklet egyenletesebb

## Optikai, Műholdas

OTD  Orbview/Microlab-1 satellite  1995-től,  **70&deg;**, LEO Apogee: 706 km,
Perigee: 696 km

LIS  Tropical Rainfall Measuring Mission (TRMM), NASA-JAXA, 1997-től,
**35&deg;** [honlap](http://trmm.gsfc.nasa.gov/)

globális jellemzők: &sim;2000 aktív zivatarfelhő, &sim;45 villám/sec

## Földi villám detektálás – elektromos/mágneses tér mérés

A villám intenzív, szélessávú e.m. jelforrás.

- spektruma DC - VHF, maximuma **VLF &sim;10 kHz**
- VHF terjedés kevésbé frekvencia függő, egyenes úton terjed
- Föld-ionoszféra hullámvezető (EIWG), veszteséges falú gömbhéj
- ULF - kismértékű csillapítás, globális hatás; VLF-ben 6-10000 km; HF-VHF
  &lt;2-300 km
- &sim;0.5 ms hosszú impulzus (150km)
- A jelalak villám típustól, kisülési csatorna szerkezetétől, stb., irreguláris
  módon függ, és terjedés során torzul

National Lightning Detection Network - USA  
Global Lightning Network - GLN  
akár 50 jel is érkezhet  másodpercenként - összepárosítás?, koincidencia?

## Nagyfrekvenciás, regionális villám detektorok

- VHF, szabadtéri terjedés, egyenes terj. út
- direkt rálátás, 2D, 3D, pontos, nagy hatásfokú, költséges
- DF (interferometria), TOA (állomáspárok, időkül., hiperbolák metszete, 4
  áll.)
- kis hatósugár, sűrű (50-200km) hálózat, jell. országos lefedettséggel
- impulzus hossz, jelalak/burkoló jellemzők, kisülés típus

## VLF, globális villám detektor hálózat – WWLLN.net

- akadémiai intézmények együttműködése
- globális hálózat
- szélessávú VLF adatsoron TOA, realtív áramerősség, hely/idő koord.
- nagy hatósugár, ritka (500-2000km) hálózat, glob lefedettség, nem egyenletes
- kis költség, kis (30-40%) hatásfok &larr; villámok többször körbemennek

## Űridőjárási kutatások: földi mérések – whistlerek

- A Föld plazmakörnyezete előmágnesezett, anizotróp plazma &rarr; diszperzív
  közeg
- villám rövid impulzusa szélessávú (UWB) gerjesztés &rarr; whistler

- t(f) = (2c)<sup>&minus;1</sup> f <sup>&minus; 1 &frasl; 2</sup>
  &int;<sub>S</sub> (f<sub>p</sub> f<sub>H</sub>) &frasl; (f<sub>H</sub>
  &minus; f) <sup>3 &frasl; 2</sup> d*s*

## Űridőjárási kutatások: földi mérések – az AWDANet

1.  Orrferkvencia
2.  Diszperzió  1 + 2 &rArr; hol & mi  *hol* terjedt a whistler a
plazmaszférában  *mi* volt ott  (mekkora volt a plazmasűrűség)  &rArr;
Űr-időjárási modellek kulcs-paramétere

GOES-16: Geostationary Lightning Mapper

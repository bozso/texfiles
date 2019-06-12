\include{html.gpp}

\define{\vu}{\mat{u}}
\define{\vg}{\mat{g}}
\define{\vn}{\mat{n}}
\define{\vm}{\mat{M}}
\define{\vh}{\mat{M}}
\define{\vj}{\mat{j}}
\define{\vb}{\mat{B}}
\define{\vt}{\mat{T}}
\define{\vh}{\mat{H}}
\define{\vz}{\mat{Z}}
\define{\ve}{\mat{e}}
\define{\vomega}{\mat{\Omega}}
\define{\mRe}{\text{Re}_{\text{m}}}

\define{\dim{one}{two}}{\frac{\text{\one}}{\text{\two}}}


\h2{Kőzetek mágnesezhetősége, szuszceptibilitás}


\ul{
    \li{mágneses szuszceptibilitás:}
    $$ \vm = \chi_v \vh $$
    $$ \vb = \mu_0 (\vm + \vh) = \mu_0 (1 + \chi_v) \vh = \mu_0 \mu_r \vh $$
    \li{mag körüli elektron &rarr; elemi köráram, saját és pályamomentum,
        spin mágneses momentum}
    \li{\em{diamágneses anyagok:} lezárt héj, elektronok ellentétes spinű
        párokban, mágneses momentum az elektronok pályamomentumából; külső
        térben indukált mágneses momentum; kvarc, gipsz, földpát; $\chi_v < 0$}
    \li{\em{paramágneses anyagok:} mágneses momentum elektronpálya és spinből;
        random elhelyezkedés &rarr; kioltják egymás terét; külső mágneses tér
        &harr; hőmozgás; piroxén, olivin; $\chi_v > 0$}
    \li{\em{ferromágneses anyagok:} lezáratlan alhéj, spin saját mágneses
        momentum, vascsoport elemeiben kvantummechanikai kicserélődés &rarr;
        spinek párhuzamosan állnak be; \em{Curie-hőmerséklet} felett
        paramágnessé válnak; magnetit, hematit, wüstit; $\chi_v \gg 1$}
}

\h2{Lokális koordinátarendszer}

\ul{
    \li{x-tengely: földrajzi észak}
    \li{y-tengely: földrajzi kelet}
    \li{z-tengely: helyi függőleges iránya}
}

\ul{
    \li{$\vt = \vh + \vz$}
    \li{$\tan{I} = \frac{Z}{H}$}
    \li{dipólusegyenlet: $\tan{I} = 2 \cot{\theta}$, $\theta$: pólustávolság}
    \li{egynlítőn: $H \approx 30 000 \text{nT}$, póluson: $Z \approx 60 000 \text{nT}$}
    \li{mágneses egyenlítő: $I = \deg{0}$, mágneses pólusokon: $I = \pm \deg{90}$}
}

<p><a href="https://commons.wikimedia.org/wiki/File:XYZ-DIS_magnetic_field_coordinates.svg#/media/File:XYZ-DIS_magnetic_field_coordinates.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/XYZ-DIS_magnetic_field_coordinates.svg/1200px-XYZ-DIS_magnetic_field_coordinates.svg.png" alt="XYZ-DIS magnetic field coordinates.svg"></a><br>By <a href="//commons.wikimedia.org/wiki/User:Chym%C3%A6ra" title="User:Chymæra">Chymæra</a>
Recreated in <a href="https://en.wikipedia.org/wiki/LaTeX" class="extiw" title="w:LaTeX">LaTeX</a> by: <a href="//commons.wikimedia.org/wiki/User:Krishnavedala" title="User:Krishnavedala">Rubber Duck</a> (<a href="//commons.wikimedia.org/wiki/User_talk:Krishnavedala" title="User talk:Krishnavedala">☮</a> • <a href="//commons.wikimedia.org/wiki/Special:Contributions/Krishnavedala" title="Special:Contributions/Krishnavedala">✍</a>) - <span class="int-own-work" lang="en">Own work</span>
Metadata for the image was published at the <a rel="nofollow" class="external text" href="http://r.chymera.eu/items/show/2">Chymera Network Resources</a>. An up-to-date version of the file can be found <a rel="nofollow" class="external text" href="http://dl.dropbox.com/u/58490933/selfmade-pics/educational/idst.svg">here</a> ., <a href="https://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=19810392">Link</a></p>

\h2{Földi tér leírása}

\ul{
    \li{centrális axiális dipól: $\vt(r, \theta) = - \frac{\mu_0}{4\pi}
                                  \frac{m_d}{r^3} \left(2\cos\theta \ve _r
                                  + \sin\theta \ve _{\theta} \right)$}
    \li{nem centrális és/vagy nem axiális dipól, $\approx \deg{10}$ a földrajzi észak
        és a dipól }
    \li{dipól: földmágneses pólusok, egyenlítő}
    \li{Gömbi harmonikus sorfejtés:}
    $$ W(r,\theta,\lambda) = a \sum_{n=1}^{+\infty} {\left( \frac{a}{r}\right)}^{n+1}
     \sum_{m = 0}^{n} (g_n^m \cos m\lambda + h_n^m \sin m \lambda)P_n^m(\cos\theta)$$
}


\h2{Földi tér belső eredete: Áramlás a külső magban}

\ul{
    \li{szinte ugyanazon egyenletrendszer írja le mint a köpenyben zajló áramlást}
    \li{két lényeges különbség:}
    \ol{
        \li{külső mag vizkozitása többb mint 20 nagyságrenddel kisebb,
            viszkózus erő jelentősége sokkal kisebb, Coriolis-erőé sokkal
            jelentősebb}
        \li{fémes összetétel &rarr; elektromos és mágneses hatások,
            Lorenzt-erő és MHD}
    }
}

\h3{Alapegyenletek}

\ul{
    \li{Boussinesq-approximáció, sűrűség mindenhol konstans kivéve a termikus
        felhajtóerőben, ahol a hőmérésklettől függ}
    \li{állandó modellparaméterek: $\mat{\Omega}$, $\vg$, $\alpha$, $c_p$,
        $K$, $\sigma$, $\eta$, $\eta^* = \inv{(\mu \sigma)}$
        a mágneses diffuzivitás}
}

\ol{
    \li{Kontinuitási egyenlet}
    $$ \nabla \vu = 0$$
    \li{Navier-Stokes egyenlet}
    $$ \rho_0 \der{\vu}{t} = - 2 \rho_0 \cross{\vomega}{\vu} + \rho(T) \vg
                             - \nabla p + \eta \laplace \vu + \cross{\vj}{\vb} $$
    \li{Hőtranszport egyenlet}
    $$ \rho_0 c_p \der{T}{t} = K \laplace T + H $$
    \li{MHD alapegyenlet}
    $$ \par{t} = \rot{(\cross{\vu}{\vb})} + \eta^* \laplace \vb $$
}

\ul{
    \li{diffúzió nélkül &rarr; mágneses erővonalak befagyása}
    \li{advekció nélkül &rarr; mágneses tér expnenciális lecsengése}
    $$ \tau = \mu \sigma L^2 \pow{\pi}{-2} $$
    $$ \sub{\tau}{Föld} \approx 24000 \text{yr} \cdot \mu_r $$
    \li{\b{Figyelem!} A vas relatív mágneses permeabilitása akár $\pow{10}{3}$
        nagyságrendet is változhat!}
    \li{szükséges még egy egyenlet, az állapotegyenlet:
        $\rho(T) = \rho_0 (1 - \alpha \delta T)$}
}

\h4{Dimenziótlan egyenletek}

\ul{
    \li{Busse-féle közelítés, $\rho = \rho_0$ mindenhol}
    \li{redukált nyomás: $\tilde{p} = p \inv{\rho_0} + W$, $\vg = - \nabla W$}
    \li{karakterisztikus mennyiségek}
    \ul{
        \li{$L$: külső mag sugara}
        \li{$U$: külső magban lévő áramlás karakterisztikus sebessége}
        \li{$\Omega_0$: Föld forgási szögsebessége}
        \li{$B_0$: külső mag mágneses térerejének karakterisztikus nagysága}
    }
    \li{dimenziótlan számok becslése}
    \ul{
       \li{$U$: nondipóltér nyugati driftje, $\deg{0.2}\inv{\year}$ &rarr;
           $\si{4}{\milli\meter\inv{\second}}$}
       \li{$B_0$: dipoltér nagysága távolság köbével csökken &rarr;
           $\si{\sci{2.5}{-4}}{\text{nT}}$}
    }
}

\center{
<table>
    \tr{
        \th{Dimenziótlan szám}
        \th{Mit mér?}
        \th{Nagyságrendje a köpenyben}
    }
    \tr{
        \td{$\text{Ro}$: Prandtl-szám}
        \td{$\dim{inercia erő}{Coriolis-erő}$}
        \td{$\pow{10}{-6}$}
    }
    \tr{
        \td{$\text{Ek}$: Ekman-szám}
        \td{$\dim{viszkózus erő}{Coriolis-erő}$}
        \td{$\pow{10}{-15}$}
    }
    \tr{
        \td{$\text{El}$: Elsasser-szám}
        \td{$\dim{Lorentz-erő}{Coriolis-erő}$}
        \td{$0.04$}
    }
    \tr{
        \td{$\mRe$: mágneses Reynolds-szám}
        \td{$\dim{mágneses advekció}{mágneses diffúzió}$}
        \td{$875 \mu_r$}
    }
</table>
}

\ul{
    \li{Külső magban az inercia és viszkózus erő elhanyagolható a
        Coriolis-erőhöz képest}
    \li{két féle közelítés}
    \ol{
        \li{erős tér modellek, $\text{El} \ne 0$, mágneses tér Lorentz-erőn
            keresztül befolyásolja az áramlást}
        \li{geynbge tér modellek, $\text{El} = 0$}
    }
    \li{további vizsgálatok - gyenge tér modell, három dimenziótlan szám kicsiny}
    $$ 2 \cross{\vomega}{\vu} = - \nabla \tilde{p} $$
    \li{Taylor-Proudmann-tétel}
    $$ (\vomega \nabla) \vu = 0 $$
    \li{ha $\vomega = (0, 0, \omega_0) \rightarrow \par{z} w = 0$}
}


Dimenziótlan MHD egyenlet:
\ul{
    $$ \par{t} \vb = \rot{(\cross{\vu}{\vb})} + \inv{\mRe} \laplace \vb $$
    \li{új dimenziótlan szám}
    $$ \mRe = \sigma \mu L U $$
    \li{kritikus $\mRe \approx 10$}
}

\h3{Ekman-határréteg szerepe}

\ul{
    \li{korábban láttuk: $\par{z} \vu = 0$}
    \li{külső magot minden oldalról több nagyságrenddel nagyobb viszkozitású
        közeg határól, határok merevek &rarr; nincs áramlás &rarr; külső
        magban nincs áramlás}
    \li{Ekman-szám kicsi &rarr; súrlódás elhanyagolható, határokhoz közel nem
        igaz &rarr; Ekman-határréteg}
    \li{egyszerű 2D model, alsó határ merev, ott nincs áramlás, alsó határtól
        távol geosztrófikus}
    \li{$\delta$ vastagságú Ekman-rétegben + inkompresszibilis, izoviszkózus,
        newtoni reológiájú súrlódási tag, $\text{Ek} \approx
        \sqrd{\delta}\pow{L}{-2} \rightarrow \delta \ll L$, Ekman-réteg vékony!}
    \li{redukált nyomás változása elhanyagolható $\tilde{p} = \tilde{p}_0$}
    \li{vertikális változások dominálnak}
    \li{határ közelében akkor is van $y$ irányú sebesség ha a geosztrófikus
        tartományban nem, áramlás irány nagysága eltér a geosztrófikustól}
    \li{a határrétegben az áramlás $\deg{45}$-os szöget zát be a
        geosztrófikussal}
    \li{határrétegben van sugár irányú sebességkomponens, tömegmegmaradás
        miatt ha befelé áramlik az anyag az oszlop belsejében fel kell
        emelkednie}
    \li{ha a Taylor-oszlop forog és létezik határréteg &rarr; oszlop
        belsejében lézetnie kell vertikális áramlásnak (felfele vagy lefele
        forgásiránytól függően), Ekman-pumpálás}
}

\imref{https://cdn.iopscience.com/images/books/978-0-7503-1052-9/live/bk978-0-7503-1052-9ch6f1_online.jpg}


\h3{Kvalitatív értelmezés}

\ul{
    \li{ha földforgás nem lenne, köpenyszerű cellás áramlás, de sokkal
        hevesebb, szükséges hőméréskletkülönbség: szekuláris hő - melegebb
        belső mag, hidegebb köpeny}
    \li{vas inkompatibilis urániummal, tóriummal, nem lehet jelentős a
        radioaktív hőtermelés; külső mag kifagyása &rarr; fűtés (látens hő)}
    \li{földforgás figyelembe vétele: Taylor-oszlopok, belső magot hűtik}
    \li{Ekman-határréteg figyelembe vétele: vertikális áramlás is &rarr;
        csavart áramlás \em{(helikoidális áramlás)}, felcsavarja a plazmába
        fagyott erővonalakat, Glatzmaier-Roberts-féle mágneses dinamó modell}
    \li{köpeny és külső mag áramlás kapcsolatban van, CMB hőárameloszlások
        segíthetik, vagy hátráltathatják a pólusfordulást illetve
        stabilizálhatják a külső magban zajló áramlást}
}

\h2{Mágneses obszervatóriumok}

\ul{
    \li{földi mágneses tér összetevőinek időbeli változásának mérése}
    \li{kb. 1930-as évektől, Magyarországon: a Tihanyi és
        nagycenki Széchenyi István Geofizikai Obszervatórium}
    \li{variációs műszerek mágneses tér időbeli változása, relatív műszerek}
    \li{variációs műszerek kalibrálása: abszolút műszerekkel,
        obszervatóriumok közötti összeméresre szolgáló relatív műszerekkel}
    \li{alapelv: mgánestűre a mágneses tér forgatónyomatékot gyakorol}
    \li{komponensek, inklináció, deklináció mérése}
}

Történelmi áttekintés
\ul{
    \li{Tihanyi obszervatórium - 1955}
    \li{Széchenyi István Geofizikai Obszervatórium - 1957}
    \li{Konkoly Thege alapította (1871) ógyallai Csillagviszgáló és Meteorológiai,
        Geofizikai Intézet, Osztrák-Magyar Monarchia
        első vidéki obszervatóriuma (1900)}
}
\include{html.gpp}

\define{\vp}{\mat{p}}
\define{\vu}{\mat{u}}

\define{gdiv_u}{\gdiv{\vu}}

\define{\vr}{\mat{r}}
\define{\vk}{\mat{k}}

\define{\mdef}{\mat{\varepsilon}}

\h2{Bevezetés}

\ul{
    \li{földrengések regisztrálása, Föld belső szerkezetének meghatározása}
    \li{földrengés komoly veszélyforrás, emberi életek}
    \li{legnagyobb történelmi földrengés: Lisszabon (1755); &approx; 60 000
        halálos áldozat; tűzvész és cunami; Skóciában, Skandináviában érezték hatását; becsült Richter magnitúdó: 8.75}
    \li{ESA ERS-1 műhold; 1992-es Szent András-törésvonal földrengés,
        2-3 m-es horizontális elmozdulás}
}


<p><a href="https://commons.wikimedia.org/wiki/File:2D_geometric_strain.svg#/media/File:2D_geometric_strain.svg">
<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/2D_geometric_strain.svg/1200px-2D_geometric_strain.svg.png" width="600" alt="2D geometric strain.svg">
</center>
</a><br>By <a href="//commons.wikimedia.org/wiki/File:2D_geometric_strain.png" title="File:2D geometric strain.png">2D_geometric_strain.png</a>: <a href="//commons.wikimedia.org/wiki/User:Sanpaz" title="User:Sanpaz">Sanpaz</a>
derivative work: <a href="//commons.wikimedia.org/wiki/User:Mircalla22" title="User:Mircalla22">Mircalla22</a> (<a href="//commons.wikimedia.org/wiki/User_talk:Mircalla22" title="User talk:Mircalla22"><span class="signature-talk">talk</span></a>) - <a href="//commons.wikimedia.org/wiki/File:2D_geometric_strain.png" title="File:2D geometric strain.png">2D_geometric_strain.png</a>, Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=7680077">Link</a></p>

<p>
<a href="https://commons.wikimedia.org/wiki/File:Stress_Strain_Ductile_Material.png#/media/File:Stress_Strain_Ductile_Material.png">
<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/8/84/Stress_Strain_Ductile_Material.png" width="600" alt="Stress Strain Ductile Material.png">
</center>
</a><br>By Breakdown - <span class="int-own-work" lang="en">Own work</span>,<a href="http://creativecommons.org/licenses/by-sa/3.0/" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=3702892">Link</a></p>

\h2{Deformációs tenzor}

$$ \mdef _{ij} = \half (\partial_i u_j + \partial_j u_i ) $$
$$ \theta = \frac{\Delta V}{V} = \trace \mdef = \div \vu $$

\h2{Rugalmas feszültség tenzor}

\h2{Általánosított Hooke-törvény}

$$ p_{ij} = c_{ijkl} \mdef _{kl}$$

\h2{Izotróp testek - Lamé-állandók:}

$$ \lambda  = \frac{E \sigma}{ (1 + \sigma)(1 - 2\sigma)}$$
és
$$ \mu = \frac{E}{2(1 + \sigma)} $$
anyagi minőség, hőmérséklet, nyomás függvényei

$$ p_{ij} = \delta_{ij} \lambda \theta + 2 \mu \mdef _{ij} $$

vagy

$$ \vp = \lambda\theta \vu + 2 \mu \mdef $$

\h2{Hullámegyenlet}

$$ \rho \par{t}^2 \vu = \mat{f} + (\lambda + 2 \mu) \gdiv_u  - \mu \rot \rot \vu $$

\h3{Szeparálás}

$$ \Theta = \div \vu $$
$$ \rho \par{t}^2 \Theta = (\lambda + 2 \mu) \laplace \Theta $$
$$ \par{t}^2 \Theta = \alpha^{-2} \laplace \Theta \hspace{25pt} \alpha = \sqrt{\frac{\lambda + 2 \mu}{\rho}} $$

$$ \phi = \rot \vu $$
$$ \rho \par{t}^2 \phi = \mu \laplace \phi $$
$$ \par{t}^2 \phi = \beta^{-2} \laplace \phi \hspace{25pt} \beta = \sqrt{\frac{\mu}{\rho}} $$

\h3{Általános megoldás}

$$ \Theta(\vr, t) = G(\vk \vr \pm c t) $$

Tipikus választás

$$ \Theta = \mat{A} \exp (i (\vk \vr \pm \omega t)) $$
$$ \vk = \frac{2 \pi}{\lambda} \mat{n} \hspace{25pt} \omega = \frac{2\pi}{T}$$

Fázissebesség: $ v_f = \frac{\omega}{k} $
Csoportsebesség: $ \mat{v} _g = \frac{\partial \omega}{\partial \vk} $

\h3{Energiasűrűség}

$$ e = \half \rho \omega^2 A^2 $$

\h2{Rugalmas hullámok törése}


\h2{Földrengések intenzitása}

\ul{
    \li{felszíni jelenségek, pusztítás alapján; tapasztalati skála -
        makroszeizmológiai megfigyeléseken alapul}
    \li{Föld különböző területein, különböző skálák}
    \li{történelmi földrengések leírása}
    \li{\em{Mercalli-Cancai-Sieberg skála}, 1917; MSK-64 skála}
    \li{pl. nem érzékelhető-, gyenge-, mérsékelt-, erős-, romboló-,
        katasztrofális földrengés; épületek sérülése, pusztulása,
        domborzat változása}
    \li{Kövesligethy Radó eljárás, felszíni intenzitás eloszlás &rarr; fészekmélység}
}

\h2{Földrengések magnitúdója}

\ul{
    \li{műszeres megfigyelésen alapul, földrengés során felszabadult energáit
        jellemzi; Richter vezette be 1935-ben, Kalifornia}
    \li{Richter: $M = \log A - \log A_0$, $A$: epicentrumtól 100 km-e mikronban
    mért legnagyobb amplitúdó, $A_0$: skálatényező, zeró magnitúdójú rengés
    amplitúdója}
    \li{$M \propto \log E$}
    \li{nincs felső határa, eddigi legnagyobb: 8.7-8.8}
    \li{magyarországi rengések: $M = 0.5 I_0 + 1.75$m $I_0$: epicentrális
        intenzitás}
}


\h2{A Föld belső szerkezete - PREM modell}

információ: szeizmika, magas nyomáson és hőmérsékleten végzett kísérletek,
geokémia, mgnetotellúrika, ásványfizika

\h3{A Föld radiális szerkezete}

\ul{
    \li{Andrija Mohorovicic (1909): kéreg-köpeny határ (Moho)}
    \li{Beno Gutenberg (1913): Köpeny-Mag határ (Gutenberg-felület)}
    \li{Inge Lehmann (1936): belső és külső mag közötti határ
        (Lehmann-felület)}
    \li{Sir Harold Jeffreys (1939): bizonyítékok az átmeneti zóna létezésére}
    \li{Bullen (1940): összegzés, hat zóna}
    \center{
        <table style="width:50%">
            \tr{\th{Betűjel} \th{Zóna}}
            \tr{\td{A} \td{Kéreg}}
            \tr{\td{B} \td{Felső köpeny}}
            \tr{\td{C} \td{Átmeneti Zóna}}
            \tr{\td{D} \td{Alsó köpeny}}
            \tr{\td{E} \td{Külső mag}}
            \tr{\td{F} \td{Belső mag}}
        </table>
    }
    \li{Ma már nem használatos felosztás}
}


\h4{A Föld radiális kémiai összetétele}

\ol{
    \li{\b{Kéreg}}
    \ul{
        \li{óceáni kéreg - vastagság $0 - \si{6}{\km}$, főként üledék és bazalt}
        \li{kontinentális kéreg - vastagság $\approx \si{30}{\km}$,
            üledékek, granodiorit}
        \li{óceáni kéreg sűrűbb}
    }
    \li{\b{Köpeny}}
    \ul{
        \li{kéregtől kb. $\si{2900}{\km}$-ig tart, döntően magnéziumszilikát}
        \li{60% olivin, 30% piroxén, 10% gránát}
    }
    \li{\b{Mag}: fémes összetétel, 80% vas, 5% nikkel, kisebb sűrűségű ötvözetek,
        és ötvöző anyagok}
}


\h4{A Föld radiális mechanikai szerkezete}

\ol{
    \li{\b{Litoszféra}: szilárd burok, kb. $\si{100}{\km}$ vastag,
        kontinentális litoszféra ennek kétszerese is lehet, minden
        idősálán szilárd}
    \li{\b{Mezoszféra}: asztenoszféra alatt, emberi időskálán döntően szilárd}
    \li{\b{Külső mag}: $2890 - \si{5150}{\km}$, folyékony}
    \li{\b{Belső mag}: $5150 - \si{6370}{\km}$, szilárd}
}


\h3{PREM-modell}

\ul{
    \li{\it{Preliminary Reference Earth Model}, kiinduló radiális (1D-s) modell}
    \li{bementi adat: szeizmológiai menetidőgörbék és a Föld
        sajátrezgéseinek frekvenciái}
    \li{$v_p(r)$ és $v_s(r)$ szeizmikus hullámterjedési sebességek a mélység
        függvényében + Adams-Williamson-egyenlet &rarr; $\rho(r)$ és $g(r)$
        &rarr; rugalmas paraméterek (Lamé-állandók, Young-modulus, Poisson-arány)}
    \li{$v_p$ és $v_s$ diszkontinuitások &larr; kémiai változások, ásványtani
        fázishatárok}
    \li{alsó köpeny - két rész, D' (homogénebb) és D''}
    \li{CMB ugrás sebességben és sűrűségben (magnéziumszilikát &rarr;
        fémes összetétel)}
    \li{belős és külső meg határa: folyékony &rarr; szilárd}
    \li{$g$ köpenyben kb. állandó, egyre közelebb kerülünk a nagy sűrűségű
        fémes maghoz}
    \li{nyomás kb. litosztatikus/hidrosztatikus, CMB után gyorsabban nő a
        nagyobb sűrűség miatt; középpontban $\approx \si{350}{\giga\pa}$}
}

Adams-Williamson-egyenlet:
$$ \der{\rho}{r} = - \frac{G M(r)}{\sqrd{r}} \frac{\rho(r)}{\Phi}
                   + \alpha \rho(r) \tau $$
\ul{
    \li{$ \Phi = \sqrd{v_p} - \frac{4}{3} \sqrd{v_s}$}
    \li{$\alpha$: lineáris hőtágulási együttható}
    \li{$\tau$: szuperadiabatikus hőmérsékleti gradiens}
}

Bullen-féle inhomogenitási tényező:

$$ \eta_B = \Phi\der{\rho}{p} $$

$\eta_B$ sűrűség nyomásváltozás viszonyítása az adiabatikus körülmények között
bekövetkezett sűrűségváltozáshoz. 
\ul{
    \li{$\eta_B = 1$: sűrűség adiabatikusan változik}
    \li{$\eta_B > 1$: sűrűség gyorsabban nő a nyomással}
    \li{$\eta_B < 1$: sűrűség lassabban nő a nyomással}
}


\center{
    \row{
        \col{
            \imref{https://ds.iris.edu/spudservice/data/9991842?nolog=y}{PREM modell.}
        }
        \col{
            <p><a href="https://commons.wikimedia.org/wiki/File:EarthGravityPREM.svg#/media/File:EarthGravityPREM.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/EarthGravityPREM.svg/1200px-EarthGravityPREM.svg.png" alt="EarthGravityPREM.svg"></a><br>By <a href="//commons.wikimedia.org/wiki/User:Con-struct" title="User:Con-struct">Con-struct</a> - Dziewonski, A.M. (1981). "Preliminary reference Earth model". Physics of the Earth and Planetary Interiors 25: 297–356.
            <a rel="nofollow" class="external free" href="http://geophysics.ou.edu/solid_earth/prem.html">http://geophysics.ou.edu/solid_earth/prem.html</a>
            <a href="//commons.wikimedia.org/wiki/User:AllenMcC." title="User:AllenMcC.">AllenMcC.</a>, <a href="//commons.wikimedia.org/wiki/File:EarthGravityPREM.jpg" title="File:EarthGravityPREM.jpg">File:EarthGravityPREM.jpg</a> for the linear density curve, <a href="https://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=27390559">Link</a></p>
            <p><a href="https://commons.wikimedia.org/wiki/File:RadialDensityPREM.jpg#/media/File:RadialDensityPREM.jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/8/89/RadialDensityPREM.jpg" alt="RadialDensityPREM.jpg"></a><br>By <a href="//commons.wikimedia.org/wiki/User:AllenMcC." title="User:AllenMcC.">AllenMcC.</a> - <span class="int-own-work" lang="en">Own work</span>, Paper: <a rel="nofollow" class="external free" href="http://www.gps.caltech.edu/uploads/File/People/dla/DLApepi81.pdf">http://www.gps.caltech.edu/uploads/File/People/dla/DLApepi81.pdf</a>, <a href="https://creativecommons.org/licenses/by/3.0" title="Creative Commons Attribution 3.0">CC BY 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=12476245">Link</a></p>
        }
    }
}


\h3{A köpeny}

\h4{Felső köpeny}

\ul{
    \li{Moho-felülettől $\si{660}{\km}$-ig, átmeneti zóna, nincs éles határ}
    \li{legfelsőbb része a szeizmikus fedő, szeizmikus hullámok relatíve
        nagy terjedési sebsség }
    \li{fedő alatt alacsony sebsségű zóna \it{(LVZ, low velocity zone)} 
        - parciálisan olvadt asztenoszféra, jelenléte függ a felette található
        képződménytől}
    \li{\it{szeizmikus diszkontinuitás:} $410$ és $\si{660}{\km}$
        hullámterjedési sebesség ugrásszerűen megnő}
}

\h4{Alsó köpeny}

\ul{
    \li{leghomogénabb (összetétel, ásványtani szerkezet)}
    \li{$\eta_B \approx 1$ &larr; alsó köpeny jelentős része adiabatikus}
    \li{termikus, termokémiai konvekció homogenizáló  hatása}
}

\h4{Legalsó köpeny}

\ul{
    \li{D' és D'' (CMB felett $200 - \si{300}{\km}$) réteg}
    \li{laterálisan erősen inhomogén}
    \li{nagyméretű negatív szeizmikus anomália, LLSVP
        \it{(large low shear velocity province)}, Pacifikum és Afrika alatt,
        kiterjedés; horizontális: több $\si{1000}{\km}$
        vertikális: több $\si{100}{\km}$}
    \li{$v_s$: -2 &ndash; -4%, $v_p$: 0 &ndash; -1% &rarr;
        valószínűleg nem csak hőmérsékletbeli változás, összetételbeli is}
    \li{elképzelés: köpeny meleg, kis sűrűségű képződényei}
    \li{a két LLSVP több $\si{100}{\myr}$ létezik, felhajtóerőt
        valami kompenzálja, magas vaskoncentráció}
    \li{ULVZ \it{(ultra low velocity zone)}: néhány $\si{10}{\km}$-es
        kiterjedés, 10 &ndash; 30%-nyi olvadék, alacsonyabb olvadáspontú vas}
    \li{forró foltok nagyobb valószínűséggel találhatóak LLSVP határai mint,
        belseje felett}
    \li{numerikus modell &rarr; konvekció LLSVP-n belül}
    \li{LLSVP-n kívüli tartományok, szeizmikus értelemben gyorsak,
        szubdukálódott óceáni lemezek \q{temetője}}
}


\h3{Ásványtani fázishatárok a felső köpenyben}


\h4{Exoterm}

\ul{
    \li{$\gamma > 0$, látens hő fejlődik $L_H > 0$}
    \li{alábukó lemez hidegebb Clapeyron-görbét kisebb nyomáson éri el &rarr;
        kisebb mélységben kezdődik az átalakulás, átalakulás közben hő
        fejlődik &rarr; lemez kis mértékben felmelegszik, majd tovább süllyed}
    \li{meleg hőoszlop melegebb Clapeyron-görbét nagyobb nyomáson éri el &rarr;
        nagyobb mélységben kezdődik az átalakulás, átalakulás közben hő
        elnyelődik &rarr; hőoszlop kis mértékben hül, majd tovább emelkedik}
    \li{áramlást segít}
}


\h4{Endoterm}

\ul{
    \li{$\gamma < 0$, látens hő fejlődik $L_H < 0$}
    \li{alábukó lemez hidegebb Clapeyron-görbét kisebb nyomáson éri el &rarr;
        nagyobb mélységben kezdődik az átalakulás, átalakulás közben hő
        elnyelődik &rarr; lemez kis mértékben lehül, majd tovább süllyed}
    \li{meleg hőoszlop melegebb Clapeyron-görbét kisebb nyomáson éri el &rarr;
        kisebb mélységben kezdődik az átalakulás, átalakulás közben hő
        fejlődik &rarr; hőoszlop kis mértékben felmelegszik, majd tovább
        emelkedik}
    \li{áramlást akadályoz}
}


\h4{Kvalitatív elemzés}

\define{\ra}{\rho_{\alpha}}
\define{\rb}{\rho_{\beta}}

\ul{
    \li{Fázishatár elhajlásból származó negatív felhajtóerő:
        $F_A \approx \gamma \frac{\rb - \ra}{\rb} L \Delta T$}
    \li{Fázishatár elhajlásának nagysága:
        $\Delta h \approx \gamma \frac{\Delta T}{\rb g}$}
    \li{Fázisátment során felszabaduló hő:
        $L_H = \gamma T_s \frac{\rb -\ra}{\rb\ra}$,
        hőmérsékletváltozás: $L_H = c_p m \Delta T_L$}
    \li{Látens hőből származó hőmérséklet változás miatt bekövetkező
        sűrűségváltozás felhajtóereje:
        $F_B = \rb \alpha \Delta T_L L \Delta h g$}
    \li{Látens hőből származó fázishatár elhajlás felhajtóereje:
        $F_A \approx \gamma \frac{\rb - \ra}{\rb} L \Delta T_L$}
}



\h4{A $\si{410}{\km}$-es ásványtani fázisátmenet}

\ul{
    \li{Perry Byerly (1926): $\Delta > \deg{20}$ letörés a mentidő görbékben}
    \li{olivin kristály fázisátmenete $\si{13.5}{\giga\pa}$ nyomáson és
        $\si{1600}{\celsius}$ hőmérsékleten, $\alpha$-spinell &rarr;
        $\beta$-spinell, \it{exoterm}, kiterjedés: $\approx \si{10}{\km}$}
    \li{$\Delta\rho \approx$ 7 &ndash; 8%; $\Delta v_p = 0.3 - \si{0.4}{\kmps}$}
    \li{Clapeyron-görbe merekedksége:
        $\gamma \approx \si{1.6}{\mega\pa \pow{K}{-1}}$}
    \li{piroxénnek is van fázisátalakulása, de Ca tartalom miatt sokkal
        szélesebb tartományon következik be}
}


\h4{A $\si{660}{\km}$-es ásványtani fázisátmenet}

\ul{
    \li{éles határ $< \si{5}{\km}$, határ aljáról reflektálódó hullámok}
    \li{olivin $\gamma$-szerkezet $\si{32.1}{\giga\pa}$ nyomáson és
        $\si{1600}{\celsius}$ hőmérsékleten &rarr; perovszkit és
        magneziovüsztit, \it{endoterm}}
    \li{$\Delta\rho \approx$ 10%; $\Delta v_p = 0.4 - \si{0.6}{\kmps}$}
    \li{Clapeyron-görbe merekedksége:
        $\gamma \approx -\si{2.5}{\mega\pa \pow{K}{-1}}$}
    \li{gránát ásványcsoport fázisátalakulás, sokkal szélesebb tartományon}
}


\h4{Érők nagyságrandje a két fázishatár esetén}


<table>
    \tr{
        \th{Lebukó lemezre ható erők $[\newton \inv{\meter}]$}
        \th{A: Fázishatár elhajlás}
        \th{B: Látens hő okozta hőtágulás}
        \th{C: Látens hő okozta fázishatár elhajás}
        \th{Eredő erő nagysága}
    }
    \tr{
        \td{$\si{410}{\km}$-es fázishatár}
        \td{$-\sci{6.4}{12}$}
        \td{$+\sci{6.3}{10}$}
        \td{$+\sci{3.5}{11}$}
        \td{$\approx-\sci{6}{12}$}
    }
    \tr{
        \td{$\si{660}{\km}$-es fázishatár}
        \td{$+\sci{1.0}{13}$}
        \td{$-\sci{3.0}{10}$}
        \td{$+\sci{1.9}{12}$}
        \td{$\approx+\sci{1.2}{13}$}
    }
</table>

A fázishatár elhajlás okozta erő domináns.


\h4{Egyéb ásványtani fázisátmenetek}

\ul{
    \li{ilivin-piroxén-gránát számos fázisátmenet}
    \li{olivin $\si{520}{\km}$ $\beta$-spinell &rarr; $\gamma$-spinell
        - nincs szeizmológiai hatás}
    \li{a két fázishatár éles, de mélységük akár több $\si{10}{\km}$-t
        is változhat.}
    \li{a fázishatárok globálisnak tekinthetőek}
    \li{magas hőmérséklet és nyomás hatására fellépő sűrűségváltozás
        mindössze 3% körüli, \it{exoterm}, széles tartományon megy végbe}
    \li{extrém nagy nyomáson és hőmérsékleten perovszkit &rarr;
        posztperovszkit, $\gamma \approx 7 - \si{8}{\mega\pa \pow{K}{-1}}$,
        $200 - \si{300}{\km}$-el a CMB felett; hideg szubdukálódó lemez
        &rarr; posztperovszkit lencse}
}

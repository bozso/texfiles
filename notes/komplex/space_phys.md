\include{html.gpp}

\define{\e0}{\epsilon_0}
\define{\vv}{\mat{v}}
\define{\va}{\mat{A}}
\define{\vx}{\mat{x}}
\define{\vk}{\mat{k}}
\define{\vE}{\mat{E}}
\define{\vB}{\mat{B}}
\define{\vj}{\mat{j}}
\define{\ome}{\omega_{pe}}
\define{\pdens}{\pow{\cm}{-3}}

\define{\sp}{\sigma_P}
\define{\sh}{\sigma_H}
\define{\spar}{\sigma_{\parallel}}


\h2{Bevezetés}

\h3{Plazma definíciója}

\ul{
    \li{töltött részecske gáz, egyenlő számú
        pozitív és negatív töltésű részecske}
    \li{stacionárius állapotban kvázineutrális}
    \li{néhány $\eV$ termikus energia, forró ionizált gáz}
    \li{szabad mozgás, ütközésektől eltekintve}
    \li{univerzum anyagának $\approx 99\%$-a plazma}
}

\h3{Debye árnyékolás}

\ul{
    \li{térfogatelemben ugyanannyi pozitív és negatív töltésű
        részecske &rarr; részecskék leárnyékolják egymás elektromos
        terét}
    \li{\em{Debye-távolság} $\lambda_D \prop T_e, \inv{n_e}$}
    \li{Debye-távolságon túl részecske tere leárnyékolódik}
    \li{\b{Első kritérium:} kvázineutrális a plazma ha $\lambda_D \ll L$}
    \li{\b{Második kritérium:} plazmaparaméter $\Lambda = n_e \cubed{\lambda_D} \gg 1 $}
}


\h3{Plazmafrekvencia}

\ul{
    \li{plazmáknak karakterisztikus rezgési frekvenciája}
    \li{külső zavar &rarr; elektronok rezgőmozgást végeznek}
    \li{nem teljesen ionizált gáz &rarr; elektronok ütköznek a semleges
        részecskékkel, karakterisztikus idő $\tau_n$}
    \li{\b{Harmadik kritérium:} $ \ome \tau_n \gg 1 $}
}

$$ \ome = \pow{\par{ n_e \pow{e}{2} \inv{(m_e \e0)}}}{\half} $$


\h3{Geofizikai plazmák}

\h4{Napszél}

\ul{
    \li{napkorona szuperszónikus tágulása, nagy vezetőképesség,
        $v \approx \si{500}{\kps}$, $n_e \approx \si{5}{\pdens} $} 
    \li{elektronok és protonok, kb. 5% He}
    \li{nap mágneses mezeje \q{befagyva} a plazmába, napszél elvonszolja}
    \li{Föld mágneses tere lelassítja és eltéríti}
    \li{\em{bow shock} napszél lelassul szuperszónikus sebességről
        szubszónikusra, kinetikus energia &rarr; termális energia}
}


\h4{Magnetoszféra}

\ul{
    \li{IMF erővonalak nem keresztezik a földi mágneses tér erővonalait}
    \li{\em{magnetopauza}, mágneses \q{üreg}: \em{magnetoszféra}}
    \li{napszél kinetikus nyomása &harr; földi mágneses tér nyomása}
    \li{napfelöli oldal \q{összenyomva}, éjszakai oldal elnyújtva,
        \q{mágneses csóva}}
    \li{elsősorban elektronok és protonok, kis részben hélium, oxigén ionok}
    \li{\q{sugárzási zónák}: $2 - 6 R_E$ távolság, nagy energiájú elektronok
        és protonok}
}


\h4{Ionoszféra}

\ul{
    \li{UV sugárzás a Napból ionizálja a semleges atmoszféra egy részét}
    \li{$\approx \si{80}{\km}$ felett túl ritka az ütközéses rekombináció}
    \li{átmenet a \em{plamzmaszférába}, hideg sűrű plazma, tórusz alakú régió
        a sugárzási-öveken belül, együtt forog a Földdel}
    \li{\em{plazmapauza} $4 R_E$, sűrűség lecsökken $\si{1}{\pdens}$-re}
}

<table>
    \tr{
        \th{Plazma}
        \th{Elektronsűrűség $[\pdens]$}
        \th{Sebesség $[\kps]$}
        \th{Hőmérséklet $[K]$}
        \th{Mágneses tér $[\text{nT}]$}
    }
    \tr{
        \td{Napszél}
        \td{5}
        \td{500}
        \td{$\pow{10}{5}$}
        \td{5}
    }
    \tr{
        \td{Sugárzási övek}
        \td{1}
        \td{-}
        \td{$\sci{5}{7}$}
        \td{$100 - 1000$}
    }
    \tr{
        \td{Plasma sheet}
        \td{0.5}
        \td{-}
        \td{$\sci{5}{6}$}
        \td{10}
    }
    \tr{
        \td{Mágneses csóva}
        \td{$\pow{10}{-2}$}
        \td{-}
        \td{$\pow{10}{5}$}
        \td{$\approx 30$}
    }
    \tr{
        \td{Ionoszféra}
        \td{$\pow{10}{5}$}
        \td{-}
        \td{$\pow{10}{3}$}
        \td{$\pow{10}{4}$}
    }    
    \tr{
        \td{Plazmaszéra}
        \td{$\sci{5}{2}$}
        \td{-}
        \td{$\sci{5}{3}$}
        \td{$\pow{10}{3}$}
    }    
</table>


\h3{Magnetoszferikus áramok}

\ul{
    \li{sokszor elektronok és ionok nem mozognak együtt &rarr; elektromos
        áram &rarr; töltés, energia, tömeg és impulzus szállítás, mágneses tér}
    \li{földi dipóltér torzulása &harr; elektromos áramok}
    \li{\em{magnetopauza áram}, \em{csóva áram}, \em{neutrális ív áram}}
    \li{\em{gyűrűáram} sugárzási-zóna részecskéi, nyugati irány,
        pattogó mozgás + drift}
}

\imref{https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.geomag.us%2Finfo%2FMagnetosphere%2Fmagnetosphere.jpg&f=1}


\h2{Egyetlen részecske mozgása}

\ul{
    \li{t.f.h.: nem kölcsönható részecskék, nem befolyásolják a külső
        mágneses teret; igaz ritka plazmáknál, ahol nincs kollektív mozgás,
        külső mgáneses térnek elég erősnek kell lennie}
    \li{Coulomb- és Lorentz-erők: $m \dot{\vv} = q (\vE + \cross{\vv}{\vB})$}
}

\h3{Körmozgás}

\ul{
    \li{ha $\vE = 0$, csak Lorentz-erő &rarr; körmozgás:
        $ \omega_g = q B \inv{m} $, girofrekvencia, ciklotronfrekvencia}
    \li{részecske körmozgása által generált mágneses mező ellentétes a
        külsővel, \em{diamágneses hatás}}
}

\h3{Elektromos drift}

\ul{
    \li{mágneses térrel párhuzamos elektromos komponens nem tarható fennt
        &larr; elektromok nagyon mozgékonyak a mágneses
        mező mentén}
    \li{stacionárius elektromos és mágneses mező esetén &rarr;
        \em{$\cross{E}{B}$ drift}: $ \vv _R = (\cross{\vE}{\vB})\pow{B}{-2} $}
    \li{elektromos töltés előjelétől független}
    \li{fizikai háttér: Lorentz-transzformáció}
}


\h2{Csapdázott részecskék}

\h3{Dipól mező}

\ul{
    \li{földfelszíntől nem túl távol a Föld mágneses tere jól közelíthető
        egy mágneses dipólus terével}
    $$ B(\lambda, L) = \frac{B_e}{\cubed{L}}
       \frac{\pow{\par{1 + 3 \pow{\sin}{2} \lambda}}{\half}}{\pow{\cos}{6} \lambda} $$
    \li{$L = r_e \inv{R_E}$; $\hspace{5pt} B_E$ egyenlítői mágneses mező nagysága
        a Föld felszínén}
    \li{egy adott $L$ értkkel rendelkező erővonal hol metszi a Föld felszínét:}
    $$ \cos^2 \lambda_E = \inv{L} $$
}


\h3{Gyűrűáram}

\ul{
    \li{nyugati irányú áramerősség, minden mozgó részecske egy kis gyűrűáramot
        eredményez; összes részecske hatása &rarr; gyűrűáram}
    \li{gyűrűáram &rarr; \em{mágneses zavar} a földi mágneses térben}
    \li{\em{mágneses vihar} több részecske érkezik a csóvából a gyűrűáramba
        &rarr; gyűrűáram teljes energiája megnő &rarr; egyenlítői
        magnetogrammokon látható mágneses térerősség lecsökken}
    \li{mágneses vihar, két fázis}
    \ol{
        \li{megnövekedett elektromos tér több részecskét szállít a belső
            magnetoszférába megnövelve a gyűrűáram erősségét}
        \li{1-2 nappal a vihar kezdete után az elektromos tér és a részecske
            szállítás intenzitása visszatér a normális erősségre,
            a gyűrűáram részecskék száma lecsökken, több napig is elterthat}
    }
    \li{extra energia kiszámítható a \em{Dst index} alapján}
    \li{\em{Dst index}: egyenlítői zavar átlagos értéke, 4 alacsony
        szélességű mágneses obszervatórium adataiból}
    \li{nagyobb mágneses vihar során: $+\si{\sci{5}{15}}{\joule}$ és $+ \si{\pow{10}{7}}{\ampere}$}
}


\h2{Ütközéses plazmák vezetőképessége}


\ul{
    \li{\em{ütközéses} (részlegesen- és teljesen ionizált) és
        \em{ütközésmentes} (ütközések rendkívül ritkán) plazmák}
    \li{részelgesen ionozált plazma: Coulomb- és direkt-ütközések,
        teljesen ionozált plazma: csak Coulomb-ütközések}
}


\h3{Részlegesen ionizált plazma}


\ul{
    \li{legtöbb ütközés töltött és semleges részecskék (nehéz, kompakt
        akadály) között}
    \li{átlagos szabadúthossz: $\lambda_n = \inv{(n_n \sigma_n)}$}
    \li{befolyásol: rekombináció, ellenállás, áramsűrűség, töltött részecsék
        diffúziója}
}


\h3{Teljesen ionizált plazma}

\ul{
    \li{Coulomb-kölcsönhatás, atmosugárnál sokkal nagyobb távolságon
        kölcsönhatnak}
    \li{Debye-árnyékolás hatása, Debye-gömb $\ne$
        ütközés hatáskeresztmetszete, nagy energiájú részecskék átjutnak}
    \li{ütközési frekvencia: $\nu_{ei} \propto n_e \pow{m_e}{-2} \pow{v_e}{-3}$}
    \li{átlagos szabadúthossz: $\lambda_e \propto \lambda_D \Lambda
        \inv{\par{\ln \Lambda}} $}
    \li{geofizikai plazmák általábna ütközésmentesnek tekinthetőek:}
    \ul{
        \li{$lambda_e \gg \text{plazma kiterjedése}$}
        \li{$\nu_{ei} \ll \ome$}
    }
    \li{elektron-elektron és ion-ion ütközések esetén, egyensúly
        gyorsan kialakul az impulzus cserék során}
}

\h3{A plazma vezetőképessége}

Mozgásegyenlet kiegészítése plusz ütközési taggal.

\h4{Nem előmágnesezett plazma}

\ul{
    \li{t.f.h.: $\vB = 0$, elektronok sebessége: $\vv _e$, ütközési cetrumok
        mozdulatlanok, $\vE = \eta \vj$, $\eta \propto \nu_c \inv{n_e}$}
}


\h4{Előmágnesezett plazma}

\ul{
    \li{\em{általánosított Ohm-törvény:} $\vj = \sigma_0 (\vE +
        \cross{\vv}{\vB}$, $\sigma_0 = \inv{\eta}$}
    \li{alsó-ionoszféra, ion-semleges részecske ütközések &rarr;
        vezetőképesség mátrix (anizotrópia)}
    \li{z-tengely irányába mutató mágneses tér esetén:}
    $$
    \sigma = 
    \begin{bmatrix}
    \sp & -\sh & 0 \\
    \sh & \sp & 0 \\
    0 & 0 & \spar
    \end{bmatrix}
    $$
    ahol,
    \ul{
        \li{$\sp = \sqrd{\nu_c} \inv{\par{\sqrd{\nu_c} + \sqrd{\omega_{ge}}}}
            \sigma_0 $, \em{Pedersen-vezetőképesség}, mágneses térre merőleges}
        \li{$\sh = - \omega_{ge} \nu_c \inv{\par{\sqrd{\nu_c} + \sqrd{\omega_{ge}}}}
            \sigma_0 $, \em{Hall-vezetőképesség}, iránya: $-\cross{\vE}{\vB}$}
        \li{$\spar = \sigma_0$, mágneses térrel párhuzamos vezetőképesség}
    }
    \li{$\abs{\omega_{ge}} \approx \nu_c$ maximum anizotrópia, Hall- és
        Pedersen-vezetőképesség egyforma nagyságrendben}
    \li{$\abs{\omega_{ge}} < \nu_c$ Pedersen-vezetőképesség dominál}
    \li{$\abs{\omega_{ge}} > \nu_c$ elektronok $\cross{E}{B}$ drift,
        Hall-vezetőképesség dominál}
}


\h3{Ionoszféra kialakulása}

\h4{Napból származó UV sugárzás ionizáló hatása}

\ul{
    \li{$E_{\text{foton energia}} > E_{\text{ionozációs}}$ - UV tartomány,
        magasabb energiatartományú sugárzás intenzitása kisebb}
    \li{elsősorban horizontális struktúra, semleges gáz sűrűsége:}
    $$ n_n(z) = n_0 \exp(-z \inv{H}) $$
    \li{skálatényező:}
    $$ H = \frac{k_B T_n}{m_n g} $$
    \li{ionprodukciós rátának lesz egy maximuma.}
}

\row{
    \col{
        <p><a href="https://commons.wikimedia.org/wiki/File:Atmosphere_with_Ionosphere.svg#/media/File:Atmosphere_with_Ionosphere.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Atmosphere_with_Ionosphere.svg/1200px-Atmosphere_with_Ionosphere.svg.png" alt="Atmosphere with Ionosphere.svg"></a><br>By Bhamer, updated to SVG by <a href="//commons.wikimedia.org/wiki/User:Tomtheman5" title="User:Tomtheman5">tiZom</a> - English Wikipedia, Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=2178742">Link</a></p>
    }
    \col{
        \imref{https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fmalagabay.files.wordpress.com%2F2012%2F10%2Finternational-quiet-solar-year-daytime-ionospheric-and-atmospheric-composition.gif&f=1}
    }
}


\h4{Nagy energiájú részecskék ionizáló hatása}

\ul{
    \li{elsősorban erővonalak mentén mozgó nagy energiájú elektronok ütközéses
        ionizációja}
    \li{fontos szerep éjszaka és nagyobb szélességeken}
    \li{$\sub{E}{elektron} > \sub{E}{ionizációs}$, pl. oxigén esetén
        $\si{35}{\eV}$}
    \li{nagyobb energiájú részecskék alacsonyabbra elérnek,
        $\sub{E}{elektron} = \si{300}{\kilo\eV}$ &rarr; $\si{70}{\km}$}
}

\h4{Rekombináció és befogás}

\ul{
    \li{befogás: elektront semleges atom befogja &rarr; negatív ion}
    \li{két együtthatóval írható le: $\alpha_r$ rekombinációs és
        $beta_r$ befogási együttható}
    \li{kontinuitási egyenlet: $\dot{n_e} = q_{v,e} - \alpha_r \sqrd{n_e}
        - \beta_r n_e$, egyensúlyban $\dot{n_e} = 0$}
    \li{alacsonyabban a rekombináció dominál $\beta_r = 0$}
    $$ n_e = \pow{\par{\frac{q_{v,e}}{\alpha_r}}}{\half} $$
    \li{magasabban a befogás dominál $\alpha_r = 0$}
    $$ n_e = \frac{q_{v,e}}{\beta_r} $$
}

\h3{Ionoszféra rétegek}

\ul{
    \li{valós profil függ: semleges atmoszférát alkotó elemek abszorbciós
        tulajdonságai - nagyon változékony, rekombinációs- és
        befogási együtthatók &rarr; különböző rétegek alakulnak ki}
    \li{alsó ionoszféra: \em{D-réteg} $< \si{90}{\km}$, gyengén ionizált,
        semleges gáz dominálja, nem tekinthető plazmának}
    \li{felső ionoszféra $> \si{90}{\km}$, semleges gáz számottevő összetevő
        $\si{500}{\km}$-ig}
    \li{\em{E-réteg:} hoszabb hullámhosszú UV sugárzás abszorbciója,
        ionizációs csúcs $\si{110}{\km}$-nél, oxigén ion dominancia}
    \li{\em{F-réteg:} két rétegből áll az \em{F1}- ($\si{200}{\km}$) és
        \em{F2}-rétegből ($\si{300}{\km}$)}
    \li{\em{F1-réteg:} nappal észlelhető, keletkezése hasonló az E-réteghez,
        de rövidebb hullámhosszú UV sugárzás kelti}
    \li{\em{F1-réteg:} fontosabb réteg alsó F2 oxigén atom meghatározó szerep,
        felső F2 csökkenő neutrális gáz sűrűség, növekvő elektron sűrűség,
        ionizációs csúcs legnagyobb elektronsűrűség az ionoszférában:
        $\si{\pow{10}{6}}{\pdens}$}
    \li{éjszaka az E- és F-réteg összeolvad}
}

\h3{Ionoszféra vezetőképessége}

\ul{
    \li{elektronok és ionok ütköznek semleges részecskékkel}
    \li{ionok ütközése semleges részecskékkel matematikailag úgyanúgy
        kezelhető, mint az elektronoké}
    \li{ion vezetőképesség tenzor hozzáadható az elektron vezetőképesség
        tenzorhoz}
}


\ul{
    \li{$\approx \si{100}{\km}$-nél ionok semleges atomokkal mozognak &larr;
        magas ütközési frkevencia, elektronok $\cross{E}{B}$ driftje alkotja
        a Hall-áramot}
    \li{$\si{125}{\km}$-en $\nu_{in} \approx \omega_{gi}$, ionok elektromos
        tér irányába kezdenek el mozogni &rarr; Pedersen-áram}
    \li{E-réteg felett ionok elektronok $\cross{E}{B}$ drift, nincs áram
}

\imref{https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fwdc.kugi.kyoto-u.ac.jp%2Fionocond%2Fexp%2Ffigs%2Fionocond.gif&f=1}

\ul{
    \li{Pedersen-vezetőképesség maximum: $\approx \half \sh $,
        $\si{130}{\km}$}
    \li{Hall-vezetőképesség maximum: $\si{\pow{10}{-2}}{\cond}$,
        $\si{100}{\km}$}
    \li{Párhuzamos-vezetőképesség sokkal nagyobb$ \si{\pow{10}{2}}{\cond}$}
}


\h3{Ionoszféra áramrendszerei}

\center{
<p><a href="https://commons.wikimedia.org/wiki/File:Diurnal_ionospheric_current.jpg#/media/File:Diurnal_ionospheric_current.jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/a/a9/Diurnal_ionospheric_current.jpg" alt="Diurnal ionospheric current.jpg"></a><br>Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=306257">Link</a></p>
}

\ul{
    \li{ionok és kisebb mértékben elektronok a semleges részecskékkel együtt
        mozognak}
    \li{atmoszférikus szélrendszerek és árapály hatások &rarr; ionok mágneses
        erővonalak mentén mozognak &rarr; áram, töltések szeparálása &rarr;
        elektromos tér}
}


\h4{\em{Sq} áramrendszer}

\ul{
    \li{napi nyugodt (\em{solar quiet}) áramrendszer, nappali ionoszféra
        legfontosabb áramrendszere közepes szélességeken}
    \li{árapály: napos és félnapos periódusidő, napsugárzás által felfűtött
        atmoszféra}
    \li{mágneses mezeje mérhető földi obszervatóriumokban &rarr;
        áramrendszer rekonstrukció}
    \li{két örvényes áramrendszer az északi- és déli féltekén}
}

\h4{Egyenlítői elektrojet}

\ul{
    \li{geomágneses egyenlítőnél az északi- és déli Sq áramrendszer találkozik
        &rarr; elektrojet}
    \li{mágneses mező geometriája, merőlegesen beeső napsugárzás &rarr;
        vezetőképesség megnövekedés, jet áram felerősödése}
    \li{Pedersen- és másodlagos Hall-áram &rarr; totál áram,
        \em{Cowling-vezetőképesség}}
    $$ \sigma_C = \sp + \frac{\pow{\sh}{2}}{\sp} $$
    \li{Cowling-vezetőképesség egy nagyságrenddel nagyobb mint a
        Pedersen-vezetőképesség}
    \li{elektrojet által okozott mágneses zavar tipikus értéke:
        $50 - \si{100}{\text{nT}}$}
}


\h4{Auróra sugárzás}

\ul{
    \li{kiszóródó elektronok nem csak ionizálnak, magasabb szélességeken
        semleges atmoszférával ütközve sugárzást is létrehoznak,
        látható tartomány}
    \li{kb. $\deg{70}$ szélességen látható, \em{aurora oval} övön belül}
    \li{kelet-nyugat irányú auróra ívek}
    \li{semleges atomok gerjesztése, visszatérés az alapállapotba &rarr;
        látható tartományban sugárzás}
    \li{vörös és zöld szín: oxigén atom, ibolya és kék szín: nitrogén molekula}
}


\h2{Konvekció és szubvihar}

\h3{Konvekció és rekonnekció}

\ul{
    \li{\em{konvekció:} plazma és erővonalak együttes driftje}
    \li{magnetoszférában a konvekció forrása, a napszél áramlás impulzusa}
    \li{ha IMF délies, az északi irányú földi mágneses tér erővonalai
        összekapcsolódhatnak az IMF erővonalaival &rarr; rekonnekció}
    \li{napszél elvonszolja az összekapcsolódott erővonalat a mágneses csóva
        felé}
    \li{a mágneses csóvában $100 - 200 R_E$ távolságban, a két nyitott
        erővonal újabb rekonnekció &rarr; zárt földi erővonal, nyitott
        napszél erővonal}
    \li{mágneses feszültség miatt zárt erővonal földfelé fog mozogni, befagyott
        plazmát szállít}
    \li{rekonnekció az ún. \em{X-vonal} mentén történik, semleges vonal
        mágneses tér nagysága zéró}
}

\center{
    \row{
        \col{
            \imref{https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fffden-2.phys.uaf.edu%2F104_spring2004.web.dir%2FCarla_Tomsich%2FIMAGES%2Fmagnetosphere.jpeg&f=1}
        }
        \col{
            \imref{https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fe%2Fe2%2FMagnetic_reconnection_process_in_the_earth%2527s_magnetosphere_Science_2_lg.png&f=1}
        }
    }
}


\h3{Konvekciós elektromos mező}

\ul{
    \li{rekonnekció meghajt egy csóvairányú plazmaáramlást a poláris
        régión keresztül, belső magnetoszférában napirányú konvekció}
    \li{rekonnekció legerősebb délis IMF esetén}
    \li{belső magnetoszféra plazmaáramláas földi megfigyelő számára ekvivalens
        egy konvektív elektromos térrel, t.f.h.:
        homogén $0.2 - \si{0.5}{\text{mV}\inv{meter}}$}
}

\h3{Árnyékolás}

\ul{
    \li{belső magnetoszféra konvekciós elektromos mezőt csökkenti az
        elektronok és protonok különböző drift útvonala}
    \li{különböző drift útvonal &rarr; gyenge töltés szeparáció}
}


\h3{Magasság szerint integrált Ohm-törvény}

\ul{
    \li{ionoszféra vezetőképesség tenzor 3 komponens &rarr;
        3 típusú áramot fog generálni a konvekciós elektromos mező}
    \ol{
        \li{Mágneses mező irányával megegyező áram,
            \em{(field-aligned current)}}
        \li{\em{Pedersen-áram:} merőleges $\vB$-re és párhuzamos az ionoszféra
            konvekciós elektromos mezejével}
        \li{\em{Hall-áram:} $\cross{\vE}{\vB}$ irányú}
    }
    \li{$\sigma_{\parallel} > \sp, \sh$ &rarr; $E_{\parallel} < E_{\perp}$}
    \li{nagy szélességeken, erővonalak szinte vertikálisak, elektromos
        tér horizontális és magasságtól független &rarr; magasság szerint
        integrált mennyiségek}
    $$ \Sigma_P = \int \sp \md z $$
    $$ \Sigma_H = \int \sh \md z $$
    $$ J_{\perp} = \int j_{\perp} \md z $$
    $$ J_{\perp} = \Sigma_P \vE _{\perp} -
                   \Sigma_H (\cross{\vE _{\perp}}{\vB}) \inv{B} $$
    \li{semleges atmoszféra szélerősség elhanyagolva,
        $j_{\parallel}$ (field-aligned current)
        kontinuitási egyenletből számolható}
    $$
    j_{\parallel} = (\nabla_{\perp} \Sigma_P) \vE _{\perp} - (\nabla_{\perp}
                    \Sigma_H) \cdot (\cross{\vE _{\perp}}{\vB})\inv{B}
                     + \Sigma_P (\nabla_{\perp} \vE _{\perp})
       
    $$
}


\h3{Joule-fűtés és az \em{AE} Index}

\ul{
    \li{aurora elektrojet tipikus fűtési értékei: $5
        - \si{50}{\milli\watt\sqrd{\meter}}$}
    \li{\em{aurora elektrojet index}, globális aurora elektrojet aktivitás
        indexe &rarr; teljes Joule-fűtés becsülhető}
    \li{\em{AE-index:} 12 aurora zónában található obszervatórium
        mágneses zavar északi kompoensének értékeiből számolható,
        maximum északi- és déli komponensben mért zavar értékének különsége}
    \li{empírikusan: felső atmoszféra fűtése: $\si{1}{\giga\watt}
        \leftrightarrow \si{1}{\text{nT}}$, mindkét féltekét figyelembe véve:
        Joule-fűtés, részecské kiszóródás (feleakkora hatásfok mint
        Joule-fűtés)}
    \li{nagyobb mágneses viharoknál: $\text{AE} = \si{1000}{\text{nT}}
        \rightarrow \si{\pow{10}{12}}{\watt}$}
}


\h3{Mágneses szubvihar}

\ul{
    \li{\em{napfelöli rekonnekciós ráta}: egységnyi idő alatt
        összekapcsolódott mágneses fluxus, függ: napszél sebesség, IMF déli
        komponensének nagysága (erősen változékony)}
    \li{minden napfelől összekapcsolt mágneses erővonal
        rekonnektálódik &rarr; konvekció}
    \li{napfelöli és csóvabeli rekonnekciós rátának a nagysága csak átlagban
        kell megegyezzen, elvonszolt erővonalak csak egy része
        konvektálódik vissza a napfelöli oldalra, maradék erővonal eltárolódik
        a mágneses csóvában}
    \li{kb. egy óra múlva, csóvában eltárolt erővonalak rekonnektálódnak,
        nagy energia felszabadulás &rarr; magnetoszferikus szubvihar}
    \li{néhány szubvihar egymás után &rarr; gyűrűáram jelentős megnövekedése}
}

\h4{Vihar beveztő fázisa}

\ul{
    \li{vihar kezdete, napfelöli rekonnekciós ráta megnövekedése, fluxus
        csóvába szállítódik, egy része vissza konvektávlódik a napfelöli
        oldalra}
    \li{megerősödött konvekció &rarr; erősödő aurora elektrojet
        áramsűrűség &rarr; növekvő \em{AE} index}
    \li{csóvában megnövekedett mágneses fluxus &rarr; megnövekedett semleges
        lepel áram &rarr; erővonalakat elnyűjtja &rarr; plazma lepel
        farokszerű geometria}
    \li{\em{vihar bevezető fázisa}, kb fél óráig tart, mágneses csóva
        instabillá válik a felhalmozott mágneses energiától
        &rarr; főfázis}
}


\h4{Vihar főfázisa}


\ul{
    \li{tágulási fázis (30-60 perc) aurora ívek, észak-dél irányban vékonyak,
        kezdetben az egyik ív fényereje hirtelen megnő és betölti az egész
        eget}
    \li{ionoszféra áramsűrűségek jelntősen megnőnek, plazma lepelben
        elnyújtott mágneses mező újra dipoláris jellegűvé válik}
    \li{$\approx 30 R_E$-nél egy \em{föld-közeli semleges vonal} keletkezik,
        elvonszolt mágneses fluxus itt rekonnektálódik &rarr; elnyújtott
        erővonalak dipolárisabb formát vesznek fel}
    \li{két semleges vonal közötti tartomány a \em{plazmoid}, mágneses
        erővonalai zárt hurkokat alkotnak}
}


\h4{Vihar utófázis}

\ul{
    \li{45 perc elteltéval a rekonnekció a föld-közeli semleges vonalnál
        és a szubvihar aktivitás csillapodik, megszűnik}
    \li{ionoszféra áramok nagysága elkezd csökkenni}
    \li{1 - 2 óráig tart, magnetoszféra nyugodt állapotba visszatér}
    \li{vihar vége és egy újabb kezdete átlapolódhat}
    \li{föld-közeli semleges vonal csóva irányába kezd mozogni &rarr;
        plazmoidot csóva irányába nyomja, kidobódik a mágneses csóvából}
}


\h2{Magnetopauza}

\center{
    \imref{http://www.physics.usyd.edu.au/~cairns/teaching/lecture14/img33.gif}
}

\ul{
    \li{napszél plazma nem tud behatolni a földi mágneses tér fluxuscsöveibe}
    \li{napszél eltérül, dinamikus nyomása összenyomja a földi teret}
    \li{keskeny határréteg alakul ki a \em{magnetopauza}}
    \li{elsőrendben erintő irányú diszkontinuitásként kezelhető}
}


\h3{Magnetopauza alakja}

\ul{
    \li{nyomásegyensúly: napszél dinamikus nyomás &harr; geomágneses mező}
    \li{közelítések: napszél mágneses nyomása és elektronok dinamikus nyomása
        elhanyagolható, magnetoszféra plazma dinamikus nyomása elhanyagolható}
    \li{nemlineáris parciális differenciálegyenlet írja le a térbeli alakját,
        numerikusan számítható}
    \li{közelítő egyenlet a magnetopauza \q{orr}-részén a kritikus pontban
        &rarr; $10 R_E$, nyugodt körülmányek között}
    \li{numerikus számítások eredményei}
    \ul{
        \li{nincs folytonos megoldás, mely összekötné a nappali és éjjeli
            magnetopauzát}
        \li{egyenlítői síkban a magnetopauza \q{sima}}
        \li{nagy szélességeken diszkontinuitás &rarr; poláris tölcsér,
            földi dipól tér geometriája miatt}
    }
}

\center{
<table>
    \tr{
        \th{Merkúr}
        \th{Föld}
        \th{Jupiter}
        \th{Szaturnusz}
        \th{Uránusz}
        \th{Neptunusz}
    }
    \tr{
        \td{1.4}
        \td{10}
        \td{75}
        \td{20}
        \td{20}
        \td{25}
    }
</table>
}


\h3{Magnetopauza áramrendszer}

\ul{
    \li{felületi áramok, napszél ionok és elektronok fél giro körzést
        tesznek, mágneses tér visszafordítja őket}
    \li{átmeneti réteg vastagsága $\approx$ ion girorádiusz}
    \li{ionok, elektronok ellentétes irányú girációja &rarr; keskeny
        felületi áramréteg; áramréteg mágneses tere összenyomja a
        magnetoszférát}
    \li{becsült áramsűrűség: $\si{\pow{10}{-6}}{\ampere\pow{\meter}{-2}}$,
        teljes áramerősség $\si{\pow{10}{7}}{\ampere}$}
    \li{egyenlítőnél a magnetopauza áram hajnal-shzürkület irányú}
    \li{magnetopauza csóván két részre válik}
}

\h2{Hullámok plazmákban és fluidumokban}

\ul{
    \li{plazmát sokfajta külső és belső hatás megzavarhatja}
    \li{termális fluktuáció - kvantumelmélettel számíthatóak}
    \li{külső zavar &rarr; plazmahullámok, zavar energiájának szállítása
        egész plazmatérfogatra}
    \li{ULF, ELF és VLF hullámok}
    \li{szükséges: zavar aplitúdója nagyobb legyen mint a hőfluktuáció}
    \li{feltételezések}
    \ul{
        \li{hideg plazma, hőfluktuáció alapból kicsik}
        \li{nemlineáris hatásoktól eltekintünk}
    }
    \li{többfajta megközelítés, többfajta plazmamodell}
    \li{zavar matematikai modellje:}
    $$ \va(\vx,t) = \va(\vk, \omega) \exp{(i \vk \vx - i \omega t)}$$
    \li{fázis-sebesség: $\sub{\vv}{ph} = \omega \vk \pow{k}{-2}$
        csoportsebesség: $\sub{\vv}{gr} = \par{\vk} \omega$}
}

\h3{Nem előmágnesezett plazma}

\h4{Langmuir rezgések}

\ul{
    \li{\q{lomha} ionok, gyors elektronok, kis zavar}
    \li{elektronok ionokhoz képest oszcillálnak, plazmafrekvencia}
    $P_{e,i}^2 = n_{e,i} \pow{q_{e,i}}{2}\inv{(m_{e,i} \e0)}$
}


\h4{Langmuir hullám}

\ul{
    \li{figyelembe véve az elektronok hőnyomásának adiabatikus
        megváltozását a Newton-egyenletben és feltételezve konstans
        elektron hőmérékletet}
    $$ \omega_l^2 =  \sqrd{P_e} + \sqrd{k} \gamma_e
                     \sqrd{v}_{\text{thermal}} $$
    \li{\em{Langmuir diszperziós reláció}, ha az elektronok hőméréklete
        nem zérus az oszcillációk elkezdenek terjedni a plazmában
        &rarr; elektrosztatikus hullámok}
}

\h4{Ion-akusztikus hullámok}

\ul{
    \li{alacsony frekvenciákon az ionok rezgését is figyelembe kell venni,
        nyomásuk elhanyagolva}
    \li{protonok esetén $P_e \approx 40 P_i$, ilyen alacsony frekvencián az
        elektronok szinte azonnal reagálnak a változó elektromos mezőre
        &rarr; elektronok dinamikája: elektronok nyomása és Coulomb-erő ki kell
        egyenlítse egymást}
    \li{elektronok számsűrűség-eloszlása Boltzmann-szerű lesz}
    \li{\em{ion-akusztikus hullámok:} ugyanolyan tulajdonságúak mint a
        semleges gázban terjedő hanghullámok}
}


\center{
<table>
    \tr{
        \th{Mennyiség}
        \th{Egyenlet}
        \th{Plazma modell}
    }
    \tr{
        \td{Plazmafrekvencia, Langmuir rezgés}
        \td{$P_{e,i}^2 = n_{e,i} \pow{q_{e,i}}{2}\inv{(m_{e,i} \e0)}$}
        \td{Kvázineutrális, nem előmágnesezett plazma}
    }
    \tr{
        \td{Girofrekvencia}
        \td{$G_{e,i}^2 = q_{e,i} \cdot B \cdot \inv{m_{e,i}}$}
        \td{Előmágnesezett plazma, homogén mágneses tér}
    }
    \tr{
        \td{Langmuir hullám}
        \td{$\omega_l^2 =  \sqrd{P_e} + \sqrd{k} \gamma_e
                           \sqrd{v}_{\text{thermal}}$}
        \td{Kvázineutrális, nem előmágnesezett plazma, elektronok
            hőnyomásának változása figyelembe véve}
    }
    \tr{
        \td{Ion-akusztikus hullámok}
        \td{$ \sqrd{\omega_{ia}} = \gamma_e k_B T_e \inv{m_i} \sqrd{k}$}
        \td{Kvázineutrális, nem előmágnesezett plazma, elektronok
            hőnyomása egynsúlyban az Coulomb-erővel, ion hőnyomás
            elhanyagolva}
    }
    \tr{
        \td{Ordenáris elektromágneses hullámok}
        \td{$ \sqrd{\omega_{om}} = \sqrd{P_e} + \sqrd{c} \sqrd{k} $}
        \td{elektromágness hullám szabad térben, nem előmágnesezett plazma
            jelenléteben, hullám nem terjedhet $P_e$ alatt}
    }
    \tr{
        \td{Alfvén hullám}
        \td{$ \omega_A = \pm k_{\parallel} v_A $}
        \td{ideális MHD, erővonalak rezgése}
    }
    \tr{
        \td{Elektron whistler}
        \td{$ \omega_w = \sqrd{k} \sqrd{c} G_e \pow{P_e}{-2} $}
        \td{hideg mágnesezett elektron plazma, párhuzamos terjedés
            hosszú hullámú határeset (kis $k$)}
    }
    \tr{
        \td{Felső hibrid frekvencia}
        \td{$ \sqrd{h_u} = \sqrd{G_e} + \sqrd{P_e} $}
        \td{hideg mágnesezett elektron plazma, merőleges terjedés,
            ciklotron és plazma tulajdonságok keverednek}
    }
    \tr{
        \td{Alsó hibrid frekvencia}
        \td{$ \sqrd{h_l} = \sqrd{P_i} + \sqrd{G_i}
                            \inv{(1 + \sqrd{P_e} \pow{G_e}{-2})} $}
        \li{két folyadék elmélet, merőleges terjedés, $\omega \ll G_e$}
    }    
</table>
}


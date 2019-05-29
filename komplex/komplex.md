\include{html.gpp}

/*
\h1{Szeizmológia}
\include{seismo.md}

\h1{Geotermika}
\include{geotherm.md}

\h1{Földmágnesség}
\include{magneto.md}
*/

\h1{Gravitáció, földalak, változó forgás}

\h2{Föld nehézségi erőtere}

\ul{
    \li{tömegvonzási erő}
    $$ \mat{F} = -G \frac{Mm}{r^2} \frac{\mat{r}}{r} $$
    $$ \mat{F} = \mat{g} m $$
    \li{gravitációs térerősség}
    $$ \mat{g} = -G \frac{M}{r^2} \frac{\mat{r}}{r} $$
    \li{tömegvonzási potenciál}
    $$ V = - \frac{GM}{r} $$
    \li{centrifugális erő és potenciál}
    $$ \mat{F}_c = m \omega^2 \frac{\mat{p}}{p} $$
    $$ \mat{g}_c = \omega^2 \frac{\mat{p}}{p} $$
    $$ V_c = \half \omega^2 p^2 $$
    \li{tömegonzási potenciál}
    $$ U(r,\theta,\lambda) = \frac{GM}{r} \left\{ 
    1 - \sum_{n = 2}^{\infty} {\left(\frac{a}{r}\right)}^n
    [J_n P_n(\cos\theta) + \sum_{m=1}^{n} (J_n^m \cos m \lambda
    + K_n^m \sin m \lambda) P_n^m(\cos\theta)] \right\}
    + \frac{\omega^2 r^2}{2}\sin^2 \theta$$
    \li{$P_n(\cos\theta)$ - teljesen normalizált \em{Legendre-függvények}}
    \li{$m = 0$ zonális, $m \ne 0$ tesszerális, $m = n$ szektoriális harmonikusok}
    \li{mesterséges holdak pályaelem perturbációiból meghatározhatóak az együtthatók}
    
}

\h2{Földalak}

\ul{
    \li{elméleti földalak - célszerű választás: forgási ellipsziod (saját
    tömegvonzási erőterében forgó homogén folyadékszerű tömeg)}
    \li{lapultság: $f = \frac{a - c}{c}$, első numerikus excentricitás:
        $e^2 = \frac{a^2 - c^2}{c^2}$}
    \li{ekvipotenciális felületek nem ellipsziod alakúak}
    \li{Föld normál nehézségi erőtere: sorfejtésből csak zonális tagok}
    \li{normál nehézségi gyorsulás az ellipszoid felszínén}
    $$ g = g_E \left( 1 + f^* \sin^2\Phi - \frac{1}{4} f_4 \sin^2 2 \Phi \right) $$
    \li{$f^* = \frac{g_P - g_E}{g_E}$, $f_4 = \half(f^2 + 5 fm)$,
        $m = \frac{\omega^2 a^2 c}{GM}$}
    \li{Gauss javaslata: nyugalmi tengerszinttel egybeeső potenciálfelület
        legyen a Föld alakja, gyakorlatban max. 2 m eltérés a két felület
        között}
}

\h2{Gavitációs anomáliák}

\ul{
    \li{szabadlevegő korrekció, $h$: referncia felület feletti magasság}
    $$ g_{\text{free-air}} = \par{r}g h $$
    \li{szélességi korrekció, $x$: távolság a referencia állomástól,
        észkra pozitív}
    $$ g_{\text{free-air}} = \par{\Phi}g x $$
    \li{Bouger-korrekció}
    $$ g_{\text{bouger}} = 2\pi G \rhi h$$
}

\h2{Föld forgásának változása}

\ul{
    \li{\em{árapálysúrlódás} &rarr; szögsebesség csökkenés}
    \li{\em{luniszoláris precesszió}: egyenlítő nem esik egybe az ekliptika
        síkjával, Nap, Hold forgatónyomatéka &rarr; precesszió,
        $T = 26 000 \text{yr}$}
    \li{\em{planetáris precesszió:} Föld keringási pályasíkja változik &rarr;
        egynelítő és ekliptika közötti szög változik: $\deg{20} - \deg{24.5}$,
        $T = 40 000 \text{yr}$}
    \li{pólusmozgás: forgási pólus változik a Föld szilárd tömegéhez képest}
    \li{megfigyelése obszervatóriumokkal, Chandler 435 napos ciklus, 10 m-en
        belül, két komponens: 365 napos és 14 napos, Föld rugalmas
        tulajdonságainak figyelembe vétele}
}


/*
\h1{Föld körüli térség fizikája}
\include{space_phys.md}
*/
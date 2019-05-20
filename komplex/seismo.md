#include "latex.gpp"

#define @vp @mat(p)
#define @vu @mat(u)
#define @mdef @mat(\varepsilon)


## Bevezetés

- földrengések regisztrálása, Föld belső szerkezetének meghatározása
- földrengés komoly veszélyforrás, emberi életek
- legnagyobb történelmi földrengés: Lisszabon (1755); &approx; 60 000 halálos
áldozat; tűzvész és cunami; Skóciában, Skandináviában érezték hatását; becsült Richter magnitúdó: 8.75
- ESA ERS-1 műhold; 1992-es Szent András-törésvonal földrengés, 2-3 m-es
horizontális elmozdulás

<p><a href="https://commons.wikimedia.org/wiki/File:2D_geometric_strain.svg#/media/File:2D_geometric_strain.svg">
<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/2D_geometric_strain.svg/1200px-2D_geometric_strain.svg.png" width="600" alt="2D geometric strain.svg">
</center>
</a><br>By <a href="//commons.wikimedia.org/wiki/File:2D_geometric_strain.png" title="File:2D geometric strain.png">2D_geometric_strain.png</a>: <a href="//commons.wikimedia.org/wiki/User:Sanpaz" title="User:Sanpaz">Sanpaz</a>
derivative work: <a href="//commons.wikimedia.org/wiki/User:Mircalla22" title="User:Mircalla22">Mircalla22</a> (<a href="//commons.wikimedia.org/wiki/User_talk:Mircalla22" title="User talk:Mircalla22"><span class="signature-talk">talk</span></a>) - <a href="//commons.wikimedia.org/wiki/File:2D_geometric_strain.png" title="File:2D geometric strain.png">2D_geometric_strain.png</a>, Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=7680077">Link</a></p>

<img src="https://raw.githubusercontent.com/bozso/texfiles/master/images/SAR_Kilauea_topo_interferogram.jpg">

<p>
<a href="https://commons.wikimedia.org/wiki/File:Stress_Strain_Ductile_Material.png#/media/File:Stress_Strain_Ductile_Material.png">
<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/8/84/Stress_Strain_Ductile_Material.png" width="600" alt="Stress Strain Ductile Material.png">
</center>
</a><br>By Breakdown - <span class="int-own-work" lang="en">Own work</span>,<a href="http://creativecommons.org/licenses/by-sa/3.0/" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=3702892">Link</a></p>

## Deformációs tenzor

$$ \mdef _{ij} = \half (\partial_i u_j + \partial_j u_i ) $$
$$ \theta = \frac{\Delta V}{V} = \tr \mdef = \div \vu $$

## Rugalmas feszültség tenzor

## Általánosított Hooke-törvény
$$ p_{ij} = c_{ijkl} \mdef _{kl}$$

## Izotróp testek - Lamé-állandók:

$$ \lambda  = \frac{E \sigma}{ (1 + \sigma)(1 - 2\sigma)}$$
és
$$ \mu = \frac{E}{2(1 + \sigma)} $$
anyagi minőség, hőmérséklet, nyomás függvényei

$$ p_{ij} = \delta_{ij} \lambda \theta + 2 \mu \mdef _{ij} $$

vagy

$$ \vp = \lambda\theta \vu + 2 \mu \mdef $$

## Hullámegyenlet

$$ \rho \par{t}^2 \vu = \mat{f} + \div \vp $$
$$ \rho \par{t}^2 u_i = f_i + \par{j} p_{ij} $$

\define{gdiv_u}{\gdiv{\vu}}

$$ \par{i} p_{ij} = \lambda \delta_{ij} \par{j} \par{k} u_k  + \mu \par{j} (\par{i} u_j + \par{j} u_i) $$
$$ \par{j} p_{ij} = \lambda \par{i} \par{k} u_k  + \mu \par{j} \par{i} u_j + \mu \par{j} \par{j} u_i $$
$$ \div \vp = \lambda \gdiv_u  + \mu \gdiv_u + \mu \laplace \vu $$
$$ \laplace \vu = \gdiv_u - \rot \rot \vu $$
$$ \div \vp = (\lambda + 2 \mu) \gdiv_u  - \mu \rot \rot \vu $$
$$ \rho \par{t}^2 \vu = \mat{f} + (\lambda + 2 \mu) \gdiv_u  - \mu \rot \rot \vu $$

### Szeparálás

$$ \Theta = \div \vu $$
$$ \rho \par{t}^2 \Theta = (\lambda + 2 \mu) \laplace \Theta $$
$$ \par{t}^2 \Theta = \alpha^{-2} \laplace \Theta \hspace{25pt} \alpha = \sqrt{\frac{\lambda + 2 \mu}{\rho}} $$

$$ \phi = \rot \vu $$
$$ \rho \par{t}^2 \phi = \mu \laplace \phi $$
$$ \par{t}^2 \phi = \beta^{-2} \laplace \phi \hspace{25pt} \beta = \sqrt{\frac{\mu}{\rho}} $$

### Általános megoldás

\define{\vr}{\mat{r}}
\define{\vk}{\mat{k}}

$$ \Theta(\vr, t) = G(\vk \vr \pm c t) $$

Tipikus választás

$$ \Theta = \mat{A} \exp (i (\vk \vr \pm \omega t)) $$
$$ \vk = \frac{2 \pi}{\lambda} \mat{n} \hspace{25pt} \omega = \frac{2\pi}{T}$$

Fázissebesség: $ v_f = \frac{\omega}{k} $
Csoportsebesség: $ \mat{v} _g = \frac{\partial \omega}{\partial \vk} $

### Energiasűrűség

$$ e = \half \rho \omega^2 A^2 $$

## Rugalmas hullámok törése



\center{\imref{https://ds.iris.edu/spudservice/data/9991842?nolog=y}{PREM modell.}}

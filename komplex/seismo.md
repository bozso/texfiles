# Bevezetés

\(
    \def\laplace{{\mathop{}\!\mathbin\bigtriangleup}}
    \def\bold#1{{\bf #1}}
    \def\tr{{\mathrm{Tr} \hspace{2pt}}}
    \def\div{{\nabla \hspace{2pt}}}
    \def\gdiv#1{{\nabla \left(\nabla #1 \right) \hspace{2pt}}}
    \def\rot{{\nabla \times \hspace{2pt}}}
    \def\mat#1{{\mathbf{#1}}}
    \def\mdef{{\mathbf{\varepsilon}}}
    \def\half{{\frac{1}{2}}}
    \def\par#1{{\hspace{2pt} \partial_{#1}}}
\)

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

<p>
<a href="https://commons.wikimedia.org/wiki/File:Stress_Strain_Ductile_Material.png#/media/File:Stress_Strain_Ductile_Material.png">
<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/8/84/Stress_Strain_Ductile_Material.png" width="600" alt="Stress Strain Ductile Material.png">
</center>
</a><br>By Breakdown - <span class="int-own-work" lang="en">Own work</span>,<a href="http://creativecommons.org/licenses/by-sa/3.0/" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=3702892">Link</a></p>

Deformációs tenzor:
$$ \mdef_{ij} = \half (\partial_i u_j + \partial_j u_i ) $$
$$ \theta = \frac{\Delta V}{V} = \tr \mdef = \div\mat{u} $$

Rugalmas feszültség tenzor:

Általánosított Hooke-törvény:
$$ p_{ij} = c_{ijkl} \mdef_{kl}$$

Izotróp testek  
Lamé-állandók:
$$ \lambda  = \frac{E \sigma}{ (1 + \sigma)(1 - 2\sigma)}$$
és
$$ \mu = \frac{E}{2(1 + \sigma)} $$
anyagi minőség, hőmérséklet, nyomás függvényei

$$ p_{ij} = \delta_{ij} \lambda \theta + 2 \mu \mdef_{ij} $$

vagy

$$ \mat{p} = \lambda\theta\mat{I} + 2 \mu \mdef $$

$$ \rho \par{t}^2 \mat{u} = \mat{f} + \div\mat{p} $$
$$ \rho \par{t}^2 u_i = f_i + \par{j} p_{ij} $$

$$ \par{j} p_{ij} = \lambda \delta_{ij} \par{j} \par{k} u_k  + \mu \par{j} (\par{i} u_j + \par{j} u_i) $$
$$ \par{j} p_{ij} = \lambda \par{i} \par{k} u_k  + \mu \par{j} \par{i} u_j + \mu \par{j} \par{j} u_i $$
$$ \div \mat{p} = \lambda \gdiv{\mat{u}}  + \mu \gdiv{\mat{u}} + \mu \laplace \mat{u} $$
$$ \laplace \mat{u} = \gdiv{\mat{u}} - \rot \rot \mat{u} $$
$$ \div \mat{p} = (\lambda + 2\mu) \gdiv{\mat{u}}  - \mu \rot \rot \mat{u} $$
$$ \rho \par{t}^2 \mat{u} = qmat{f} + (\lambda + 2\mu) \gdiv{\mat{u}}  - \mu \rot \rot \mat{u} $$

Szeparálás:

$$ \Theta = \div \mat{u} $$
$$ \rho \par{t}^2 \Theta = (\lambda + 2\mu) \laplace \Theta $$
$$ \par{t}^2 \Theta = \alpha^{-2} \laplace \Theta \hspace{25pt} \alpha = \sqrt{\frac{\lambda + 2 \mu}{\rho}} $$

$$ \phi = \rot \mat{u} $$
$$ \rho \par{t}^2 \phi = \mu \laplace \phi $$
$$ \par{t}^2 \phi = \beta^{-2} \laplace \phi \hspace{25pt} \beta = \sqrt{\frac{\mu}{\rho}} $$





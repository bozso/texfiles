#! /usr/bin/env python

from os.path import join as pjoin
import gnuplot.gnuplot as gp
from tempfile import NamedTemporaryFile as tmp


def read_until(f, comp="\n"):
    current = f.readline()
    
    while comp != current:
        yield current
        current = f.readline()


def parse_kout(path):
    with open(path, "r") as f:
        line = f.readline()
        while "Matched solution" not in line:
            line = f.readline()
        
        f.readline()
        f.readline()
        f.readline()
        f.readline()
        
        los = "\n".join(line.strip() for line in read_until(f))
        
        gnss = "{} {}\t 0.0\t 0.0\t 0.0\t GNSS\n{}"\
               .format(los.split()[0], los.split()[1], f.readline())
        
    return los, gnss


def style_kalman(colors):
    lw = 4
    tpl = "set style line {num} lc rgb '{color}' pt 7 ps 0.75 lt 0 lw {lw}"
    
    gp.call(tpl.format(num=1, color=colors["red"], lw=lw))
    
    gp.call(tpl.format(num=2, color=colors["green"], lw=lw))

    gp.call(tpl.format(num=3, color=colors["blue"], lw=lw))
    
    
    lw = 4
    tpl = "set style line {num} lc rgb '{color}' pt 0 ps 2 lt 1 lw {lw}"
    
    gp.call(tpl.format(num=4, color=colors["red"], lw=lw))
    
    gp.call(tpl.format(num=5, color=colors["green"], lw=lw))
    
    gp.call(tpl.format(num=6, color=colors["blue"], lw=lw))


def style_los(colors):
    lw = 2
    tpl1 = "set style line {num} lc rgb '{color}' pt 7 ps 0.75 lt 1 lw {lw}"
    tpl2 = "set style line {num} lc rgb '{color}' pt 2 ps 0.75 lt 1 lw {lw}"
    
    gp.call(tpl1.format(num=1, color=colors["blue"], lw=lw))
    gp.call(tpl2.format(num=2, color=colors["darkblue"], lw=lw))
    gp.call(tpl1.format(num=3, color=colors["green"], lw=lw))
    gp.call(tpl2.format(num=4, color=colors["lightgreen"], lw=lw))


def plot(*stations, ref=None, rootdir=None, outdir=None, fontsize=15, term="eps",
         keypos="left top", gnss_range=None, los_range=None):
    
    colors = gp.nicer()
    
    gp.set("xlabel", "'Decimal year' font ',22'")
    
    #gp["key"] = "out horiz"
    gp.set("key", keypos)
    
    
    for station in stations:
        filename = pjoin(rootdir, "{}-{}_s_interpol.kout".format(station, ref))
        
        los, gnss = parse_kout(filename)
        
        gp.set("ylabel", "'Deformation [mm]' font ',22'")
        style_kalman(colors)
        
        with tmp("w", delete=False) as f1, tmp("w", delete=False) as f2:
            
            f1.write(los)
            f2.write(gnss)
            
            gp.output(pjoin(outdir, "%s-%s_kalman.png" % (station, ref)),
                      term=term, fontsize=fontsize)
                      
            #gp.ranges(y=gnss_range)
    
            gp.call("plot '{name1}' u 2:3 title 'North'    with lp ls 1,"
                    "     '{name1}' u 2:4 title 'East'    with lp ls 2,"
                    "     '{name1}' u 2:5 title 'Height' with lp ls 3,"
                    "     '{name2}' u 2:3 title 'GPS-North'     with lp ls 4,"
                    "     '{name2}' u 2:4 title 'GPS-East'     with lp ls 5,"
                    "     '{name2}' u 2:5 title 'GPS-Height'  with lp ls 6"
                    .format(name1=f1.name, name2=f2.name))
        
        asc_g = pjoin(rootdir, "%s-%s_g_asc.los" % (station, ref))
        dsc_g = pjoin(rootdir, "%s-%s_g_dsc.los" % (station, ref))
        
        asc_s = pjoin(rootdir, "{}-{}_s_asc.los".format(station, ref))
        dsc_s = pjoin(rootdir, "{}-{}_s_dsc.los".format(station, ref))

        gp.output(pjoin(outdir, "{}-{}_los.png".format(station, ref)),
                  term=term, fontsize=fontsize)
        
        style_los(gp, colors)
        gp["ylabel"] = "'LOS deformation [mm]' font ',22'"
        
        #gp.ranges(y=los_range)
        
        gp("plot '{}' u 2:3 title 'ASC Gamma'  with lp ls 1,"
           "     '{}' u 2:3 title 'ASC StaMPS' with lp ls 2,"
           "     '{}' u 2:3 title 'DSC Gamma'  with lp ls 3,"
           "     '{}' u 2:3 title 'DSC StaMPS' with lp ls 4"
           .format(asc_g, asc_s, dsc_g, dsc_s))



def plot_kalman(*stations, ref=None, rootdir=None, outdir=None, fontsize=15,
                term="eps", keypos="left top", ranges=None):

    gp.set("key", False)
    gp.set("xlabel", "'Decimal year since 2016' font ',%g'" % fontsize)
    
    gp.output(pjoin(outdir, "dszekcso_kalman.png"),
              term=term, fontsize=fontsize, size=(1200,500), enhanced=True)

    multi = gp.multiplot(len(stations), left=10, between=7.5, key_width=0.0,
                         width=20, ckeys=True)

    gp.set("ylabel", "'Deformation [mm]' font ',%g'" % fontsize)
    style_kalman(gp.nicer())
    

    for ii, station in enumerate(stations):
        filename = pjoin(rootdir, "%s-%s_s_interpol.kout" % (station, ref))
        
        los, gnss = parse_kout(filename)
        
        if ranges is not None:
            gp.ranges(y=ranges)
        
        
        with tmp("w", delete=False) as f1, tmp("w", delete=False) as f2:
            
            f1.write(los)
            f2.write(gnss)
            
            gp.title(r"Movement of reflector %s \nrelative to %s" % (station, ref))
            
            multi.plot(ii, "plot '{name1}' u ($2-2016):3 title 'North'      with lp ls 1,"
                           "     '{name1}' u ($2-2016):4 title 'East'       with lp ls 2,"
                           "     '{name1}' u ($2-2016):5 title 'Height'     with lp ls 3,"
                           "     '{name2}' u ($2-2016):3 title 'GPS-North'  with lp ls 4,"
                           "     '{name2}' u ($2-2016):4 title 'GPS-East'   with lp ls 5,"
                           "     '{name2}' u ($2-2016):5 title 'GPS-Height' with lp ls 6"
                           .format(name1=f1.name, name2=f2.name))
        
    gp.call("unset title")
    
    titles = ("North", "East", "Height", "GPS-North", "GPS-East", "GPS-Height")
    
    plot = ", ".join("2 title '%s' with lp ls %d" % (title, ii+1) for ii, title in enumerate(titles))
    
    gp.call(
    """
    set lmargin at screen %g
    set rmargin at screen 1
    set key center center
    set border 0
    unset tics
    unset xlabel
    unset ylabel
    set yrange [0:1]
    plot %s
    """ % (multi.margins(multi.nplot)[0] - 0.35, plot))

        
def main():
    
    term = "pngcairo"
    ext = "png"
    
    outdir = "/home/istvan/Dokumentumok/texfiles/images"
    root = "/home/istvan/Dokumentumok/texfiles/presentations/geomatika2018"
    
    #gp.debug()
    
    rootdir = root + "/dszekcso"
    plot_kalman("IB2", "IB3", "IB4", ref="IB1", rootdir=rootdir, outdir=outdir,
                term=term, fontsize=13, ranges=[-600,400])
    
    return 0
    
    rootdir = root + "/fonyod"
    plot("KV", "RE", ref="PH", rootdir=rootdir, outdir=outdir, term=term)

    rootdir = root + "/kulcs"
    plot("A1", "A2", "A3", "A4", ref="AR", rootdir=rootdir, outdir=outdir, term=term)
         


if __name__ == "__main__":
    main()

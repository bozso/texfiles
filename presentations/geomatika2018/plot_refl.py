#! /usr/bin/env python

from os.path import join as pjoin
from gnuplot import Gnuplot, linedef
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


def style_kalman(gp, colors):
    lw = 4
    tpl = "set style line {num} lc rgb '{color}' pt 7 ps 0.75 lt 0 lw {lw}"
    
    gp(tpl.format(num=1, color=colors["red"], lw=lw))
    
    gp(tpl.format(num=2, color=colors["green"], lw=lw))

    gp(tpl.format(num=3, color=colors["blue"], lw=lw))
    
    
    lw = 4
    tpl = "set style line {num} lc rgb '{color}' pt 0 ps 2 lt 1 lw {lw}"
    
    gp(tpl.format(num=4, color=colors["red"], lw=lw))
    
    gp(tpl.format(num=5, color=colors["green"], lw=lw))

    gp(tpl.format(num=6, color=colors["blue"], lw=lw))


def style_los(gp, colors):
    lw = 2
    tpl1 = "set style line {num} lc rgb '{color}' pt 7 ps 0.75 lt 1 lw {lw}"
    tpl2 = "set style line {num} lc rgb '{color}' pt 2 ps 0.75 lt 1 lw {lw}"
    
    gp(tpl1.format(num=1, color=colors["blue"], lw=lw))
    gp(tpl2.format(num=2, color=colors["darkblue"], lw=lw))
    gp(tpl1.format(num=3, color=colors["green"], lw=lw))
    gp(tpl2.format(num=4, color=colors["lightgreen"], lw=lw))


def plot(*stations, ref=None, rootdir=None, outdir=None, fontsize=15, term="eps",
         keypos="left top", gnss_range=None, los_range=None):
    
    gp = Gnuplot(debug=0)
    colors = gp.nicer()

    
    gp["xlabel"] = "'Decimal year' font ',22'"
    
    gp["key"] = "out horiz"
    gp["key"] = keypos
    
    
    for station in stations:
        filename = pjoin(rootdir, "{}-{}_s_interpol.kout".format(station, ref))
        
        los, gnss = parse_kout(filename)
        
        gp["ylabel"] = "'Deformation [mm]' font ',22'"
        style_kalman(gp, colors)
        
        
        
        with tmp("w", delete=False) as f1, tmp("w", delete=False) as f2:
            
            f1.write(los)
            f2.write(gnss)
            
            gp.output(pjoin(outdir, "{}-{}_kalman.png".format(station, ref)),
                      term=term, fontsize=fontsize)
                      
            #gp.ranges(y=gnss_range)
    
            gp("plot '{name1}' u 2:3 title 'North'    with lp ls 1,"
               "     '{name1}' u 2:4 title 'East'    with lp ls 2,"
               "     '{name1}' u 2:5 title 'Height' with lp ls 3,"
               "     '{name2}' u 2:3 title 'GPS-North'     with lp ls 4,"
               "     '{name2}' u 2:4 title 'GPS-East'     with lp ls 5,"
               "     '{name2}' u 2:5 title 'GPS-Height'  with lp ls 6"
               .format(name1=f1.name, name2=f2.name))
        
        asc_g = pjoin(rootdir, "{}-{}_g_asc.los".format(station, ref))
        dsc_g = pjoin(rootdir, "{}-{}_g_dsc.los".format(station, ref))
        
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
        
        
def main():
    
    term = "pngcairo"
    ext = "png"
    
    outdir = "/home/istvan/Dokumentumok/texfiles/images"
    root = "/home/istvan/Dokumentumok/texfiles/presentations/geomatika2018/network_hu"
    
    
    rootdir = root + "/fonyod"
    plot("KV", "RE", ref="PH", rootdir=rootdir, outdir=outdir, term=term)

    rootdir = root + "/kulcs"
    plot("A1", "A2", "A3", "A4", ref="AR", rootdir=rootdir, outdir=outdir, term=term)
         

    rootdir = root + "/dszekcso"
    plot("IB2", "IB3", "IB4", ref="IB1", rootdir=rootdir, outdir=outdir, term=term)

if __name__ == "__main__":
    main()

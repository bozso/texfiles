filename=bozsoi_ps_csomad

pdf:
	pdflatex ${filename}
	bibtex ${filename}||true
	pdflatex ${filename}
	pdflatex ${filename}

read:
	evince ${filename}.pdf &

clean:
	rm *.aux *.blg *.out *.bbl *.log *.lof *.lot *.toc

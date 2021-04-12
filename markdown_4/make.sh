pandoc notes.md \
--toc \
--toc-depth=2 \
--number-sections \
--bibliography ref_list.bib \
--variable pagestyle=headings \
--variable classoption=twocolumn \
--variable papersize=a4paper \
--variable fontfamily=arev \
--output=notes.pdf


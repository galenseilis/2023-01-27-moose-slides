LATEXMK ?= latexmk
PYTHON ?= python3

TARGET  := slides
OUTDIR  := build
RELEASE := 2023-01-27_Galen_Seilis_moose_orientation.pdf

.PHONY: all sem clean

all: $(RELEASE)

$(OUTDIR)/$(TARGET).pdf: $(TARGET).tex $(wildcard figures/*/*) | $(OUTDIR)
	$(LATEXMK) -pdf -shell-escape -interaction=nonstopmode -halt-on-error \
		-outdir=$(OUTDIR) $(TARGET).tex

$(RELEASE): $(OUTDIR)/$(TARGET).pdf
	cp $< $@

$(OUTDIR):
	mkdir -p $@

sem:
	$(PYTHON) scripts/dag.py

clean:
	rm -rf $(OUTDIR) _minted-$(TARGET)

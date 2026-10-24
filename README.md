# A Moosy Proposal

Slides for a talk presented on **27 January 2023** to Roy Rea at the University of Northern British Columbia (UNBC). The talk proposes using citizen science and Bayesian hierarchical models to estimate the average direction of moose travel from weak, locally observed indicators.

The presentation covers:

- the motivation for citizen-science data collection;
- field indicators of moose orientation (tracks, snapped plants, chewed bark and buds, scat, and wildlife cameras);
- covariates and confounds such as wind, slope, aspect, vegetation, and snowmelt;
- Bayesian and multilevel modelling approaches;
- opportunities for collaboration.

## Repository layout

```text
.
├── slides.tex                 LaTeX source for the presentation
├── Makefile                   Build, clean, and figure-regeneration targets
├── README.md
├── LICENSE                    GNU General Public License v3.0
├── 2023-01-27_..._orientation.pdf   Prebuilt release copy of the slides
├── figures/
│   ├── background/            Title, context, and motivation images
│   ├── indicators/            Field photos of moose indicators
│   ├── model/                 Structural-equation-model diagram (sem.pdf)
│   ├── icons/                 Small UI/icon images used in the slides
│   └── unused/                Assets not currently referenced by slides.tex
└── scripts/
    └── dag.py                 Regenerates the SEM diagram with semopy
```

All image paths in `slides.tex` are relative to the repository root. When adding an image, place it in the most appropriate `figures/` subdirectory and reference it with the full relative path.

## Building the slides

### Requirements

- A reasonably complete TeX Live installation with `beamer`, `tcolorbox`, `minted`, `pgf`/TikZ, `tikzlings`, `smartdiagram`, `algorithm2e`, `ccicons`, `booktabs`, `colortbl`, `pifont`, `xstring`, `ifoddpage`, `relsize`, `listings`, `pdfcol`, and `tikzfill`.
- `latexmk`
- Pygments (`pygmentize`) if the `pythoncode` minted environment is used.
- On newer TeX Live releases, minted may require the `latexminted` Python package (`python3 -m pip install latexminted`).

On Debian/Ubuntu, the following is a good starting point:

```bash
sudo apt install latexmk texlive-latex-recommended texlive-latex-extra \
  texlive-science texlive-pictures texlive-fonts-extra python3-pygments
```

### Build

From the repository root:

```bash
make
```

This compiles `slides.tex` into `build/slides.pdf` and copies the result to the release filename in the repository root. The build uses `-shell-escape` because the document loads the `minted` package.

To compile directly without `make`:

```bash
latexmk -pdf -shell-escape -interaction=nonstopmode -halt-on-error \
  -outdir=build slides.tex
```

To remove all generated build files:

```bash
make clean
```

## Regenerating the SEM figure

The diagram at `figures/model/sem.pdf` is generated from the model description in `scripts/dag.py` using [semopy](https://semopy.com/) and Graphviz.

```bash
python3 -m pip install semopy
sudo apt install graphviz   # if graphviz is not already installed
make sem
```

The script writes both `figures/model/sem.pdf` (used by the slides) and a Graphviz `.dot` file named `figures/model/sem` (ignored by git).

## Notes on assets

Images credited in the slides retain their original licenses and attributions. The presentation source and build tooling are distributed under the terms of the GNU General Public License v3.0; see [LICENSE](LICENSE).

Files in `figures/unused/` are kept for reference but are not part of the current presentation.

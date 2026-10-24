from pathlib import Path

import semopy

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "figures" / "model" / "sem.pdf"

desc = '''
orientation =~ tracks + snappedplants + chewedbark + chewedbuds + scat + cameras + aspect
scat ~ wind + slope + aspect + vegetation + snowmelt + debris
tracks ~ debris + vegetation + snowmelt

disturbance =~ scat
'''

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

model = semopy.Model(desc)
semopy.semplot(model, str(OUTPUT), plot_covs=True, plot_exos=True)

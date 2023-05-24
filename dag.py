import semopy

desc = '''
orientation =~ tracks + snappedplants + chewedbark + chewedbuds + scat + cameras + aspect
scat ~ wind + slope + aspect + vegetation + snowmelt + debris
tracks ~ debris + vegetation + snowmelt

disturbance =~ scat
'''

m = semopy.Model(desc)
g = semopy.semplot(m, 'sem.pdf', plot_covs=True, plot_exos=True)

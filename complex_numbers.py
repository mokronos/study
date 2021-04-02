import matplotlib.pyplot as plt, mpld3

fig = plt.figure()
plt.plot([2,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
html = mpld3.fig_to_html(fig)

mpld3.save_html(fig, "complex_plane.html")


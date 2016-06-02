__author__ = "Horea Christian"
__license__ = "BSD"

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from nilearn import plotting
from os import path

plt.style.use('ggplot')

def main(stat_map="nii/tstat.nii.gz", template="~/NIdata/templates/medres_QBI_chr.nii.gz", black_bg=False, cut_coords=(-50,8,45)):
	template = path.expanduser(template)

	colors_plus = plt.cm.autumn(np.linspace(0., 1, 128))
	colors_minus = plt.cm.winter(np.linspace(0, 1, 128))
	colors = np.vstack((colors_minus, colors_plus[::-1]))

	mymap = mcolors.LinearSegmentedColormap.from_list('my_colormap', colors)

	for i in ['none', 'nearest', 'bilinear', 'bicubic', 'spline16','spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric','catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']:
		display = plotting.plot_stat_map(stat_map, bg_img=template,threshold=2.5, vmax=40, cmap=mymap, black_bg=black_bg, cut_coords=cut_coords, annotate=True, title=i+" interpolation", draw_cross=False, interpolation=i)
		plt.savefig(i, dpi=700)

if __name__ == '__main__':
	main()

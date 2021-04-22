# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 11:53:15 2021

@author: AMIT
"""

from skimage import exposure
import matplotlib.pyplot as plt_imshow
import cv2
import matplotlib.pyplot as plt

scr = cv2.imread(r"C:\Users\AMIT\Desktop\source1.png")
ref = cv2.imread(r"C:\Users\AMIT\Desktop\source2.png")

# determine if we are performing multichannel histogram matching
# and then perform histogram matching itself
print("[INFO] performing histogram matching...")
multi = True if scr.shape[-1] > 1 else False
matched = exposure.match_histograms(scr, ref, multichannel=multi)

# show the output images
cv2.imshow("Source", scr)
cv2.imshow("Reference", ref)
cv2.imshow("Matched", matched)



# construct a figure to display the histogram plots for each channel
# before and after histogram matching was applied
(fig, axs) =  plt.subplots(nrows=3, ncols=3, figsize=(8, 8))
# loop over our source image, reference image, and output matched
# image
for (i, image) in enumerate((scr, ref, matched)):
	# convert the image from BGR to RGB channel ordering
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	# loop over the names of the channels in RGB order
	for (j, color) in enumerate(("red", "green", "blue")):
		# compute a histogram for the current channel and plot it
		(hist, bins) = exposure.histogram(image[..., j],
			source_range="dtype")
		axs[j, i].plot(bins, hist / hist.max())

		# compute the cumulative distribution function for the
		# current channel and plot it
		(cdf, bins) = exposure.cumulative_distribution(image[..., j])
		axs[j, i].plot(bins, cdf)

		# set the y-axis label of the current plot to be the name
		# of the current color channel
		axs[j, 0].set_ylabel(color)
  
# set the axes titles
axs[0, 0].set_title("Source")
axs[0, 1].set_title("Reference")
axs[0, 2].set_title("Matched")

cv2.waitKey(0)
cv2.destroyAllWindow()
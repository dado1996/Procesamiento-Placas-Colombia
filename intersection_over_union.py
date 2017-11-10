from collections import namedtuple
import numpy as np
import cv2

def bb_intersection_over_union(a, b):
	xA = max(a[0],b[0])
	yA = max(a[1],b[1])
	xB = max(a[2],b[1])
	yB = max(a[3],b[3])

	interArea = (xB - xA + 1) * (yB - yA + 1)

	a_Area = (a[2] - a[0] + 1) * (a[3] - a[1] + 1)
	b_Area = (b[2] - b[0] + 1) * (a[3] - a[1] + 1)

	iou = interArea / float(a_Area + b_Area - interArea)

	return iou

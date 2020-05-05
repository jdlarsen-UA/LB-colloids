import os
from lb_colloids import PSphere
import matplotlib.image as mpimg
import numpy as np


ws = os.path.abspath(os.path.dirname(__file__))
data = os.path.join(ws, "..", "data")
outpth = os.path.join(ws, "temp")


def test_psphere():
	grain_radius = 20
	porosity = 0.40
	dimension = 200
	sensitivity = 0.01

	psp = PSphere(radius=grain_radius, porosity=porosity,
				  dimension=dimension, sensitivity=sensitivity)

	matrix = psp.get_matrix()
	mpor = PSphere.static_porosity(matrix)

	if (porosity - sensitivity) <= mpor <= (porosity + sensitivity):
		pass
	else:
		raise AssertionError("Porosity out of defined tolerance")

	if not psp.percolates:
		raise AssertionError("Porous media does not percolate")

	porosity = 0.25

	psp = PSphere(radius=grain_radius, porosity=porosity,
				  dimension=dimension, sensitivity=sensitivity)

	mpor = psp.matrix_porosity

	if (porosity - sensitivity) <= mpor <= (porosity + sensitivity):
		pass
	else:
		raise AssertionError("Porosity out of defined tolerance")

	if not psp.percolates:
		raise AssertionError("Porous media does not percolate")

	psp.save_image(os.path.join(outpth, "psphere_test.png"))

	img = mpimg.imread(os.path.join(outpth, "psphere_test.png"))
	img_matrix = np.array(img[:, :, 0], dtype=bool)

	img_por = PSphere.static_porosity(img_matrix)

	if abs(mpor - img_por) > sensitivity:
		raise AssertionError("Porous media not written to disk correctly")


def test_lb_image():
	pass


def test_lb_model():
	pass
	
	
def test_colloid_model():
	pass
	

if __name__ == "__main__":
	test_psphere()

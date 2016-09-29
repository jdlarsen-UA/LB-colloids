#!/bin/bash

python LB_2Dimage.py -i 2D_64_255.png -c f0,s255 -o 64f-tstr.hdf5 -b 10
#python LB_2Dimage.py -i synthetic.png -c f255,s0 -o tstr.hdf5 -b 10

python LB_2Dpermeability.py -i 64f-tstr.hdf5 -n 501  -q 100 -p 50 -f ftestr -u pu
#python LB_2Dpermeability.py -i tstr.hdf5 -n 3001  -q 100 -p 50 -f testr -k f

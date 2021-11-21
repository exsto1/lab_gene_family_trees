import os
from subprocess import run
infile = "temp/msa_new.phylip"
outfile = "temp/msa_new_tree.tre"

# run(f"/home/exsto/PHYML/PhyML-3.1/PhyML-3.1_linux64 -i {infile} -d aa", shell=True)
# run(f"/home/exsto/MPBOOT/mpboot-sse-1.1.0-Linux/bin/mpboot -s {infile} -st AA", shell=True)
# run(f"/home/exsto/FASTME/fastme-2.1.5/binaries/fastme-2.1.5-linux64 --input_data {infile} -p ", shell=True)
run(f"/home/exsto/FASTME/fastme-2.1.5/binaries/fastme-2.1.5-linux64 -i {infile} -p -o nj_tree.tre -m N", shell=True)
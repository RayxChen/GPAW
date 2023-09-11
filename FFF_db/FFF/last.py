import os
from ase.io import read, write

print(os.getcwd())

atoms = read("./ab.traj", index=-1)

write("./a1.traj", atoms)

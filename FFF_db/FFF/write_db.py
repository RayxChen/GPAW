from ase.io import read, write
import numpy as np
import ase.db
from ase.db import connect
from pathlib import Path

d = {"AABB_octa":"8EtFeP_AABB", "ABAB_octa":"8EtFeP_ABAB", "tetra":"4PhFeP",
     "pc":"FePC", "cl_pc":"16ClFePC", "cooh_pc":"4CO2HFePC", "nh2_pc":"4NH2FePC"}

p = Path('./')

name_db='MacrocyclesOptimised'
con = ase.db.connect(name_db+'.db')


for species in p.iterdir():
    if species.is_dir():
        for x in species.iterdir():
            if x.is_dir():
                if species.stem != 'base':
                    atoms = read(f'{x}/a1.traj')
                    save_name = d[x.stem] + '_' + species.stem
                    print(save_name)
                    con.write(atoms, name=save_name)
                else:
                    for y in {'m0', 'm2'}:
                        atoms = read(f'{x}/{y}/a1.traj')
                        save_name = d[x.stem] + '_' + y
        
                        print(save_name)
                        con.write(atoms, name=save_name)
        
    

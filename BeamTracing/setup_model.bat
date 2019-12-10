echo off

python surf_coord_abs.py --surf=beam --pxyz=0 0 0 --rxyz=0.1 0.1 0
python surf_coord_axs.py --refe=beam --surf=surf1_beam 
python surf_coord_axs.py --refe=surf1_beam --surf=surf1_beam_rght --pxyz=-10 0 0 --rxyz=-0.5 0 0
python surf_coord_axs.py --refe=surf1_beam --surf=surf1_beam_left --pxyz=10 0 0 --rxyz=0.5 0 0
python surf_coord_axs.py --refe=surf1_beam --surf=surf1_beam_uppr --pxyz=0 10 0 --rxyz=0 0.5 0
python surf_coord_axs.py --refe=surf1_beam --surf=surf1_beam_bott --pxyz=0 -10 0 --rxyz=0 -0.5 0

python surf_coord_abs.py --surf=surf1 --pxyz=-50 0 0 --rxyz=0 0 0
python surf_coord_abs.py --surf=surf2 --pxyz=-25 0 500 --rxyz=0 180 0
python surf_coord_abs.py --surf=surf3 --pxyz=500 0 500 --rxyz=0 0 0
python surf_coord_abs.py --surf=surf4 --pxyz=500 0 1000 --rxyz=0 0 0

python surf_coord_rel.py --surf=surf1 --rxyz=0 0 0
python surf_coord_rel.py --surf=surf2 --rxyz=0 -45 0
python surf_coord_rel.py --surf=surf3 --rxyz=0 -45 0
python surf_coord_rel.py --surf=surf4 --rxyz=0 0 0

python surf_coord_rel.py --surf=surf2 --rxyz=0 0.1 0

python surf.py --surf=surf1 --lxy=100 100 --nxy=200 200 --rxy=0 0
python surf.py --surf=surf2 --lxy=150 150 --nxy=200 200 --rxy=1000 1500
python surf.py --surf=surf3 --lxy=200 200 --nxy=200 200 --rxy=250 500
python surf.py --surf=surf4 --lxy=200 200 --nxy=200 200 --rxy=0 0

python surf_stp.py --surf=surf1
python surf_stp.py --surf=surf2
python surf_stp.py --surf=surf3
python surf_stp.py --surf=surf4

python ray_trace.py
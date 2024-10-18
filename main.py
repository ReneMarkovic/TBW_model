import numpy as np
import matplotlib.pyplot as plt
import sys
from TWB import model, vizualizacija, analiza
from tqdm.auto import tqdm as tqdm

## Globalni parametri simulacije

global Sth,Velikost_plazu, TFIN,cx,cy
Velikost_plazu = 0#Spremenljivka, ki beleži čez koliko celic se je plaz razširil.
Nx=51 #Število razdelkov na x osi
Ny=51 #Število razdelkov na y osi

T_FIN=10_000 #Število iteracij
START=int(0.8*T_FIN) #Število iteracij, ki se zanemarijo

Sth=4 #Mejna vrednost strmine, ki sproži plaz
cx=int(Nx/2) #x lega kjer se spuiščajo zrna peska
cy=int(Ny/2) #y lega kjer se spuiščajo zrna peska
pos=[cx,cy] #seznam leg, kjer se spuščajo zrna peska
st_zrn=4 #ŠTevilo zrn, ki se na vsako lokacijo spussti v vsaki iteraciji


pbar = tqdm(total=T_FIN)

#model.run_model(Nx = Nx, Ny = Ny, pos = pos, st_zrn = st_zrn, TFIN = T_FIN, Sth = Sth)
plazovi, dt, S = model.run_model(Nx, Ny, pos, st_zrn, T_FIN, Sth, pbar)

save_figure=True
vizualizacija.Fig_1(plazovi,S,Sth,START,save_figure)
vizualizacija.Fig_2(dt,plazovi,START,save_figure)
vizualizacija.Fig_3(plazovi,START,save_figure)
# #############################################################################
#  Code for the manuscript:
#
# Molecular docking coupled with machine learning to screen inhibitors 
# of SARS-CoV-2: A comprehensive analysis of the structure of the 
# potential ligands 
#
# Lilian Caroline Kramer Biasi, Opalina Vetrichelvan, 
# Luís Fernando Mercier Franco
#            
# This code presents a graphical interface for the prediction of the binding 
# energy with different variants of the SARS-CoV-2 spike protein, for more 
# information see our manuscript
#                                                                              
# Version number: 1.0.0                                                        
# #############################################################################
#                      University of Campinas (Unicamp)              
#                      School of Chemical Engineering               
#                                                                              
#                 --------------------------------------           
#                  Developer:  Lilian Caroline Kramer Biasi
#                  Supervisor: Luís Fernando Mercier Franco         
#                 --------------------------------------     
#                  Created on February 3rd, 2021      
#                  Disponible online on January 19th, 2022     
#               
# #############################################################################
# Disclaimer note: 
# Authors assume no responsibility or liability for the use of this code.      
# #############################################################################
# Input file:
#
# - Excel file containing the molecular docking results.
#
# #############################################################################

import pandas as pd
import sklearn.ensemble
#import sklearn.metrics
import tkinter as tk
from tkinter import ttk


#---------- 7KDJ ---------------------------------------
read_file1 = pd.read_excel ("Supplementary Table.xlsx", sheet_name='PDB 7KDJ')
df1 = pd.DataFrame(read_file1)

X21 = df1[['Number of rings', 'Number of heavy atoms',
           'Fraction of C atoms that are SP3 hybridized', 
           'Number of rotatable bonds', 'Number of aromatic carbocycles',
           'Number of hydrogen bond donors']]
Y21 = df1["Binding affinity (kcal/mol)"]

X21 = X21.astype(float)
Y21 = Y21.astype(float)

X21_train, X21_validation, y21_train, y21_validation = sklearn.model_selection.train_test_split(
        X21, Y21, test_size = 0.2, random_state = 0)

m1 = sklearn.ensemble.RandomForestRegressor(n_estimators=500,max_features = 0.6,
                                            bootstrap=False, n_jobs=-1)
m1.fit(X21_train, y21_train)

# -------------------- de Oliveira---------------------------------------------
read_file2 = pd.read_excel ("Supplementary Table.xlsx", 
                            sheet_name='de Oliveira et al.')
df2 = pd.DataFrame(read_file2)


X22 = df2[['Number of rings', 'Number of heavy atoms',
           'Fraction of C atoms that are SP3 hybridized', 
           'Number of rotatable bonds', 'Number of aromatic carbocycles',
           'Number of hydrogen bond donors']]
Y22 = df2["Binding affinity (kcal/mol)"]

X22 = X22.astype(float)
Y22 = Y22.astype(float)

X22_train, X22_validation, y22_train, y22_validation = sklearn.model_selection.train_test_split(
        X22, Y22, test_size = 0.2, random_state = 0)

m2 = sklearn.ensemble.RandomForestRegressor(n_estimators=500,max_features = 0.6, 
                                            bootstrap=False, n_jobs=-1)
m2.fit(X22_train, y22_train)

#----------------------- 6VSB ------------------------------------
read_file3 = pd.read_excel ("Supplementary Table.xlsx", sheet_name='PDB 6VSB')
df3 = pd.DataFrame(read_file3)

X23 = df3[['Number of rings', 'Number of heavy atoms',
           'Fraction of C atoms that are SP3 hybridized', 
           'Number of rotatable bonds', 'Number of aromatic carbocycles',
           'Number of hydrogen bond donors']]
Y23 = df3["Binding affinity (kcal/mol)"]

X23 = X23.astype(float)
Y23 = Y23.astype(float)

X23_train, X23_validation, y23_train, y23_validation = sklearn.model_selection.train_test_split(
        X23, Y23, test_size = 0.2, random_state = 0)

m3 = sklearn.ensemble.RandomForestRegressor(n_estimators=500,max_features = 0.6, 
                                            bootstrap=False, n_jobs=-1)
m3.fit(X23_train, y23_train)


def calculo():
    try:
        ring=float(ringe.get())
    except:
        ring=0
    try:
        HA=float(HAe.get())
    except:
        HA=0
    try:
        SP3=float(SP3e.get())
    except:
        SP3=0
    try:
        rot=float(rote.get())
    except:
        rot=0
    try:
        Hd=float(Hde.get())
    except:
        Hd=0
    try:
        arom=float(arome.get())
    except:
        arom=0
     
    spike=str(spikechoosen.get())
    
    if spike ==' 7KDJ':
        energy= round(m1.predict([[ring, HA, SP3, rot, Hd, arom]])[0], 1)
        mostrar_x.set("Binding affinity = "+str(energy) + " kcal/mol")
    elif spike == ' de Oliveira et al. (2020)':
        energy= round(m2.predict([[ring, HA, SP3, rot, Hd, arom]])[0], 1)
        mostrar_x.set("Binding affinity = "+str(energy) + " kcal/mol")
    elif spike == ' 6VSB':
        energy= round(m3.predict([[ring, HA, SP3, rot, Hd, arom]])[0], 1)
        mostrar_x.set("Binding affinity = "+str(energy) + " kcal/mol")
    else:
        mostrar_x.set("Please select a spike variant")
        



    
#---------------interface -----------------------------------
  
app = tk.Tk()
app.title("Binding affinity [kcal/mol]")
app.geometry('720x380')


mostrar_x = tk.IntVar()

# Label
tk.Label(app, text = "Select the Spike variant :",
         font = ("Times New Roman", 10)).grid(column = 0,
         row = 1, padx = 10, pady = 25)
  
# Combobox creation
n = tk.StringVar()
spikechoosen = ttk.Combobox(app, width = 27, textvariable = n)
  
# Adding combobox drop down list
spikechoosen['values'] = (' de Oliveira et al. (2020)', ' 6VSB', ' 7KDJ')
  
spikechoosen.grid(column = 1, row = 1)
spikechoosen.current()


# Reading the ligand features:
tk.Label(app, text='Please enter the values* of:' , height = 1).grid(row=3,
        column=1)

tk.Label(app, text='*NOTE: One can use RDKit Python`s library to count these '
         + 'numbers', height = 1, font=('Ariel', 7), foreground="gray").grid(
                 row=4,column=1)


tk.Label(app, text='Number of rings' , height = 1).grid(row=5,column=0)
ringe = tk.Entry (app,width=18)
ringe.grid(row=5,column=1)


tk.Label(app, text='Number of heavy atoms' , height = 1).grid(row=6,column=0)
HAe = tk.Entry (app,width=18)
HAe.grid(row=6,column=1)

tk.Label(app, text='Fraction of carbon atoms that are sp³ hybridized', 
         height = 1).grid(row=7,column=0)
SP3e = tk.Entry (app,width=18)
SP3e.grid(row=7,column=1)

tk.Label(app, text='Number of rotatable bonds' , height = 1).grid(row=8,
        column=0)
rote = tk.Entry (app,width=18)
rote.grid(row=8,column=1)

tk.Label(app, text='Number of hydrogen bond donors' , height = 1).grid(row=9,
        column=0)
Hde = tk.Entry (app,width=18)
Hde.grid(row=9,column=1)

tk.Label(app, text='Number of aromatic carbocycles' , height = 1).grid(row=10,
        column=0)
arome = tk.Entry (app,width=18)
arome.grid(row=10,column=1)

tk.Label(app, text='' , height = 1, font=('Ariel', 5)).grid(row=11,column=0)
tk.Label(app, text='' , height = 1, font=('Ariel', 5)).grid(row=12,column=0)

# Computing the result:
tk.Button(app,text="Estimate the binding energy",width=22,command = calculo, 
          font=('Ariel', 11, 'bold')).grid(row=13, column=0)

tk.Label(app, textvariable = mostrar_x, font=('Ariel', 11, 'bold')).grid(
        row=13, column=1)

# Acknowledgment:
tk.Label(app, text='' , height = 1, font=('Ariel', 5)).grid(row=20,column=0)
tk.Label(app, text='' , height = 1, font=('Ariel', 8)).grid(row=20,column=1)

tk.Label(app, text='Thank you for using the graphical interface developed by '+
         'Lilian Caroline Kramer Biasi' , height = 1, font=('Ariel', 8),
         foreground="gray").grid(row=23,column=1)

tk.Label(app, text='This interface use the data from the manuscript DOI: '
         + '(to be published)' , height = 1, font=('Ariel', 8),
         foreground="gray").grid(row=24,column=1)

tk.Label(app, text='In case of doubts and suggestions e-mail to: '
         +'lilian.biasi@outlook.com ' , height = 1, font=('Ariel', 8),
         foreground="gray").grid(row=25,column=1)

tk.Label(app, text='Laboratory of Complex Systems Engineering - University of '
         + 'Campinas' , height = 1, font=('Ariel', 8),
         foreground="gray").grid(row=26,column=1)


app.mainloop()

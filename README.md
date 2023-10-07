# A Graphical User Interface (GUI) for prediction of SARS-CoV-2 spike protein binding energy with different ligands


```
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣴⣶⡆⠀⣶⣶⣦⣤⣤⣄⠀ ⢠⣾⣿⣦
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⢰⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⡄⠘⢿⣿⠟
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣧⠀⢻⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⠂⢠⣠⣤⣶⣦⡀
                                    ⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣇⠈⢿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⠏⢀⣿⣿⣿⣿⣿⣿⣦⡀
                                    ⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⡆⠘⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⡏⠀⣾⣿⣿⣿⣿⣿⣿⡿⠋⢀
                                    ⠀⠀⠀⣴⣿⣦⡀⠙⢿⣿⣿⣿⣿⣿⣿⡄⠸⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⡟⠀⣼⣿⣿⣿⣿⣿⣿⠟⢀⣴⣿⣧
                                    ⠀⠀⣼⣿⣿⣿⣿⣦⡀⠙⢿⣿⣿⣿⣿⣷⡀⢹⣿⣿⣿⡇⠀⣿⣿⣿⡿⠁⣰⣿⣿⣿⣿⣿⠟⢁⣴⣿⣿⣿⣿⣧
                                    ⠀⣼⣿⣿⣿⣿⣿⣿⣿⣦⡀⠙⢿⣿⣿⣿⣧⠀⢻⣿⣿⡇⠀⣿⣿⣿⠃⢰⣿⣿⣿⣿⠟⢁⣴⣿⣿⣿⣿⣿⣿⣿⣧
                                    ⠀⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠙⢿⣿⣿⣇⠀⢿⣿⡇⠀⣿⣿⠇⢠⣿⣿⣿⠟⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠃
                                    ⣼⣶⣤⣄⡈⠙⠛⠿⣿⣿⣿⣿⣿⣦⡀⠙⢿⣿⡆⠈⠛⠃⠀⠛⠋⠀⣾⣿⠟⠁⣠⣾⣿⣿⣿⣿⡿⠿⠛⠉⣀⣠⣴⣶⡄
                                    ⣿⣿⣿⣿⣿⣿⣶⣤⣀⡉⠙⠻⢿⣿⣿⣦⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⢠⣾⣿⣿⠿⠛⠋⢁⣠⣴⣶⣿⣿⣿⣿⣿⣿⡀
                                    ⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⠉⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠋⢁⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧
                                    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⣠⣶⣄
                                    ⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡄⠀ ⢻⣿⣿⡿
                                    ⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠂⠀⠈⠙⠋
                                    ⠀⠀⠘⣿⣿⣿⣿⣿⠿⠛⠋⢁⣠⣤⣶⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋
                                    ⠀⠀⠀⠘⠟⠋⢉⣀⣤⣶⣿⣿⣿⣿⠟⠁⣠⣦⣄⡀⠀⠀⠀⠀⠀⠀⣤⣦⡈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁
                                    ⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⠟⠁⣠⣾⣿⣿⣿⣿⣿⣶⣶⣾⣧⠀⢻⣿⣿⣦⡈⠻⣿⣿⣿⣿⡿⠟⠉
                                    ⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⡟⠁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠈⠿⢿⣿⣿⣦⡈⠻⠛⠉
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠺⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⢀⣤⣤⡈⠙⠋⠁
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠻⠿⠿⠿⠿⠿⠿⠇⠀ ⣿⣿⣿⡇
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠈⠙⠋

                         /██   /██   /██   /██   /██████    /██████     /██████    /██      /██   /███████
                        | ██  | ██  | ███ | ██  |_  ██_/   /██__  ██   /██__  ██  | ███    /███  | ██__  ██
                        | ██  | ██  | ████| ██    | ██    | ██  \__/  | ██  \ ██  | ████  /████  | ██  \ ██
                        | ██  | ██  | ██ ██ ██    | ██    | ██        | ████████  | ██ ██/██ ██  | ███████/
                        | ██  | ██  | ██  ████    | ██    | ██        | ██__  ██  | ██  ███| ██  | ██____/
                        | ██  | ██  | ██\  ███    | ██    | ██    ██  | ██  | ██  | ██\  █ | ██  | ██
                        |  ██████/  | ██ \  ██   /██████  |  ██████/  | ██  | ██  | ██ \/  | ██  | ██
                         \______/   |__/  \__/  |______/   \______/   |__/  |__/  |__/     |__/  |__/
```

<p align="right"><b><sub>Version: 1.0.0 (in construction)</sub></b></p>

## Important Note: The Excel table necessary for running the algorithm will be available only after the publication of the manuscript, as it contains data that, without a proper explanation (provided in the manuscript) can create false alarms about the containment of COVID-19. The data must be carefully and responsibly used, the information necessary for it is given in the manuscript.

<p align="center"><b>Authors</b></p>
<p align="center">
Lilian Caroline Kramer Biasi<br>
Opalina Vetrichelvan<br>
Luís Fernando Mercier Franco<br></p>

# Introduction
<p align="justify">
This material is supplementary to our manuscript <i>"A Synergistic Approach of Molecular Docking and Artificial Intelligence for Drug Discovery: A Comprehensive Analysis of Ligand Structures Using SARS-CoV-2 as a Case Study (to pe published)".</i><br />
Molecular docking simulations were carried out between two SARS-CoV-2 spike glycoprotein variants and more than 9,000 ligands. One of the spike variants was reported at the beginning of the pandemic (<a href="https://www.rcsb.org/structure/6vsb">PDB: 6VSB</a>), and the other contains mutation D614G and is fully cleaved by Furin (<a href="https://www.rcsb.org/structure/7KDJ">PDB: 7KDJ</a>), which affects the affinity of the complex ligand-spike. From the molecular docking results of each SARS-CoV-2 spike protein variant mentioned above plus the results reported by <a href="https://doi.org/10.1080/07391102.2020.1772885">de Oliveira et al. (2020)</a>, a machine learning model was trained, and can here be used for a fast prediction of the binding energy of different ligands with the spike variants. <br />
</p><br>

## Keywords
Molecular docking, Machine Learning, Artificial Intelligence, SARS-CoV-2

## Highlights
  * Graphical User Interface (GUI) for fast prediction of the binding energy of different ligands and SARS-CoV-2 spike proteins <br />  
  * Artificial intelligence tool to accelerate drug design <br />

## Contents 
* <a href="#disclaimer">1. Disclaimer</a>
* <a href="#language-and-prerequisites">2. Language and Prerequisites</a>
* <a href="#building-and-running">3. Building and Running</a>
* <a href="#citing-us">4. Citing us</a>
* <a href="#reporting-errors">5. Reporting Errors</a>

## Disclaimer
<p align="justify">
The authors make no warranties about the use of this software. The authors hold no liabilities for the use of this software. The authors do not 
 recommend the use of this software whatsoever. The algorithm is made freely available to clarify any details discussed in our manuscript.
 All information contained herein regarding any specific methodology does not constitute or imply its endorsement or recommendation by the authors.
</p>

## Language and prerequisites
<p align="justify">
The main program is written in <a href="https://www.python.org/">Python 3.7</a>, and use the following libraries that must be previously installed:
</p>

  * <a href="https://pandas.pydata.org/">Pandas</a> <br />  
  * <a href="https://scikit-learn.org/stable/">scikit-learn</a> <br />
  * <a href="https://docs.python.org/3/library/tkinter.html">tkinter</a> <br />
</p>

## Building and Running
<p align="justify">
The code and the Excel file (containing the results of the molecular docking analyses) here available must be saved in the same folder. <br />
Run the Covid-GUI.py file using a <a href="https://www.python.org/">Python</a> compiler of your preference. We used <a href="https://www.spyder-ide.org/">Spyder</a> in Windows, no other compiler or operational system was tested.<br />
After running the code, an interface will open like this:<br /></p>
  
<em><p align="center">
<b>Figure 01:</b> Program interface<br>
Click [here](https://user-images.githubusercontent.com/43482626/150620883-e1ab8936-deae-438d-986e-00d2e757d47f.png) to zoom the figure in.
</p></em>

![fig0](https://user-images.githubusercontent.com/43482626/150620883-e1ab8936-deae-438d-986e-00d2e757d47f.png)

<p align="justify">
Select the spike protein variant:<br />
</p>

<em><p align="center">
<b>Figure 02:</b> Selecting the SARS-CoV-2 spike variant<br>
Click [here](https://user-images.githubusercontent.com/43482626/150620968-2276b111-d717-4e08-a96e-413666e81549.png) to zoom the figure in.
</p></em>
  
![fig1](https://user-images.githubusercontent.com/43482626/150620968-2276b111-d717-4e08-a96e-413666e81549.png)

<p align="justify">
The available variants are the one elevated by <a href="https://doi.org/10.1080/07391102.2020.1772885">de Oliveira et al. (2020)</a>, the one available as <a href="https://www.rcsb.org/structure/6vsb">PDB: 6VSB</a>, and the one available as <a href="https://www.rcsb.org/structure/7KDJ">PDB: 7KDJ</a>. For more information about the variants, see our manuscript. <br />
  
Enter the features of the ligand you desire to analyze, and then press the button to estimate the binding energy:
</p>

<em><p align="center">
<b>Figure 03:</b> Entering the features (1) and calculating the binding energy (2)<br>
Click [here](https://user-images.githubusercontent.com/43482626/150620968-2276b111-d717-4e08-a96e-413666e81549.png) to zoom the figure in.
</p></em>

![fig2](https://user-images.githubusercontent.com/43482626/150621285-3f0d75f1-6ad1-4bd2-abe1-74a995bad56d.png)

<p align="justify">
The required features can be manually counted from a molecule or can be counted using <a href="https://www.rdkit.org/">RDKit</a>
<br /></p>

## Citing us
<p align="justify">
If any of the codes here available was useful to you in any way, we kindly ask for you to cite our work: <i>"Molecular docking coupled with machine learning to screen inhibitors of SARS-CoV-2: A comprehensive analysis of the structure of the potential ligands (to pe published)"</i>
</p>

## Reporting Errors
<p align="justify">
If you spot an error in the program files and all other documentation, please submit an issue report using the <a href="https://github.com/LESC-Unicamp/Covid-GUI/issues">Issues</a> tab. 
</p>

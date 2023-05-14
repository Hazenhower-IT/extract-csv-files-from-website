import pandas as pd

#Inserire il link da cui si vuole estrarre il file 

# (clicca col tasto destro del mouse sul file che 
#  si vuole scaricare da internet e fai "copia 
#  indirizzo link, poi incollalo qui sotto tra le parentesi)
df_premier21 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2223/E0.csv")

# Rinomino le colonne con nomi piu significativi
df_premier21.rename(columns={"FTHG":"home_goals", 
                             "FTAG":"away_goals"}, inplace= True)
print(df_premier21)
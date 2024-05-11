#!/usr/bin/python

import keyboard
import pandas as pd
import os

orig_path = os.getcwd()
print( orig_path )
# Laden der Excel-Tabelle
df = pd.read_excel('RPGMusik.xlsx')
print(df)
# Funktion zum Abspielen von MP3-Dateien
def play_music(index):
    #Plays Music of a certain type
    if df['Notifier'].str.contains(index).any():
        mp3_path = df.loc[df['Notifier'] == index, 'MP3_Path'].values[0]
        print( 'start wmplayer "{}/{}"'.format(orig_path,mp3_path) )
        os.system( 'start wmplayer "{}/{}"'.format(orig_path,mp3_path) )
    else:
        print("Die eingegebene Nummer ist nicht in der Tabelle vorhanden.")

# Funktion, die bei der Tastenkombination ALT+SHIFT+M aufgerufen wird
def on_hotkey():
    try:
        index = str(input("Bitte geben Sie die Nummer des Musikstücks ein: "))
        play_music(index)
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")

# Tastenkombination ALT+SHIFT+M registrieren
keyboard.add_hotkey('alt+shift+m', on_hotkey)

# Endlosschleife, um das Skript im Hintergrund laufen zu lassen
keyboard.wait('esc')  # Warten auf ESC-Taste, um das Skript zu beenden

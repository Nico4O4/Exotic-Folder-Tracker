import os, time
import json


#--JSON Existiert--
def json_config():
    
    os.chdir(os.path.dirname(os.path.abspath(__file__))) #wechselt in das verzeichnis der .py datei, damit die configs immer im selben ordner liegen
    
    if os.path.exists("configs.json"):#falls file vorhanden
        with open("configs.json", "r") as f:
            data = json.load(f)#LOAD = echtes dict /list/ objekt [] {} ||| LOADS = dict / list in string "{}" "[]" wandelt es in echte um         
            
            value_from_dict = data.get("Path_to_folder")
            
            os.chdir(value_from_dict)
            print("JSON CONFIG LOADED\n")
            programm()
        


#--Falls JSON File nicht vorhanden--
    else:
        os.chdir(os.path.dirname(os.path.abspath(__file__))) #wechselt in das verzeichnis der .py datei, damit die configs immer im selben ordner liegen
     
        user_input = input("Insert Path to track the Folder: ")
        
        formatted_user_input = user_input.replace('"', '') # -> ' ' entfern das "" aus dem user innput weil pfade das oft enthalten und ersetzt es mit nichts
        if os.path.exists(formatted_user_input):
            data_short_saver = {"Path_to_folder" : formatted_user_input} #das dict!
        
            with open("configs.json", "x") as file:
                json.dump(data_short_saver, file, indent=4) #data_short_saver -> info mit dict aka dateiobjeekt | file -> geöffnet json file an sich
        
            with open("configs.json", "r") as f:
                data = json.load(f)#LOAD = echtes dict /list/ objekt [] {} ||| LOADS = dict / list in string "{}" "[]" wandelt es in echte um         
            
                value_from_dict = data.get("Path_to_folder")
                

                os.chdir(value_from_dict)
                
                print("DONE - JSON FILE CREATED AT: ", os.getcwd())
                programm()
        else:
            print("\nInvalid User Input. Please Insert Valid Path to Track files.")
            json_config()
        


def programm():
    last_modification_time = 0
    recent_file = None
    last_access = 0

#   |-----------------------------------------------------------------|
#   |programm (): mit Hilfe gelöst vom Discord Server "Hoodinformatik"|
#   |-----------------------------------------------------------------|

    # 1. Ordnen scannen und schauen
    for nehmer in os.scandir():
        
        #check ob es eine datei ist und speziell txt datei ist
        if nehmer.is_file() and nehmer.name.endswith('.txt'):
            modification_time = nehmer.stat().st_mtime_ns #st_mtime_ns -> last modification = letzte änderung nano sekunden in INT (nur inhalt zählt)

            
            # 2. schaut ob ob die datei neuer ist
            if modification_time > last_access : #vergleich ob modification_time grösser ist als stdtimezero
                # neue zeitpunkte der datei speichern
                recent_file = nehmer.name #in recent file wird der name der datei gepackt
                last_modification_time = modification_time 
                last_access = nehmer.stat().st_atime_ns # st_atime_ns -> last acces = letzer ZUGRIFF nano sekunden in INT (öffnen, lesen, inhalt anzeigen)


            
    if recent_file is not None: #wenn passende datei (mit txt endung gefunden wurde) wird die var recent_file ein wert gegeben und if block ausgeführt
        final_time_modification = time.ctime(last_modification_time/1e9) #in lesbare zeit umwandeln
        final_time_last_access = time.ctime(last_access/1e9) #in lesbare zeit uwmandeln

        with open(recent_file, 'r', encoding='utf-8') as file:
            contents = file.read()
        
            print(f"\n\nLast modified file: {recent_file}")
            print(f"Time since last modification: {final_time_modification}")                
            print(f"Time since last access: {final_time_last_access}")
            print(f"\n---CONTENTS OF THE FILE---\n\n")
            print(contents)
    else:
        print("No .txt file detected. Folder maybe empty or no .txt file in it.")

    x = input("\nPress Enter to exit... ")
    exit()


json_config()

#  /\                     /\
# //\\ \\\\\\\\\\\\\\\\  //\\
# |<>| Made by: Nico4O4  |<>|
# \\// ////////////////  \\//
#  \/                     \/
#  /\                     /\              
import tkinter as tk



"""Fenetre"""

fenetre = tk.Tk()
fenetre.title("IHM SCADA")
fenetre.geometry("800x600")
label = tk.Label(fenetre, text="Supervision de la salle T/H/P", font=("courier new gras", 20), padx = 20, pady = 20)
label.pack()



"""LabelFrame configuration"""

frame_configuration = tk.LabelFrame(fenetre, text="Configuration", bg="grey", fg="black", font = ("courier", 12), padx = 50, pady = 50)
frame_configuration.pack(fill=tk.X) #LabelFrame


label_alerte_configuration = tk.Label(frame_configuration,text="RAS", bg="lightgreen", padx = 20, pady = 20)
label_alerte_configuration.pack(side=tk.LEFT) #Label ALERTE

label_vitesse_configuration = tk.Label(frame_configuration,text="Vitesse de transmission", bg="grey", padx = 20)
label_vitesse_configuration.pack(side=tk.LEFT) #Label vitesse

entry_vitesse_configuration = tk.Entry(frame_configuration, width=8, justify="center")
baudrate = 9600 #Temporaire
entry_vitesse_configuration.pack(side=tk.LEFT) #Entrée vitesse
entry_vitesse_configuration.insert(0, baudrate) #Texte de base vitesse

entry_port_configuration = tk.Entry(frame_configuration, width=8, justify="center")
port = "COM3" #Temporaire
entry_port_configuration.pack(side=tk.RIGHT) #Entrée PORT
entry_port_configuration.insert(0, port) #Texte de base

label_port_configuration = tk.Label(frame_configuration,text="PORT", bg="grey", padx = 20)
label_port_configuration.pack(side=tk.RIGHT) #Label PORT



"""LabelFrame requete ModBus"""

frame_requete_modbus = tk.LabelFrame(fenetre, text="Requete ModBus", bg="grey", fg="black", font = ("courier", 12), padx = 50, pady = 50)
frame_requete_modbus.pack(fill=tk.X) #LabelFrame

label_requete_modbus = tk.Label(frame_requete_modbus,text="Requête", bg="grey", padx = 50)
label_requete_modbus.pack(side=tk.LEFT) #Label Requete

entry_requete_modbus = tk.Entry(frame_requete_modbus, width=40, justify="center")
entry_requete_modbus.pack(side=tk.LEFT) #Entrée Requete Modbus

def action_bouton_requete_modbus():
    requete = entry_requete_modbus.get()
    valeur_requete_vitesse_configuration = entry_vitesse_configuration.get()
    valeur_requete_port_configuration = entry_port_configuration.get()
    print(requete)
    reponse_requete = requete
    return reponse_requete #Action du bouton envoyer
bouton_requete_modbus = tk.Button(frame_requete_modbus, text="Envoyer", padx = 10, command=action_bouton_requete_modbus)
bouton_requete_modbus.pack(side=tk.LEFT) #Bouton envoyer



"""LabelFrame données"""

frame_donnees = tk.LabelFrame(fenetre, text="Données", bg="grey", fg="black", font = ("courier", 12), padx = 50, pady = 50)
frame_donnees.pack(fill=tk.X) #LabelFrame

label_reponse_donnees = tk.Label(frame_donnees,text="Réponse", bg="grey", padx = 50)
label_reponse_donnees.pack(side=tk.LEFT) #Label Requete

reponse_requete = ""
label_reponse_donnees_affiche = tk.Label(frame_donnees,text=reponse_requete, bg="grey", padx = 50)
label_reponse_donnees_affiche.pack(side=tk.LEFT) #Affichage de la réponse



"""Affichage de la fenetre"""

fenetre.mainloop()
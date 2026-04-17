import tkinter as tk
import modbus

port = "COM8"
baudrate = 9600
requete = bytes([0x01, 0x03, 0x00, 0x00, 0x00, 0x05, 0x85, 0xC9])
reponseModbus=""
temperature = 0
humidite = 0
pression = 0
etat_alarme = 0

def envoyer_requete():
    global port,baudrate,requete, reponseModbus, temperature, humidite, pression, etat_alarme
    sucess, reponseModbus, temperature, humidite, pression, etat_alarme = modbus.envoyer_trame(port, baudrate, requete)
    label_reponse_donnees_affiche.configure(text=reponseModbus)  # Affichage de la réponse
    label_reponse_temperature_donnees.configure(text=temperature)
    label_reponse_humidite_donnees.configure(text=humidite)
    label_reponse_pression_donnees.configure(text=pression)
    maj_alarme(etat_alarme)

def maj_alarme(etat_alarme):
    if etat_alarme == 0:
        label_alerte_configuration.configure(text="RAS", bg="lightgreen")
    elif etat_alarme == 1:
        label_alerte_configuration.configure(text="ALERTE", bg="blue")
    elif etat_alarme == 2:
        label_alerte_configuration.configure(text="CRITIQUE", bg="red")

def reset_alarme():
    print("reset alarme")
    requete_reset = bytes([0x01, 0x05, 0x00, 0x01, 0xFF, 0x00, 0xDD, 0xFA])


"""Fenetre"""
fenetre = tk.Tk()
fenetre.title("IHM SCADA")
fenetre.geometry("800x650")
label = tk.Label(fenetre, text="Supervision de la salle T/H/P", font=("courier new gras", 20), padx = 20, pady = 20)
label.pack()



"""Frame message"""

frame_message_alerte = tk.LabelFrame(fenetre, bg="grey")
frame_message_alerte.pack(fill=tk.X)

label_alerte_configuration = tk.Label(frame_message_alerte,text="RAS", bg="lightgreen", padx = 20, pady = 20)
label_alerte_configuration.pack(side=tk.LEFT) #Label ALERTE

label_message_alerte = tk.Label(frame_message_alerte, text="A modifier", bg="grey", padx = 20, pady = 20)
label_message_alerte.pack(side=tk.LEFT) #Label message ALERTE



"""LabelFrame configuration"""

frame_configuration = tk.LabelFrame(fenetre, text="Configuration", bg="grey", fg="black", font = ("courier", 12), padx = 50, pady = 50)
frame_configuration.pack(fill=tk.X) #LabelFrame

label_vitesse_configuration = tk.Label(frame_configuration,text="Vitesse de transmission", bg="grey", padx = 20)
label_vitesse_configuration.pack(side=tk.LEFT) #Label vitesse

entry_vitesse_configuration = tk.Entry(frame_configuration, width=8, justify="center")
entry_vitesse_configuration.pack(side=tk.LEFT) #Entrée vitesse
entry_vitesse_configuration.insert(0, baudrate) #Texte de base vitesse

entry_port_configuration = tk.Entry(frame_configuration, width=8, justify="center")
entry_port_configuration.pack(side=tk.RIGHT) #Entrée PORT
entry_port_configuration.insert(0, port) #Texte de base

label_port_configuration = tk.Label(frame_configuration,text="PORT", bg="grey", padx = 20)
label_port_configuration.pack(side=tk.RIGHT) #Label PORT



"""LabelFrame requete ModBus"""

frame_requete_modbus = tk.LabelFrame(fenetre, text="Requete ModBus", bg="grey", fg="black", font = ("courier", 12), padx = 50, pady = 50)
frame_requete_modbus.pack(fill=tk.X) #LabelFrame

label_requete_modbus = tk.Label(frame_requete_modbus,text="Requête", bg="grey", padx = 50)
label_requete_modbus.pack(side=tk.LEFT) #Label Requete

entry_requete_modbus = tk.Entry(frame_requete_modbus, width=40)
entry_requete_modbus.pack(side=tk.LEFT) #Entrée Requete Modbus
entry_requete_modbus.insert(0, requete.hex())


bouton_requete_modbus = tk.Button(frame_requete_modbus, text="Envoyer", padx = 10, command=envoyer_requete)
bouton_requete_modbus.pack(side=tk.LEFT) #Bouton envoyer

bouton_reset_alarme_modbus = tk.Button(frame_requete_modbus, text="Reset alarme", padx = 10, command=reset_alarme)
bouton_reset_alarme_modbus.pack(side=tk.LEFT) #Bouton reset



"""LabelFrame données"""

frame_donnees = tk.LabelFrame(fenetre, text="Données", bg="grey", fg="black", font = ("courier", 12), padx = 50, pady = 50)
frame_donnees.pack(fill=tk.X) #LabelFrame

sous_frame_reponse_donnees = tk.LabelFrame(frame_donnees, bg="grey", fg="black")
sous_frame_reponse_donnees.pack(fill=tk.X) #Sous LabelFrame

label_reponse_donnees = tk.Label(sous_frame_reponse_donnees,text="Réponse", bg="grey", padx = 50)
label_reponse_donnees.pack() #Label Requete

label_reponse_donnees_affiche = tk.Label(sous_frame_reponse_donnees, bg="grey", padx = 50)
label_reponse_donnees_affiche.pack()

sous_frame_temperature_donnees = tk.LabelFrame(frame_donnees, bg="grey", fg="black")
sous_frame_temperature_donnees.pack(side=tk.LEFT) #Sous LabelFrame

label_reponse_temperature_donnees = tk.Label(sous_frame_temperature_donnees,text="Température", bg="grey", padx = 50)
label_reponse_temperature_donnees.pack()

sous_frame_humidite_donnees = tk.LabelFrame(frame_donnees, bg="grey", fg="black")
sous_frame_humidite_donnees.pack(side=tk.LEFT) #Sous LabelFrame

label_reponse_humidite_donnees = tk.Label(sous_frame_humidite_donnees,text="Humidité", bg="grey", padx = 50)
label_reponse_humidite_donnees.pack()

sous_frame_pression_donnees = tk.LabelFrame(frame_donnees, bg="grey", fg="black")
sous_frame_pression_donnees.pack(side=tk.LEFT) #Sous LabelFrame

label_reponse_pression_donnees = tk.Label(sous_frame_pression_donnees,text="Pression", bg="grey", padx = 50)
label_reponse_pression_donnees.pack()


"""Affichage de la fenetre"""

fenetre.mainloop()
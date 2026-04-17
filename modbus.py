import serial
import time

def envoyer_trame(port,baudrate, requete):
    try :
        ser = serial.Serial(port, baudrate, timeout=1)
        ser.write(requete)
        time.sleep(0.1)
        reponseModbus= ser.read(15)
        temperature = (reponseModbus[3] << 8 | reponseModbus[4])/10
        temperature = f"Temperature : {temperature:.2f}°C"
        humidite = reponseModbus[7] << 8 | reponseModbus[8]
        humidite = f"Humidite : {humidite}%"
        pression = reponseModbus[5] << 8 | reponseModbus[6]
        pression = f"Pression : {pression}hPa"
        etat_alarme = reponseModbus[12]
        reponseModbus = reponseModbus.hex()
        ser.close()
        print(reponseModbus)
        return True, reponseModbus, temperature, humidite, pression, etat_alarme
    except Exception as e:
        return False, e



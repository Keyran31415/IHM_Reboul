import serial
import time

def envoyer_trame(port,baudrate, requete):
    try :
        ser = serial.Serial(port, baudrate, timeout=1)
        ser.write(requete)
        time.sleep(0.1)
        reponseModbus= ser.read(15)
        reponseModbus = reponseModbus.hex()
        ser.close()
        print(reponseModbus)
        return True, reponseModbus
    except Exception as e:
        return False, e



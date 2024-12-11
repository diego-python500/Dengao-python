from playsound import playsound
import random

segundos = int(input("Segundos que você quer converter para minutos: "))
minutos = segundos // 60
segundos_restantes = segundos % 60
nengue = random.randint(6,6)
if nengue == 1:
    playsound('/home/usuario/Downloads/Cow_hurt1.oga') 
if nengue == 2:
    playsound('/home/usuario/Downloads/Cave13.ogg') 
if nengue == 3:
    playsound('/home/usuario/Downloads/Villager_hurt1.oga') 
if nengue == 4:
    playsound('/home/usuario/Downloads/Spider_idle4.oga') 
if nengue == 5:
    playsound('/home/usuario/Downloads/Thorns2.ogg')
if nengue == 6:
    playsound('/home/usuario/Downloads/Thorns2.ogg') 
    playsound('/home/usuario/Downloads/Spider_idle4.oga') 
    playsound('/home/usuario/Downloads/Villager_hurt1.oga')
    playsound('/home/usuario/Downloads/Cave13.ogg')
    playsound('/home/usuario/Downloads/Cow_hurt1.oga') 


print(minutos, "minutos", segundos_restantes, "segundos")


from email.message import EmailMessage
import random
import smtplib

#Variables

from_addr    = 'amigosecretofamily2022@gmail.com' #your gmail account. Must have options for 3rd party login 
subj         = 'Amigo Secreto' 
message      = 'Howdy from a python function' 
login        = 'amigosecretofamily2022@gmail.com' #your gmail account 
password     = 'mhbmktxvovxzijog'#your password


#Send Email Method
def sendemail(from_addr, to_addr_list,subject, message,login, password,):
    email = EmailMessage()
    email["From"] = from_addr
    email["To"] = to_addr_list
    email["Subject"] = subject
    email.set_content(message)
    smtp = smtplib.SMTP_SSL("smtp.gmail.com")
    smtp.login(login, password)
    smtp.sendmail(from_addr, to_addr_list, email.as_string())
    smtp.quit()
              



#Read File Secretos.txt

file = open('secretos.txt', 'r')
amigos = [[]*2] #array for storing each participant
for line in file:
    amigos.append(line.split(','))
    

amigos.pop(0)

#print(amigos)

Juego = [[0 for x in range(3)] for y in range(len(amigos))] 


#print(Juego)

participantes = []          
for i in range(len(amigos)):
    participantes.append(amigos[i][0])

#print(participantes)


for i in range(0,len(amigos)):
    Juego[i][0] = amigos[i][0] #name giver
    Juego[i][1] = amigos[i][1].replace('\n','').replace(' ','') #email giver
    nombreAmigo = Juego[i][0]
    while(nombreAmigo==Juego[i][0]): #Not giving to himself
        if(len(participantes)!=1):
            nombreAmigo = participantes[random.randint(0,len(participantes)-1)] #take out the paper =)
        else:
            nombreAmigo = participantes[0] #last paper
        Juego[i][2] = nombreAmigo #asign the reciver to the giver
        participantes.pop(participantes.index(nombreAmigo)) #remove paper


for i in range(0,len(amigos)):
    intro = 'Querid@ %s :\n' %Juego[i][0]
    cuerpo = 'Queremos contarte que para el juego del amigo secreto, te ha tocado regalarle a %s \n' %Juego[i][2] 
    fin =  'Recuerda que debe ser de un valor de máximo de 10000.- y debe ser entregado el día 24 a las 8:00pm\n'
    despedida = 'Que tengas un lindo dia'
    msje = intro + cuerpo + fin + despedida
    sendemail(from_addr, Juego[i][1],subj, msje,login,password)

     



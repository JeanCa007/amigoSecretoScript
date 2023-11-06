
from email.message import EmailMessage
import random
import smtplib

#Variables

from_addr    = 'amigosecretobytesmidas@gmail.com' #your gmail account. Must have options for 3rd party login 
subj         = 'Amigo Secreto' 
message      = 'Howdy from a python function' 
login        = 'amigosecretobytesmidas@gmail.com' #your gmail account 
password     = 'roteuzggtnjpzlhx'#your password


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
    print('Este %s :\n' %Juego[i][0] + '- %s' %Juego[i][2])
    intro = 'Querid@ %s :\n' %Juego[i][0] + '\n' 
    cuerpo = 'Este año, tendremos dos intercambios de regalos de amigo secreto y queremos contarte que para el juego del amigo secreto, te ha tocado regalarle a %s' %Juego[i][2] + '\n' + '\n'
    cuerpo2= 'Fechas:' + '\n' + '-24 de Noviembre - Regalo pequeño - Office Day ' +'\n'
    cuerpo3= '-15 de Diciembre - Regalo Grande - Office Day ' +'\n' + '\n'
    fin =  'Presupuesto: '+ '\n'+'-Regalo pequeño ₡5.000'+ '\n'
    fin2 =  '-Regalo grande ₡20.000'+ '\n' + '\n'
    tips='Tips para elegir un regalo: '+ '\n'+ '\n' +'-Piensa en los intereses y hobbies de tu amigo secreto'+ '\n' + '\n'
    tips2='-Si no estás seguro de qué regalar, puedes preguntar a un amigo en común.'+ '\n' + '\n'
    tips3='-Puedes apoyarte en la lista de opciones de Google Docs compartida en el gurpo de Signal'+ '\n' + '\n'
    tips4='-No olvides envolver el regalo en papel craft para mantener el anonimato.'+ '\n' + '\n'
    despedida = 'Esperamos que disfrutes de esta actividad !!'
    msje = intro + cuerpo+ cuerpo2+cuerpo3+ fin+fin2+tips+tips2+tips3+tips4 + despedida
    #print(msje)
    sendemail(from_addr, Juego[i][1],subj, msje,login,password)

     


##print(msje)

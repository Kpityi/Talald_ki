import PySimpleGUI as sg
import random

sg.theme('graygraygray')
menu=[
  ['File',['New Game', '---', 'Exit']],[ 'Help',['About','A játékról']]
]
Score=1000
My_Score=0
layout= [
  [sg.Menu(menu)],
  [sg.Text('Elért pontszám: '), sg.Text(0, k='_My_Score_'),sg.Push(), sg.Text('    Találd ki!', font="Helvetica, 40", pad=(1,20)), sg.Push(), sg.Text("Megszerezhető Pontok: "),sg.Text(1000, k='_Score_')],
  [sg.Push(), sg.Image('./cards/alex.png', size=(80,140), key='Alex'),sg.Image('./cards/alfred.png', size=(80,140), key='Alfred'),sg.Image('./cards/anita.png', size=(80,140), key='Anita'),sg.Image('./cards/anne.png', size=(80,140), key='Anne'),sg.Image('./cards/bernard.png', size=(80,140), key='Bernard'),sg.Image('./cards/bill.png', size=(80,140), key='Bill'),sg.Image('./cards/charles.png', size=(80,140), key='Charles'),sg.Image('./cards/clarie.png', size=(80,140), key='Clarie'), sg.Push()],
  [sg.Push(), sg.Image('./cards/david.png', size=(80,140), key='David'),sg.Image('./cards/eric.png', size=(80,140), key='Eric'),sg.Image('./cards/frans.png', size=(80,140), key='Frans'),sg.Image('./cards/george.png', size=(80,140), key='George'),sg.Image('./cards/herman.png', size=(80,140), key='Herman'),sg.Image('./cards/joe.png', size=(80,140), key='Joe'),sg.Image('./cards/maria.png', size=(80,140), key='Maria'),sg.Image('./cards/max.png', size=(80,140), key='Max'), sg.Push()],
  [sg.Push(), sg.Image('./cards/paul.png', size=(80,140), key='Paul'),sg.Image('./cards/peter.png', size=(80,140), key='Peter'),sg.Image('./cards/philip.png', size=(80,140), key='Philip'),sg.Image('./cards/richard.png', size=(80,140), key='Richard'),sg.Image('./cards/robert.png', size=(80,140), key='Robert'),sg.Image('./cards/sam.png', size=(80,140), key='Sam'),sg.Image('./cards/susan.png', size=(80,140), key='Susan'),sg.Image('./cards/tom.png', size=(80,140), key='Tom'), sg.Push()],
  [sg.Spin([
    'Férfi?', 
    'Nő?', 
    'Szőke hajú?',
    'Fekete hajú?', 
    'Vörös hajú?',
    'Barna hajú?', 
    'Ősz/fehér hajú?', 
    'Hosszú haja van?', 
    'Rövid haja van?',
    'Kopasz?',
    'Kék szeme van?',
    'Barna szeme van?',
    'Fülbevalót visel?',
    'Van a fején sapka, vagy kalap?',
    'Bajuszos?',
    'Szakállas?',
    'Szemüveges?',
    'Nagy orra van?',
    'Kicsi orra van?'] , k="player_question", s=(30,2)), sg.Button('Kérdés'),sg.Push(), 
    sg.Combo(['','Alex', 'Alfred', 'Anita', 'Anne', 'Bernard', 'Bill', 'Charles', 'Clarie', 'David', 'Eric', 'Frans', 'George', 'Herman', 'Joe', 'Maria', 'Max', 'Paul', 'Peter', 'Philip', 'Richard', 'Robert', 'Sam', 'Susan', 'Tom'], default_value="válasz", k='megfejt'), sg.Button('Rákérdezek')]
]

window=sg.Window('Találdi ki', layout, resizable=True, size=(800,700))

cards=['Alex', 'Alfred', 'Anita', 'Anne', 'Bernard', 'Bill', 'Charles', 'Clarie', 'David', 'Eric', 'Frans', 'George', 'Herman', 'Joe', 'Maria', 'Max', 'Paul', 'Peter', 'Philip', 'Richard', 'Robert', 'Sam', 'Susan', 'Tom']
  
card=random.choice(cards)


while True:

  
  person={
    'Alex':{
      'nem':'férfi',
      'haj':'fekete',
      'haj_hossz': 'rövid',
      'szem':'barna',
      'fülbevaló':'nem',
      'sapka/kalap':'nem',
      'bajusz':'igen', 
      'szakáll':'nem',
      'szemüveg':"nem",
      'orr':'kicsi'
    },
    'Alfred':{
      'nem':'férfi',
      'haj':'vörös', 
      'haj_hossz':'hosszú',
      'szem':'kék',
      'fülbevaló':'nem',
      'sapka/kalap':'nem', 
      'bajusz':'igen', 
      'szakáll':'nem',
      'szemüveg':"nem",
      'orr':'kicsi'
    },
    'Anita':{
      'nem':'nő',
      'haj':'szőke',
      'haj_hossz':'hosszú',
      'szem':'kék',
      'fülbevaló':'nem',
      'sapka/kalap':'nem',
      'bajusz':'nem',
      'szakáll':'nem',
      'szemüveg':"nem",
      'orr':'kicsi' 
      
    },
    'Anne':{
      'nem':'nő',
      'haj':'fekete',
      'haj_hossz':'rövid',
      'szem':'barna',
      'fülbevaló':'igen',
      'sapka/kalap':'nem',
      'bajusz':'nem', 
      'szakáll':'nem',
      'szemüveg':"nem",
      'orr':'nagy' 
      
    },
    'Bernard':{
      'nem':'férfi',
      'haj':'barna',
      'haj_hossz':'rövid',
      'szem':'barna',
      'fülbevaló':'nem',
      'sapka/kalap':'igen',
      'bajusz':'nem', 
      'szakáll':'nem',
      'szemüveg':"nem",
      'orr':'nagy'
    },
    'Bill':{
      'nem':'férfi',
      'haj':'vörös',
      'haj_hossz':'kopasz',
      'szem':'barna',
      'fülbevaló':'nem',
      'sapka/kalap':'nem',
      'bajusz':'nem', 
      'szakáll':'igen',
      'szemüveg':"nem",
      'orr':'kicsi'
    },
    'Charles':{
      'nem':'férfi',
      'haj':'szőke',
      'haj_hossz':'rövid',
      'szem':'barna',
      'fülbevaló':'nem',
      'sapka/kalap':'nem',
      'bajusz':'igen', 
      'szakáll':'nem',
      'szemüveg':"nem",
      'orr':'kicsi'
    },
    'Clarie':{
      'nem':'nő',
      'haj':'vörös',
      'haj_hossz':'rövid',
      'szem':'barna',
      'fülbevaló':'igen',
      'sapka/kalap':'igen',
      'bajusz':'nem', 
      'szakáll':'nem',
      'szemüveg':"igen",
      'orr':'kicsi'
    },
    'David':{
      'nem':'férfi',
      'haj':'szőke',
      'haj_hossz':'rövid',
      'szem':'barna',
      'fülbevaló':'nem',
      'sapka/kalap':'nem',
      'bajusz':'nem', 
      'szakáll':'igen',
      'szemüveg':"nem",
      'orr':'kicsi'
    },
    'Eric':{
      'nem':'férfi',
      'haj':'szőke',
      'haj_hossz':'rövid',
      'szem':'barna',
      'fülbevaló':'nem',
      'sapka/kalap':'igen',
      'bajusz':'nem', 
      'szakáll':'nem',
      'szemüveg':"nem",
      'orr':'kicsi'
    },
    'Frans':{
      'nem':'férfi',
      'haj':'vörös',
      'haj_hossz':'rövid',
      'szem':'barna',
      'fülbevaló':'nem',
      'sapka/kalap':'nem',
      'bajusz':'nem', 
      'szakáll':'nem',
      'szemüveg':"nem",
      'orr':'kicsi'
    },
    'George':{
      'nem':'férfi',
      'haj':'ősz',
      'haj_hossz':'rövid',
      'szem':'barna',
      'fülbevaló':'nem',
      'sapka/kalap':'igen',
      'bajusz':'nem', 
      'szakáll':'nem',
      'szemüveg':"nem",
      'orr':'kicsi'
    },
    'Herman':{
      'nem':'férfi',
      'haj':'vörös',
      'haj_hossz':'kopasz',
      'szem':'barna',
      'fülbevaló':'nem',
      'sapka/kalap':'nem',
      'bajusz':'nem', 
      'szakáll':'nem',
      'szemüveg':"nem",
      'orr':'nagy'
    },
    'Joe':{
      'nem':'férfi',
      'haj':'szőke',
      'haj_hossz':'rövid',
      'szem':'barna',
      'fülbevaló':'nem',
      'sapka/kalap':'nem',
      'bajusz':'nem', 
      'szakáll':'nem',
      'szemüveg':"igen",
      'orr':'kicsi'
    },
    'Maria':{
      'nem':'nő',
      'haj':'barna',
      'haj_hossz':'hosszú',
      'szem':'barna',
      'fülbevaló':'igen',
      'sapka/kalap':'igen',
      'bajusz':'nem', 
      'szakáll':'nem',
      'szemüveg':"nem",
      'orr':'kicsi'
    },
    'Max':{
      'nem':'férfi',
      'haj':'fekete',
      'haj_hossz':'rövid',
      'szem':'barna',
      'fülbevaló':'nem',
      'sapka/kalap':'nem',
      'bajusz':'igen', 
      'szakáll':'nem',
      'szemüveg':"nem",
      'orr':'nagy'
    },
    'Paul':{
      'nem':'férfi',
      'haj':'ősz',
      'haj_hossz':'rövid',
      'szem':'barna',
      'fülbevaló':'nem',
      'sapka/kalap':'nem',
      'bajusz':'nem', 
      'szakáll':'nem',
      'szemüveg':"igen",
      'orr':'kicsi'
    },
    'Peter':{
      'nem':'férfi',
      'haj':'ősz',
      'haj_hossz':'rövid',
      'szem':'kék',
      'fülbevaló':'nem',
      'sapka/kalap':'nem',
      'bajusz':'nem', 
      'szakáll':'nem',
      'szemüveg':"nem",
      'orr':'nagy'
    },
    'Philip':{
      'nem':'férfi',
      'haj':'fekete',
      'haj_hossz':'rövid',
      'szem':'barna',
      'fülbevaló':'nem',
      'sapka/kalap':'nem',
      'bajusz':'nem', 
      'szakáll':'igen',
      'szemüveg':"nem",
      'orr':'kicsi'
    },
    'Richard':{
      'nem':'férfi',
      'haj':'barna',
      'haj_hossz':'kopasz',
      'szem':'barna',
      'fülbevaló':'nem',
      'sapka/kalap':'nem',
      'bajusz':'igen', 
      'szakáll':'igen',
      'szemüveg':"nem",
      'orr':'kicsi'
    },
    'Robert':{
      'nem':'férfi',
      'haj':'barna',
      'haj_hossz':'rövid',
      'szem':'kék',
      'fülbevaló':'nem',
      'sapka/kalap':'nem',
      'bajusz':'nem', 
      'szakáll':'nem',
      'szemüveg':"nem",
      'orr':'nagy'
    },
    'Susan':{
      'nem':'nő',
      'haj':'ősz',
      'haj_hossz':'hosszú',
      'szem':'barna',
      'fülbevaló':'nem',
      'sapka/kalap':'nem',
      'bajusz':'nem', 
      'szakáll':'nem',
      'szemüveg':"nem",
      'orr':'kicsi'
    },
    'Tom':{
      'nem':'férfi',
      'haj':'fekete',
      'haj_hossz':'kopasz',
      'szem':'kék',
      'fülbevaló':'nem',
      'sapka/kalap':'nem',
      'bajusz':'nem', 
      'szakáll':'nem',
      'szemüveg':"igen",
      'orr':'kicsi'
    },
    'Sam':{
      'nem':'férfi',
      'haj':'ősz',
      'haj_hossz':'kopasz',
      'szem':'barna',
      'fülbevaló':'nem',
      'sapka/kalap':'nem',
      'bajusz':'nem', 
      'szakáll':'nem',
      'szemüveg':"igen",
      'orr':'kicsi'
    }
  }

 
  card_nem=person[card]['nem']
  card_haj=person[card]['haj']
  card_haj_hossz=person[card]['haj_hossz']
  card_szem=person[card]['szem']
  card_fulbevalo=person[card]['fülbevaló']
  card_kalap=person[card]['sapka/kalap']
  card_bajusz=person[card]['bajusz']
  card_szakall=person[card]['szakáll']
  card_szemuveg=person[card]['szemüveg']
  card_orr=person[card]['orr']
  
  

  event, value=window.read()



  

  if event=="Kérdés":
    question=value['player_question']
    if question=='Férfi?':
      for i in person.keys():
        t=person[i]['nem']
        if t==card_nem:
          pass
        else:
          window[i].update(filename='./cards/card_back.png', size=(80,140))
      Score=Score-100
      window['_Score_'].update(Score)
    elif question=='Nő?':
      for i in person.keys():
        t=person[i]['nem']
        if t==card_nem:
          pass
        else:
          window[i].update(filename='./cards/card_back.png', size=(80,140))
      Score=Score-100
      window['_Score_'].update(Score)
    elif question=='Szőke hajú?':
      if card_haj=="szőke":
        for i in person.keys():
          t=person[i]['haj']
          if t!="szőke":
            window[i].update(filename='./cards/card_back.png', size=(80,140))
      elif card_haj!="szőke":
        for i in person.keys():
          t=person[i]['haj']
          if t=="szőke":
            window[i].update(filename='./cards/card_back.png', size=(80,140))
      Score=Score-100
      window['_Score_'].update(Score)
    elif question=='Fekete hajú?':
      if card_haj=="fekete":
        for i in person.keys():
          t=person[i]['haj']
          if t!="fekete":
            window[i].update(filename='./cards/card_back.png', size=(80,140))
      elif card_haj!="fekete":
        for i in person.keys():
          t=person[i]['haj']
          if t=="fekete":
            window[i].update(filename='./cards/card_back.png', size=(80,140))
      Score=Score-100
      window['_Score_'].update(Score)
    elif question=='Vörös hajú?':
      if card_haj=="vörös":
        for i in person.keys():
          t=person[i]['haj']
          if t!="vörös":
            window[i].update(filename='./cards/card_back.png', size=(80,140))
      elif card_haj!="vörös":
        for i in person.keys():
          t=person[i]['haj']
          if t=="vörös":
            window[i].update(filename='./cards/card_back.png', size=(80,140))
      Score=Score-100
      window['_Score_'].update(Score)
    elif question=='Barna hajú?':
      if card_haj=="barna":
        for i in person.keys():
          t=person[i]['haj']
          if t!="barna":
            window[i].update(filename='./cards/card_back.png', size=(80,140))
      elif card_haj!="barna":
        for i in person.keys():
          t=person[i]['haj']
          if t=="barna":
            window[i].update(filename='./cards/card_back.png', size=(80,140))
      Score=Score-100
      window['_Score_'].update(Score)
    elif question=='Ősz/fehér hajú?':
      if card_haj=="ősz":
        for i in person.keys():
          t=person[i]['haj']
          if t!="ősz":
            window[i].update(filename='./cards/card_back.png', size=(80,140))
      elif card_haj!="ősz":
        for i in person.keys():
          t=person[i]['haj']
          if t=="ősz":
            window[i].update(filename='./cards/card_back.png', size=(80,140))
      Score=Score-100
      window['_Score_'].update(Score)
    elif question=='Hosszú haja van?':
      if card_haj_hossz=='hosszú':
        for k in person.keys():
          e=person[k]['haj_hossz']
          if e=="rövid":
            window[k].update(filename='./cards/card_back.png', size=(80,140))
          elif e=="kopasz":
            window[k].update(filename='./cards/card_back.png', size=(80,140))
      elif card_haj_hossz=='rövid' or card_haj_hossz=='kopasz':
        for k in person.keys():
          e=person[k]['haj_hossz']
          if e=='hosszú':
            window[k].update(filename='./cards/card_back.png', size=(80,140))
      Score=Score-100
      window['_Score_'].update(Score)         
    elif question=='Rövid haja van?':
      if card_haj_hossz=='rövid':
        for k in person.keys():
          e=person[k]['haj_hossz']
          if e=="hosszú":
            window[k].update(filename='./cards/card_back.png', size=(80,140))
          elif e=="kopasz":
            window[k].update(filename='./cards/card_back.png', size=(80,140))
      elif card_haj_hossz=='hosszú' or card_haj_hossz=='kopasz':
        for k in person.keys():
          e=person[k]['haj_hossz']
          if e=='rövid':
            window[k].update(filename='./cards/card_back.png', size=(80,140)) 
      Score=Score-100
      window['_Score_'].update(Score)    
    elif question=='Kopasz?':
      if card_haj_hossz=='kopasz':
        for k in person.keys():
          e=person[k]['haj_hossz']
          if e=="rövid":
            window[k].update(filename='./cards/card_back.png', size=(80,140))
          elif e=="hosszú":
            window[k].update(filename='./cards/card_back.png', size=(80,140))
      elif card_haj_hossz=='rövid' or card_haj_hossz=='hosszú':
        for k in person.keys():
          e=person[k]['haj_hossz']
          if e=='kopasz':
            window[k].update(filename='./cards/card_back.png', size=(80,140))  
      Score=Score-100
      window['_Score_'].update(Score)  
    elif question=='Kék szeme van?':
      if card_szem=='kék':
        for k in person.keys():
          e=person[k]['szem']
          if e=="barna":
            window[k].update(filename='./cards/card_back.png', size=(80,140))
      elif card_szem=='barna':
        for k in person.keys():
          e=person[k]['szem']
          if e=='kék':
            window[k].update(filename='./cards/card_back.png', size=(80,140))
      Score=Score-100
      window['_Score_'].update(Score)  
    elif question=='Barna szeme van?':
      if card_szem=='barna':
        for k in person.keys():
          e=person[k]['szem']
          if e=="kék":
            window[k].update(filename='./cards/card_back.png', size=(80,140))
      elif card_szem=='kék':
        for k in person.keys():
          e=person[k]['szem']
          if e=='barna':
            window[k].update(filename='./cards/card_back.png', size=(80,140)) 
      Score=Score-100
      window['_Score_'].update(Score)
    elif question=='Fülbevalót visel?':
      for i in person.keys():
        t=person[i]['fülbevaló']
        if t==card_fulbevalo:
          pass
        else:
          window[i].update(filename='./cards/card_back.png', size=(80,140))
      Score=Score-100
      window['_Score_'].update(Score)
    elif question=='Van a fején sapka, vagy kalap?':
      for i in person.keys():
        t=person[i]['sapka/kalap']
        if t==card_kalap:
          pass
        else:
          window[i].update(filename='./cards/card_back.png', size=(80,140))
      Score=Score-100
      window['_Score_'].update(Score)
    elif question=='Bajuszos?':
      for i in person.keys():
        t=person[i]['bajusz']
        if t==card_bajusz:
          pass
        else:
          window[i].update(filename='./cards/card_back.png', size=(80,140))
      Score=Score-100
      window['_Score_'].update(Score)
    elif question=='Szakállas?':
      for i in person.keys():
        t=person[i]['szakáll']
        if t==card_szakall:
          pass
        else:
          window[i].update(filename='./cards/card_back.png', size=(80,140))
      Score=Score-100
      window['_Score_'].update(Score)
    elif question=='Szemüveges?':
      for i in person.keys():
        t=person[i]['szemüveg']
        if t==card_szemuveg:
          pass
        else:
          window[i].update(filename='./cards/card_back.png', size=(80,140))
      Score=Score-100
      window['_Score_'].update(Score)
    elif question=='Nagy orra van?':
      for i in person.keys():
        t=person[i]['orr']
        if t==card_orr:
          pass
        else:
          window[i].update(filename='./cards/card_back.png', size=(80,140))
      Score=Score-100
      window['_Score_'].update(Score)
    elif question=='Kicsi orra van?':
      for i in person.keys():
        t=person[i]['orr']
        if t==card_orr:
          pass
        else:
          window[i].update(filename='./cards/card_back.png', size=(80,140))
      Score=Score-100
      window['_Score_'].update(Score)
  elif event=='Rákérdezek':
    megoldas=value['megfejt']
    if megoldas==card:
      My_Score=My_Score+Score
      window['_My_Score_'].update(My_Score)
      sg.Popup('Gratulálok eltaláltad!!!')
    else:
      My_Score=My_Score/2
      window['_My_Score_'].update(My_Score)
      sg.Popup('Sajnos nem jó választ adtál a helyes megoldás: ', card, " lett volna!")
      # card='Kezdj új játékot!'
  # Menu
  elif event=="About":
    sg.popup('A találd ki egy közkedvelt táblajáték, mely jó szórakozást nyújt mind a fiatalabb mind az idősebb korosztály számára. \n A játék az eredeti Guess Who? táblajáték lapjai alapján készült verzió: 1.0\n\n                 Bluetoon Software copyright © 2022')   
  elif event=="A játékról":
    sg.popup('A játék kezdetekor a számítógép húz egy lapot. A játékosnak a gép által kihúzott lapon szereplő személy nevét ki kell találnia. A játékos úgy juthat közelebb a megoldáshoz, hogy kérdéseket tesz fel (bal alsó sarokban lévő menü segéítségével ki kell választani egy kérdést, ezután rá kell kattintani a "Kérdés" feliratú gombra), melyekre a gép "válaszol" és a válasznak megfelelően elrejti a kiesett lapokat. Ha a megfelelő kérdéseket tesz fel a játékos akkor a végén már csak 1 lap marad ekkor rá kell kérdezni a személye (jobb oldali menüből válasszuk ki a kívánt lapot és kattintsunk a "Rákérdezek gombra). Ha mindent jól csináltunk 100%-os bizonyosszággal meg tudjuk mondani melyik lap volt a computernél és ezzel meg is nyertük a játékot! Jó szórakozást!')   
  elif event=='New Game':
    for i in person:
      cardname=i.lower()
      window.FindElement(i).Update(f'./cards/{cardname}.png')
      Score=1000
      window['_Score_'].update(1000)
      card=random.choice(cards)
      
    


  if event==sg.WIN_CLOSED:
    break
    
  if event=="Exit":
    sg.popup('Viszont látásra')
    break


window.close()
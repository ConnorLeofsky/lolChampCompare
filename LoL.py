import riotwatcher
import requests
import csv
from csv import reader
import pandas as pd
import numpy as np


from matplotlib import pyplot as plt
champLst = []
lolData = []

def data_version():
    ddragon = "https://ddragon.leagueoflegends.com/realms/euw.json"
    euw_json = requests.get(ddragon).json()
    return euw_json['n']['champion']


def build_data_url():
    return "http://ddragon.leagueoflegends.com/cdn/" + data_version() + "/data/en_GB/champion.json"
    


def get_jsons():
    data_url = build_data_url()
    data_json = requests.get(data_url).json()
    champ_list = data_json['data'].keys()
    return data_json, champ_list


def createDic(title, lst):
    res_dct = {title[i]: lst[i] for i in range(0, len(lst))}
    return res_dct


def level_math(base, per_level, level):
    level_stat = base + (per_level * level)
    return level_stat


def topComp(champ, counter):
    enter = 0
    yourName = ''
    yourChamp = []
    counterName = ''
    counterChamp = []
    x = np.arange(1,19)
    for i in range(0, len(champLst)):
        if(champLst[i]['Name'] == champ):
            yourName = champLst[i]['Name']
            yourChamp = champLst[i]
            enter += 1
        if(champLst[i]["Name"] == counter):
            counterName = champLst[i]['Name']
            counterChamp = champLst[i]
            enter += 1
        if(enter == 2):
            break
    aTT = float(yourChamp["Attack Speed"])
    aTT2 = float(counterChamp["Attack Speed"])
    aTTpl = float(yourChamp["Attack Speed Per Level"])
    aTTpl2 = float(counterChamp["Attack Speed Per Level"])
    y1 = level_math(aTT, aTTpl, x)
    y2 = level_math(aTT2, aTTpl2, x)
    df=pd.DataFrame({'x': x, yourName : y1, counterName: y2})
    plt.figure(figsize=(12, 7))
    plt.title("Attack Speed")
    plt.xlabel("Lvl")
    plt.ylabel("Attack Speed")
    plt.plot( 'x', yourName, data=df, marker='', markerfacecolor='blue', linewidth=2)
    plt.plot( 'x', counterName, data=df, marker='', color='black', linewidth=2)

    plt.legend()

    
#def jungleComp():
    
    
    
#def midComp():

    
    
#def adcComp():

    
    
#def supComp():

    
    
def row_headings():
    return [
        "Name",
        "HP",
        "HP Per Level",
        "MP",
        "MP Per Level",
        "Move Speed",
        "Armor",
        "Armour Per Level",
        "Spell Block",
        "Spell Block Per Level",
        "Attack Range",
        "HP Regen",
        "HP Regen Per Level",
        "MP Regen",
        "MP Regen Per Level",
        "Attack Damage",
        "Attack Damage Per Level",
        "Attack Speed",
        "Attack Speed Per Level"
    ]


def create_file():
    data_json, champ_list = get_jsons()
    file_name = 'champStats.csv'
    with open(file_name, 'w', newline='', encoding='utf8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(row_headings())
        for champ in champ_list:
            name = data_json['data'][champ]['name']
            hp = data_json['data'][champ]['stats']['hp']
            hpperlevel = data_json['data'][champ]['stats']['hpperlevel']
            mp = data_json['data'][champ]['stats']['mp']
            mpperlevel = data_json['data'][champ]['stats']['mpperlevel']
            movespeed = data_json['data'][champ]['stats']['movespeed']
            armor = data_json['data'][champ]['stats']['armor']
            armorperlevel = data_json['data'][champ]['stats']['armorperlevel']
            spellblock = data_json['data'][champ]['stats']['spellblock']
            spellblockperlevel = data_json['data'][champ]['stats']['spellblockperlevel']
            attackrange = data_json['data'][champ]['stats']['attackrange']
            hpregen = data_json['data'][champ]['stats']['hpregen']
            hpregenperlevel = data_json['data'][champ]['stats']['hpregenperlevel']
            mpregen = data_json['data'][champ]['stats']['mpregen']
            mpregenperlevel = data_json['data'][champ]['stats']['mpregenperlevel']
            attackdamage = data_json['data'][champ]['stats']['attackdamage']
            attackdamageperlevel = data_json['data'][champ]['stats']['attackdamageperlevel']
            attackspeed = data_json['data'][champ]['stats']['attackspeed']
            attackspeedperlevel = data_json['data'][champ]['stats']['attackspeedperlevel']
            writer.writerow([name, hp, hpperlevel, mp, mpperlevel, movespeed, armor, armorperlevel, spellblock, spellblockperlevel, attackrange, hpregen, hpregenperlevel, mpregen, mpregenperlevel, attackdamage, attackdamageperlevel, attackspeed, attackspeedperlevel])

def matchup(lane):
    if(lane == 't'):
        champ1 = input("Top Laner: ")
        champ3 = input("Enemy Top Laner: ")
#        champ2 = input("Jungler: ")
        topComp(champ1, champ3)
#        jungleComp(champ2)
#    elif(lane == 'm' or lane == 'j'):
#        champ1 = input("Jungler: ")
#        champ2 = input("Mid laner: ")
#        jungleComp(champ1)
#        midComp(champ2)
#    elif(lane == 'b'):
#        champ1 = input("ADC: ")
#        champ2 = input("Suport: ")
#        adcComp(champ1)
#        supComp(champ2)
        

def create():
    create_file()
    open_file = open('champStats.csv')
    rfile = reader(open_file)
    lolData = list(rfile)  
    for i in range(1, len(lolData)):
        dic = createDic(lolData[0], lolData[i])
        champLst.append(dic)
def main():
    create()
#    lane = input("What lane are you playing?(Top(t), Jungle(j), Mid(m), Bottom(b))")
  #  matchup(lane)
    print("done")



if __name__ == "__main__":
    main()
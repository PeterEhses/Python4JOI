import pandas
import json
import numpy
#pandas.set_option('display.max_columns', 50)
f = open("./Full Attribute Scores/target-filenames.txt","r")
lines = f.read()
line_ar = lines.split("\n")
#print(line_ar[0])
output = {}
second = {}
for x in line_ar:
    temp = x.split(",")
    output[temp[1]] = temp[0]
#print(output)
for x in output:
    print(output[x])
    break

dem_att = pandas.read_excel("./Full Attribute Scores/demographic others labels/demographic-others-labels.xlsx","Final Values")
#print(dem_att.iloc[1])
psy_att = pandas.read_excel("./Full Attribute Scores/psychology attributes/psychology-attributes.xlsx","Final Values")
#print(dem_att)
#print(psy_att)

structure = {
        "id":int,
        "demographic":{
                "Image #":int,
                "Age":["<20","20-30","30-45","45-60","60+"],
                "Attractive":int, #1 least, 5 most
                "Famousnes":int,#1 () - 3 ()
                "Commonnes":int,
                "Emotion Ammount":int,#1 (little) - 5 (a lot)
                "Emotion":["Neutral","Happiness","Sadness","Anger","Fear","Surprise","Disgust"],
                "Eye Direction":["Front","Up","Down","Left","Right"],
                "Face Direction":["Front","Up","Down","Left","Right"],
                "Facial Hair":["None","Some","A Lot"],
                "Friendly":int,#1 (very unfriendly - 5 (very friendly)
                "Makeup":["None","Some","A Lot"],
                "Gender":["Male","Female"],
                "Movie Castability":["None","Some","A Lot"],
                "Profile Picture-Ability":["None","Some","A Lot"],
                "Image Quality":int,#1 (poor) - 5 (very good)
                "Race":["Other","White","Black","East Asian","South Asian","Hispanic","Middle Eastern"],
                "Memorability":int,#1 (forgettable) - 5 (memorable)
                "Expression Speed":int,#1 (slowly) - 5 (quickly)
                "Teeth Showing":["None","Some","A Lot"]
                },
        "psychologic":{
                #psych labels ^= row headers
                }
        }
 
#print(structure)  



for x in output:
    #print(output[x])
    #print(int(output[x]))
    pos = int(output[x])-1
    output[x]=dem_att.iloc[pos]
    second[x]=psy_att.iloc[pos]
    #print(second[x])
for x in output:
    temp=output[x].values
    
    age = "nan"
    try:
        age = "60+"
        if temp[2]<1.5:
            age = "<20"
        elif temp[2]<2.5:
            age = "20-30"
        elif temp[2]<3.5:
            age = "30-45"
        elif temp[2]<4.5:
            age = "30-45"
        elif temp[2]<5.5:
            age = "45-60"
    except:
        #print("I'm bad at this") 
        outahere = True
        
    emotion = "nan"
    try:    
        emotion = "Disgust"
        if temp[6]<0.5:
            emotion = "Neutral"
        elif temp[6]<1.5:
            emotion = "Happiness"
        elif temp[6]<2.5:
            emotion = "Sadness"
        elif temp[6]<3.5:
            emotion = "Anger"
        elif temp[6]<4.5:
            emotion = "Fear"
        elif temp[6]<5.5:
            emotion = "Surprise"
    except:
        #print("I'm bad at this") 
        outahere = True
        
    eyes = "nan"
    try:     
        eyes = "Right"
        if temp[8]<1.5:
            eyes = "Front"
        elif temp[8]<2.5:
            eyes = "Up"
        elif temp[8]<3.5:
            eyes = "Down"
        elif temp[8]<4.5:
            eyes = "Left"
    except:
        #print("I'm bad at this") 
        outahere = True
        
    head = "nan"   
    try:
        head = "Right"
        if temp[9]<1.5:
            head = "Front"
        elif temp[9]<2.5:
            head = "Up"
        elif temp[9]<3.5:
            head = "Down"
        elif temp[9]<4.5:
            head = "Left"
    except:
        #print("I'm bad at this") 
        outahere = True 
        
    gender = "nan"
    try:     
        gender = "Female"
        if temp[14]<0.5:
            gender = "Male"
    except:
        #print("I'm bad at this") 
        outahere = True
        
    race = "nan"
    try:     
        race = "Other"
        if temp[18] < 0.5:
            race = "Other"
        elif temp[18] <1.5:
            race = "White"
        elif race <2.5:
            temp[18] = "Black"
        elif race <3.5:
            race = "East Asian"
        elif temp[18] <4.5:
            race = "South Asian"
        elif temp[18] <5.5:
            race = "Hispanic"
        elif temp[18] <6.5:
            race = "Middle Eastern"
    except:
        #print("I'm bad at this") 
        outahere = True
        
        
    output[x]={
            "id":temp[0],
            "demographic":{
                    "Image #":temp[1],
                    "Age":age,
                    "Age Precision":temp[2],
                    "Attractive":temp[3],
                    "Famousness":temp[4],
                    "Commonness":temp[5],
                    "Emotion Ammount":temp[6],
                    "Emotion":emotion,
                    "Emotion Precision":temp[7],
                    "Eye Direction":eyes,
                    "Eye Precision":temp[8],
                    "Face Direction":head,
                    "Face Precision":temp[9],
                    "Facial Hair":temp[10],
                    "Friendlyness":temp[12],
                    "Makeup Amount":temp[13],
                    "Gender":gender,
                    "Gender Precision":temp[14],
                    "Movie Castability":temp[15],
                    "Profile Picture-Ability":temp[16],
                    "Image Quality":temp[17],
                    "Race":race,
                    "Race Precision":temp[18],
                    "Memorability":temp[19],
                    "Expression Speed":temp[20],
                    "Teeth-ness":temp[21]
                    },
            "psychologic":{}
            }
            
    keys = second[x].keys().tolist()
    #print(keys)
    temp2 = second[x].values
    #print(temp2)
    i = 0
    excl = [0,1,5,6,17,18,19,20,31,32,45,46,47,48]
        
    while i < len(keys):
        
        if i in excl:
            #print(i) 
            outahere = True
        else:
            output[x]["psychologic"][keys[i]] = float(temp2[i])
        i+=1
        
#print(output)
for x in output:
    for n in output[x]["demographic"]:
        if type(output[x]["demographic"][n]) is not str:
            try:
                output[x]["demographic"][n] = float(output[x]["demographic"][n])
            except:
                outahere = True


with open('data.json', 'w') as fp:
    json.dump(output, fp)
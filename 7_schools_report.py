"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the AAC, Big 12, Big Ten, and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""

import json

infile = open('school_data.json','r')

list_of_schools = json.load(infile)

conf = [372,108,107,130]

for i in list_of_schools:
    if i['NCAA']["NAIA conference number football (IC2020)"] in conf:
        if i["Graduation rate  women (DRVGR2020)"] > 75:
            print('University:',i['instnm'])
            print('Graduation rate for women:',f'{i["Graduation rate  women (DRVGR2020)"]}%')
            print()
            print()
for i in list_of_schools:
    if i['NCAA']["NAIA conference number football (IC2020)"] in conf:
        if i["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"] != None and i["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"] > 50000:
            print('University:',i['instnm'])
            print('Total price for in-state students living off campus:',f'${i["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"]:,.2f}')
            print()
            print()
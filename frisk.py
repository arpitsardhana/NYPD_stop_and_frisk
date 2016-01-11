import os
import sys
import time
import csv
import matplotlib.pyplot as plt
import operator
from pylab import *

def is_number(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

input_file = str(sys.argv[1])


file_open = open(input_file,'r')
data = dict()
count = 0
code = dict()
with open(input_file, 'rb') as f:
     for row in csv.reader(f, delimiter=',', skipinitialspace=True):
	if count == 0:
		   #date = row.index("datestop")
		   #data[date] = dict() 
		   #code[date] = "Month" 

		   #timestop = row.index("timestop")
		   #data[timestop] = dict()

		   #crimesusp = row.index("crimsusp")
		   #data[crimesusp] = dict()


		   #sex = row.index("sex")
		   #data[sex] = dict()

		   race = row.index("race")
		   #data[race] = dict()
		   code[race] = "Race"

		   arstmade = row.index("arstmade")
		   #data[arstmade] = dict()
		   #code[arstmade] = "Arrest Made"

		   #sumissue = row.index("sumissue")
		   #data[sumissue] = dict()
		   #code[sumissue] = "Summon Issues"

		   age = row.index("age")
		   data[age] = dict()

		   #ht_feet = row.index("ht_feet")
		   #ht_inch = row.index("ht_inch")
		   #data[ht_feet] = dict()
		   #data[ht_inch] = dict()

		   #weight  = row.index("weight")
		   #data[weight] = dict()

		   #haircolor = row.index("haircolr")
		   #data[haircolor] = dict()

		   #eyecolor = row.index("eyecolor")
		   #data[eyecolor] = dict()

		   #build = row.index("build")
		   #data[build] = dict()
	           #code[build] = "Build"

		   #crossst = row.index("crossst")
		   #data[crossst] = dict()

		   #city = row.index("city")
		   #data[city] = dict()

		   count += 1
		   continue
	
	#l_dict = data[timestop]
        #l_value = row[timestop].strip().replace(" ","")	
	#s = len(l_value)
	#l_value = l_value[0:s-6]
	arr_made = row[arstmade].strip().replace(" ","") 
	#for key in data:
	#l_dict = data[date]
	#l_value = row[key].strip().replace(" ","")
	#arr_made = 
	#s = len(l_value)
	#l_value = l_value[0:s-6]
	#l_value = l_value[0:s-2]
        l_dict = data[age]
        l_value_1 = row[age].strip().replace(" ","")
	race_value = row[race].strip().replace(" ","")
	print race_value
	if is_number(l_value_1) : 
		l_value = (int(l_value_1) - 5 )/10
	else :
		l_value = 100
	if l_value < 0:
		l_value = 101 
		#continue
	
	if l_value > 8 and l_value < 100:
		l_value = 102

	if l_value >= 100 :
		l_value = 100
	
	if l_value in l_dict :
#		l_dict[l_value] += 1
                race_l = l_dict[l_value]
                if race_value == 'B':
                        race_l[0] += 1
                elif race_value == 'W':
                        race_l[1] += 1
                elif race_value == 'P' or race_value == 'Q':
                        race_l[2] += 1
                else :
                        race_l[3] += 1

		#if arr_made == 'Y':
		#	l_dict[l_value] += 1
	else :
		l_dict[l_value] = [0,0,0,0] 
		race_l = l_dict[l_value]
		if race_value == 'B':
			race_l[0] += 1
		elif race_value == 'W':
			race_l[1] += 1
		elif race_value == 'P' or race_value == 'Q':
			race_l[2] += 1
		else :
			race_l[3] += 1 
		#if arr_made == 'Y':
		#	l_dict[l_value] = 1
		#else :
		#	l_dict[l_value] = 0
			
	


      	   

	
		
new_data = dict() 

for key in data:
	dic = data[key]
	size = len(dic)
	new_data[key] = dict()
	if size > 15:
		local_l = dic.values() 
		local_l = sorted(local_l,reverse=True)
		val = local_l[14]
		#print "values"
		#print local_l , val
	else :
		new_data[key] = data[key].copy()
		continue
	
	for item in dic:
		cnt = dic[item]
		if cnt >=  val:
			new_data[key][item] = cnt 
	             	
			 
#for key in data:
	#data[key] = sorted(data[key],reverse=True)



	
file_open.close()
#print date,timestop,crimesusp,sex,race,age,ht_feet,ht_inch,weight,haircolor,eyecolor,build,crossst,city
#print new_data

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')
#autolabel(rects1)
fontsize = 16
ax = gca()

plt.gcf().subplots_adjust(bottom=0.15)
for tick in ax.xaxis.get_major_ticks():
     tick.label1.set_fontsize(fontsize)
     tick.label1.set_fontweight('bold')
for tick in ax.yaxis.get_major_ticks():
     tick.label1.set_fontsize(fontsize)
     tick.label1.set_fontweight('bold')


legend()
dic = data[age]
#dic = sorted(dic)
print dic
#a = plt.bar(range(len(dic)), dic.values(), align="center")
#plt.xticks(range(len(dic)), list(dic.keys()),rotation = 90)
#plt.ylabel("value", fontsize=16, fontweight='bold')
#plt.xlabel(code[key], fontsize=16, fontweight='bold')
#autolabel(a)
#plt.show()

#for key in new_data:
#	if len(new_data[key]) <= 1:
#		continue
#	dic = new_data[key]
#	a = plt.bar(range(len(dic)), dic.values(), align="center")
#	plt.xticks(range(len(dic)), list(dic.keys()),rotation = 90)
#	plt.ylabel("value", fontsize=16, fontweight='bold')
#	plt.xlabel(code[key], fontsize=16, fontweight='bold')
#	autolabel(a)
#	plt.show()
#	name = str(key) + "png"
	#plt.savefig(name, bbox_inches='tight')


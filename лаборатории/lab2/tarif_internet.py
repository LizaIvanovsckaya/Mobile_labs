#Протарифицировать абонента с IP-адресом 192.168.250.3 
#с коэффициентом k: 3руб/Мб
import matplotlib.pyplot as plot
import datetime
import time
import pylab
abonent = '192.168.250.3'
file = open("dump.txt")
onstring = file.read().split("\n")[:-1]
i = 0
while i<len(onstring):
	onstring[i]=onstring[i].split()
	if (abonent in onstring[i][4]) or (abonent in onstring[i][6]):
		i +=1
	else:
		onstring.pop(i)
		continue
for i in range(len(onstring)):
	t = onstring[i][0]+' '+onstring[i][1]
	onstring[i][1] = datetime.datetime.strptime(t, '%Y-%m-%d %H:%M:%S.%f')
for i in range(len(onstring)):
	for j in range(len(onstring)-i-1):
		if onstring[j][1].time() > onstring[j+1][1].time():
			onstring[j], onstring[j+1] = onstring[j+1], onstring[j]
sum = 0
time_gr = []
bytes = []
for i in range(len(onstring)):
	if abonent in onstring[i][4]:
		time_gr.append(onstring[i][1])
		if onstring[i][9]=='M':
			sum += float(onstring[i][8])*1024
			bytes.append(sum)
		else: 
			sum += int(onstring[i][8])/1024
			bytes.append(sum)
	if abonent in onstring[i][6]:
		time_gr.append(onstring[i][1])
		if onstring[i][9]=='M':
			sum += float(onstring[i][8])*1024
			bytes.append(sum)
		else: 
			sum += int(onstring[i][8])/1024
			bytes.append(sum)
print("Трафик в Кб",sum)
sum = sum / 1024
sum_rub = sum * 3
print("Трафик в Мб",sum)
print("Сумма в рублях",sum_rub)
plot.plot(time_gr,bytes)
plot.ylabel('Объем трафика, в Кб')
plot.xlabel('Время')
plot.show()
time.sleep(100)
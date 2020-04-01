import csv
import datetime
 
FILENAME = "data.csv"
tarif1 = datetime.datetime(2020,4,1,00,00,00)
tarif2 = datetime.datetime(2020,4,1,00,30,00)
tarif3 = datetime.datetime(2020,4,1,1,00,00)
summa_tlf = 0
summa_sms = 0
summa = 0
with open(FILENAME, "r", newline="") as file:
	reader = csv.reader(file)
	i= 0
	for row in reader:
		#входящие
		if row[2] == '933156729':
			t = row[0]
			dt = datetime.datetime.strptime(t, '%Y-%m-%d %H:%M:%S')
			#от 00:00 до 00:30
			if (dt.time() < tarif2.time()) and (dt.time() > tarif1.time()):
				summa_tlf = summa_tlf + 0*float(row[3])
			#от 00:30 до 01:00
			if (dt.time() > tarif2.time()) and (dt.time() < tarif3.time()):
				summa_tlf = summa_tlf + 2*float(row[3])
		#исходящие
		if row[1] == '933156729':
			t = row[0]
			dt = datetime.datetime.strptime(t, '%Y-%m-%d %H:%M:%S')
			#от 00:00 до 00:30
			if (dt.time() < tarif2.time()) and (dt.time() > tarif1.time()):
				summa_tlf = summa_tlf + 3*float(row[3])
			#от 00:30 до 01:00
			if (dt.time() > tarif2.time()) and (dt.time() < tarif3.time()):
				summa_tlf = summa_tlf + 2*float(row[3])
			#смс
			if int(row[4]) > 50:
				summa_sms = summa_sms + (int(row[4])-50)*2
print ("Итоговая стоимость звонков и смс абонента 933156729 (в рублях): ",summa_tlf+summa_sms)
print("Итоговая стоимость всех звонков абонента 933156729 (в рублях): ",summa_tlf)
print("Итоговая стоимость всех СМС абонента 933156729 (в рублях):",summa_sms)

		




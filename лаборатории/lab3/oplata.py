import sys
import os
import comtypes.client
from docxtpl import DocxTemplate

doc = DocxTemplate("shablon.docx")
all = 166.44 + 53.38 #сумма за телефонию и интернет
nds = 0.2*all #НДС
total = all + nds #Итого с НДС
context = { 'bank' : "ПАО Сбербанк", 'bik' : "123456789", 'sch1':"123456789123456789", 'inn':"47586907385", 'kpp':"4536758908", 'sch2':"123456789123654789", 'name':"ООО Палитра", 'number':"123", 'date1':"27 апреля", 'date2':"20", 'inn2':"12346907385", 'kpp2':"9876758908", 'index':"123321", 'city':"г. Санкт-Петербург", 'street':"Кронверкский пр-т", 'dom':"дом 49", 'name2':"Васильев А.Г.", 'tel':"933156729", 'osnova':"№ 12345 от 25.03.2020", 'telefonia':"Услуга Телефония", 'price1':"166,44", 'internet':"Услуга Интернет", 'price2':"53,38", 'together':all, 'nds':nds, 'itogo':total, 'itogo2':"Двести шестьдесят три рубля и семьдесят восемь копеек", 'N1':"Сидоров А.А.",'N2':"Панов П.П."}
doc.render(context)
doc.save("СЧЕТ.docx")

wdFormatPDF = 17

in_file = os.path.abspath ("СЧЕТ.docx")
out_file = os.path.abspath("Счёт.pdf")
word = comtypes.client.CreateObject('Word.Application')
doc = word.Documents.Open(in_file)
doc.SaveAs(out_file, FileFormat=wdFormatPDF)
doc.Close()
os.remove("СЧЕТ.docx")


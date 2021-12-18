from Other_files import Append_to_baza as app
from Other_files import Read_on_baza as tarjimon
while True:
    tanlov = int(input("1.so'z kiritish\n2.so'z qidirish\n0.chiqish\n>>>> "))
    if tanlov==1:
        app.append()
    elif tanlov==2:
        tarjimon.tarjimasi()
    elif tanlov==0:
        break
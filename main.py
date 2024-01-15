import yfinance as yf
import csv
from tabulate import tabulate


#getting user input
nav=input("Ievadiet 0, ja vēlaties ievadīt datus, 1 ja vēlaties apskatīt statistiku, -1, ja vēlaties iziet no programmas, 2 ja vēlaties apskatīt visus datus: ")

while nav=="0":
    stock = input("Lūdzu ievadiet vēlamas akcijas tickeri (piem., AAPL): ")
    start_date = input("Ievadiet invsetīciju sākuma datumu (formā yyyy-mm-dd): ")
    end_date = input("Ievadiet beigu datumu (formā yyyy-mm-dd): ")
    freq = input("Ievadiet 1, ja vēlatie iemaksas veikt reizi mēnesī, 2, ja vēlaties tās veikt reizi gadā: ")
    cap = input("Ievadiet sākuma kapitāla summu: ")
    sum = input("Ievadiet kādu summu vēlaties iemaksāt katrā reizē: ")
    match freq:
        case "1":
            df = yf.download(stock,
                start=start_date,
                end=end_date,
                progress=False)
            df['Date'] = df.index
            df_first_of_month = df.groupby(df['Date'].dt.to_period("M")).first()
            df_last_of_month = df.groupby(df['Date'].dt.to_period("M")).last()

            portfelis = float(cap)/float(df_first_of_month.iloc[0]['Open'])

            for i in range (1, len(df_first_of_month)):
                portfelis=portfelis+float(sum)/df_first_of_month.iloc[i]['Open']
            protfela_vertiba=portfelis*float(df_last_of_month.iloc[len(df_last_of_month)-1]['Close'])
            pelna=protfela_vertiba-float(cap)-(float(sum)*int(len(df_first_of_month)))
            iemaksas=float(cap)+(float(sum)*int(len(df_first_of_month)))
            pelna_procentos = (float(pelna)/float(iemaksas))*100
            print("Dati saglabāti!")
            data=[stock, freq, start_date, end_date,iemaksas, portfelis, protfela_vertiba, pelna, pelna_procentos]
            with open('data.csv', mode='a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)
            nav=input("Ievadiet 0, ja vēlaties ievadīt datus, 1 ja vēlaties apskatīt statistiku, -1, ja vēlaties iziet no programmas: ")

        case "2":
            df = yf.download(stock,
                start=start_date,
                end=end_date,
                progress=False)
            df['Date'] = df.index
            df_first_of_year = df.groupby(df['Date'].dt.to_period("Y")).first()
            df_last_of_year = df.groupby(df['Date'].dt.to_period("Y")).last()

            portfelis = float(cap)/float(df_first_of_year.iloc[0]['Open'])

            for i in range (1, len(df_first_of_year)):
                portfelis=portfelis+float(sum)/df_first_of_year.iloc[i]['Open']
            protfela_vertiba=portfelis*float(df_last_of_year.iloc[len(df_last_of_year)-1]['Close'])
            pelna=protfela_vertiba-float(cap)-(float(sum)*int(len(df_first_of_year)))
            iemaksas=float(cap)+(float(sum)*int(len(df_first_of_year)))
            pelna_procentos = (float(pelna)/float(iemaksas))*100
            print("Dati saglabāti!")
            data=[stock,freq ,start_date, end_date, iemaksas, portfelis, protfela_vertiba, pelna, pelna_procentos]
            with open('data.csv', mode='a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data) 
            nav=input("Ievadiet 0, ja vēlaties ievadīt datus, 1 ja vēlaties apskatīt statistiku, -1, ja vēlaties iziet no programmas: ")   

if nav=="1":
    data=[]
    with open("data.csv", "r") as f:
        next(f)
        for line in f:
            row=line.rstrip().split(",")
            data.append(row)
    max_return = 0
    info=[]
    for i in range (0, len(data)):
        return_value = float(data[i][8])
        if(return_value>max_return):
            max_return=return_value
            info=data[i]
    print("Vieslielākā relatīvā pelņa ir", info[0], "akcijai ar peļņu", info[8], "procentu apmērā laika posmā no", info[2], "līdz", info[3])

    min_return = float(data[0][8])
    info=[]
    for i in range (0, len(data)):
        return_value = float(data[i][8])
        if(return_value<min_return):
            min_return=return_value
            info=data[i]
    print("Viesmazākā relatīvā pelņa ir", info[0], "akcijai ar peļņu", info[8], "procentu apmērā laika posmā no", info[2], "līdz", info[3])
elif nav=="2":
    data=[]
    with open("data.csv", "r") as f:
        next(f)
        for line in f:
            row=line.rstrip().split(",")
            data.append(row)
    print(tabulate(data, headers=["Stock"," ", "Sākuma datums", "Beigu datums", "Iemaksātais daudzums", "Akciju daudzums", "Portfeļa vērtība", "Pelņa","Peļņa, %"]))

else:
    exit()



        


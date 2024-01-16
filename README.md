# Projekta darbs "Investīciju kalkulators"

## Programmas uzdevums:
"Investīviju kalkulators" ir programma, kas ļauj lietotājam aprēķināt investīciju peļņu noteiktā laika posmā ar iespēju izvēlēties vēlamo akciju, starta kapitāla summu, reinvestēšanas biežumu un reinvestējamās summas apjomu. Visi aprēķinātie dati tiek saglabāti .csv failā, kas dod iespēju pēcāk lietotājam apskatīt un analizēt dažādu akciju peļņas, dažādos periodos kā arī piedāvā izvadīt lielāko un mazāko procentuālo peļņu. 

## Programmas darbība, izmanotās bibliotēkas:
### Datu iegūšana
Programmai ir navigācija, kas sastāv no 4 iespējām: Ievadīt jaunus akciju datus, izvadīt statistiku par lielāko un mazāko procentuālo peļņu, izvadīt visus saglabātos datus un iziet no programmas. Finanšu dati tiek iegūti no "Yahnoo finance" (href - https://finance.yahoo.com/) un to iegūšanai tiek izmantota bibliotēka "yfinance" (href - https://pypi.org/project/yfinance/). Funkcija "yf.download()" kā parametrus pieprasa akcijas tickeri, sākuma datumu un beigu datumu. Dati tiek saglabāti dataframe, kas ļauj pēcāk ar tiem manipulēt. 
### Datu apstrāde
Atkarībā no lietotāja izvēlētā reinvestīciju biežuma, dati tiek kārtoti ar frekvenci "freq="M"" vai "freq="Y"" un tiek ņemta mēneša vai gada  pirmā akcijas "Open" cena. Kad dati ir sakārtoti, akciju daudzuma aprēķināšanai tiek ņemta šī "Open" cena un reizināta ar reinvestējamo summu. Lai aprēķinātu Akciju vērtību investīcijas perioda beigās, tiek ņemta pēdējā pieejamā "Close" cena laika periodā un reizināta ar uzkrāto akciju daudzumu. Procentuālā peļņa katrai akcijai tiek aprēķināta dalot peļņu ar investēto naudas summu. 
### Datu rakstīšana un lasīšana
Kad visi dati ir aprēķināti, tie tiek saglabāti failā "data.csv". Faila rakstīšanai un lasīšanai tiek izmantota bibliotēka "csv" (href - https://docs.python.org/3/library/csv.html). Datu saglabāšanai tiek izmantota funkcija "open("data.csv, mode="a")", kas papildina failu ar jaunu ierakstu, savukārt datu lasīšanai tiek izmantota "open("data.csv, mode="r")". Kad lietotājs pieprasa visu datu izvadīšanu, dati tiek ielasīti sarakstā un izvadīti, papildus formatējot ar bibliotēkas "tabulate" (href - https://pypi.org/project/tabulate/) palīdzību, savukārt brīdī, kad tiek pieprasīta statistika, ar cikla palīdzību tiek salīdzinātas "Peļņa procentos" vērtības, saglabātas mainīgajos un izvadīta lielākā un mazākā vērtība.  

## Programmas izmantošanas metodes:
Programma ir piemērota lietotājiem, kas vēlas sākt investēt akciju tirgū, bet nav pārliecināti par savu investēšanas stratēģiju. Lai arī aprēķiniem tiek ņemti pagātnes dati (programmatūra nemodelē iespējamās nākotnes vērtības), šāda informācija var būt noderīga analīzes nolūkiem un stratēģijas izstrādāšanai. Mainot ievaddatus (Akcija, laika periods, iemaksu biežums, starta kapitāls, iemaksu apjoms) var modelēt dažādas situācijas, tādā vedā izvēloties sev piemērotāko investēšanas veidu. 


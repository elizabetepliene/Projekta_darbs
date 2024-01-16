Projekta darbs "Investīciju kalkulators"

Vispārējs apraksts:
"Investīviju kalkulators" ir programma, kas ļauj lietotājam aprēķināt investīciju peļņu noteiktā laika posmā ar iespēju izvēlēties vēlamo akciju, starta kapitāla summu, reinvestēšanas biežumu un reinvestējamās summas apjomu. Visi aprēķinātie dati tiek saglabāti .csv failā, kas dod iespēju pēcāk lietotājam apskatīt un analizēt dažādu akciju peļņas, dažādos periodos kā arī piedāvā izvadīt lielāko un mazāko procentuālo peļņu. 

Programmas darbība, izmanotās bibliotēkas:
Programmai ir navigācija, kas sastāv no 4 iespējām: Ievadīt jaunus akciju datus, izvadīt statistiku par lielāko un mazāko procentuālo peļņu, izvadīt visus saglabātos datus un iziet no programmas. Finanšu dati tiek iegūti no "Yahnoo finance" (href - https://finance.yahoo.com/) un to iegūšanai tiek izmantota bibliotēka "yfinance" (href - https://pypi.org/project/yfinance/),kas kā funkcijas parametrus pieprasa akcijas tickeri, sākuma datumu un beigu datumu. Dati tiek saglabāti dataframe, kas ļauj pēcāk ar tiem manipulēt. 
Atkarībā no lietotāja izvēlētā reinvestīciju biežuma, tiek ņemta mēneša vai gada  pirmā akcijas "Open" cena. Kad dati ir sakārtoti, akciju daudzuma aprēķināšanai tiek ņemta šī "Open" cena un reizināta ar reinvestējamo summu. Lai aprēķinātu Akciju vērtību investīcijas perioda beigās, tiek ņemta pēdējā pieejamā "Close" cena laika periodā un reizināta ar uzkrāto akciju daudzumu. Procentuālā peļņa katrai akcijai tiek aprēķināta dalot peļņu ar investēto naudas summu. Kad visi dati ir aprēķināti, tie tiek saglabāti failā "data.csv". 
"data.csv" faila rakstīšanai un lasīšanai tiek izmantota bibliotēka "csv" (href - https://docs.python.org/3/library/csv.html). Datu saglabāšanai tiek izmantota funkcija "open("data.csv, mode="a")", kas papildina failu ar jaunu ierakstu, savukārt datu lasīšanai tiek izmantota "open("data.csv, mode="r")". 


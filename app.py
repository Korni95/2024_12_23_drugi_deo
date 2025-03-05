import sys
import arrow

timezone = None
date_format = None
#print(arrow.now())
if len(sys.argv) > 1:
    #print(sys.argv) PROVERA STA VIDI PROGRAM
    #print("Ima dodathih argumenata")
    n = len(sys.argv)
    for i in range(len(sys.argv)):
        #python app.py -t Asia/Tokyo
        #python app.py --timezone Asia/Tokyo
        if sys.argv[i] == "-t" or sys.argv[i] == "--timezone":
            timezone = sys.argv[i + 1]
        elif sys.argv[i] == "-f" or sys.argv[i] == "--format":
            date_format = sys.argv[i + 1]
            
if timezone is None and date_format == None:
    print(arrow.now().format("DD.MM.YYYY. HH:mm"))
elif timezone is None and date_format is not None:
    try:
        print(arrow.now().format(date_format))
    except:
        print(f"Format '{date_format}' nije validni format.\nPogledajte dokumentaciju na: https://arrow.readthedocs.io/")
elif timezone is not None and date_format is None:
    try:
        print(arrow.utcnow().to(timezone).format("DD.MM.YYYY. HH:mm"))
    except:
        print(f"Vremenska zona nije dobra.\nPogledajte dokumentaciju na: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones")
else:
    try:
         print(arrow.utcnow().to(timezone).format(date_format))
    except Exception as ex:
        print(ex)
        
'''
            if i < n-1:
                try:
                    t_str = arrow.utcnow().to(sys.argv[i+1]).format("DD.MM.YYYY. HH:mm")
                    print(t_str)
                except:
                    print("Nije prepoznata vremenska zona: ", sys.argv[i+1])
                
            else:
                print("Potrebno je da unesete vremensku zonu.")
else:
    #print("Niste pokrenuli aplikaciju sa dodatnim argumentima.")
    print(arrow.now().format("DD.MM.YYYY. HH:mm"))
'''
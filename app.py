import sys
import arrow
#print(arrow.now())
if len(sys.argv) > 1:
    #print(sys.argv) PROVERA STA VIDI PROGRAM
    #print("Ima dodathih argumenata")
    n = len(sys.argv)
    for i in range(len(sys.argv)):
        #python app.py -t Asia/Tokyo
        #python app.py --timezone Asia/Tokyo
        if sys.argv[i] == "-t" or sys.argv[i] == "--timezone":
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
    
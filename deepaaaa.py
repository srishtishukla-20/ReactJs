print("hello")
def main():
    allDataDict={}
    specific_data={}
    list=[]
    main_dict={"caruser":list}


    i=0
    bike=10
    car=10
    bus=10
    bikeSpot=0
    carSpot=0
    busSpot=0
    while True:
    
        Vnumber=int(input(" vnumber :  "))
        Vtype=input("Vtype :  ")
        if Vtype =="bike":
            if bike==8:
                print("no apace availabe")
                # break
            else:
                car-=1
                bikeSpot+=  1
                print("spot available",bike,"your type :",Vtype,"your number :",Vnumber,"spotNumber",bikeSpot)
            
        elif Vtype =="car":
            if bus==8:
                print("no apace availabe")
                # break
            else:
                car-=1
                carSpot+=1
                print("spot available",car,"your type :",Vtype,"your number :",Vnumber,"spotNumber",carSpot)
        elif Vtype =="bus":
                if bus==8:
                    print("no apace availabe")
                    # break
                else:
                    bus-=1
                    busSpot+=1
                    print("spot available",bus,"your type :",Vtype,"your number :",Vnumber,"spotNumber",busSpot)
        else:
            print("Sorry spot is not available for this type of vehicle")

        if bike==8 and car==8 and bus==8 :
            print("jjj")
            break
        
    
    i+=1

    
main()
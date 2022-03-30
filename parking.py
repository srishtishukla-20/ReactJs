import time
import json
import os


print("hellow")
def main():
    allDataDict={}
    specific_data={}
    list=[]
    main_dict={"car_user":list}

    bike=10
    car=10
    bus=10
    bikeSpot=0
    carSpot=0
    busSpot=0

    while True:
        inTime= time.asctime(time.localtime(time.time()))
    
        Vnumber=int(input(" vnumber :  "))
        Vtype=input("Vtype :  ")
        if Vtype =="bike":
            if bike==8:
                print("no apace availabe")
                # break
            else:
                bike-=1
                bikeSpot+=  1
                specific_data["spots_number"]=bikeSpot
                print("spot available",bike,"your type :",Vtype,"your number :",Vnumber,"spotNumber",bikeSpot)
            
        elif Vtype =="car":
            if car==8:
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
        specific_data["vehicle_number"]=Vnumber
        specific_data["vehicle_type"]=Vtype
        
        specific_data["inTime"]=inTime
        allDataDict[Vnumber]=specific_data
        
        if os.path.exists("task1.json")==True:
            with open("task1.json") as f1:
                file1=json.loads(f1.read())
                k=file1["car_user"]
                k.append(allDataDict)
                main_dict["car_user"]=k
                with open("task1.json","w") as f_2:
                    json.dump(main_dict, f_2, indent=4)
        else:
            list.append(allDataDict)
            with open ("task1.json","w") as f:
                file=json.dump(main_dict,f,indent=4)
main()



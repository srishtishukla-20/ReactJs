import time
import json
import os

allDataDict={}
specific_data={}
list=[]
main_dict={"car_user":list}

print("* WELCOME TO THE PYTHON PARKING SLOT * \n ")
motorcycle_spots=10
compact_spots=10
large_spots=10
motorcycle_spot_number=0
compact_spots_number=0
large_spots_number=0


def chekIn_Entry(motorcycle_spots, compact_spots,large_spots,motorcycle_spot_number,compact_spots_number,large_spots_number):
    inTime= time.asctime(time.localtime(time.time()))

    print ("\nWe have Theseslots available : ","\n","Motorcycle spots = ",motorcycle_spots,"\n","Compact spots = ",compact_spots,"\n","Large_spots = ",large_spots)
    i=0
    while i<=32:
        inTime= time.asctime(time.localtime(time.time()))
    
        Vnumber=int(input(" Vehicle_number :  "))
        Vtype=input("Vehicle_type :  ")
        if Vtype =="bike":
            if motorcycle_spots==0:
                print("no apace availabe")
            #     # break
            # else:
                motorcycle_spots-=1
                motorcycle_spot_number+=  1
                specific_data["spots_number"]=motorcycle_spots
                print("spot available",motorcycle_spots,"your type :",Vtype,"your number :",Vnumber,"spotNumber",motorcycle_spot_number)
            
        elif Vtype =="car":
            if compact_spots==0:
                print("no apace availabe")
            #     # break
            # else:
                compact_spots-=1
                compact_spots_number+=1
                specific_data["spots_number"]=compact_spots
                print("spot available",compact_spots,"your type :",Vtype,"your number :",Vnumber,"spotNumber",compact_spots_number)
        elif Vtype =="bus":
                if large_spots==0:
                    print("no apace availabe")
                #     # break
                # else:
                    large_spots-=1
                    large_spots_number+=1
                    specific_data["spots_number"]=large_spots
                    print("spot available",large_spots,"your type :",Vtype,"your number :",Vnumber,"spotNumber",large_spots_number)
        else:
            print("Sorry spot is not available for this type of vehicle")

        if motorcycle_spots==0 and compact_spots==0 and large_spots==0 :
            print("No space")
            break
        i+=1

        specific_data["vehicle_number"]=Vnumber
        specific_data["vehicle_type"]=Vtype
        specific_data["large_spots_number"]=large_spots_number
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
            






def checkOut_Entry():
    out_vehicle_number=input("Please enter your vehicle number :   ")

    with open ("task1.json") as f:
        data_for_amount=json.load(f)
        for key in data_for_amount["car_user"]:
            # for pre_key in key.keys():
                # print(key)
            if out_vehicle_number in key.keys():
                # print(out_vehicle_number)
                intime=key[out_vehicle_number]["inTime"][11:17]
                # print(intime)
                for_amount1=intime.replace(":","")
                print(for_amount1)

                outtime= time.asctime(time.localtime(time.time()))
                temp_outtime=outtime[11:17]
                for_amount2=temp_outtime.replace(":","")
                print(for_amount2)
                amoumt=abs(int(for_amount1)-int(for_amount2))
                if amoumt<30:
                    amoumt=30
                    print(amoumt)
                else:
                    amoumt=amoumt//30*50
                    print(amoumt)
                print("__This is your check in data__ \nout_vehicle_number  :  ",key[out_vehicle_number],"\nvehicle_type  :  ",key[out_vehicle_number]["vehicle_type"],"\nlarge_spots_number  :  ",key[out_vehicle_number]["large_spots_number"],"\ninTime  :  ",key[out_vehicle_number]["inTime"],"\nCheck out time :   ",outtime,"\nYour amount is :   ",amoumt)
                break

            else:
                print("\n\n              XXX   Your data does not exist  XXX    ")
                break


def options():
    enterance =  int(input("If you want to checkIn for it press 1\nIf you want to check out for it press 2\nIf you are here for visit only press 3\n\nPRESS  :   "))
    if enterance==1:
        chekIn_Entry(motorcycle_spots, compact_spots,large_spots,motorcycle_spot_number,compact_spots_number,large_spots_number)

    elif enterance==2:
        checkOut_Entry()

    elif enterance==3:
        print("Thank you for visiting ")

    else:
        print("\nERROR\nPlease press right key!")
options()


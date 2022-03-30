import time
import json
import os

allDataDict={}
specific_data={}
list=[]
main_dict={"car_user":list}

print("* WELCOME TO THE PYTHON PARKING SLOT * \n ")
motorcycle_spots=32
compact_spots=32
large_spots = 32

motorcycle_spot_number=1
compact_spots_number=1
large_spots_number = 1

def chekIn_Entry(motorcycle_spots, compact_spots,large_spots,motorcycle_spot_number,compact_spots_number,
large_spots_number):
    inTime= time.asctime(time.localtime(time.time()))

    print ("\nWe have Theseslots available : ","\n","Motorcycle spots = ",motorcycle_spots,"\n","Compact spots = ",compact_spots,"\n","Large_spots = ",large_spots)
    vehicle_type = input("Please enter your Vehicle Type :   ")
    vehicle_number = input("Please enter your Vehicle Number :   ")

    while motorcycle_spot_number<=32 or compact_spots_number<=32 or large_spots_number<=32:

        if vehicle_type == "bike":
            motorcycle_spot_number+=1
              
            print("\n\nTHIS IS YOUR RISIPT\n** FOR STARTING 30 MINUTES COST WILL BE 50 RUPEES FOR EVERY NEXT 30 MINUTES WILL INCREASE BY 30 RUPEES **","\nvehicle type = ",vehicle_type,"\nvehicle_number = ",vehicle_number,"\nparkin slot number = ",motorcycle_spot_number)

        
        elif vehicle_type=="car":
            compact_spots_number+=1
           
        
            print("\n\nTHIS IS YOUR RISIPT\n** FOR STARTING 30 MINUTES COST WILL BE 50 RUPEES FOR EVERY NEXT 30 MINUTES WILL INCREASE BY 30 RUPEES  **","\nvehicle type = ",vehicle_type,"\nvehicle_number = ",vehicle_number,"\nparkin slot number = ",compact_spots_number)
            
        elif vehicle_type == "bus":
            large_spots_number+=1
           
            print("\n\nTHIS IS YOUR RISIPT\n** FOR STARTING 30 MINUTES COST WILL BE 50 RUPEES FOR EVERY NEXT 30 MINUTES WILL INCREASE BY 30 RUPEES  **","\nvehicle type = ",vehicle_type,"\nvehicle_number = ",vehicle_number,"\nparkin slot number = ",large_spots_number)
        
        else:
            print("Sorry for this type of vehicle the slot is not available ")
    while motorcycle_spots>=1 or compact_spots>=1 or large_spots>=1:
        if vehicle_type == "bike":
            motorcycle_spots-=1
                
            print("\n\nTHIS IS YOUR RISIPT\n** FOR STARTING 30 MINUTES COST WILL BE 50 RUPEES FOR EVERY NEXT 30 MINUTES WILL INCREASE BY 30 RUPEES **","\nvehicle type = ",vehicle_type,"\nvehicle_number = ",vehicle_number,"\nparkin slot number = ",motorcycle_spot_number)
        elif vehicle_type=="car":
            compact_spots-=1
           
            print("\n\nTHIS IS YOUR RISIPT\n** FOR STARTING 30 MINUTES COST WILL BE 50 RUPEES FOR EVERY NEXT 30 MINUTES WILL INCREASE BY 30 RUPEES  **","\nvehicle type = ",vehicle_type,"\nvehicle_number = ",vehicle_number,"\nparkin slot number = ",compact_spots_number)
            
        elif vehicle_type == "bus":
            large_spots-=1
           
            print("\n\nTHIS IS YOUR RISIPT\n** FOR STARTING 30 MINUTES COST WILL BE 50 RUPEES FOR EVERY NEXT 30 MINUTES WILL INCREASE BY 30 RUPEES  **","\nvehicle type = ",vehicle_type,"\nvehicle_number = ",vehicle_number,"\nparkin slot number = ",large_spots_number)
        
        else:
            print("Sorry for this type of vehicle the slot is not available ")

        
    specific_data["vehicle_number"]=vehicle_number
    specific_data["vehicle_type"]=vehicle_type
    specific_data["large_spots_number"]=large_spots_number
    specific_data["inTime"]=inTime
    allDataDict[vehicle_number]=specific_data
    
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
    enterrence =  int(input("If you want to checkIn for it press 1\nIf you want to check out for it press 2\nIf you are here for visit only press 3\n\nPRESS  :   "))
    if enterrence==1:
        chekIn_Entry(motorcycle_spots, compact_spots,large_spots,motorcycle_spot_number,compact_spots_number,large_spots_number)

    elif enterrence==2:
        checkOut_Entry()

    elif enterrence==3:
        print("Thank you for visiting ")

    else:
        print("\nERROR\nPlease press right key!")
options()



# def nextEntry():
#     while True:
#         entry=int( input("\n\n\nfor Entry press 1 for exit press \n  PRESS  :   "))
#         if entry==1:
#             options()
#         else:
#             print(" __EXIT__")
    
# nextEntry()
    

# __________________
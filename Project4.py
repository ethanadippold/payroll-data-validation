#Program 4
#Ethan Dippold
#D
InputFile=open("PayData.txt","r")
Lines=InputFile.readlines()
for i in range(len(Lines)):
    Lines[i]=Lines[i].rstrip()
for i in range(len(Lines)):
    if i==0:
        print(Lines[0])
    else:
        print(Lines[i])
        try: 
            x=Lines[i].split(":")
            y=x[0].strip()
            z=x[1].strip()
            paytypes=[b.strip() for b in y.split(",")]
            regular=int(paytypes[0])
            otpay=int(paytypes[1])
            totpay=int(paytypes[2])

            if totpay !=(regular + otpay):
                print("pay calc reports problem")
        except: 
            print ("formatting problem")

import base64
import pandas as pd

### READS CSV

df = pd.read_csv('216Export.csv')

### SELECT CSV COLUMN 
Direct = df['URL']
#decoded_binary_data = base64.b64decode(df)
#my_string.split("world",1)[1]

### CREATE DYNAMIC LISTS
keyslist = []
Partnerlist = []
### FOR CYCLE FOR ITERATING OVER EACH URL
for URL in Direct:
    stringz = str(URL)

    ### TRY TO CUT THE STRING AT GSPK, IF NOT WORK THEN ADD NONE TO STRING
    try:
        Partnerz = stringz.split("gspk=",1)[1]
    except:
        Partnerz = "NONE&gsxid="
    ### SAVE SPLITTED VALUED
    PartnerDef = Partnerz.split("&gsxid=",1)[0]
    Partnerstr = str(PartnerDef)
    keyslist.append(Partnerstr)
    value = Partnerstr
    ### IF THE BASE 64 LENGHTS IS INCORRECT, CORRECT IT AND DECODE IT
    try: 
        if len(value) % 4:
             value += '=' * (4 - len(value) % 4)
### DECODIFICATION METHOD
        PartnerKey = base64.urlsafe_b64decode(value).decode('utf-8')
    #except:
        #PartnerKey = 'Error'
        
    
    print(PartnerKey)
    Partnerlist.append(PartnerKey)
    
df['PartnerKey'] = Partnerlist
df.to_csv("Result.csv", encoding='utf-8', index=False)
    
#df2 = pd.DataFrame(Partnerlist) 
#decoded_binary_data = base64.b64decode(df2)
#print(decoded_binary_data)
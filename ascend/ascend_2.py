import re
import pytz
import pandas as pd
from datetime import datetime

customer_profile={
    'id':list(range(1,14,1)),
    
    'fullname':['Somchai Jaidee','Mr. Pongchai Sukhum','Samart T.','sarawut Aromdee','Miss Shakira Ifugao Sarte','Miss Autumn Dumlao','tanawat Chaiprasit','Nattapong Juntasa','Sirichai Kadesadayurat','chatchai Kaouthai','Teerapat Kasamsun','panupong Kongkatitum','Mr. Jovan Eliseo Manahan'],
    
    'country':['THA','Thailand','THAI','Thai','PHL','Philippines','BKK','Thai Land','THAILAND','thailand','thai','thai','philippines'],
    
    'email':['Somchai_J@email.com','PS@GM.com','samart.t@alphaSystem.com','sa.tan@nowhere','shakira.sarte@lemonworks.ph','autumn-d.webrover','tanawat@happiness.com','Natt_happy@enigmotors.in.th','sirichai.kadesadayurat@signalshade.org','0891125569','*Teerapat@pridesoftware.com','0099wera@karmabite.com','jovan@goldlimited.com'],
    
    'national_id':['1848823941380','9317894961770','00004716573017274','9-783-152311-163','PH68-192867-39','PH50-278965-89','9405423082031','3555155686052','2840070178083','7863689498428A','00009550456733749','3067271589470','PH72-618948-40'],
    
    'updated_timestamp':['1/5/2018 6:00:14 AM','2/22/2018 8:50:47 AM','1/18/2018 4:43:57 AM','1/3/2018 12:56:24 PM','2018-02-22 13:07:07','2018-02-12 02:12:58','2/23/2018 1:34:45 PM','2/20/2018 4:54:03 AM','1/11/2018 1:22:48 PM','1/19/2018 10:55:59 AM','1/11/2018 7:59:04 AM','1/19/2018 1:08:39 PM','2018-02-15 07:19:18']
    
}


#Create dataframe
csv_input=pd.DataFrame(customer_profile)

class dataConversion:
    def __init__(self):
        self.name = None
        self.country = None
        self.email = None
        self.id = None
        self.dt = None

    def verify_name(self, name):
        # print(name)
        name_lower = name.lower()
        for i in ["mr","mr.","ms","ms.","miss"]:
            if name_lower[:5].find(i) != -1:
                idx = name_lower.index(i)
                name_without_prefix = name[idx+len(i)+1:]
                return  name_without_prefix.strip()
        # print(name)
        return name.strip()
    
    def convert_country(self, country):
        if len(country) == 3:
            if country.lower() in ["tha","bkk"]:
                return "THA"
            elif country.lower().strip() in ["phl","mnl"]:
                return "PHL"
            else:
                return "Not found in database"
        else:
            if country.lower().find("thai") != -1:
                return "THA"
            if country.lower().find("phil") != -1:
                return "PHL"
            else:
                return "Not found in database"


    def check_email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email)):
            return email
    
        else:
            return "n/a"

    def verify_id(self, id, country):
        # print(id)
        # print(type(id))
        if isinstance(id, float):
            # print("Here")
            id = str(int(id))
        cleansed_id = id.replace("-","")
        if country.lower() == "tha":
            return cleansed_id[:13]
        elif country.lower() == "phl":
            if cleansed_id[:2].lower() == "ph":
                return cleansed_id[:10]
            else:
                return cleansed_id[:12]

    def convert_time(self, dt, country):
        local_time = None
        if country.lower() == "tha":
            local_time = pytz.timezone("Asia/Bangkok")
        elif country.lower() == "phl":
            local_time = pytz.timezone("Asia/Manila")
        else:
            return "Cannot convert timezone"
        for dt_format in ["%m/%d/%Y %I:%M:%S %p","%Y-%m-%d %H:%M:%S"]:
            try:
                naive_dt = datetime.strptime(dt, dt_format)
                local_dt = local_time.localize(naive_dt, is_dst=None)
                utc_dt = local_dt.astimezone(pytz.utc)
                return utc_dt
            except:
                continue


for index, row in csv_input.iterrows():
    # print("{} - {} {} {} {} {}".format(index,row['fullname'],row['country'],row['email'],row['national_id'],row['updated_timestamp']))
    dc = dataConversion()
    fullname = dc.verify_name(row['fullname'])
    country = dc.convert_country(row['country'])
    email = dc.check_email(row['email'])
    nation_id = dc.verify_id(row['national_id'], country)
    timestamp = dc.convert_time(row['updated_timestamp'], country)

    print("{} - {} {} {} {} {}".format(index,fullname,country,email,nation_id,timestamp))
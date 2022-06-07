import pandas as pd
import datetime as dt


#create object for data-frame

customer_profile={
    'id':list(range(1,14,1)),
    
    'fullname':['Somchai Jaidee','Mr. Pongchai Sukhum','Samart T.','sarawut Aromdee','Miss Shakira Ifugao Sarte','Miss Autumn Dumlao','tanawat Chaiprasit','Nattapong Juntasa','Sirichai Kadesadayurat','chatchai Kaouthai','Teerapat Kasamsun','panupong Kongkatitum','Mr. Jovan Eliseo Manahan'],
    
    'country':['THA','Thailand','THAI','Thai','PHL','Philippines','BKK','Thai Land','THAILAND','thailand','thai','thai','philippines'],
    
    'email':['Somchai_J@email.com','PS@GM.com','samart.t@alphaSystem.com','sa.tan@nowhere','shakira.sarte@lemonworks.ph','autumn-d.webrover','tanawat@happiness.com','Natt_happy@enigmotors.in.th','sirichai.kadesadayurat@signalshade.org','0891125569','*Teerapat@pridesoftware.com','0099wera@karmabite.com','jovan@goldlimited.com'],
    
    'national_id':['1848823941380','9317894961770','00004716573017274','9-783-152311-163','PH68-192867-39','PH50-278965-89','9405423082031','3555155686052','2840070178083','7863689498428A','00009550456733749','3067271589470','PH72-618948-40'],
    
    'updated_timestamp':['1/5/2018 6:00:14 AM','2/22/2018 8:50:47 AM','1/18/2018 4:43:57 AM','1/3/2018 12:56:24 PM','2018-02-22 13:07:07','2018-02-12 02:12:58','2/23/2018 1:34:45 PM','2/20/2018 4:54:03 AM','1/11/2018 1:22:48 PM','1/19/2018 10:55:59 AM','1/11/2018 7:59:04 AM','1/19/2018 1:08:39 PM','2018-02-15 07:19:18']
    
}


#Create dataframe
df_customer_profile=pd.DataFrame(customer_profile)

#Start Manipulate fullname column
#Get rid of Mr. Miss  
df_customer_profile['fullname']=pd.Series([i[len('Miss '):] if i.find('Miss')!=-1 else (i[len('Mr. '):] if i.find('Mr.')!=-1 else i) for i in df_customer_profile['fullname']])

#insert parentheses for middle name
df_customer_profile['fullname']=pd.Series([i if len(i.split())==2 else '{} ({}) {}'.format(i.split()[0],i.split()[1],i.split()[-1]) for i in df_customer_profile['fullname']])

#End fullname column


#Start Manipulate country column (may be could use pycountry)
#TH
df_customer_profile['country']=pd.Series(['THA' if (i.lower()).split()[0] in 'thailand' else ('THA' if i=='BKK' else i) for i in df_customer_profile['country']])



#PHL
df_customer_profile['country']=pd.Series(['PHL' if i.lower() in 'philippines' else i for i in df_customer_profile['country']])

#End Manipulate country column


#Start Manipulate email column
df_customer_profile['email']=pd.Series([i if i.find('@')!=-1 and i[i.find('@'):].find('.')!=-1 else 'n/a' for i in df_customer_profile['email']])

#End Manipulate email coulumn


#Start Manipulate national_id column
#Get rid of '-'
df_customer_profile['national_id']=pd.Series([i if i.find('-')==-1 else ''.join([j for j in i.split('-') ]) for i in df_customer_profile['national_id']])

#TH national_id must 13 digits
df_customer_profile['national_id']=pd.Series([i if i.find('A')==-1 else i[:len(i)-1] for i in df_customer_profile['national_id']])
df_customer_profile['national_id']=pd.Series([i if len(i)<=13 else i[4:] for i in df_customer_profile['national_id']])


#End Manipulate national_id column

#Start Manipulate updated_timestamp
df_customer_profile['updated_timestamp']=pd.to_datetime(df_customer_profile['updated_timestamp'])








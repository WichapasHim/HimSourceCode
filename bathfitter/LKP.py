
columns1="""[CommissionBK]
,[CommissionSK]
,[CommissionSourceID]
,[CommissionTypeSK]
,[EOISK]
,[EmployeeSK]
,[InstallType]
,[PayableDateSK]
,[LineAmount]
,[dwEffectiveFrom]
,[dwEffectiveTo]
,[dwActiveRec]
,[dwCreateDate]
,[dwUpdateDate]
,[dwType1Hash]
,[dwType2Hash]"""



f=open('C:\\Users\\Wichapas.Darojana\\Him\\Personsal\\Python\\bathfitter\\sql.txt',mode='w')
def gen_sql(columns1:str):
    a=''.join(columns1.split('\n'))
    #print(a)
    s=''
    for i in a:
        if i=='[' or i==']':
            continue
        s=s+i
    #print(s)        
    column_clean=s.split(',')
    column_clean.pop(0)
    #print(column_clean)
    #print(column_clean)
    #h='TARGET.{} <> SOURCE.{} OR'.format(column_clean[0],column_clean[0])
    #print(h)
    column_clean_2=[]
    for i in column_clean:
        s='TARGET.{}<>SOURCE.{}\n'.format(i,i)
        column_clean_2.append(s)
    final_clean_1=' OR '.join(column_clean_2)
    #print(final_clean_1)


    column_clean_3=[]
    for i in column_clean:
        s='TARGET.{}=SOURCE.{}'.format(i,i)
        column_clean_3.append(s)
        
    final_clean_2=' ,\n'.join(column_clean_3)

    return """WHEN MATCHED 

THEN UPDATE SET \n {}

WHEN NOT MATCHED BY TARGET 


""".format(final_clean_2)
    
    
   
    
f.write(gen_sql(columns1))



def makec (column):
    a=''.join(columns1.split('\n'))
    #print(a)
    s=''
    for i in a:
        if i=='[' or i==']':
            continue
        s=s+i
    #print(s)        
    column_clean=s.split(',')
    urfirst = "THEN \nINSERT\n ("
    ursecond = "\n VALUES \n("
    for c in column_clean:
        urfirst=urfirst+c+",\n"
        ursecond = ursecond +"SOURCE."+c+",\n"
    urfirst=urfirst[0:-1]+")"
    ursecond=ursecond[0:-1]+")"
    return urfirst[:-2]+')'+ursecond[:-2]+')'
    
f.write(makec(columns1))

f.close()





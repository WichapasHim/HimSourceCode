UPDATE [dbo].[SrcUpGaurd_staging_1]
SET [EQ Assets]=replace(replace(replace([EQ Assets],'[',''),']',''),'"','')

DECLARE @i INT =1
DECLARE @j INT=1
DECLARE @COUNT_ID INT=(SELECT COUNT(*) FROM dbo.SrcUpGaurd_staging_1)

WHILE(@i<=@COUNT_ID)
BEGIN
        DECLARE @COUNT_HOST INT=(SELECT a.COUNT_ID FROM (SELECT [id],LEN([EQ Assets]) -len(replace([EQ Assets],',',''))+1 as COUNT_ID FROM [dbo].[SrcUpGaurd_staging_1] where @i=upgaurd_SK) as a)
        print @COUNT_HOST
        print @i
        IF (@COUNT_HOST=1)
            BEGIN
                INSERT INTO dbo.SrcUpGaurd_staging_2  
                    SELECT [id]
                    ,[Title]
                    ,[Finding]
                    ,[Risk]
                    ,[Category]
                    ,[Severity]
                    ,[Overview]
                    ,[Remediation Overview]
                    ,[EQ Assets]
                    ,[Domain]
                    ,[UpGaurdDomainName]
                    ,[UpGaurdDomainIP]
                    ,[Source] FROM dbo.SrcUpGaurd_staging_1 where @i=upgaurd_SK
            END
        ELSE
            BEGIN
               
                WHILE (@j<=@COUNT_HOST)
                BEGIN
                    DECLARE @SEP_HOST VARCHAR(4000)=(SELECT a.sep           from              (SELECT 
                                        value as sep ,ROW_NUMBER() OVER (ORDER BY value ) as ROWNUM
                                        FROM 
                                        STRING_SPLIT((select [EQ Assets] from dbo.SrcUpGaurd_staging_1 where upgaurd_SK=@i), ',')
                            
                            WHERE
                                TRIM(value) <> '' ) as a
                    where a.rownum=@j)

                    INSERT INTO dbo.SrcUpGaurd_staging_2  
                    SELECT [id]
                    ,[Title]
                    ,[Finding]
                    ,[Risk]
                    ,[Category]
                    ,[Severity]
                    ,[Overview]
                    ,[Remediation Overview]
                    ,@SEP_HOST
                    ,[Domain]
                    ,[UpGaurdDomainName]
                    ,[UpGaurdDomainIP]
                    ,[Source] FROM dbo.SrcUpGaurd_staging_1 where @i=upgaurd_SK

                    
                    SET @j+=1
                    
                
                END
            END
    SET @j=1
    SET @i+=1
END
      
 


UPDATE [dbo].[SrcUpGaurd_test]
SET [EQ Assets]=replace(replace(replace([EQ Assets],'[',''),']',''),'"','')

DECLARE @i INT =0
DECLARE @j INT=0
DECLARE @COUNT_ID INT=(SELECT COUNT(*) FROM dbo.SrcUpGaurd_test)

WHILE(@i<@COUNT_ID)
BEGIN
        DECLARE @COUNT_HOST INT=(SELECT a.COUNT_ID FROM (SELECT [id],LEN([EQ Assets]) -len(replace([EQ Assets],',',''))+1 as COUNT_ID FROM [dbo].[SrcUpGaurd_test] where @i+1=upgaurd_SK) as a)
        IF (@COUNT_HOST=1)
            BEGIN
                print 'BET'
            END
        ELSE
            BEGIN
                DECLARE @LEN_SEP_HOST INT=0
                
                
                WHILE (@j<@COUNT_HOST)
                BEGIN
                    DECLARE @SEP_HOST VARCHAR(4000)=replace((SELECT substring([EQ Assets],0,(SELECT CHARINDEX(',',[EQ Assets],0) from [dbo].[SrcUpGaurd_test] where @i+1=upgaurd_SK)) from [dbo].[SrcUpGaurd_test] where @i+1=upgaurd_SK),',','')
                    print @SEP_HOST
                    SET @j+=1
                    SET @LEN_SEP_HOST+=LEN(@SEP_HOST)
                    /*update dbo.SrcUpGaurd_test
                    SET [EQ Assets]=RIGHT([EQ Assets],LEN([EQ Assets])-LEN(@SEP_HOST))
                    where @i=upgaurd_SK*/
                END
            END
    SET @j=0
    SET @i+=1
END
      
 


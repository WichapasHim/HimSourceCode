IF OBJECT_ID('tempdb..#tablename') IS NOT NULL
        BEGIN
            DROP TABLE #tablename
        END

 
select entityName ,isCDCenabled,ROW_NUMBER() OVER (ORDER BY entityName) AS ROWNUM into #tablename FROM
jobconfig.sourceDetail
where entityName in ('SupplierAddress','StockReceiptLineAdditionalCost')

 
 declare @rowcounts int =0
 

truncate table dbo.mergeSP

 --select * from dbo.mergeSP

select @rowcounts = count(*) from #tablename

 

 DECLARE @i int = 1

 

 WHILE (@i <= @rowcounts)  
  BEGIN
            DECLARE @tableName VARCHAR(500) = (SELECT entityName FROM #tablename WHERE ROWNUM = @i)
            Declare @isCDCenabled Bit = (select isCDCenabled FROM #tablename WHERE ROWNUM = @i)
            print @tableName
            if(@isCDCenabled = 1)
            Begin
                exec [dbo].[SP_CreateMergeCDC] @tableName,'TBP'
            End
            Else
            Begin
                exec [dbo].[SP_CreateMergeDirectQuery] @tableName,'TBP'
            End

SET @i += 1
        END
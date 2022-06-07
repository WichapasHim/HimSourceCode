 select [upgaurd_risks_SK],
    [id], [EQ Assets]  from  [dbo].[SrcUpGaurd_test_2] where [EQ Assets] not like '[0-9]%'



     select 
    distinct([EQ Assets])  from  [dbo].[SrcUpGaurd_test_2] where [EQ Assets] not like '[0-9]%'




        select  a.[EQ Assets],
   row_number() over (order by a.[EQ Assets]) as ROWNUM  from
 ( select DISTINCT([EQ Assets]) 
    from  [dbo].[SrcUpGaurd_test_2] 
    where [EQ Assets] not like '[0-9]%') a
    where ROWNUM=




select count(distinct(EQ Assets)) from [dbo].[SrcUpGaurd_test_2] 
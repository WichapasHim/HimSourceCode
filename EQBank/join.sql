UPDATE [dbo].[SrcUpGaurd_id_domain]
SET [a_records]=replace(replace(replace([a_records],'[',''),']',''),'"','')






INSERT INTO [dbo].[SrcUpGaurd]
([Title] ,
	[Finding] ,
	[Risk] ,
	[Category] ,
	[Severity] ,
	[Overview] ,
	[Remediation Overview] ,
	[EQ Assets] ,
	[Domain] ,
	[IP] ,
	[Status] ,
	[First Found Date] ,
	[Last Found Date] ,
	[Source] )
SELECT
c.[EQ Assets]+' - '+c.[Category]+' - '+c.[Finding],
c.[Finding],
c.[Risk],
c.[Category],
c.[Severity],
c.[Overview],
c.[Overview],
c.[EQ Assets],
c.[EQ Assets],
c.[a_records],
NULL,
NULL,
NULL,
'Upguard' from 
(select distinct(a.[id]),
a.[Category],
a.[Finding],
a.[Risk],
a.[Severity],
a.[Overview],
a.[EQ Assets],
b.[a_records] 
from [SrcUpGaurd_test_2] as a
left join SrcUpGaurd_id_domain as b
on a.[EQ Assets]=b.[hostnames]

order by [id]) as c



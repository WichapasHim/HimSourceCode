IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[SrcUpGaurd_staging_1]') AND type in (N'U'))
DROP TABLE [dbo].[SrcUpGaurd_staging_1];


SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SrcUpGaurd_staging_1](
	[upgaurd_SK] [int] IDENTITY(1,1) NOT NULL,
	[id] [nvarchar](400) NULL,
	[Title] [nvarchar](4000) NULL,
	[Finding] [nvarchar](4000) NULL,
	[Risk] [nvarchar](4000) NULL,
	[Category] [nvarchar](4000) NULL,
	[Severity] [nvarchar](4000) NULL,
	[Overview] [nvarchar](4000) NULL,
	[Remediation Overview] [nvarchar](4000) NULL,
	[EQ Assets] [nvarchar](4000) NULL,
	[Domain] [nvarchar](4000) NULL,
	[UpGaurdDomainName] [nvarchar](4000) NULL,
	[UpGaurdDomainIP] [nvarchar](4000) NULL,
	[Source] [nvarchar](4000) NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[SrcUpGaurd_staging_1] ADD PRIMARY KEY CLUSTERED 
(
	[upgaurd_SK] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]


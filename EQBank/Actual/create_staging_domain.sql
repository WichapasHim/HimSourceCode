IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[SrcUpGaurd_staging_domain]') AND type in (N'U'))
DROP TABLE [dbo].[SrcUpGaurd_staging_domain];



SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SrcUpGaurd_staging_domain](
	[upgaurd_domain_SK] [int] IDENTITY(1,1) NOT NULL,
	[hostnames] [varchar](4000) NULL,
	[a_records] [varchar](4000) NULL
) ON [PRIMARY];


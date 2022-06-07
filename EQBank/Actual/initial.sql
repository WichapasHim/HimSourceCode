truncate table [dbo].[SrcUpGaurd];


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
);



CREATE TABLE [dbo].[SrcUpGaurd_staging_2](
	[upgaurd_risks_SK] [int] IDENTITY(1,1) NOT NULL,
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
);


CREATE TABLE [dbo].[SrcUpGaurd_staging_domain](
	[upgaurd_domain_SK] [int] IDENTITY(1,1) NOT NULL,
	[hostnames] [varchar](4000) NULL,
	[a_records] [varchar](4000) NULL
);
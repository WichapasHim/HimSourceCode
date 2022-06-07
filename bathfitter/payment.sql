IF EXISTS(SELECT 1 FROM sys.procedures WHERE Name='SP_Load_INT_FactPayment')
DROP PROCEDURE [INT].[SP_Load_INT_FactPayment];
GO

CREATE PROC [INT].[SP_Load_INT_FactPayment] AS

DECLARE @LastJobExtractEndTime DATETIME2,
@ExtractStartTime DATETIME2,
@ExtractEndTime DATETIME2,
@SPStartTime DATETIME2 = GETUTCDATE(),
@SPName VARCHAR(50) = 'SP_Load_INT_FactPayment',
@Zone VARCHAR(50) = 'INT',
@SPEndTime DATETIME2,
@TargetTable VARCHAR(255) = 'FactPayment'

IF OBJECT_ID('tempdb..#tempLoadFactPayment') IS NOT NULL
DROP TABLE #tempLoadFactPayment

-- Retrieve latest timestamp processed in the previous run; it is used to determine new/changed records in source tables for incremental load
SELECT @LastJobExtractEndTime = COALESCE(MIN(ExtractEndTime),'2011-01-01')
FROM JobConfig.JobLastRun
WHERE [storedProcedureName] = @SPName
AND [Zone] = @zone

-- Delta Table
SELECT * INTO #tempLoadFactPayment FROM LKP.Filteredbfr_payment WHERE Modified > @LastJobExtractEndTime and Modified <= GETUTCDATE()

-- clean int tables
TRUNCATE TABLE [INT].[FactPayment]
TRUNCATE TABLE [INT].[FactPaymentReject]

-- temp table - all recs - will later be separated to int and reject pipes
IF OBJECT_ID('tempdb..#FactPaymentAll') IS NOT NULL DROP TABLE #FactPaymentAll
CREATE TABLE [int].[#FactPaymentAll]
(
	[PaymentBK] varchar(100) NULL,
	[PaymentSourceID] varchar(100) NULL,
	[EOISK] int NULL,
	[PaymentAmount] MONEY NULL,
	[TransactionDateSK] int NULL,

	[dwCreateDate] [date] NULL
);
MERGE #FactPaymentAllt AS TARGET
USING (SELECT
    p.bfr_paymentid AS [PaymentBK],
    p.bfr_paymentid AS [PaymentSourceID],
    ISNULL(fe.EOISK, -1) AS [EOISK],
    p.bfr_amount AS [PaymentAmount],
    ISNULL(dm.DateSK, -1) AS [TransactionDateSK]

	,GETUTCDATE() AS dwCreateDate
FROM tempLoadFactPayment p
JOIN Curated.DimDate dm ON dm.CalendarDate = p.bfr_transactiondateutc
JOIN Curated.FactEOI fe ON fe.EOISourceID = p.bfr_eoi) AS SOURCE
ON TARGET.PaymentBK=SOURCE.PaymentBK

WHEN MATCHED
THEN UPDATE SET 
TARGET.PaymentBK=SOURCE.PaymentBK ,
TARGET.PaymentSourceID=SOURCE.PaymentSourceID ,
TARGET.EOISK=SOURCE.EOISK,
TARGET.PaymentAmount=SOURCE.PaymentAmount,
TARGET.TransactionDateSK=SOURCE.TransactionDateSK
TARGET.dwCreateDate=GETUTCDATE()

IF OBJECT_ID('tempdb..#FactPaymentBadRecs') IS NOT NULL DROP TABLE #FactPaymentBadRecs
SELECT PaymentBK
INTO #FactPaymentBadRecs
FROM #FactPaymentAll
GROUP BY PaymentBK
HAVING COUNT(1) > 1;

-- redirect rejects
INSERT INTO [int].[FactPaymentReject]
SELECT src.* FROM #FactPaymentAll src
JOIN #FactPaymentBadRecs badrecs ON src.PaymentBK = badrecs.PaymentBK;

-- good recs - to integration
INSERT INTO [int].[FactPayment]
SELECT src.*,
	CAST(NULL AS VARBINARY(8000)) AS [dwType1Hash],
	CAST(NULL AS VARBINARY(8000)) AS [dwType2Hash]
FROM #FactPaymentAll src
LEFT JOIN #FactPaymentBadRecs badrecs ON src.PaymentBK = badrecs.PaymentBK
WHERE badrecs.PaymentBK IS NULL;

EXEC sp_INT_GenerateHashes @TableName='FactPayment';

SET @ExtractEndTime = GETUTCDATE();
SET @SPEndTime = GETUTCDATE();

-- log job run details into the [JobConfig].[JobRunHistory] table
EXEC [Jobconfig].[SP_LoadJobRunDetails] @Zone,
NULL,
@TargetTable,
@LastJobExtractEndTime,
@ExtractEndTime,
@SPStartTime,
@SPEndTime,
'Success',
NULL,
@SPName;

GO
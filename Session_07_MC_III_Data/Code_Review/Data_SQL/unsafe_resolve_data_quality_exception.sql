/*
WinTrust training sample: SQL Server stored procedure for code review only.
DO NOT EXECUTE. It contains deliberate security, correctness, and governance risks.
*/
CREATE OR ALTER PROCEDURE dbo.usp_ResolveDataQualityException
    @ExceptionId NVARCHAR(100),
    @CustomerId NVARCHAR(100),
    @Currency NVARCHAR(10),
    @ProductCode NVARCHAR(20),
    @Amount DECIMAL(18,2)
AS
BEGIN
    -- Risk: no SET NOCOUNT ON, input validation, transaction, or audit record.
    DECLARE @sql NVARCHAR(MAX);

    -- Risk: dynamic SQL concatenates user-supplied values.
    SET @sql = N'UPDATE dbo.TransactionExceptions
        SET CustomerId = ''' + @CustomerId + N''',
            Currency = ''' + @Currency + N''',
            ProductCode = ''' + @ProductCode + N''',
            Amount = ' + CAST(@Amount AS NVARCHAR(50)) + N'
        WHERE ExceptionId = ''' + @ExceptionId + N''';';

    EXEC(@sql);

    -- Risk: blindly marks exception resolved without checking affected rows,
    -- approved reference data, reconciliation, or authorization.
    UPDATE dbo.TransactionExceptions
    SET Status = 'RESOLVED'
    WHERE ExceptionId = @ExceptionId;

    -- Risk: reports success even if the update matched no row or violated business rules.
    PRINT 'Exception resolved successfully';
END;

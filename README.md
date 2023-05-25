# CSV_Search
The script receives as input the path to a CSV file to be imported, a column number in which to search, and a search key.

## This repo contains the folder containging the C# code using .Net v6 and another executable file written in python for the csv data generation for testing purposes.

### In order to execute the Program.cs:

`dotnet run <CsvFilePath> <ColumnNumber> <SearchKey>`

`<CsvFilePath>`: The path to the CSV file you want to search.
`<ColumnNumber>`: The column number (0-based index) where the search will be performed.
`<SearchKey>`: The value you want to search for.

## Run Sample
Scenario #1: Successful Operation

CLI : `dotnet run ../../test.csv 2 Fabio`
Result: `Search Results:
        8,Gialli,Fabio,16/09/1989
        10,Gialli,Fabio,19/07/1995`

Scenario #2: Erronous Operation

CLI : `dotnet run ../../test.csv 10 Fabio`
Result: `Search Results:
         Record not found`

Scenario #3: File not found
CLI: ` dotnet run ./test.csv 2 Fabio`
Result: `Error processing:Could not find file`

#### The below is the program used to achieve this operation

```public static void Main(string[] args)
{
    // Check if the required arguments are provided
    if (args.Length < 3)
    {
        Console.WriteLine("Usage: dotnet run <CsvFilePath> <ColumnNumber> <SearchKey>");
        return;
    }

    // Retrieve the command-line arguments
    string CsvFilePath = args[0];
    int ColumnNumber = int.Parse(args[1]);
    string SearchKey = args[2];

    try
    {
        // Read all lines from the CSV file
        var lines = File.ReadLines(CsvFilePath);

        // Perform the search by splitting each line into columns and filtering based on the search criteria
        var results = lines.Select(line => line.Split(','))
                           .Where(columns => columns.Length > ColumnNumber &&
                                            columns[ColumnNumber].Equals(SearchKey, StringComparison.OrdinalIgnoreCase))
                           .ToList();

        Console.WriteLine("Search Results:");

        // Check if any matching records were found
        if (results.Count == 0)
        {
            Console.WriteLine("Record not found");
        }

        // Print each matching record
        foreach (var result in results)
        {
            Console.WriteLine(string.Join(',', result));
        }
    }
    catch (Exception ex)
    {
        Console.WriteLine("Error processing: " + ex.Message);
    }
}
```
This code demonstrates a CSV search application that accepts command-line arguments for the CSV file path, the target column number, and the search key. The application reads the CSV file, performs a search based on the provided criteria, and displays the matching records.

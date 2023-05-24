using System;
using System.IO;
using System.Linq;

class Program
{
    public static void Main(string[] args)

    { 
        // Check if the required arguments are provided
        if (args.Length< 3) 
        { 
            Console.WriteLine("Usage:dotnet run <CsvFilePath> <ColumnNumber> <SearchKey>");
            return;
        }

        // Retrieve the command-line arguments
        string CsvfilePath = args[0];
        int ColumnNumber = int.Parse(args[1]);
        string SearchKey = args[2];

        //try catch block for execution 
        try
        {
            // Read all lines from the CSV file
            var lines =File.ReadLines(CsvfilePath);

            // Perform the search by splitting each line into columns and filtering based on the search criteria

            var results = lines.Select(line => line.Split(',')) 
                                //condition: if the columns.Length is larger than the column number(arg[1])
                                //to prevent the access to a wrong xolumn index
                               .Where(columns=>columns.Length >ColumnNumber && columns[ColumnNumber]  //Compares the value of the column at the specified column number with the search key.
                                                                                                      //The comparison is case-insensitive, 
                               .Equals(SearchKey,StringComparison.OrdinalIgnoreCase)).ToList();

            Console.WriteLine("Search Results:");
            // Check if any matching records were found

            if (results.Count ==0) {
                Console.WriteLine("Record not found");
            }
            // Print each matching record
            foreach (var result in results) {
                
                Console.WriteLine(string.Join(',', result));
                    }

        }catch(Exception ex)
        {
            Console.WriteLine("Error processing:" + ex.Message);

        }
    }
}
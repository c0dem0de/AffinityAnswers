#!/bin/bash

# Download the file 
curl -s "https://www.amfiindia.com/spages/NAVAll.txt" | \

# Extract scheme name and asset value fields to tsv file
#   -F = specify field separator
#   NR = skip table header
#   NF = check for 5 columns in the table
#   {} = print 4th and 5th columns from the table with tsv format ie tab
awk -F ';' 'NR>1 && NF>=5 { print $4 "\t" $5 }' > scheme_nav.tsv

# Print success alert
echo "Extracted scheme name and NAV to scheme_nav.tsv"

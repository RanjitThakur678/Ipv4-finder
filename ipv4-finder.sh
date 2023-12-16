#!/bin/bash

# Check if the url.txt file exists
if [ ! -f "url.txt" ]; then
  echo "File url.txt not found!"
  exit 1
fi

# Loop through each URL in the file
while IFS= read -r url; do

  # Perform nslookup for the current URL
  ip_addresses=$(nslookup "$url" | awk 'NR >= 4' )

  # Display IP addresses if found
  if [ -n "$ip_addresses" ]; then
    echo "$ip_addresses"
  else
    echo "No IP addresses found for $url"
  fi

  echo "----------------------"
done < "url.txt"

	

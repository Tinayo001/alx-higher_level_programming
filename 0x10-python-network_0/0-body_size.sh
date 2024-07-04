#!/bin/bash

# Check if URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

# Send GET request using curl and capture the response
response=$(curl -s -w "%{size_download}" -o /dev/null $URL)

# Display the size of the response body in bytes
echo "Size of the response body: ${response} bytes"

#!/usr/bin/bash
#sends a request to that URL, and displays the size of the body of the response
IFS_old=$IFS
echo $#
if [ $# -ne 1 ];
then
	echo "Usage: $0 Remote_URL"
else
	URL=$1
	res=$(curl -I -s "$URL" | grep "Content-Length")
	IFS=": "
	read -ra vals <<< "$res"
	echo "${vals[1]}"
fi
IFS=$IFS_old

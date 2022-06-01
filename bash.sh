#!/bin/bash

for file in templates/*.md ;
do
  echo "$file" && pandoc $file --standalone --template templates/template.html -f markdown -t html  -o `echo "$file" | sed 's/\.md/\.html/g'`;

done

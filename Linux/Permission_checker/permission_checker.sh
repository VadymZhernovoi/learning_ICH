#!/bin/bash

clear

# working in dirrectory /opt/210225-ptm
W_DIR=/opt/210225-ptm/vadym
cd $W_DIR

# get a list of permitions only for files in the directory
for FILE in * 
  do
    if [ -f $FILE ]; then
      echo "File:" $FILE $(ls -l $FILE | awk '{print "Permitions:" $1}') 
      if [[ "$FILE" == *'.sh' ]] && [ ! -x $FILE ]; then
        # set permition +x for file
        chmod +x $FILE
        echo "Added execution permition for file:" $FILE
      fi
    fi
  done 

# OR 

echo "*************"

# get a list of '.sh' files
FIND=$(find $W_DIR -iname "*.sh")

for FILE in $FIND
  do
    # check permission -x for file
    if [ -x $FILE ]; then
      echo "File:" $FILE "is already executable"
    else
      # set permition +x for file
      chmod +x $FIL
      echo "Added execution permition for file:" $FILE
    fi
  done

echo "done"

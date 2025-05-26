#!/bin/bash

  dir_source=/opt/210225-ptm/vadym/dir_source
  dir_target=/opt/210225-ptm/vadym/dir_target
  
  # create two directories
  mkdir -p $dir_source $dir_target
  
  # delete the files *.hw19 just in case, if the script was already running (so as not to clog the disk)
  rm -rf $dir_source/*.hw19 $dir_target/*.hw19
  
  # create 100 random files
  for n in {1..100}
    do
      touch $dir_source/$RANDOM.hw19
    done

  # move files to directory $dir_target if the number in the name is even
  for file in $(find $dir_source -type f -name "*.hw19") # read the files *.hw19 from the directory $dir_source
    do
      name=$(echo $file | awk -F '/' '{print $6}' | awk -F '.' '{print $1}')
      if [ $(($name % 2)) == 0 ]; then
        mv $dir_source/$name.hw19 $dir_target/
      fi 
    done

echo "done"

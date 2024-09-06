#!/bin/bash

current_directory="$(pwd)"

# Iterate over folder names
for i in {1..1}; do
    cp input geom$i
    folder_name="geom${i}"  # Generate folder name
    folder_path="${current_directory}/${folder_name}"  # Specify the path to the parent folder

    # Specify the path to the input file
    input_file_path="${folder_path}/input"

    # Modify the lines with the desired folder name
    sed -i "s/geom/geom${i}/g" "${input_file_path}"

    # Transform chk files 
    cd geom$i
    formchk mon1_geom$i.chk
    formchk mon2_geom$i.chk
    formchk complex_geom$i.chk
    charge.x complex_geom$i.com mon1_geom$i.com mon2_geom$i.com complex_geom$i.fchk mon1_geom$i.fchk mon2_geom$i.fchk
    EDA-NCI.x < input
    cd ../
    echo "Processed folder: ${folder_path}"
done

echo "All folders processed successfully."
~                                              

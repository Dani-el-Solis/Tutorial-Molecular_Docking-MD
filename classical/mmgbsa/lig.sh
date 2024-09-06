#!/bin/bash

tail -n 12 FINAL_DECOMP.dat | head -n 10 | awk 'BEGIN { FS = ","; OFS = "  "} ; {print $2,$6,$9,$12,$15,$18 }' | sort -k 7n > lig.dat


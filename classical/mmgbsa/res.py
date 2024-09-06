# Sorting

data = []
with open("residue.out", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            values = line.split()
            data.append(values)

# Sum the values in the "TotalFrac" column based on common "Res2" values
totals = {}
for values in data:
    res2 = values[1]
    total_frac = float(values[2])
    if res2 in totals:
        totals[res2] += total_frac
    else:
        totals[res2] = total_frac

# Sort the totals from highest to lowest
sorted_totals = sorted(totals.items(), key=lambda x: x[1], reverse=True)

# Get the res2 values of the first 25 lines separated by commas
res2_values = ",".join([res2 for res2, _ in sorted_totals[:10]])

# Get the number from ligand_mask
ligand_mask_number = "280"  # Replace with the actual number from ligand_mask

# Update the input file
with open("mmgbsa.in", "r") as file:
    lines = file.readlines()

with open("mmgbsa.in", "w") as file:
    for line in lines:
        if line.strip().startswith("print_res="):
            file.write("print_res={},{}\n".format(res2_values, ligand_mask_number))
        else:
            file.write(line)

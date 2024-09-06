out = open('energies.dat',"w")
out.write(' Electrostatic       Pauli        Polarization       Total        Disp+Res-pol     Induction')
out.write("\n")
for i in range(1,2):
    f = open('geom{}/complex_geom{}_ch.out'.format(i,i),"r")
    for line in f:
        if 'Interaction energy terms (in kcal/mol)' in line:
           dummy = f.readline()
           electrostatic = f.readline().split()
           electrostatic = electrostatic[2]
           out.write(str(electrostatic))
           out.write('             ')
           pauli = f.readline().split()
           pauli = pauli[2]
           out.write(str(pauli))
           out.write('      ')
           polarization = f.readline().split()
           polarization = polarization[2]
           out.write(str(polarization))
           out.write('            ')
           total = f.readline().split()
           total = total[2]
           out.write(str(total))
           out.write('       ')
           dummy = f.readline()
           dummy = f.readline()
           disp = f.readline().split()
           disp = disp[2]
           out.write(str(disp))
           out.write('          ')
           induction = f.readline().split()
           induction = induction[2]
           out.write(str(induction))
           out.write("\n")
    f.close()
out.close()

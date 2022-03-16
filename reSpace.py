fin = open("data.txt", "rt")
fout = open("cities2.txt", "wt")
for line in fin:
    fout.write(' '.join(line.split()))
    fout.write('\n')

fin.close()
fout.close()
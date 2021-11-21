file_h = open("temp/sequence.fasta")
file = file_h.readlines()
file_h.close()
file = [i.rstrip() for i in file]

names = []
seq = []
seq_temp = ""
for i in file:
    if ">" in i:
        names.append(i)
        if seq_temp:
            seq.append(seq_temp)
            seq_temp = ""
    else:
        seq_temp += i
seq.append(seq_temp)

data = []
for i in range(len(names)):
    if "[" in names[i] and "]" in names[i] and "hemoglobin" in names[i].lower() and "alpha" in names[i].lower() and "subunit" in names[i].lower() and  " a " in names[i].lower() and "partial" not in names[i].lower():
        data.append([names[i], seq[i]])

organism = {}
for i in data:
    if i[0].split("[")[1].split("]")[0] not in organism:
        organism[i[0].split("[")[1].split("]")[0].lower()] = [i]
    else:
        organism[i[0].split("[")[1].split("]")[0].lower()].append(i)


newfile = open("temp/msa.fasta", "w")
counter = 0
for i in organism:
    if counter < 101:
        newfile.write(f">{i.replace(' ', '_')}\n")
        newfile.write(organism[i][0][1] + "\n")
        counter += 1
print(counter)
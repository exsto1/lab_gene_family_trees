file_h = open("trees/taxonomy.nwk")
file = file_h.read()
file_h.close()

file = file.lower().replace(" ", "_").replace("'", "")

newfile = open("trees/taxonomy_lower.nwk", "w")
newfile.write(file)
newfile.close()
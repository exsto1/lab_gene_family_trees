from Bio.Align.Applications import MafftCommandline
mafft_exe = "./MAFFT/mafft-win"
in_file = "./temp/msa.fasta"
mafft_cline = MafftCommandline(mafft_exe, input=in_file)
print(mafft_cline)
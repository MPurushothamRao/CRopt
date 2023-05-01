from gtAI import Run_gtAI
from gtAI import gtAI 
import pandas as pd
url_GtRNAdb = "http://gtrnadb.ucsc.edu/genomes/bacteria/Esch_coli_K_12_MG1655/"
#### From GtRNAdb
GtRNA = gtAI.GtRNAdb(url_GtRNAdb)
df = pd.read_csv("../results/csv/CRopt.csv")
main_fasta = "../results/fasta/CRopt.fasta"
genetic_code_number = 1
ref_fasta = "../resources/fasta/U00096_3.fasta"
bacteria = True
size_pop = 60
generation_number = 100
df_tai , final_dict_wi, rel_values = Run_gtAI.gtai_analysis(main_fasta = main_fasta,
                                                      GtRNA = GtRNA ,genetic_code_number = genetic_code_number, ref_fasta = ref_fasta,
                                                      bacteria=bacteria, size_pop=size_pop,generation_number=generation_number)
df["tAI"] = df_tai["tai"]
print(df_tai)
df.to_csv("../results/csv/CRopt.csv", index =False, header = True)

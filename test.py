from Bio import SeqIO #
def nbr_seq (nom_du_fichier):
    """
            Prend en entrée un fichier fasta et retourne le nombre de séquences enregistrées.
    """
    i=1
    for record in SeqIO.parse(nom_du_fichier+".fasta", "fasta"):
        i+=1
    print("Le nombre de séquences est : {0} \n\n" .format(i))


def tab_res (nom_du_fichier):
    """
    Prend en entrée un fichier fasta et retourne les noms des séquences ainsi que leurs longueurs.
    """
    print("Nom de la séquence"+3*"\t"+"|\t"+"Longueur de la séquence"+"\n")
    print(72*"-"+"\n")
    for record in SeqIO.parse(nom_du_fichier+".fasta", "fasta"):
        print(str(record.name)+"\t|" + 2*"\t"+str(len(record))+"\n")

nom_fichier = input("Entrez le nom du fichier sans extension: ")
print("")
nbr_seq (nom_fichier)
tab_res (nom_fichier)


"""

L'exercice de ce soir consiste à écrire un programme qui, en interrogant l'API Entrez du NCBI,
permet à l'utilisateur de chercher un gêne par mot-clé et d'obtenir sa séquence ADN.

Notre programme s'exécute en 3 étapes :

1. Recherche de gènes par mot-clé.
   On demande à l'utilisateur d'écrire un mot-clé à rechercher dans la base de données des gènes.
   On utilise l'utilitaire ESearch qui nous retourne une liste d'identifiants de gènes correspondants aux critères de recherche.

2. Choix d'un gène parmi la liste des gènes retournés.
   On demande à l'utilisateur de choisir un gène parmi la liste retournée par la requête.
   Pour permettre à l'utilisateur de faire un choi éclairé, puisque la requête ne nous retourne que l'identifiant des gènes,
   nous devons d'abord obtenir le nom de chaque gène à l'aide de l'utilitaire ESummary.

3. Téléchargement de la séquence nucléotidique de référence (RefSeq) du gène choisi.
   On utilise l'utilitaire EFetch pour obtenir le fichier Fasta de la séquence. On l'enregiste à l'aide de la méthode SeqIO.write().
   Puisque nous n'avos pas le numéro d'accession de la séquence dans la base de données des nucléotides (nous avons seulement l'identifiant du gène dans la base de données des gènes),
   nous devons d'abord utiliser l'utilitaire ELink pour obtenir l'identifiant de la séquence nucléotidique de référence (référence croisée pour RefSeq).

"""


# Importation de Biopython
from Bio import Entrez, SeqIO


###########################################################################
# Programme principal
###########################################################################
def main():

    # Coordonnées pour NCBI Entrez
    Entrez.email = 'VotreAddresseCourrielIci'

    # Message d'accueil
    print("""Bienvenu au programme de recherche de gène par mot-clé!""")

    # Rechercher un gène par mot-clé; retourne une liste de geneId ex. [1212, 4335, 9884]
    IdList = rechercherGene()

    if len(IdList) != 0:
        # Choix d'un gène parmi la liste des gènes retournés; retourne l'index du geneId dans la liste
        index = choisirGene(IdList)
        # Téléchargement de la séquence nucléotidique de référence (RefSeq) du gène choisi
        telechargerSequence(IdList[index])
    else:
        # Message utilisateur si pas de gènes retournés
        print("""Aucun gène correspondant aux critères""")



###########################################################################
# Fonctions appelées par le programme principal
###########################################################################

def rechercherGene(): pass
    
    # Interroger l'utilisateur
    organism, keyword = None, None
    while not organism: organism = input("""Spécifiez un organisme: """).strip()  # <- J'ai ajouté le choix de l'organisme; c'est optionnel!
    while not keyword : keyword  = input("""Spécifiez un mot-clé: """).strip()

    # ESearch - Recherche par mot-clé
    """
    VOTRE CODE ICI
    """

    # Retourne la liste des identifiants des gènes
    """
    VOTRE CODE ICI
    """


def choisirGene(IdList): pass

    # ESummary - Obtention des informations sur les gènes de la liste
    """
    VOTRE CODE ICI
    """

    # Afficher la liste des gènes (avec index et description)
    for i in range(len(IdList)): print(i, summaries[i]['Description'], sep='. ')
    
    # Interroger l'utilisateur
    choix = -1
    while choix not in range(len(IdList)):
        choix = input("""Choisissez un gène parmi la liste retournée: """)
        if choix.isnumeric(): choix = int(choix)

    # Retourne l'index du gène choisi dans la liste des gènes
    return choix



def telechargerSequence(IdGene): pass

    # ELink - Obtention de la référence croisée
    """
    VOTRE CODE ICI
    """

    # EFetch - Obtention de la séquence au format Fasta
    """
    VOTRE CODE ICI
    """

    # Enregistrement du fichier Fasta
    """
    VOTRE CODE ICI
    """


###########################################################################
# Appel du programme principal
###########################################################################
if __name__ == '__main__': main()

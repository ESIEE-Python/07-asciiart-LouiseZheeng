"""Retourner la liste de tuples selon un algorithme récursif et itératif"""


#### Imports et définition des variables globales
import sys
sys.setrecursionlimit(4000)

#### Fonctions secondaires
def artcode_i(s):
    """retourne la liste de tuples selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    ca=[]
    oa=[]

    flag=False
    for k in s:
        if not flag and s[0]=="\n":
            if s[0] not in ca :
                ca.append('\n')
            if len(oa)==0:
                oa.append(1)
            flag=True

        elif s[0]==s[k]:
            if s[0] not in ca :
                ca.append(s[0])
            if len(oa)==0:
                oa.append(1)
            elif s[k]==s[k-1]:
                oa[-1]+=1
            else:
                ca.append(s[k])
                oa.append(1)

        else:
            if s[k] not in ca:
                ca.append(s[k])
                oa.append(1)
            elif s[k]==s[k-1]:
                oa[-1]+=1
            else:
                ca.append(s[k])
                oa.append(1)

    return list(zip(ca,oa))


def artcode_r(s):
    """retourne la liste de tuples selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if len(s)==0:
        return []

    k = 0
    for c in s:
        if c != s[0]:
            break
        k = k+1

    return [(s[0], k)] + artcode_r(s[k:])

#### Fonction principale
def main():
    """ Retourne la liste de tuples pour l'algorithme itératif et récursif
    
    Args:
    s: chaîne de caractères

    Returns:
    2 listes de tuples
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()

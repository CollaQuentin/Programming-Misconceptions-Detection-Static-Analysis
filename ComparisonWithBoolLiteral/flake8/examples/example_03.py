# [Note from Quentin Colla]: This is really a submission from a student to an INGInious exercise. The misconception appears at line 72.

class CoffreFort :

    def __init__(self, code, tresor) :
        """
        @pre:  code et tresor sont des chaînes de caractères représentant,
               respectivement, un code secret pour ouvrir le coffre-fort et
               le secret contenu dans le coffre-fort
        @post: un coffre-fort a été créé et initalisé avec le code donné,
               contenant le trésor donné et est initialement fermé. Ni le code
               ni le trésor sont accessibles de l'extérieur de cet objet.
        """
        self.code=code
        self.tresor=(tresor)
        self.etat=False

    def reinitialiser(self, anciencode, nouveaucode) :

        """
        @pre:  anciencode et nouveaucode sont des chaînes de caractères
               représentant un code secret; cette méthode peut être exécutée peu
               n'importe l'état (ouvert ou fermé) du coffre-fort
        @post: si le code secret actuel du coffre-fort est égal à
               l'anciencode passé en paramètre, le code secret sera remplacé
               par le nouveaucode passé en paramètre et la méthode retourne True;
               sinon rien ne se passe et la méthode retourne False
        """
        # A COMPLETER #
        if coffre.code==anciencode:
            self.code=noveaucode
            return True
        else:
            return False



    def ouvrir(self, code) :
        """
        @pre:  -
        @post: Si le code passé en paramètre est égal au code
               actuel du coffre-fort, l'état du coffre-fort change en ouvert;
               si le code passé en paramètre n'est pas le bon, son état ne change pas.
               La méthode retourne True si le coffre-fort est ouvert,
               sinon elle retourne False.
        """
        # A COMPLETER #
        if code==coffre.code:
            self.etat=True
            return True
        else:
            return False

    def fermer(self) :
        """
        @pre: -
        @post: L'état du coffre-fort change en fermé (s'il était ouvert,
               ou reste fermé s'il était déjà fermé). La méthode retourne False
               pour indiquer que le coffre-fort est fermé.
        """
        # A COMPLETER #
        self.etat=False
        return False

    def tresor(self) :
        """
        @pre:  -
        @post: si le coffre-fort est ouvert, retourne le tresor contenu
               dedans; sinon retourne None.
        """
        # A COMPLETER #
        if coffre.etat==True:
            return(tresor)
        else:
            return None
coffre = CoffreFort("1234", "mon journal intime")
print(coffre.ouvrir("1234")) #Imprime True  -> le coffre-fort est ouvert
print(coffre.tresor())       #Imprime "mon journal intime"
print(coffre.fermer())       #Imprime False -> le coffre-fort est fermé
print(coffre.tresor())       #Imprime None  -> le tresor n'est pas accessible
print(coffre.reinitialiser("1234", "4321")) #Imprime True -> le code a été changé
print(coffre.tresor())       #Imprime None  -> le tresor n'est pas accessible
print(coffre.ouvrir("1234")) #Imprime False -> le coffre-fort est fermé
print(coffre.ouvrir("4321")) #Imprime True -> le coffre-fort est ouvert
print(coffre.tresor())       #Imprime "mon journal intime"

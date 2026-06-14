import unittest
from livre_s17 import Livre
from catalogue import *

CATALOGUE = [
    Livre("1984", "Orwell", "9780451524935", 328, 1949),
    Livre("Le Meilleur des mondes", "Huxley", "9780060850524", 311, 1932),
    Livre("Fahrenheit 451", "Bradbury", "9781451673319", 256, 1953),
    Livre("La Ferme des animaux", "Orwell", "9780060935467", 152, 1945),
]

DOUBLON = Livre("1984 (réédition)", "Orwell", "9780451524935", 328, 1949)
AVEC_DOUBLON = CATALOGUE + [DOUBLON]

class TestCatalogue(unittest.TestCase):

    def test_tris(self):
        self.assertEqual(
            [l.titre for l in trier_par_titre(CATALOGUE)],
            ["1984", "Fahrenheit 451", "La Ferme des animaux", "Le Meilleur des mondes"]
        )
        self.assertEqual(
            [l.annee for l in trier_par_annee(CATALOGUE)],
            [1932, 1945, 1949, 1953]
        )
        self.assertEqual(
            [l.annee for l in trier_par_annee(CATALOGUE, recents_dabord=True)],
            [1953, 1949, 1945, 1932]
        )
        self.assertEqual(
            [(l.auteur, l.annee) for l in trier_par_auteur_puis_annee_recente(CATALOGUE)],
            [("Bradbury", 1953), ("Huxley", 1932), ("Orwell", 1949), ("Orwell", 1945)]
        )

    def test_pas_modifie(self):
        avant = CATALOGUE.copy()
        trier_par_titre(CATALOGUE)
        self.assertEqual(CATALOGUE, avant)

    def test_stable(self):
        livres = [
            Livre("A", "X", "1111111111111", 100, 2000),
            Livre("B", "Y", "2222222222222", 120, 2000),
        ]
        self.assertEqual([l.titre for l in trier_par_annee(livres)], ["A", "B"])

    def test_dedoublonner(self):
        r = dedoublonner(AVEC_DOUBLON)
        self.assertEqual(len(r), 4)
        self.assertEqual([l.titre for l in r],
                         ["1984", "Le Meilleur des mondes", "Fahrenheit 451", "La Ferme des animaux"])

    def test_regrouper(self):
        g = regrouper_par_auteur(CATALOGUE)
        self.assertEqual(set(g.keys()), {"Orwell", "Huxley", "Bradbury"})
        self.assertEqual(len(g["Orwell"]), 2)

if __name__ == "__main__":
    unittest.main()
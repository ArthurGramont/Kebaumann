import io
import unittest
from unittest.mock import patch
from kebab import commander_kebab

class TestKebab(unittest.TestCase):

    def test_commander_kebab_confirmation(self):
        # Simuler les entrées pour :
        # - crudités : "12" => sélectionne "Tomates" et "Salade"
        # - viandes : "2"  => sélectionne "Boeuf"
        # - compléments : "1"  => sélectionne "Oeufs"
        # - sauces : "345" => sélectionne "Samouraï", "Ketchup" et "Harissa"
        # - confirmation : "o"
        inputs = ["12", "2", "1", "345", "o"]
        with patch('builtins.input', side_effect=inputs), patch('sys.stdout', new=io.StringIO()) as fake_out:
            commander_kebab()
            output = fake_out.getvalue()
            # Vérification du récapitulatif
            self.assertIn("Ingrédients sélectionnés:", output)
            self.assertIn("- Salade", output)
            self.assertIn("- Boeuf", output)
            # Vérification de la confirmation de commande
            self.assertIn("Votre commande a été confirmée", output)
            # Vérification du status végétarien
            self.assertIn("avec viande", output)

    def test_commander_kebab_annulation(self):
        # Simuler les entrées pour une commande vide sur tous les niveaux
        inputs = ["", "", "", ""]
        with patch('builtins.input', side_effect=inputs), patch('sys.stdout', new=io.StringIO()) as fake_out:
            commander_kebab()
            output = fake_out.getvalue()
            self.assertIn("Vous n'avez sélectionné aucun ingrédient!", output)

if __name__ == '__main__':
    unittest.main(verbosity=2)
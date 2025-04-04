import io
import unittest
from unittest.mock import patch
from kebab import commander_kebab

class TestKebab(unittest.TestCase):

    def test_commander_kebab_confirmation(self):
        # Scénario complet avec confirmation :
        # - crudités : "12" => "Tomates" et "Salade"
        # - viandes : "2" => "Boeuf"
        # - compléments : "1" => "Oeufs"
        # - sauces : "345" => "Samouraï", "Ketchup" et "Harissa"
        # - confirmation : "o"
        inputs = ["12", "2", "1", "345", "o"]
        with patch('builtins.input', side_effect=inputs), \
             patch('sys.stdout', new=io.StringIO()) as fake_out:
            commander_kebab()
            output = fake_out.getvalue()
            self.assertIn("Ingrédients sélectionnés:", output)
            self.assertIn("- Salade", output)
            self.assertIn("- Boeuf", output)
            self.assertIn("Votre commande a été confirmée", output)
            self.assertIn("avec viande", output)

    def test_commander_kebab_annulation(self):
        # Scénario avec aucune sélection et donc aucun ingrédient ajouté
        inputs = ["", "", "", ""]
        with patch('builtins.input', side_effect=inputs), \
             patch('sys.stdout', new=io.StringIO()) as fake_out:
            commander_kebab()
            output = fake_out.getvalue()
            self.assertIn("Vous n'avez sélectionné aucun ingrédient!", output)

    def test_commander_kebab_vegetarien(self):
        # Scénario pour une commande végétarienne :
        # - crudités : "1" => "Tomates"
        # - viandes : ""  => aucune viande sélectionnée
        # - compléments : "2" => "Fromage"
        # - sauces : "45" => "Samouraï" et "Harissa"
        # - confirmation : "o"
        inputs = ["1", "", "2", "45", "o"]
        with patch('builtins.input', side_effect=inputs), \
             patch('sys.stdout', new=io.StringIO()) as fake_out:
            commander_kebab()
            output = fake_out.getvalue()
            self.assertIn("Ingrédients sélectionnés:", output)
            self.assertIn("- Tomates", output)
            self.assertIn("- Fromage", output)
            # Vérifier que le kebab est considéré végétarien
            self.assertIn("végétarien", output)
            self.assertIn("Votre commande a été confirmée", output)

    def test_commander_kebab_cancel(self):
        # Scénario de commande annulée même si des ingrédients ont été sélectionnés :
        # - crudités : "13" => "Tomates" et "Oignon"
        # - viandes : ""   => aucune viande sélectionnée
        # - compléments : "2" => "Fromage"
        # - sauces : "24" => "Samouraï" et "Ketchup"
        # - confirmation : "n" (pour annuler)
        inputs = ["13", "", "2", "24", "n"]
        with patch('builtins.input', side_effect=inputs), \
             patch('sys.stdout', new=io.StringIO()) as fake_out:
            commander_kebab()
            output = fake_out.getvalue()
            self.assertIn("Votre commande a été annulée", output)

    def test_commander_kebab_invalidCharacters(self):
        # Scénario avec des caractères invalides dans les entrées :
        # - crudités : "2a" => '2' valide pour "Salade", 'a' ignoré
        # - viandes : "0"  => aucune viande (0 est invalide)
        # - compléments : "1" => "Oeufs"
        # - sauces : "1b" => '1' valide pour "Blanche", 'b' ignoré
        # - confirmation : "o"
        inputs = ["2a", "0", "1", "1b", "o"]
        with patch('builtins.input', side_effect=inputs), \
             patch('sys.stdout', new=io.StringIO()) as fake_out:
            commander_kebab()
            output = fake_out.getvalue()
            self.assertIn("- Salade", output)
            self.assertNotIn("- Boeuf", output)
            self.assertIn("- Oeufs", output)
            self.assertIn("- Blanche", output)
            self.assertIn("Votre commande a été confirmée", output)

if __name__ == '__main__':
    # Charger et exécuter les tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestKebab)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Récupérer les noms de tests échoués (failures + erreurs)
    failed_tests = [str(test[0]) for test in result.failures + result.errors]

    # Récupérer tous les noms de tests du suite
    all_tests = []
    for test in suite:
        all_tests.append(str(test))

    # Les tests réussis sont ceux qui ne figurent pas dans la liste des tests échoués
    passed_tests = [test for test in all_tests if test not in failed_tests]

    print("\n=== Résumé des tests ===")
    print("Tests réussis:")
    for test in passed_tests:
        print(" - " + test)
    print("Tests échoués:")
    for test in failed_tests:
        print(" - " + test)
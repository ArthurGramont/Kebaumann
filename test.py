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
            recap = output.split("Ingrédients sélectionnés:")[-1]
            self.assertIn("- Salade", recap)
            self.assertIn("- Boeuf", recap)
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
            recap = output.split("Ingrédients sélectionnés:")[-1]
            self.assertIn("- Tomates", recap)
            self.assertIn("- Fromage", recap)
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
            recap = output.split("Ingrédients sélectionnés:")[-1]
            self.assertIn("- Salade", recap)
            self.assertNotIn("- Boeuf", recap)
            self.assertIn("- Oeufs", recap)
            self.assertIn("- Blanche", recap)
            self.assertIn("Votre commande a été confirmée", output)

def flatten_tests(suite):
    """Fonction utilitaire pour aplatir une suite de tests."""
    tests = []
    for item in suite:
        if item is None:
            continue
        if isinstance(item, unittest.TestSuite):
            tests.extend(flatten_tests(item))
        else:
            tests.append(item)
    return tests

if __name__ == '__main__':
    # Charger et exécuter les tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestKebab)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Récupérer les noms de tests échoués (failures + erreurs)
    failed_tests = [t.id() for t, _ in (result.failures + result.errors)]

    # Récupérer tous les noms de tests de la suite en l'aplatissant
    all_tests = [test.id() for test in flatten_tests(suite)]

    # Les tests réussis sont ceux qui ne figurent pas dans la liste des tests échoués
    passed_tests = [test for test in all_tests if test not in failed_tests]

    print("\n=== Résumé des tests ===")
    if passed_tests:
        print("Tests réussis:")
        for test in passed_tests:
            print(" - " + test)
    else:
        print("Aucun test réussi.")

    if failed_tests:
        print("\nTests échoués:")
        for test in failed_tests:
            print(" - " + test)
    else:
        print("\nAucun test échoué.")
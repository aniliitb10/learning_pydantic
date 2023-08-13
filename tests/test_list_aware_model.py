from unittest import TestCase

from player import Player, Role


class TestListAwareModel(TestCase):

    def test_simple(self):
        player_data = {'name': "Yuvi", 'teams': 'India, Punjab', 'Roles': "Batsman", 'fav_dict': {1: 3}}
        player = Player(**player_data)
        self.assertEqual("Yuvi", player.name)
        self.assertEqual(['India', 'Punjab'], player.teams)
        self.assertEqual([Role.Batsman], player.roles)

    def test_empty_fields(self):
        player_data = {'name': "Yuvi", 'teams': '', 'Roles': '', 'fav_dict': None}
        player = Player(**player_data)
        self.assertEqual("Yuvi", player.name)
        self.assertEqual([], player.teams)
        self.assertEqual([], player.roles)
        self.assertEqual(None, player.fav_dict)

    def test_by_alias(self):
        player_data = {'name': 'Raina', 'Linked Teams': 'India, Uttar Pradesh', 'Roles': '', 'fav_dict': None}
        player = Player(**player_data)
        self.assertEqual('Raina', player.name)
        self.assertEqual(['India', 'Uttar Pradesh'], player.teams)
        self.assertEqual([], player.roles)
        self.assertEqual(None, player.fav_dict)

    def test_by_first_alias(self):
        player_data = {'name': 'Raina', 'teams': 'India', 'Linked Teams': 'India, Uttar Pradesh', 'Roles': '',
                       'fav_dict': None}
        player = Player(**player_data)
        self.assertEqual('Raina', player.name)
        self.assertEqual(['India'], player.teams)
        self.assertEqual([], player.roles)
        self.assertEqual(None, player.fav_dict)

    def test_by_already_parsed_types(self):
        player_data = {'name': 'Raina', 'teams': ['India', 'Uttar Pradesh'], 'Roles': [Role.Batsman],
                       'fav_dict': None}
        player = Player(**player_data)
        self.assertEqual('Raina', player.name)
        self.assertEqual(['India', 'Uttar Pradesh'], player.teams)
        self.assertEqual([Role.Batsman], player.roles)
        self.assertEqual(None, player.fav_dict)

from unittest import TestCase, main

from hero.project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.test_first_hero = Hero("First_Hero", 10, 100, 10)
        self.test_second_hero = Hero("Second_Hero", 11, 110, 11)

    def test_if_hero_initialised_successfully(self):
        self.assertEqual("First_Hero", self.test_first_hero.username)
        self.assertEqual(10, self.test_first_hero.level)
        self.assertEqual(100, self.test_first_hero.health)
        self.assertEqual(10, self.test_first_hero.damage)

    def test_if_hero_battle_himself_raises(self):
        with self.assertRaises(Exception) as ex:
            self.test_first_hero.battle(self.test_first_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_if_hero_battle_health_0_raises(self):
        self.test_first_hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.test_first_hero.battle(self.test_second_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_if_hero_battle_health_lower_than_0_raises(self):
        self.test_first_hero.health = -1
        with self.assertRaises(ValueError) as ex:
            self.test_first_hero.battle(self.test_second_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_if_enemy_hero_battle_health_0_raises(self):
        self.test_second_hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.test_first_hero.battle(self.test_second_hero)
            self.assertEqual("You cannot fight Second_Hero. He needs to rest", str(ex.exception))

    def test_if_enemy_hero_battle_health_lower_than_0_raises(self):
        self.test_second_hero.health = -1
        with self.assertRaises(ValueError) as ex:
            self.test_first_hero.battle(self.test_second_hero)
            self.assertEqual("You cannot fight Second_Hero. He needs to rest", str(ex.exception))

    def test_if_hero_battle_draw_successfully(self):
        self.test_first_hero.health = 1
        self.test_second_hero.health = 1
        self.assertEqual("Draw", self.test_first_hero.battle(self.test_second_hero))

    def test_if_hero_battle_damage_increase_successfully(self):
        self.test_first_hero.battle(self.test_second_hero)
        self.assertEqual(15, self.test_second_hero.health)

    def test_if_enemy_hero_battle_damage_increase_successfully(self):
        self.test_first_hero.health = 122
        self.test_first_hero.battle(self.test_second_hero)
        self.assertEqual(1, self.test_first_hero.health)

    def test_if_hero_battle_stats_increase_after_win(self):
        self.test_first_hero.damage = 1000
        self.test_first_hero.health = 126
        res = self.test_first_hero.battle(self.test_second_hero)
        self.assertEqual(11, self.test_first_hero.level)
        self.assertEqual(10, self.test_first_hero.health)
        self.assertEqual(1005, self.test_first_hero.damage)
        self.assertEqual("You win", res)

    def test_if_enemy_hero_battle_stats_increase_after_win(self):
        res = self.test_first_hero.battle(self.test_second_hero)
        self.assertEqual(12, self.test_second_hero.level)
        self.assertEqual(15, self.test_second_hero.health)
        self.assertEqual(16, self.test_second_hero.damage)
        self.assertEqual("You lose", res)

    def test_if_hero_str_return_information_successfully(self):
        res = f"Hero First_Hero: 10 lvl\n" \
               f"Health: 100\n" \
               f"Damage: 10\n"
        self.assertEqual(res, self.test_first_hero.__str__())


if __name__ == '__main__':
    main()
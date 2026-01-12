import { ref } from "vue";
import type { Card } from "./interfaces";

export const cards = ref<Card[]>([]);

export const allColumns = ['cards.id', 'name', 'type', 'pokedex_number', 'hp', 'series', 'set_number',
'illustrator', 'release_year', 'attack_name', 'attack_damage', 'attack_effect']

export const columns = [
  { title: 'Id', data: 'id'},
  { title: 'Name', data: 'name'},
  { title: 'Type', data: 'type'},
  { title: 'Pokedex Number', data: 'pokedex_number'},
  { title: 'Hp', data: 'hp'},
  { title: 'Series', data: 'series'},
  { title: 'Set Number', data: 'set_number'},
  { title: 'Illustrator', data: 'illustrator'},
  { title: 'Release Year', data: 'release_year'},
  { title: 'Attack Name', data: 'attack_name'},
  { title: 'Attack Damage', data: 'attack_damage'},
  { title: 'Attack Effect', data: 'attack_effect'}
]
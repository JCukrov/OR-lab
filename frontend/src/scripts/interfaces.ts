export interface Card{
  id: number,
  name: string,
  type: string,
  pokedex_number: number,
  hp: number,
  series: string,
  set_number: number,
  illustrator: string,
  release_year: number,
  attack_name: string,
  attack_damage: number | null,
  attack_effect: string | null
}
import type { Card } from "./interfaces";
import { allColumns } from "./constants";

export function return_JSON(cards: Card[]) {
  const groupedCards = () => {
    const map = new Map<number, any>();

    cards.forEach(card => {
      const attack = {
        name: card.attack_name,
        damage: card.attack_damage,
        effect: card.attack_effect
      };

      if (map.has(card.id)) {
        map.get(card.id).attacks.push(attack);
      } else {
        map.set(card.id, {
          id: card.id,
          name: card.name,
          type: card.type,
          pokedex_number: card.pokedex_number,
          hp: card.hp,
          series: card.series,
          set_number: card.set_number,
          illustrator: card.illustrator,
          release_year: card.release_year,
          attacks: [attack]
        });
      }
    });

    return Array.from(map.values());
  };

  const data =  groupedCards();
  const jsonStr = JSON.stringify(data, null, 2);

  const blob = new Blob([jsonStr], { type: 'application/json' });
  const url = URL.createObjectURL(blob);

  const link = document.createElement('a');
  link.href = url;
  link.download = 'cards.json';
  link.click();

  URL.revokeObjectURL(url);
};

export const downloadCSV = (cards: Card[]) => {
  if (!cards.length) return;

  const headers = allColumns;
  const csvContent = [
    headers.join(','),
    ...cards.map(card => Object.values(card).map(value => `"${value ?? ''}"`).join(','))
].join('\n');
  const blob = new Blob([csvContent], { type: 'text/csv' });
  const url = URL.createObjectURL(blob);

  const link = document.createElement('a');
  link.href = url;
  link.download = 'cards.csv';
  link.click();

  URL.revokeObjectURL(url);
};
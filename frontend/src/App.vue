<script setup lang="ts">
import DataTable from 'datatables.net-vue3';
import DataTableCore from 'datatables.net-bs5';
import 'datatables.net-select-dt';
import 'datatables.net-responsive-dt';
import { onMounted, ref } from 'vue';
import axios from 'axios';

DataTable.use(DataTableCore)

const allColumns = ['cards.id', 'name', 'type', 'pokedex_number', 'hp', 'series', 'set_number',
'illustrator', 'release_year', 'attack_name', 'attack_damage', 'attack_effect']

interface Card{
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

const columns = [
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

const cards = ref<Card[]>([]);
const searchColumn = ref<string>('all')
const searchValue = ref<string>('')

const handleSearch = async() => {
  if (searchValue.value === ''){
    fetchAll()
    return
  }
  const res = await axios.post(`${import.meta.env.VITE_API_URL}/search_cards`,{
    column: searchColumn.value || 'all',
    value: searchValue.value
  })
  console.log(res.data.cards)
  cards.value = res.data.cards as Card[]
}

const fetchAll = async() => {
    const res = await axios.get(`${import.meta.env.VITE_API_URL}/cards`)
    cards.value = res.data.cards
}

function return_JSON() {
  const groupedCards = () => {
    const map = new Map<number, any>();

    cards.value.forEach(card => {
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

const downloadCSV = () => {
  if (!cards.value.length) return;

  const headers = allColumns;
  const csvContent = [
    headers.join(','),
    ...cards.value.map(card => Object.values(card).map(value => `"${value ?? ''}"`).join(','))
].join('\n');
  const blob = new Blob([csvContent], { type: 'text/csv' });
  const url = URL.createObjectURL(blob);

  const link = document.createElement('a');
  link.href = url;
  link.download = 'cards.csv';
  link.click();

  URL.revokeObjectURL(url);
};

onMounted(async() => {
  await fetchAll()
})

</script>

<template>
  <form @submit.prevent="handleSearch">
    <input type="text" v-model="searchValue" placeholder="Value..."></input>
    <select v-model="searchColumn">
      <option value="all">(wildcard)</option>
      <option v-for="item in allColumns" :value="item">{{ item }}</option>
    </select>
    <button type="submit">Search</button>
  </form>

  
  <button @click="fetchAll">Reset table</button>
  <button @click="return_JSON">Get JSON</button>
  <button @click="downloadCSV">Get CSV</button>
  <DataTable
    :columns="columns"
    :data="cards"
    :options="{searching: false}"
  />

</template>

<style>
  @import 'datatables.net-bs5';
  @import 'bootstrap'
</style>
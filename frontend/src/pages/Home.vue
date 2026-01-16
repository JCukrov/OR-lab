<script setup lang="ts">
import { onMounted, ref } from 'vue';

import DataTable from 'datatables.net-vue3';
import DataTableCore from 'datatables.net-bs5';
import 'datatables.net-select-dt';
import 'datatables.net-responsive-dt';

import Header from '../components/Header.vue';

import { downloadCSV, return_JSON } from '../scripts/download';
import { allColumns, cards, columns } from '../scripts/constants';
import { fetchAll, handleSearch } from '../scripts/utility';

const searchColumn = ref<string>('all')
const searchValue = ref<string>('')

DataTable.use(DataTableCore)


const submitSearch = async() => {
    cards.value = await handleSearch(searchValue.value, searchColumn.value)
}

const resetTable = async() => {
  cards.value = await fetchAll()
}

onMounted(async() => {
  cards.value = await fetchAll()
})

</script>

<template>
  <Header/>

  <form @submit.prevent="submitSearch">
    <input type="text" v-model="searchValue" placeholder="Value..."></input>
    <select v-model="searchColumn">
      <option value="all">(wildcard)</option>
      <option v-for="item in allColumns" :value="item">{{ item }}</option>
    </select>
    <button type="submit">Search</button>
  </form>


  <button @click="resetTable">Reset table</button>
  <button @click="return_JSON(cards)">Get JSON</button>
  <button @click="downloadCSV(cards)">Get CSV</button>
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

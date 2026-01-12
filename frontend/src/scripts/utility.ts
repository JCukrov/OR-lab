import axios from "axios"

export const handleSearch = async(searchValue: string, searchColumn: string) => {
  if (searchValue === ''){
    return fetchAll()
  }
  const res = await axios.post(`${import.meta.env.VITE_API_URL}/search_cards`,{
    column: searchColumn || 'all',
    value: searchValue
  })
  console.log(res.data.cards)
  return res.data.cards
}

export const fetchAll = async() => {
    const res = await axios.get(`${import.meta.env.VITE_API_URL}/cards`)
    return res.data.response.cards
}
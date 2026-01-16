import axios from "axios"

export const handleSearch = async(searchValue: string, searchColumn: string) => {
  if (searchValue === ''){
    return fetchAll()
  }
  const res = await axios.post(`${import.meta.env.VITE_API_URL}/search`,{
    column: searchColumn || 'all',
    value: searchValue
  })
  return res.data
}

export const fetchAll = async() => {
    const res = await axios.get(`${import.meta.env.VITE_API_URL}/card`)
    return res.data.response
}
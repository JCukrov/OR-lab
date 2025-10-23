# Pokémon Cards Dataset

Language: English

This dataset contains information about Pokémon Trading Card Game (TCG) cards.  
Each entry represents one Pokémon card with its attributes and related attacks.  
The dataset is designed for educational purposes — to demonstrate database modeling, data export, and open data publishing.

---
## 🧩 Dataset Description

**Main entity:** Pokémon card (`cards`)  
**Child entity:** Attack (`attacks`)  

Each card can have one or more attacks, creating a parent-child relationship.

### Attributes (columns / JSON keys)

| Attribute | Description |
|------------|-------------|
| `id` | Unique identifier of the card |
| `name` | Name of the Pokémon |
| `type` | Pokémon type (e.g., Grass, Psychic) |
| `pokedex_number` | Pokédex number of the Pokémon |
| `hp` | Hit Points |
| `series` | Card series name (e.g., Obsidian Flames, Black Bolt) |
| `set_number` | Number of the card in the series |
| `illustrator` | Artist who illustrated the card |
| `release_year` | Year of release |
| `attacks` | List of attacks associated with the card |
| `attack_name` | Name of the attack (in CSV version) |
| `attack_damage` | Damage points of the attack |
| `attack_effect` | Additional description or effect of the attack |

---

import sqlite3

con = sqlite3.connect('./data/database.db')
cur = con.cursor()

query ='''
DROP TABLE IF EXISTS cards
'''
cur.execute(query)
con.commit()

query ='''
DROP TABLE IF EXISTS attacks
'''
cur.execute(query)
con.commit()

query ='''
CREATE TABLE IF NOT EXISTS attacks (
        id INTEGER PRIMARY KEY,
        card_id INTEGER,
        name TEXT,
        damage TEXT,
        effect TEXT,
        FOREIGN KEY(card_id) REFERENCES cards(id) ON DELETE CASCADE
    );
'''
cur.execute(query)
con.commit()

query = '''
CREATE TABLE IF NOT EXISTS cards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        type TEXT,
        pokedex_number INTEGER,
        hp INTEGER,
        series TEXT,
        set_number TEXT,
        illustrator TEXT,
        release_year INTEGER
    );
'''

cur.execute(query)
con.commit()

query = '''
INSERT INTO "attacks" ("id","card_id","name","damage","effect") VALUES (1,1,'Stampede','10',NULL),
 (2,1,'Reckless Charge','30','This Pokemon also does 10 damage to itself.'),
 (3,3,'Double Smash','80','FLip 2 coins. This attack does 80 damage for each heads.'),
 (4,3,'Golruk Hammer','200',NULL),
 (5,2,'Tackle','10',NULL),
 (6,2,'Vine Whip','30',NULL),
 (7,4,'Plotter''s Command','30','Choose 1 of your opponent''s Active Pokemon''s attacks. During your opponent''s next turn, that Pokemon can''t use that attack.'),
 (8,4,'Super Psy Bolt','80',NULL),
 (9,5,'Spooky Balloon','50','Put 2 damage counters on 1 of your opponent''s Benched Pokemon'),
 (10,6,'Rocket Mirror',NULL,'Move all damage counters from 1 of your Benched Team Rocket''s Pokemon to your opponent''s Active Pokemon'),
 (11,6,'HeadbuttBounce','70',NULL),
 (12,7,'Look-Alike Show',NULL,'Your opponent reveals their hand. You may use the effect of a Supporter card you find there as the effect of this attack.'),
 (13,7,'Eerie Wave','20','Your opponent''s Active Pokemon is now Confused.'),
 (14,8,'Psyshot','80',NULL),
 (15,9,'Gnaw','10',NULL),
 (16,9,'Spooky Shot','20',NULL),
 (17,10,'Dream Calling',NULL,'You may search your deck for any number of Fennel cards, reveal them, and put them into your hand. Then, shuffle your deck.'),
 (18,10,'Sleep Pulse','50','Your opponent''s Active Pokemon is now Asleep.');
'''
cur.execute(query)
con.commit()

query = '''
INSERT INTO "cards" ("id","name","type","pokedex_number","hp","series","set_number","illustrator","release_year") VALUES (1,'Bonusweet','grass',761,60,'Obsidian Flames','16','Kurata So',2023),
 (2,'Snivy','grass',495,70,'Black Bolt','1','Susumu Moeya',2025),
 (3,'Golurk','psychic',623,160,'Black Bolt','43','Uta',2025),
 (4,'Oranguru','psychic',765,120,'Paldea Evolved','94','Tashinao Aoki',2023),
 (5,'Drifblim','psychic',426,110,'Astral Radiance','64','Kyoko Umemoto',2022),
 (6,'Team Rocket''s Wobbuffet','psychic',202,110,'Destined Rivals','82','Kazumasa Yasukuni',2025),
 (7,'Mr. Mime','psychic',122,90,'Temporal Forces','63','Nelnal',2024),
 (8,'Mewostic','psychic',678,90,'Surging Sparks','85','Yoriyuki Ikegami',2024),
 (9,'Greavard','psychic',971,70,'Obsidian Flames','99','Shibuzoh.',2023),
 (10,'Musharna','psychic',518,120,'Black Bolt','36','Eri Kamei',2025);
'''
cur.execute(query)
con.commit()
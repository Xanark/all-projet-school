"""
Leo Dumas
novembre 2022
"""

import sqlite3 as sq


connection = sq.connect("cinéma.sq3")

curseur = connection.cursor()
curseur.execute("PRAGMA foreign_keys = ON")


curseur.executescript("""

    DROP TABLE IF EXISTS Réalisateurs;
    DROP TABLE IF EXISTS Films;

    CREATE TABLE Réalisateurs(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    nom TEXT NOT NULL, prenom TEXT NOT NULL,
    nationalite TEXT NOT NULL, date_naissance TEXT NOT NULL);

    CREATE TABLE Films(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    titre TEXT NOT NULL, annee INTEGER NOT NULL,
    note_s REAL NOT NULL, note_p REAL NOT NULL,
    id_realisateur INTEGER NOT NULL,
    FOREIGN KEY(id_realisateur) REFERENCES Réalisateurs(id) ON DELETE CASCADE)
""")

connection.commit()

curseur.executescript("""
    INSERT INTO Réalisateurs VALUES
    (1, 'COPPOLA','Francis Ford','americain','1939-04-07'),
    (2, 'ZEMECKIS','Robert','americain','1952-14-05'),
    (3, 'DARABONT','Frank','français','1959-28-01'),
    (4, 'SPIELERG','Steven','americain','1946-18-12'),
    (5, 'SHINKAI','Makoto','japonais','1973-09-02'),
    (6, 'TARANTINO','Quentin','americain','1963-27-03'),
    (7, 'EASTWOOD','Clint','americain','1930-31-05'),
    (8, 'NOLAN','Christopher','britannique','1970-30-07')
""")
connection.commit()

curseur.executescript("""
    INSERT INTO Films VALUES
    (1, 'Forrest Gump', 1994, 4.6, 2.6, 2),
    (2, 'La ligne verte', 2000, 4.6, 2.8, 3),
    (3, 'La liste de Schindler', 1994, 4.5, 4.2, 4),
    (4, 'Le Parrin', 2013, 4.5, 4.6, 1),
    (5, 'Your Name', 2016, 4.5, 4, 5),
    (6, 'Grand Torino', 2009, 4.5, 4.7, 7),
    (7, 'Pulp Fiction', 1994, 4.5, 4.4, 6),
    (8, 'Les Enfants du Temps', 2020, 4.3, 3.8, 5),
    (9, 'Sully', 2016, 4.1, 3.8, 7)
""")

connection.commit()

curseur.executescript("""
    INSERT INTO Films VALUES(NULL, 'Les_évadés', 1996, 4.5, 3.2, 3)
""")
connection.commit()



curseur.executescript("""
    UPDATE Films SET annee = '1995' WHERE id = 10 
""")

connection.commit()

curseur.executescript("""
    DELETE FROM Réalisateurs WHERE id = 8
""")

connection.commit()

curseur.executescript("""
    DELETE FROM Films WHERE note_p <= 3
""")



connection.commit()


"""
curseur.execute("SELECT titre,annee,note_p FROM Films ORDER BY note_p DESC ")
for resultat in curseur:
    print(resultat)
"""

curseur.execute("""SELECT DISTINCT COUNT(nom) FROM Réalisateurs JOIN Films ON Films.id_realisateur = Réalisateurs.id WHERE note_p >= 4.4
""")
for resultat in curseur:
    print(resultat)
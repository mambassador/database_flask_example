DROP TABLE IF EXISTS tracks;


CREATE TABLE tracks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(50) NOT NULL,
  artist VARCHAR(50) NOT NULL,
  genre VARCHAR(50) NOT NULL,
  length INTEGER NOT NULL
);


INSERT INTO tracks (id, title, artist, genre, length)
VALUES
    (1, 'Dancing in the Moonlight', 'Emma Johnson', 'pop', 200),
    (2, 'Midnight Serenade', 'Michael Davis', 'jazz', 300),
    (3, 'Guitar Groove', 'Sophia Thompson', 'rock', 240),
    (4, 'Dreamy Piano', 'Oliver Wilson', 'classical', 180),
    (5, 'Funky Bassline', 'Ava Martinez', 'funk', 220),
    (6, 'Soulful Melody', 'James Anderson', 'r&b', 280),
    (7, 'Electric Dreams', 'Noah Wright', 'electronic', 260),
    (8, 'Smooth Saxophone', 'Noah Wright', 'smooth jazz', 320),
    (9, 'Country Roads', 'Isabella Harris', 'country', 280),
    (10, 'Latin Rhythms', 'Mason Clark', 'latin', 240),
    (11, 'Smooth Operator', 'Liam Turner', 'pop', 230),
    (12, 'Jazz Nights', 'Charlotte White', 'jazz', 320),
    (13, 'Rock Anthem', 'Lucas Thompson', 'rock', 280),
    (14, 'Piano Sonata', 'Harper Adams', 'classical', 360),
    (15, 'Funky Grooves', 'Amelia Parker', 'funk', 200),
    (16, 'Soul Serenade', 'Benjamin Mitchell', 'r&b', 250),
    (17, 'Electronic Vibes', 'Ella Scott', 'electronic', 290),
    (18, 'Smooth Jazz Journey', 'Henry Green', 'smooth jazz', 340),
    (19, 'Country Sunset', 'Scarlett Turner', 'country', 310),
    (20, 'Salsa Fiesta', 'William Baker', 'latin', 270),
    (21, 'Dancing Queen', 'Grace Wilson', 'pop', 240),
    (22, 'Trumpet Magic', 'Daniel Harris', 'jazz', 280),
    (23, 'Indie Rock Revival', 'Victoria Davis', 'rock', 320),
    (24, 'Concerto in A Minor', 'Andrew Allen', 'classical', 400),
    (25, 'Bass Funkadelic', 'Penelope Turner', 'funk', 210),
    (26, 'R&B Groove', 'Jack Thompson', 'r&b', 260),
    (27, 'Electronic Dreamscape', 'Sophie Clark', 'electronic', 300),
    (28, 'Smooth Sax Solitude', 'Joseph Wright', 'smooth jazz', 360),
    (29, 'Country Heartache', 'Chloe Martinez', 'country', 290),
    (30, 'Tropical Beats', 'Samuel Scott', 'latin', 250),
    (31, 'Summer Breeze', 'Emily Johnson', 'pop', 220),
    (32, 'Saxophone Serenade', 'Daniel Davis', 'jazz', 310),
    (33, 'Classic Rock Jam', 'Olivia Thompson', 'rock', 270),
    (34, 'Piano Concerto', 'James Adams', 'classical', 380),
    (35, 'Groovy Bassline', 'Lucy Wilson', 'funk', 190),
    (36, 'Soulful Ballad', 'Noah Mitchell', 'r&b', 240),
    (37, 'Electro Pop Energy', 'Sophia Walker', 'electronic', 280),
    (38, 'Jazz Fusion Experience', 'Oliver Green', 'smooth jazz', 330),
    (39, 'Country Serenity', 'Ava Harris', 'country', 300);
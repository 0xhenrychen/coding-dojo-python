SELECT * FROM favorites;

SELECT * FROM favorites
JOIN books ON books.id = favorites.book_id
JOIN authors ON authors.id = favorites.author_id
WHERE favorites.author_id = 2;

SELECT * FROM favorites
JOIN books ON books.id = favorites.book_id
JOIN authors ON authors.id = favorites.author_id
WHERE favorites.book_id = 7;

SELECT * FROM books
WHERE books.id NOT IN ( SELECT book_id FROM favorites WHERE author_id = 11);
				
SELECT * FROM authors;
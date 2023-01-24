-- Query: Create 5 different users: Jane Amsden, Emily Dixon, Theodore Dostoevsky, William Shapiro, Lao Xiu

-- insert into users (name, created_at, updated_at)
-- values('Jane Amsden', now(), now());

-- insert into users (name, created_at, updated_at)
-- values('Emily Dixon', now(), now());

-- insert into users (name, created_at, updated_at)
-- values('Theodore Dostoevsky', now(), now());

-- insert into users (name, created_at, updated_at)
-- values('William Shapiro', now(), now());

-- insert into users (name, created_at, updated_at)
-- values('Lao Xiu', now(), now());


-- Query: Create 5 books with the following names: C Sharp, Java, Python, PHP, Ruby

-- insert into books (title, created_at, updated_at)
-- values ('C Sharp', now(), now());

-- insert into books (title, created_at, updated_at)
-- values ('Java', now(), now());

-- insert into books (title, created_at, updated_at)
-- values ('Python', now(), now());

-- insert into books (title, created_at, updated_at)
-- values ('PHP', now(), now());

-- insert into books (title, created_at, updated_at)
-- values ('Ruby', now(), now());


-- Query: Change the name of the C Sharp book to C#

-- update books
-- set title = 'C#'
-- where id = 1;


-- Query: Change the first name of the 4th user to Bill

-- update users
-- set name = 'Bill Dostoevsky'
-- where id = 4;


-- Query: Have the first user favorite the first 2 books

-- insert into favorites (user_id, book_id)
-- values(1, 1), (1, 2);


-- Query: Have the second user favorite the first 3 books

-- insert into favorites (user_id, book_id)
-- values (3, 1), (3, 2), (3, 3);


-- Query: Have the third user favorite the first 4 books

-- insert into favorites (user_id, book_id)
-- values(4, 1), (4, 2), (4, 3), (4, 4);


-- Query: Have the fourth user favorite all the books

-- insert into favorites (user_id, book_id)
-- values(5, 1), (5, 2), (5, 3), (5, 4), (5, 5);


-- Query: Retrieve all the users who favorited the 3rd book

-- select *
-- from users
-- join favorites
-- on users.id = favorites.user_id
-- where favorites.book_id = 3;


-- Query: Remove the first user of the 3rd book's favorites

-- delete from favorites
-- where user_id = 1 and book_id = 3;


-- Query: Have the 5th user favorite the 2nd book

-- insert into favorites (user_id, book_id)
-- values(5, 2);


-- Find all the books that the 3rd user favorited

-- select *
-- from books
-- join favorites
-- on books.id = favorites.book_id
-- where favorites.user_id = 3;


-- Query: Find all the users that favorited to the 5th book

-- select *
-- from users
-- join favorites
-- on users.id = favorites.user_id
-- where favorites.book_id = 5;
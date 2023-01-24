-- Query: Create 3 new users
-- insert into users (first_name, last_name, email, created_at, updated_at)
-- values("Henry", "Chen", "henrychen14505@gmail.com", now(), now());

-- insert into users (first_name, last_name, email, created_at, updated_at)
-- values("Charlene", "Chiu", "charlene@gmail.com", now(), now());

-- insert into users (first_name, last_name, email, created_at, updated_at)
-- values("Ellie", "Chen", "ellie@gmail.com", now(), now());


-- Query: Retrieve all the users
-- select * from users;


-- Query: Retrieve the first user using their email address
-- select id, email
-- from users
-- where email = "henrychen14505@gmail.com";


-- Query: Retrieve the last user using their id
-- select *
-- from users
-- where id = 3;


-- Query: Change the user with id=3 so their last name is Pancakes
-- update users
-- set last_name = Pancakes
-- where id = 3;


-- Query: Delete the user with id=2 from the database
-- delete from users
-- where id = 2;
-- select * from users;


-- Query: Get all the users, sorted by their first name
-- select * from users
-- order by first_name;


-- BONUS Query: Get all the users, sorted by their first name in descending order
-- select * from users
-- order by first_name desc;
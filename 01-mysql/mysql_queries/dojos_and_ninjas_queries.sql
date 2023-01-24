-- Query: Create 3 new dojos
-- insert into dojos (name, created_at, updated_at)
-- values("Los Angeles Dojo", now(), now());

-- insert into dojos (name, created_at, updated_at)
-- values("San Diego Dojo", now(), now());

-- insert into dojos (name, created_at, updated_at)
-- values("San Francisco Dojo", now(), now());


-- Query: Delete the 3 dojos you just created
-- delete from dojos where id = 1 or id = 2 or id = 3;


-- Query: Create 3 more dojos
-- insert into dojos (name, created_at, updated_at)
-- values("New York Dojo", now(), now());

-- insert into dojos (name, created_at, updated_at)
-- values("Chicago Dojo", now(), now());

-- insert into dojos (name, created_at, updated_at)
-- values("Seattle Dojo", now(), now());


-- Query: Create 3 ninjas that belong to the first dojo
-- insert into ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
-- values("Kevin", "Durant", 35, 4, now(), now());

-- insert into ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
-- values("LeBron", "James", 38, 4, now(), now());

-- insert into ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
-- values("Luca", "Doncic", 23, 4, now(), now());


-- Query: Create 3 ninjas that belong to the second dojo
-- insert into ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
-- values("Kawhi", "Leonard", 30, 5, now(), now());

-- insert into ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
-- values("Stephen", "Curry", 32, 5, now(), now());

-- insert into ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
-- values("Nikola", "Jokic", 28, 5, now(), now());


-- Query: Create 3 ninjas that belong to the third dojo
-- insert into ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
-- values("Kyrie", "Irvine", 30, 6, now(), now());

-- insert into ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
-- values("Joel", "Embiid", 27, 6, now(), now());

-- insert into ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
-- values("Giannis", "Antetokounmpo", 27, 6, now(), now());


-- Query: Retrieve all the ninjas from the first dojo
-- select *
-- from dojos
-- join ninjas
-- on dojos.id = ninjas.dojo_id
-- where dojos.id = 4;


-- Query: Retrieve all the ninjas from the last dojo
-- select *
-- from dojos
-- join ninjas
-- on dojos.id = ninjas.dojo_id
-- where dojos.id = 6;


-- Query: Retrieve the last ninja's dojo
-- select *
-- from dojos
-- join ninjas
-- on dojos.id = ninjas.dojo_id
-- where ninjas.id = 9;
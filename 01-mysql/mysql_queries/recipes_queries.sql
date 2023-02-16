INSERT INTO recipes (name, description, instructions, date, under_30_mins, users_id)
                    VALUES ("Brownies", "Very delicious", "Bake for 10 mins", "2023-02-13", "Yes", "1");
SELECT * from recipes
JOIN users ON users.id = recipes.users_id;

SELECT * FROM users
JOIN recipes ON recipes.users_id = users.id;

SELECT * FROM recipes
JOIN users ON users.id = recipes.users_id;

SELECT * FROM recipes
JOIN users ON users.id = recipes.users_id
WHERE recipes.id = 5;

SELECT * FROM users
JOIN recipes ON users.id = recipes.users_id
WHERE recipes.id = 1;

SELECT * FROM recipes;

		
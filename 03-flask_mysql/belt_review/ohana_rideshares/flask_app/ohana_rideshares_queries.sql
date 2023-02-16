SELECT * from users;

INSERT INTO users (first_name, last_name, email, password)
                    VALUES ("Henry", "Chen", "henrychen14505@gmail.com", "Testing123");
                    
SELECT * from rides
JOIN users on users.id = rides.passenger_id;
SELECT * from users;
SELECT * from rides;

INSERT INTO users (first_name, last_name, email, password)
                    VALUES ("Henry", "Chen", "henrychen14505@gmail.com", "Testing123");
                    
SELECT * from rides
JOIN users on users.id = rides.passenger_id;

UPDATE rides
                     SET driver_id = 4
                     WHERE ID = 3;
                     
                     SELECT * FROM rides
                     JOIN users on users.id = rides.driver_id
						WHERE driver_id = 6;
                        
SELECT * from rides;

 SELECT * FROM rides
                    JOIN users ON users.id = rides.passenger_id;
                    
                    SELECT * FROM rides
                    JOIN users ON users.id = rides.passenger_id
                    JOIN users as users2 ON users2.id = rides.driver_id
                    WHERE rides.id = 3;
                    
                    SELECT * FROM rides R
                    JOIN users UP ON UP.id = R.passenger_id
                    JOIN users UD ON UD.id = R.driver_id
                    WHERE R.id = 1;
                   
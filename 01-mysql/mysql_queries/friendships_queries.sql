-- Query: Create 6 new users

-- insert into users (first_name, last_name, created_at, updated_at)
-- values('Henry', 'Chen', now(), now()), ('Ellie', 'Chen', now(), now()), ('Charlene', 'Chiu', now(), now()), ('David', 'Chen', now(), now()), ('Cindy', 'Chen', now(), now()), ('Gonzalo', 'Chiu', now(), now());



-- Query: Have user 1 be friends with user 2, 4 and 6

insert into friendships (user_id, friend_id)
values(1,2), (1,4), (1,6);


-- Query: Have user 2 be friends with user 1, 3 and 5

insert into friendships (user_id, friend_id)
values(2, 1), (2, 3), (2, 5);


-- Query: Have user 3 be friends with user 2 and 5

insert into friendships (user_id, friend_id)
values(3, 2), (3, 5);


-- Query: Have user 4 be friends with user 3

insert into friendships (user_id, friend_id)
values(4, 3);


-- Query: Have user 5 be friends with user 1 and 6

insert into friendships (user_id, friend_id)
values(5, 1), (5, 6);


-- Query: Have user 6 be friends with user 2 and 3

insert into friendships (user_id, friend_id)
values(6, 2), (6, 3);


-- Query: Display the relationships created as shown in the table in the above image

select users.id, users.first_name, users.last_name, users2.id as friend_id, users2.first_name as friend_first_name, users2.last_name as friend_last_name from users
join friendships on users.id = friendships.user_id
left join users as users2 on users2.id = friendships.friend_id;


-- NINJA Query: Return all users who are friends with the first user, make sure their names are displayed in results.

select users.id, users.first_name, users.last_name, users2.id as friend_id, users2.first_name as friend_first_name, users2.last_name as friend_last_name from users
join friendships on users.id = friendships.user_id
left join users as users2 on users2.id = friendships.friend_id
where users.id = 1;


-- NINJA Query: Return the count of all friendships // 13

select count(*) as total_number_of_friendships from friendships;


-- NINJA Query: Find out who has the most friends and return the count of their friends. // Henry and Ellie are tied at 3 friends each

select users.id, users.first_name, users.last_name, count(user_id) as number_of_friends from friendships
join users on friendships.user_id = users.id
group by user_id
order by count(user_id) desc;


-- NINJA Query: Return the friends of the third user in alphabetical order

select users2.id as friend_id, users2.first_name as friend_first_name, users2.last_name as friend_last_name, users.id, users.first_name, users.last_name from users
join friendships on users.id = friendships.user_id
left join users as users2 on users2.id = friendships.friend_id
where users.id = 3
order by users2.first_name;
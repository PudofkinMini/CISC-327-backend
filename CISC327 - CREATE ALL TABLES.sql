/*

CREATE TABLE accounts (
    id INT PRIMARY KEY IDENTITY(1,1),
	email varchar(1000) NOT NULL,
    username VARCHAR(1000) NOT NULL,
    password VARCHAR(1000) NOT NULL,
	premium bit NOT NULL,
	created datetime, 
	updated datetime,
	deleted datetime
);
*/
begin transaction
CREATE TABLE orders (
    id INT PRIMARY KEY IDENTITY(1,1),
	account_id int NOT NULL,
    delivery_date datetime NOT NULL,
    driver varchar(1000) NOT NULL,
	status varchar(1000) NOT NULL,
	created datetime, 
	updated datetime,
	deleted datetime
);
select * from orders

CREATE TABLE ordered_items (
    id INT PRIMARY KEY IDENTITY(1,1),
	order_id int NOT NULL,
    menu_item_id int NOT NULL,
	created datetime, 
	updated datetime,
	deleted datetime
);
select * from ordered_items

CREATE TABLE restaurants (
    id INT PRIMARY KEY IDENTITY(1,1),
	name varchar(1000) NOT NULL,
    category varchar(1000) NOT NULL,
	price varchar(1000) NOT NULL,
	logo varchar(1000), 
	created datetime,
	updated datetime,
	deleted datetime
);
select * from restaurants

CREATE TABLE menu_items (
    id INT PRIMARY KEY IDENTITY(1,1),
	restaurant_id int NOT NULL,
    name varchar(1000) NOT NULL,
	price numeric(25, 2) NOT NULL,
	calories int,
	image varchar(1000),
	created datetime,
	updated datetime,
	deleted datetime
);
select * from menu_items


CREATE TABLE payments (
    id INT PRIMARY KEY IDENTITY(1,1),
	account_id varchar(1000) NOT NULL,
    restaurant_id varchar(1000) NOT NULL,
	subtotal numeric(25, 2) NOT NULL,
	total numeric(25, 2) NOT NULL, 
	created datetime,
	updated datetime,
	deleted datetime
);
select * from payments


rollback transaction




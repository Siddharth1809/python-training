select * from inventory

create table inventory (id int not null auto_increment,
Name varchar(255) not null,
Category varchar(255) not null,
ExpiryDate datetime,
ManufactureDate datetime,
Quantity int,
primary key(id))

alter table inventory add column Image varchar(255) after Quantity



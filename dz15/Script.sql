create table authors(
	id int primary key,
	first_name varchar(50),
	last_name varchar(50)
);
	   
create table books(
	id int primary key,
	title varchar(100),
	author_id int,
	publication_year int,
	 foreign key (author_id) references authors(id)
);

create table sales( 
	id int primary key,
	book_id int,
	quantity int,
	foreign key(book_id) references books(id)
);

insert into authors (id, first_name, last_name) values
(1, 'Lewis', 'Carroll'),
(2, 'Joanne', 'Rowling'),
(3, 'Antoine', 'de Saint-Exupery'),
(4, 'William', 'Shakespeare');

insert into books (id, title, author_id, publication_year) values 
(1, 'Harry Potter', 2, 1997),
(2, 'The Little Prince', 3, 1943),
(3, 'Alice’s Adventures in Wonderland', 1, 1865),
(4, 'Through the Looking-Glass, and What Alice Found There', null, 1871);

insert into sales (id, book_id, quantity) values
(1, 1, 100),
(2, 2, null),
(3, 3, 65),
(4, 4, null);

select authors.first_name as author_first_name,
	   authors.last_name as author_last_name,
	   books.title
from authors
inner join books on books.author_id = authors.id;


select authors.first_name as author_first_name,
	   authors.last_name as author_last_name,
	   books.title
from authors
left join books on books.author_id = authors.id;

select books.title as book_title,
       authors.first_name as author_first_name,
       authors.last_name as author_last_name
from authors
right join books on books.author_id = authors.id;

select authors.first_name as author_first_name,
       authors.last_name as author_last_name,
       books.title as book_title,
       sales.quantity
from authors
inner join books on books.author_id = authors.id
inner join sales on sales.book_id = books.id;

select authors.first_name as author_first_name,
       authors.last_name as author_last_name,
       books.title as book_title,
       sales.quantity
from authors
left join books on books.author_id = authors.id
left join sales on sales.book_id = books.id;

select authors.first_name as author_first_name,
       authors.last_name as author_last_name,
       sum(sales.quantity) as total_books_sold
from authors 
inner join books on books.author_id = authors.id
inner join sales on sales.book_id = books.id
group by authors.id, authors.first_name, authors.last_name;

select authors.first_name as author_first_name,
       authors.last_name as author_last_name,
       sum(sales.quantity) as total_books_sold
from authors 
left join books on books.author_id = authors.id
left join sales on sales.book_id = books.id
group by authors.id, authors.first_name, authors.last_name;

select first_name, last_name
from authors
where id = (
	select author_id
	from ( 
	select books.author_id,
		   sum(sales.quantity) as total_sales
	from books
	inner join sales on sales.book_id = books.id
	where sales.quantity is not null and books.author_id is not null
	group by books.author_id
	order by total_sales desc 
	limit 1
	)
);

select books.title, sales.quantity
from books
inner join sales on books.id = sales.book_id
where sales.quantity is not null
  and sales.quantity > (
      select avg(quantity)
      from sales
      where quantity is not null 
  );


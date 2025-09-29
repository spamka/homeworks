create table employees(
	name varchar,
	pos varchar,
	department varchar,
	salary decimal(10, 2)
);

insert into employees(name, pos, department, salary) 
values ('Victor Petrovich', 'Cook', 'Kitchen', 5000.01),
	   ('Sofia Yanovna', 'Manager', 'Administration', 6000.00),
	   ('Kostya', 'Barman', 'Bar', 4800.00);

update employees set pos = 'Chief' where name = 'Victor Petrovich';

alter table employees
add hire_date DATE default '2025-09-24';


create or replace function get_avg_salary() 
returns decimal
as $$
declare 
	avg_salary decimal;
begin
	select avg(salary) into avg_salary from employees;
	return avg_salary;
end;
$$ language plpgsql;

create or replace function find_manager()
returns table (
	name varchar,
	pos varchar,
	department varchar,
	salary decimal,
	hire_date date
	)
as $$
begin
	return query
	select * from employees e where e.pos = 'Manager';
end;
$$ language plpgsql;
	
create or replace function higher_salary()
returns table (
	name varchar,
	pos varchar,
	department varchar,
	salary decimal,
	hire_date date
	)
as $$
begin
	return query
	select * from employees e where e.salary > 5000;
end;
$$ language plpgsql;

create or replace function find_department()
returns table (
	name varchar,
	pos varchar,
	department varchar,
	salary decimal,
	hire_date date
	)
as $$
begin
	return query
	select * from employees e where e.department = 'Bar';
end;
$$ language plpgsql;

select * from get_avg_salary();

select * from find_manager();

select * from higher_salary();

select * from find_department();

drop table employees;
	   

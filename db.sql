create schema if not exists content;

CREATE EXTENSION if not exists "uuid-ossp";

SET search_path TO content,public;

create table if not exists content.train(
	id uuid primary key,
	name text not null
);

create table if not exists content.wagon(
	id uuid primary key,
	train_id uuid references content.train not null,
	name text not null,
	class text not null,
	capacity int not null,
	check(class_wagon in ('плацкарт', 'купе', 'СВ'))
);

create table if not exists content.privilege(
	id uuid primary key,
	category text not null,
	description text not null,
	tariff text,
	discount int not null
);

create table if not exists content.city(
	id uuid primary key,
	name_city text not null
);

create table if not exists content.service(
	id uuid primary key,
	name text not null,
	price numeric not null,
	is_optional boolean not null
);

create table if not exists content.service_to_ticket(
	service_id int references content.service,
	ticket_id int references content.ticket,
	primary key (service_id, ticket_id)
);

create table if not exists content."user"(
	id uuid primary key,
	full_name text not null,
	docs int not null
);

create table if not exists content.trip(
	id uuid primary key,
	train_id uuid references content.train not null,
	city_departure uuid references content.city not null,
	city_arrival uuid references content.city not null,
	way_departure int not null,
	way_arrival int not null,
	time_departure timestamp with time zone,
	time_arrival timestamp with time zone
);

create table if not exists content.ticket(
	id uuid primary key,
	wagon_id uuid references content.wagon not null,
	priv_id uuid references content.privilege not null,
	trip_id uuid references content.trip not null,
	user_id uuid references content.user not null,
	price numeric not null,
	availability boolean not null,
	place int not null
);

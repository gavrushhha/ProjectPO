create schema if not exists content;

create table if not exists content.train(
	id uuid primary key,
	name_train text not null
);

create table if not exists content.wagon(
	id uuid primary key,
	train_id uuid references content.train not null,
	name_wagon text not null
);

create table if not exists content.tariff(
	id uuid primary key,
	name_tariff text not null,
	discount int not null
);

create table if not exists content.privilege(
	id uuid primary key,
	name_privilege text not null,
	discount int not null
);

create table if not exists content.place(
	id uuid primary key,
	wagon_id uuid references content.wagon not null,
	class_wagon text not null,
	position text not null
);

create table if not exists content.city(
	id uuid primary key,
	name_city text not null
);

create table if not exists content.product(
	id uuid primary key,
	name_product text not null,
	price money,
	availability boolean not null
);

create table if not exists content.user(
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
	train_id uuid references content.train not null,
	tariff_id uuid references content.tariff not null,
	priv_id uuid references content.privilege not null,
	place_id uuid references content.place not null,
	trip_id uuid references content.trip not null,
	user_id uuid references content.user not null,
	product_id uuid references content.product,
	price money,
	availability boolean
);
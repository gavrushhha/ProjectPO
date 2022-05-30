create schema if not exists content;

CREATE EXTENSION if not exists "uuid-ossp";

SET search_path TO content,public;

create table if not exists content.train(
  id uuid primary key,
  name text not null,
  unique(name)
);

create table if not exists content.wagon(
  id uuid primary key,
  train_id uuid references content.train not null,
  name int not null,
  class_wagon text not null,
  capacity int not null,
  unique(train_id, name)

);

create table if not exists content.privilege(
  id uuid primary key,
  category text not null,
  description text,
  discount int not null,
  unique(category, discount)
);

create table if not exists content.city(
  id uuid primary key,
  name_city text not null,
  unique(name_city)
);

create table if not exists content.service(
  id uuid primary key,
  name text not null,
  price numeric not null,
  is_optional boolean not null,
  unique(name, price)
);

create table if not exists content.person(
  id uuid primary key,
  username text not null,
  docs text not null,
  email text not null,
  unique(username, docs)
);

create table if not exists content.trip(
  id uuid primary key,
  train_id uuid references content.train not null,
  city_departure_id uuid references content.city not null,
  city_arrival_id uuid references content.city not null,
  way_departure int not null,
  way_arrival int not null,
  time_departure timestamp with time zone,
  time_arrival timestamp with time zone,
  unique(train_id, city_departure_id, city_arrival_id)
);

create table if not exists content.ticket(
  id uuid primary key,
  wagon_id uuid references content.wagon not null,
  priv_id uuid references content.privilege not null,
  trip_id uuid references content.trip not null,
  user_id uuid references content.person not null,
  price numeric not null,
  place int,
  unique(wagon_id, trip_id, place)
);

create table if not exists content.service_to_ticket(
  service_id uuid references content.service,
  ticket_id uuid references content.ticket,
  primary key (service_id, ticket_id)
);
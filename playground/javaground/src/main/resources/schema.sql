create table person
(
    seq      bigint identity not null primary key,
    name     varchar(10),
    nickname varchar(20),
    age      int
);

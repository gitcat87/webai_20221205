create table Vacation (
    fordate integer not null,
    month integer not null,
    createDate datetime(6),
    id bigint not null,
    modifiedDate datetime(6),
    address varchar(255),
    birthdate varchar(255),
    classname varchar(255),
    enddate varchar(255),
    name varchar(255),
    phonenumber varchar(255),
    reason varchar(255),
    reasondate varchar(255),
    startdate varchar(255),
    primary key (id)
);
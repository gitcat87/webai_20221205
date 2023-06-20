package com.kb.org.model;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDate;
import java.time.LocalDateTime;

@Getter
@Setter
@Entity //테이블 만들어주는 라이브러리

public class Vacation extends BaseTimeEntity{
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id", nullable = false)
    private long id;

    private int month;
    private String startdate;
    private String enddate;
    private  int fordate;
    private  String classname;
    private  String name;
    private  String birthdate;
    private  String address;
    private  String phonename;
    private  String reason;
    private  String reasondate;
}

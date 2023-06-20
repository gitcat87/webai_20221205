package com.kb.org.model;

import jakarta.persistence.*;
import  lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import java.util.List;


@Getter
@Setter
@Entity
@ToString
public class Member extends BaseTimeEntity {
    @Id
    @GeneratedValue(strategy =  GenerationType.IDENTITY)
    private  Long id;

    private String name;

    @Column(unique = true)
    private  String email;

    private  String pwd;

    private String gubun;

//    @OneToMany
//    List<Board> boarlist;

    //휴가신청서.. 학생신청서
}

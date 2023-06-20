package com.kb.org.controller;


import com.kb.org.model.Member;
import com.kb.org.repository.MemberRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class MainController {
    @Autowired
    MemberRepository memberRepositoty;

    @GetMapping("/")
    public String main(){
        Member member1 = new Member();
        Member member2 = new Member();

        member1.setName("name1");
        member1.setEmail("aa@naver.com");

        member2.setName("name2");
        member2.setEmail("bb@naver.com");

        memberRepositoty.save(member1);
        memberRepositoty.save(member2);

        System.out.println("일로오나");
        return "main";
    }
    @GetMapping("/aa")
    public String aa(){
        System.out.println("일로오나");
        return "aa";
    }


}

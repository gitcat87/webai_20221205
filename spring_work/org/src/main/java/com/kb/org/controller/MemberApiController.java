package com.kb.org.controller;

import com.kb.org.model.Member;
import com.kb.org.repository.MemberRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

//콘트롤러의 패키지는 url주소를 지정하는 용도로 사용중이다
@RestController
@RequestMapping("memberapi")
public class MemberApiController {
    @Autowired
    MemberRepository memberRepository;

    @GetMapping("select")
    public List<Member> select(){
        List<Member> list = memberRepository.findAll();
        return list;
    }

    @PostMapping("insert")
    public String insert(@RequestBody Member reqm){

        memberRepository.save(reqm);

        return "insert 됨";
    }


    @PostMapping("delete")
    public String delete(@RequestBody Member reqm){
        // 해당되는 id가 있으면 delete가 되어야 한다.
        Member dbMember = memberRepository.findById(reqm.getId()).orElse(null);
        if(dbMember == null){
            return "삭제할 행이 없습니다";
        }
        else{
            memberRepository.delete(reqm);
            return "delete됨";
        }

    }

    @PostMapping("update")
    public String update(@RequestBody Member reqm){
        //행이 있으면 update
        //행이 없으면 insert
        Member dbMember = memberRepository.findById(reqm.getId()).orElse(null);
        if(dbMember == null){
            return "수정할 행이 없습니다";
        }
        else{
            memberRepository.save(reqm);
            return "update됨";
        }
    }
}










package com.kb.org.controller;


import com.kb.org.model.Vacation;
import com.kb.org.repository.VacationRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

//콘트롤러의 패키지는 url주소를 지정하는 용도로 사용중이다
@RestController
@RequestMapping("vacationapi")
public class VacationApiController {
    @Autowired
    VacationRepository vacationRepository;

    @GetMapping("select")
    public List<Vacation> select(){
        List<Vacation> list = vacationRepository.findAll();
        return list;
    }

    @PostMapping("insert")
    public String insert(@RequestBody Vacation reqm){

        vacationRepository.save(reqm);

        return "insert 됨";
    }


    @PostMapping("delete")
    public String delete(Vacation reqm){
        // 해당되는 id가 있으면 delete가 되어야 한다.
        Vacation dbVacation = vacationRepository.findById(reqm.getId()).orElse(null);
        if(dbVacation == null){
            return "삭제할 행이 없습니다";
        }
        else{
            vacationRepository.delete(reqm);
            return "delete됨";
        }

    }

    @PostMapping("update")
    public String update(Vacation reqm){
        //행이 있으면 update
        //행이 없으면 insert
        Vacation dbVacation = vacationRepository.findById(reqm.getId()).orElse(null);
        if(dbVacation == null){
            return "수정할 행이 없습니다";
        }
        else{
            vacationRepository.save(reqm);
            return "update됨";
        }
    }
}










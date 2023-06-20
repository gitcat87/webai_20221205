package com.kb.org.controller;

import com.kb.org.model.Board;
import com.kb.org.repository.BoardRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.List;

@Controller
@RequestMapping("board")

public class BoardController {
    //http://localhost:8080/board/select

    @Autowired
    BoardRepository boardRepository;
    @GetMapping("select")
    public String select(){
        List<Board>  list = boardRepository.findAll();
        System.out.println(list);
        return "board";
    }

    @GetMapping("insert")
    public String insert(){
        boardRepository.save(new Board());
        return "board";
    }


}

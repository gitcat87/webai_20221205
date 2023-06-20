package com.kb.org.repository;

import com.kb.org.model.Member;
import org.springframework.beans.factory.annotation.Autowired;
import com.kb.org.repository.MemberRepository;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public interface MemberRepository  extends JpaRepository<Member, Long> {
}

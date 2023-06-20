package com.kb.org.repository;

import com.kb.org.model.Vacation;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Controller;

@Controller
public interface VacationRepository extends JpaRepository<Vacation, Long> {

}

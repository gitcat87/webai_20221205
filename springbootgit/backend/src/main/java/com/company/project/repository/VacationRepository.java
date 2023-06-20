package com.company.project.repository;


import com.company.project.entity.Vacation;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Controller;

@Controller
public interface VacationRepository extends JpaRepository<Vacation, Long> {

}

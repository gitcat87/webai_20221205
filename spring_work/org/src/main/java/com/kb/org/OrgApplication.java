package com.kb.org;

import com.kb.org.test.AA;
import com.kb.org.test.BB;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.data.jpa.repository.config.EnableJpaAuditing;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

import java.util.ArrayList;
import java.util.List;


@SpringBootApplication
@EnableJpaAuditing
public class OrgApplication {

	@Bean
	public WebMvcConfigurer corsConfigurer() {
		return new WebMvcConfigurer() {
			@Override
			public void addCorsMappings(CorsRegistry registry) {
				registry.addMapping("/**").allowedOrigins("*");
			}
		};
	}

	public static void main(String[] args) {
		SpringApplication.run(OrgApplication.class, args);

		//Colletion 또는 generic

//		AA a1 = new AA();
//		a1.setA("a11a11");
//		a1.setB(10);
//
//		AA a2 = new AA();
//		a1.setA("a11a11");
//		a1.setB(10);
//
//
//		List<AA> list = new ArrayList<>();
//		list.add(a1);
//		list.add(a1);
//
//		System.out.println(list);
//
//		BB<String, AA> bb = new BB<>();
//
//		bb.setT("T입니다");
//		bb.setK(a1);
//
//		System.out.println(bb);
	}

}

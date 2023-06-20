<%@ page import="java.util.Scanner" errorPage="error.jsp" %>

<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<!-- Jsp : Java Server Pages 
		html 파일 안에서 java 언어를 작성 할 수 있는게 바로 Jsp -> 수정이 용이하다
	-->

	<!--  html 주석 :: 화면에서는 안 나오고 소스 보기에서는 나온다 -->
	<%--jsp 주석 :: 화면에서는 안 나오고 소스 보기에서도 안 나온다 --%>
	
	<!-- 디렉티브(지시어) :: JSP 파일의 속성 지정 -->
	<%-- 1.페이지 지시어 현재 문서의 1~2문단 <%@ page %> --%>
	<%-- 2. include 지시어 :: <%@ include file="파일명" %> --%>
	<%-- 3. taglib 지시어 <%@ taglib %> --%>
	
	<!-- 스크립트 요소 :: html 파일에 java 코드 작성시 사용 -->
	<!-- 1. ::선언 태그-->
	<%!
		int n1=1;
		int n2=2;
	%>
	<!-- 2. 표현 태그 -->
	<h1>n1과 n2의 합은 <%=n1+n2 %></h1>
	<%--3. 이거 만능이라 함<% %> --%>
	<%
		int a; int b;
		System.out.println("a와 b를 선언했습니다");
		a=5;
		b=1;
		System.out.println("a와 b의 합은"+(a+b)+"입니다.");
		
	%>
</body>
</html>
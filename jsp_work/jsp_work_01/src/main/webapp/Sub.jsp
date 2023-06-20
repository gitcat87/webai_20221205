<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h2>Web 인공지능 1차반 명단</h2>
	<hr>
	<!-- 선언부 -->
	<%!
		String name[] = {"김성학","고연국", "박근형", "전미영", "장호성", "최대현"};
		String t = "이유나";
		
	%>
	<h3>담당교사 :<%=t %> </h3>
	<h3>학생 명단</h3>
	<ul> <%-- 학생 리스트 출력 --%>
		<% int i; 
		for(i=0;i<6;i++){ %>
			
			<li><%=name[i] %></li>
		
		<% } %>
	</ul>
</body>
</html>
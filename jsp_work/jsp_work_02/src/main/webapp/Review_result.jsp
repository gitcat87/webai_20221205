<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	request.setCharacterEncoding("UTF-8");
%>

<jsp:useBean id="emp" class="company.Employee" />
<jsp:setProperty name="emp" property="*" />

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>직원 정보 출력</title>
</head>
<body>
	<h1>입력하신 직원 정보입니다.</h1>
	<hr>
	
	<h3>
		이름: ${emp.getName()}		<br>
		나이: ${emp.getAge()}		<br>
		성별: <%=emp.getGender() %>	<br>
		업무: <%=emp.getWork() %>		<br>
		연봉: <jsp:getProperty name="emp" property="money" />만원
	</h3>
	
	<%-- jsp:forward 액션 태그 :: 표현되는 결과값 덮어쓰기 --%>
	<%-- jsp:param 액션 태그 :: forward/include 수행 시, 파라미터값 수정 --%>
	<jsp:forward page="welcome.jsp">
		<jsp:param name="name" value="LeeYuna" />
	</jsp:forward>
	
	
	<%-- include 지시어<%@ include %>는 파일의 모든 내용 포함 --%>
	<%-- include 액션 태그는, 표현되는 결과값만 포함 --%>
	<jsp:include page="welcome.jsp" />
</body>
</html>





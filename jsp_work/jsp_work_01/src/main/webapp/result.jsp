<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h1>계산기 프로그램</h1>
	<hr>
	<%
		//문자열로 입력받은 숫자 int형으로 파싱
		String cal = request.getParameter("cal");
		int num1 = Integer.parseInt(request.getParameter("num1"));
		int num2 = Integer.parseInt(request.getParameter("num2"));

		int plus = 0;	

		
		if(cal.equals("sum"))
		{
			plus = num1+ num2;
		}
		else if(cal.equals("min"))
		{			
			plus = num1 - num2;	
		}
		else if(cal.equals("div"))
		{
			plus = num1/num2;
		}
		else if(cal.equals("mul"))
		{
			plus = num1*num2;
		}
		else if(cal.equals("mod"))
		{
			plus = num1%num2;
		}
		else
		{
			out.println("먼저 연산할 옵션을 선택해 주세요");	
		}
	%>
	<%--if 도 써도 되는데 swtich(기준값)case "조건value": 연산식 break ;--%>
	<h3>수행 연산: <%= cal %></h3>
	<h3>연산 결과: <%= plus %></h3>
	<button onclick="location.href='input.html'">돌아가기</button>
	
</body>
</html>
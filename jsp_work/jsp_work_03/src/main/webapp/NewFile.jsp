<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%-- taglib 지시어 :: 사용자 정의 태그 --%>
    <%@ taglib prefix="tag" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<%-- Jstl 응용 문법 :: 변수 --%>
	<%-- <c:set/>변수 선언 prefix에 설정한 value값을 넣기 set은 변수를 선언하는 부분--%>
	<tag:set var="web" value="Web Ai 과정"/> <%-- 변수 이름을 설정 --%>
	<tag:out value="${web}" default="null 값입니다."/> <%-- 선언한 변수를 사용 출력부--%>
	<tag:remove var="web"/> <%-- 변수를 삭제 --%>
	<tag:out value="${web}"/> <%--remove가 정상적으로 작동 했으면 이 라인은 출력 되지 않는다. --%>	
	
	<%-- Jstl 응용 문법 :: 흐름 제어 --%>
	<tag:set var="gender" value="female"/>
	<tag:set var="age" value="40"/>
	<%-- c:if :: 조건문, else if 및 else 지원x --%>	
	<tag:if test="${gender=='female'}"> <%-- if문을 쓴다면 조건식인데 test속성을 사용한다 --%>
		<h3>해당 학생은 여성입니다.</h3>
	</tag:if>
	
	<tag:choose> <%-- if - else if - else 형식의 조건문 작성()  --%>
		<tag:when test="${gender=='female' && age>=20 && age<40}"> <%-- 조건문 필요로 하는 if, else if 사용 --%>
			<h2>해당 학생은 2030 여성지원 과정에 참여 가능합니다.</h2>
		</tag:when>
		<tag:otherwise> <%-- else와 같은 역할 --%>
			<h2>해당 학생은 대상자가 아닙니다.</h2>
		</tag:otherwise>

	</tag:choose>
	
			<%-- tag:forEach :: 반복문 역할 --%>
			<tag:set var="array" value="${[100,200,300,400,500]}" />
			<tag:forEach var="arr" items="${array}" varStatus="i">
				<h3>${i.index}번째 값은 ${arr}</h3>
			</tag:forEach>
	
			<%-- tag:forTokens:: --%>
		<tag:forTokens var="student" items="김성학,고연국,박근형,장호성,전미영,최대현" delims="," varStatus="i">
			${student}			
		</tag:forTokens>
</body>
</html>
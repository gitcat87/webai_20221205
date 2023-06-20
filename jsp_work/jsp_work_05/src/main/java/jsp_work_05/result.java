package jsp_work_05;

import jsp_work_05.user;
import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class result
 */
@WebServlet("/result")
public class result extends HttpServlet {
	private static final long serialVersionUID = 1L;

    /**
     * Default constructor. 
     */
    public result() {
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		response.getWriter().append("Served at: ").append(request.getContextPath());
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html;charset=UTF-8");
		request.setCharacterEncoding("utf-8");
		
		String name=request.getParameter("name");
		int age=Integer.parseInt(request.getParameter("age"));
		String gender=request.getParameter("gender");
		String tel=request.getParameter("tel");
		String email=request.getParameter("email");
		
		user u = new user(name, age, gender, tel, email);
		
		
		PrintWriter pw=response.getWriter();
		pw.println("<!doctype html><html><head meta charset=utf-8></head><body>");
		pw.println("<p>이름: "+u.getName()+"<br>나이: "+u.getAge()+"<br>성별: "+u.getGender());
		pw.println("<br>전화번호: "+u.getTel()+"<br>이메일: "+u.getEmail()+"</p><br>");
		
		if(u.Teenager()==true) {
			pw.println("<p>해당 사용자는 미성년자입니다.</p>");
		}
		if(u.Teenager()==false) {
			pw.println("<p>해당 사용자는 미성년자가 아닙니다.</p>");
		}
		
		pw.println("</body></html>");
	}
	//서블릿 생성 될때 자동으로 수행
	public void init() {
		System.out.println("init 실행");
	}
	//서블릿이 사용자의 요청을 처리할 때 자동으로 수행
	public void service() {
		System.out.println("service 실행");
	}
	//서블릿이 소멸 될때 자동으로 수행
	public void destroy() {
		System.out.println("destroy 실행");
	}
}

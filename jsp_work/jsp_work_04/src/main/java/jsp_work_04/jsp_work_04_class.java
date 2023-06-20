package jsp_work_04;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import java.io.PrintWriter;

class student{
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getAge() {
		return age;
	}
	public void setAge(String age) {
		this.age = age;
	}
	public String getGender() {
		return gender;
	}
	public void setGender(String gender) {
		this.gender = gender;
	}
	private String name;
	private String age;
	private String gender;	
	
	public student(String n, String a, String g) {
		this.name=n;
		this.age=a;
		this.gender=g;
	}
}


/**
 * Servlet implementation class jsp_work_04_class
 */
@WebServlet("/hello")
public class jsp_work_04_class extends HttpServlet {
	private static final long serialVersionUID = 1L;

    /**
     * Default constructor. 
     */
    public jsp_work_04_class() {
    	super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		System.out.println("success~~~~");
		
		response.setContentType("text/html; charset=UTF-8");
		PrintWriter pw=response.getWriter();
		pw.println("<doctype html><html><head>");
		pw.println("<title>hello!!!</title></head>");
		pw.println("<body><h1>HellowWorld!!");
		pw.println("</body></html>");
		
		pw.close();
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html; charset=utf-8");
		PrintWriter pw=response.getWriter();
		
		pw.println("<!doctype html><html><head></head><body>");
		
		String name=request.getParameter("name");
		String age=request.getParameter("age");
		
		String gender=request.getParameter("gender");
		student st= new student(name, age, gender);
		if(name==""||age==""||gender==null) {
			pw.println("<h3>입력받지 않은 항목이 있습니다. 다시 실행해주세요.</h3>");
			
		}
		else {
			pw.println("<h3>이름: "+st.getName()+"<br>나이 "+st.getAge()+"<br>성별 "+
					st.getGender()+"</h3>");
		}
		
		// 학생 클래스에 대한 객체 생성 완료
		
		
		
		
		
		pw.println("</h3></body></html>");
		
		System.out.println("End of Program");
	}

}

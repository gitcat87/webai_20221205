package Login;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebInitParam;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


/**
 * Servlet implementation class Login
 */
@WebServlet(urlPatterns ={"/login"},initParams= 
		{@WebInitParam(name="id",value="lyn99730"),
		@WebInitParam(name="password",value="qwer1234")})
		
		
public class Login extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Login() {
        super();
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
		
		request.setCharacterEncoding("utf-8");
		// 사용자가 입력한 아이디 비번
		String id_input=request.getParameter("id");
		String pw_input=request.getParameter("pw");
		
		// 서버 상에 저장된 아이디 비번
		String id_server = getInitParameter("id");
		String pw_server = getInitParameter("password");
		
		response.setContentType("text/html; charset=utf-8");
		PrintWriter print = response.getWriter();
		print.println("<!doctype html><html><head></head><body>");
		if(id_input.equals(id_server) && pw_input.equals(pw_server)) {
			print.println("<h1>환영합니다, "+id_input+"님ㅋ</h1>");
		}
		else {
			print.println("<h2>아이디와 비밀번호가 올바르지 않습니다.</h2>");
		}
		print.println("<h1>입력받은 아이디 :"+id_input+"</h1>");
		print.println("<h1>입력받은 패스워드 :"+pw_input+"</h1>");
		
		print.println("<h1>서버상의 아이디 :"+id_server+"</h1>");
		print.println("<h1>서버상의 패스워드 :"+pw_server+"</h1>");
		print.println("</body></html>");
	}

}

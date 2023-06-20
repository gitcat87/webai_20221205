package login;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebInitParam;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class login
 */
//@WebServlet(urlPatterns= {"/login"},
//	initParams= {@WebInitParam(name="id",value="lyn99730"),
//			@WebInitParam(name="pw", value="qwer1234")})	
//	

@WebServlet("/login")
public class login extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public login() {
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
		
		String id_in=request.getParameter("id");
		String pw_in=request.getParameter("pw");
		String id_sv=getServletContext().getInitParameter("id");
		String pw_sv=getServletContext().getInitParameter("pw");
		
		response.setContentType("text/html;charset=utf-8");
		PrintWriter pw=response.getWriter();
		pw.println("<!doctype html><html><head></head><body>");
		if(id_in.equals(id_sv) && pw_in.equals(pw_sv)) {
			pw.println("<h3>환영합니다!!!</h3>");
		}
		else {
			pw.println("<h3>아이디와 비밀번호가 일치하지 않습니다.</h3>");
		}
		pw.println("</body></html>");
	}

}

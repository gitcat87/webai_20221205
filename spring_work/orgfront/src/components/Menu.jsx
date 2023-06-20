import { Button, Box, rgbToHex } from '@mui/material';
import { useNavigate } from 'react-router-dom';



const Menu = (props) => {
    const navigate = useNavigate();
    return (
      <Box
        variant="body2"
        color="text.secondary"
        align="center"
        {...props}
      >
        <Button
          type="submit"
          variant="contained"
          sx={{
            mr: 1,
            width: "22%",            
              backgroundColor: rgbToHex("#3B4890"),
              whiteSpace:"nowrap"
            
          }}
          onClick={() => {
            navigate("/vaform");
                }}
               
        >
          휴가계작성
        </Button>
        <Button
          type="submit"
          variant="contained"
          sx={{
            mr: 1,
            width: "22%",
            whiteSpace:"nowrap",
            backgroundColor: rgbToHex("#3B4890"),
          }}
          onClick={() => {
            navigate("/valist");
          }}
        >
          휴가계목록
        </Button>
        <Button
          type="submit"
          variant="contained"
          sx={{
            mr: 1,
            width: "22%",

            backgroundColor: rgbToHex("#3B4890"),
          }}
          onClick={() => {
            navigate("/board");
          }}
        >
          게시판
        </Button>
        <Button
          type="submit"
          variant="contained"
          sx={{
            mr: 1,
            width: "22%",

            backgroundColor: rgbToHex("#3B4890"),
          }}
          onClick={() => {
            navigate("/member");
          }}
        >
          회원관리
        </Button>
      </Box>
    );
}
 
export default Menu;
import * as React from "react";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import Link from "@mui/material/Link";
import Paper from "@mui/material/Paper";
import Box from "@mui/material/Box";
import Grid from "@mui/material/Grid";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";
import { createTheme, hexToRgb, hslToRgb, rgbToHex, ThemeProvider } from "@mui/material/styles";

import { useNavigate } from "react-router-dom";
import { red } from "@mui/material/colors";


function Copyright(props) {
  return (
    <Typography
      variant="body2"
      color="text.secondary"
      align="center"
      {...props}
    >
      {"Copyright © "}
      <Link color="inherit" href="https://mui.com/">
        Your Website
      </Link>{" "}
      {new Date().getFullYear()}
      {"."}
    </Typography>
  );
}

// TODO remove, this demo shouldn't need to reset the theme.

const defaultTheme = createTheme();

export default function Main() {
  const navigate = useNavigate();

  const handleSubmit = event => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    console.log({
      email: data.get("email"),
      password: data.get("password"),
    });
    navigate("main");
  };

  return (
    <ThemeProvider theme={defaultTheme}>
      <Grid container component="main" sx={{ height: "100vh" }}>
        <CssBaseline />
        <Grid
          item
          xs={false}
          sm={4}
          md={7}
          sx={{
            backgroundImage:
              "url(https://source.unsplash.com/random?wallpapers)",
            backgroundRepeat: "no-repeat",
            backgroundColor: t =>
              t.palette.mode === "light"
                ? t.palette.grey[50]
                : t.palette.grey[900],
            backgroundSize: "cover",
            backgroundPosition: "center",
          }}
        />
        <Grid
          item
          xs={12}
          sm={8}
          md={5}
          component={Paper}
          elevation={6}
          square
          sx={{ backgroundColor: "rgba(0,0,0,0.1)" }}
        >
          <Box
            sx={{
              my: 8,
              mx: 4,
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
            }}
          >
            <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
              <LockOutlinedIcon />
            </Avatar>
            <Typography component="h1" variant="h5">
              Main
            </Typography>
            <Box noValidate sx={{ mt: 1 }}>
              <Button
                type="submit"
                variant="contained"
                sx={{
                  mt: 3,
                  mb: 2,
                  mr: 3,
                  width: "45%",
                  height: "151.8px",
                  backgroundColor: rgbToHex("#3B4890"),
                }}
                onClick={() => {
                  navigate("/vaform");
                }}
              >
                휴가계 작성
              </Button>
              <Button
                type="submit"
                variant="contained"
                sx={{
                  mt: 3,
                  mb: 2,
                  width: "45%",
                  height: "151.8px",
                  backgroundColor: rgbToHex("#3B4890"),
                }}
                onClick={() => {
                  navigate("/valist");
                }}
              >
                휴가계 리스트
              </Button>
              <Button
                type="submit"
                variant="contained"
                sx={{
                  mt: 3,
                  mb: 2,
                  mr: 3,
                  width: "45%",
                  height: "151.8px",
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
                  mt: 3,
                  mb: 2,
                  width: "45%",
                  height: "151.8px",
                  backgroundColor: rgbToHex("#3B4890"),
                }}
                onClick={() => {
                  navigate("/member");
                }}
              >
                회원관리
              </Button>

          
            </Box>
          </Box>
        </Grid>
      </Grid>
    </ThemeProvider>
  );
}

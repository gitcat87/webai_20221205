const express = require('express');

const router = express.Router();

router.get("/", (req, res) => {
  const users = "아잉 유저";
  res.render("users", { users });
});


module.exports = router;
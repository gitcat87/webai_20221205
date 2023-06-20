const express = require('express');
const { User } = require('../models');
const router = express.Router();

router.get("/", async(req, res) => {
  const users = await User.findAll();
  res.render("sequelize", { users });
});

router.get("/index", async (req, res) => {
  const users = await User.findAll();
  res.render("index", { users });
});



module.exports = router;
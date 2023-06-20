const express = require('express')

const router = express.Router();

router.get('/', (req, res) => {
    const users = "commnets 유저";
    res.render("users", { users });
})

module.exports = router;
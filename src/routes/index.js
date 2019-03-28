const express = require('express');
const bodyParser = require('body-parser');
const router = express.Router();

const account = require('../accounts');

  app.use(bodyParser.json());
  app.use(bodyParser.urlencoded({ extended: true }));

/* GET home page. */
router.get('/', function(req, res, next) {
  // res.render('index', res.locals.commonData);
  console.log("router js works")
});

module.exports = router;
const express = require('express');
const bodyParser = require('body-parser');
const router = express.Router();

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

/* GET home page. */
app.get('/', (req, res) => {
  // res.render('ussd', res.locals.commonData);
  res.render('ussd');
});

module.exports = router;
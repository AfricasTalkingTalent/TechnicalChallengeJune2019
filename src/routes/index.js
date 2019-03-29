const express = require('express');
const bodyParser = require('body-parser');
const router = express.Router();

const app = express();


app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

/* GET home page. */
router.get('/', (req, res) => {
  res.render('ussd');
});

router.post('/', (req, res) => {
  menu(req).run(req.body, ussdResult => {
    res.send(ussdResult);
  });
});

module.exports = router;
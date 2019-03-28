
var express = require('express');
var router = express.Router();

// index route
router.get('/', function(req, res){
  res.render('home', {
    title: 'Home'
  });
});

// login route
// router.get('./login', function(req, res){
//   res.render('login', {
//     title: 'Login'
//   });
// });

router.get('/', function(req, res, next) {
  if (req.session.loggedIn === true) {
      res.render('index', {
        title: 'Home'
      });
  } else {
      res.redirect('/login');
  }
});

router.get('/login', function(req, res, next) {
  if (req.session.loggedIn === true) {
      res.redirect('/');
  } else {
      res.render('login', {
          title: 'Login'
      });
  }
});

// Process login form
router.post('/login', function(req, res) {
  var username = req.body.username;
  var email = req.body.email;

  if (username === CONFIG_USERNAME && email === CONFIG_EMAIL) {
      res.redirect('/');
  } else {
      res.redirect('/login');
  }
});
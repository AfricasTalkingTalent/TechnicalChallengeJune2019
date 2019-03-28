// load the npm modules
var express = require('express');
var path = require('path');
var exphbs = require('express-handlebars');

import routes from './src/routes';

// create the server
var app = express();

// set the views
app.set('views', path.join(__dirname, 'views'));
app.engine('handlebars', exphbs({defaultLayout: 'main'}));
app.set('view engine', 'handlebars');

// create the homepage route
app.get('/', (req, res) => {
  res.render('register');
});

// tell the server what port to listen on
app.set('port', (process.env.PORT || 3000));
app.listen(app.get(PORT), () => {
  console.log('Listening on port ' + app.get('port'));
})
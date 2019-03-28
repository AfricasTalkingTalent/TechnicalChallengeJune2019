// import npm modules
const express = require('express');

const routes = require('./routes/index');

const app = express(); // initialize the app

const router = express.Router();

// tell the server what port to listen on
const port = process.env.PORT || 3000;
// app.set('port', (port);
app.set('port', port);
app.listen(app.get('port'), () => {
  console.log('Listening on port ' + app.get('port'));
})

module.exports = router;
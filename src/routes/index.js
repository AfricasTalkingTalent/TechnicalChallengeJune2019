const express = require('express');
const bodyParser = require('body-parser');

const account = require('../accounts');

const routes = app => {
  app.use(bodyParser.json());
  app.use(bodyParser.urlencoded({ extended: true }));

  const router = express.Router();

  app.post('/', (req, res) => {
    account(req).run(req.body, ussdResult => {
      res.send(ussdResult);
    });
  });
  return router;
};

return routes;
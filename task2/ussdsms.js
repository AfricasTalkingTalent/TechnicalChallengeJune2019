const express = require("express");
const http = require("http");
const morgan = require("morgan");
const bodyParser = require("body-parser");

const app = express();
const creds = {
  apiKey: "81e96d14fe55fe44ca8b82dad9fd4c98ffd3ac7d6ce0418fc94186c0ecb740a9",
  username: "sandbox"
};
const AT = require("africastalking")(creds);
const sms = AT.SMS;
app.use(morgan("dev"));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get("*", (req, res) => {
  res.send("USSD App with nodejs");
});

app.post("*", (req, res) => {
  // message to be sent
  const message = "Successfully registered";
  // an array storing phone numbers
  const phoneNumbers = ["+254797240975"];
  const opts = {
    to: phoneNumbers,
    message
  };
  let { sessionId, serviceCode, text } = req.body;
  if (text == "") {
    // This is the first request. Note how we start the response with CON
    let res1 = `CON Enter your email`;
    res.send(res1);
  } else if (typeof text === "string") {
    // Request for username
    let res2 = `CON Enter Username`;
    res.send(res2);
  } else if (typeof text === "string") {
    // Sends a sms after registration
    sms
      .send(opts)
      .then(info => {
        res.json(info);
      })
      .catch(err => console.log(err));
  } else {
    res.status(400).send("Bad request!");
  }
});

// creating a local server
const server = http.createServer(app);
const port = 5000;

server.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

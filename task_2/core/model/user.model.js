const mongoose = require('mongoose');

module.exports = class User{

  constructor(username,emailAddress){
      this._id = new mongoose.Types.ObjectId;
      this.username = username;
      this.emailAddress = emailAddress;
  }

};
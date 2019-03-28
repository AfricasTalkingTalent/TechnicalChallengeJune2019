const mongoose = require('mongoose');

const userSchema = mongoose.Schema({
    _id: mongoose.Schema.Types.ObjectId,
    username: {type: String, required: true},
    emailAddress: {type: String, required: true}
},{timestamps:true})

module.exports = mongoose.model('Users',userSchema);
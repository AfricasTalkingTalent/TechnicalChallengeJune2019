const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const cors = require('cors');
const morgan = require('morgan');
require('dotenv').config();
const routes = require('./core/routes/index')
const mongoose = require('mongoose')

app.use(function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers",
        "Origin, X-Requested-With, Content-Type, Accept, Authorization");

    if (req.method === "OPTIONS") {
        res.header('Access-Control-Allow-Methods', 'POST, GET');
        return res.status(200).json({});
    }
    next();
});

mongoose.connect(process.env.MONGO_ATLAS_URL,{useNewUrlParser:true},(err)=>{
    if(!err){
        console.log('You have been connected successfully to MongoDB');

    }else{
        console.log('Error Loading Connection',err.message);
    }
});


app.use(morgan('dev'));
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());
app.use(cors());
app.use('/api/v1',routes);


app.use((req, res, next) => {
    const error = new Error('Route Not Found');
    error.status = 404;
    next(error);
    return res.status(404).send({
        message: 'Route Not Found'
    })
});

app.use((err, req, res) => {
    res.status(err.status || 500);
    res.json({
        err: {
            message: err.message
        }
    })
});


module.exports = app;
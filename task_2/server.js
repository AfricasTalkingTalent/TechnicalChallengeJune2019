const http = require('http');
const app = require('./app');
const port = process.env.PORT || 3000
const server = http.createServer(app);

let createServer = async () => {
    try{
        await server.listen(port);
        console.log("Server Running on Port ", port);
    } catch (e) {
        console.log("Error Creating Server",e.message);
    }
};

createServer();


module.exports = server;
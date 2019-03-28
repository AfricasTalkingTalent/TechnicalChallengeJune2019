const Extractor = require('./extractor')
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});
let extractor = new Extractor();

readline.question('Enter File Directory to Search',(directory)=>{
    let filepath = directory
    readline.question('Enter String to Query',(stringQuery)=>{
        extractor.searchFileDirectory(filepath,stringQuery)
    })
})



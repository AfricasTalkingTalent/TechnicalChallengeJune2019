var http = require('http');

const path = require('path');
const fs = require('fs');


//dir parameter is for directory path

function searchFilesInDirectory(dir , ext) {
    let filter = 'a';

    if (!fs.existsSync(dir)) {
        console.log(`Specified directory: ${dir} does not exist`);
        return;
    }

    const files = fs.readdirSync(dir);
    const found = getFilesInDirectory(dir, ext);

    found.forEach(file => {
        const fileContent = fs.readFileSync(file);

        
        // We want full words, so we use full word boundary in regex.
        const regex = new RegExp(filter);
        if (regex.test(fileContent)) {
            console.log(`Letter a is found in the following: ${file}`);
        }
    });
}

// Using recursion, we find every file with the desired extention, even if its deeply nested in subfolders.
function getFilesInDirectory(dir, ext) {
    if (!fs.existsSync(dir)) {
        console.log(`Specified directory: ${dir} does not exist`);
        return;
    }

    let files = [];
    fs.readdirSync(dir).forEach(file => {
        const filePath = path.join(dir, file);
        const stat = fs.lstatSync(filePath);

        // If we hit a directory, apply our function to that dir. If we hit a file, add it to the array of files.
        if (stat.isDirectory()) {
            const nestedFiles = getFilesInDirectory(filePath, ext);
            files = files.concat(nestedFiles);
        } else {
            if (path.extname(file) === ext) {
                files.push(filePath);
            }
        }
    });

    return files;
}

//call the function searchFilesInDirectory and pass the first argument as a path to the directory containing files and second argument as extension of the files
let result = searchFilesInDirectory('/home','.txt');

console.log(result);
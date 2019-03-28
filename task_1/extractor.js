const path = require('path')
const fs = require('fs')

//const directoryToFiles = path.join(__dirname,'files');

module.exports = class Extractor {

    //Abstract a function to include a file Directory and the Search String

    searchFileDirectory(fileDirectory,searchString){
        let directoryToFiles = path.join(__dirname,`${fileDirectory}`) // Construct Directory

        fs.readdir(directoryToFiles,function(err,fetchedFiles){
            if(err){
                console.error("Error Loading File Directory"+err)
                return
            }
            fetchedFiles.forEach(function(individualFile){
                console.log(individualFile)
                let renamedDirectory = path.join(__dirname,`${fileDirectory}/${individualFile}`) // Reconstruct the directory path upon each file

                fs.readFile(renamedDirectory,function (err,fetchedData) { //Read Individual File
                    if(err) {
                        console.error("Error Loading File"+err)
                        return
                    }
                    const data = fetchedData.toString() // Convert Buffered Data to String
                    if(data.includes(`${searchString}`)){ // Search for String
                        console.log(`The Letter ${searchString} has been found in ${renamedDirectory}`)


                        //Show on which directory that letter has been found

                    }else if(!data.includes(`${searchString}`)){
                        console.log(`The letter ${searchString} has not been found in ${renamedDirectory}`)


                        //Show on which directory letter has not been found
                    }
                })
            })

        })
    }
};


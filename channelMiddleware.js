const spawn = require('child_process').spawn;
const fs = require('fs');
const multer = require('multer');
const upload = multer({ dest: 'uploads/' })
const channel = (req, res, next) =>{
    const process = spawn('python', ['./imageChanneler.py', req.file.filename]);
    process.stdout.on('data',(data)=>{
        console.log(data.toString());
    })
    next();
}
module.exports = channel;
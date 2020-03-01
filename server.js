const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const hbs = require('hbs');//adding template engine
const multer = require('multer');//file uploading helper
const app = express();

// configuration for file upload
const storage = multer.diskStorage({
    destination: function (req, file, cb) {
      cb(null, 'uploads')
    },
    filename: function (req, file, cb) {
      cb(null,  file.filename + '.jpg');
    }
  })
const upload = multer({ storage:storage });

//middleware for channeling image
const middleware = require('./channelMiddleware');

//view engine configuration for templating
app.set('view engine', 'hbs');
app.use(express.static(path.join(__dirname, './views')));

const PORT = process.env.PORT || 3000;

app.get('/', (req, res) =>{
    res.render('index')
})

app.post('/channel',upload.single('image'), middleware, (req, res) =>{
    res.render('channel');
})

app.listen(PORT, function(){
    console.log('successful!!!')
})
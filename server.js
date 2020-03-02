const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const spawn = require('child_process').spawn;
const hbs = require('hbs');//adding template engine
const multer = require('multer');//file uploading helper
const app = express();
// configuration for file upload
const storage = multer.diskStorage({
    destination: function (req, file, cb) {
      cb(null, 'views/uploads')
    },
    filename: function (req, file, cb) {
      cb(null, 'image.jpg');
    }
  })
const upload = multer({ storage:storage });


//view engine configuration for templating
app.set('view engine', 'hbs');
app.use(express.static(path.join(__dirname, './views')));

const PORT = process.env.PORT || 3000;

app.get('/', (req, res) =>{
    res.render('index')
})

app.post('/channel', upload.single('image'), (req, res) =>{
      const process = spawn('python' ,['./imageChanneler.py']);
      process.stdout.on('end',(err, data)=>{
        res.render('channel');
      })
})
app.get('/merge', (req, res)=>{
  const process = spawn('python', ['./mergeChannel.py']);
  process.stdout.on('end', (err, data)=>{
    res.render('merge')
  })
})
app.listen(PORT, function(){
    console.log('successful!!!')
})
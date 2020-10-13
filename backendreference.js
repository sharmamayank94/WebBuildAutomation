var express = require('express');
var ejs = require('ejs');

var app = express();

app.use('/public', express.static("static"));
app.set('view engine', 'ejs')

app.get('/', (req, res)=>{
	res.render('home.ejs');
});

app.listen(3000, (a, b)=>{
	console.log("Listening");
});
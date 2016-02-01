var express    = require('express');        
var app        = express();                 
var upload = require('./upload.js');
var spawn = require('child_process').spawn;
var child;
var uploadFile = upload.uploadFile;
var response; 

var sys = require('sys')
var exec = require('child_process').exec;
var child;
var Bing = require('node-bing-api')({ accKey: "fJa9Rz0oU9/2O+Nq6tL9wZN8EZPhqf7lWO72SFTzom4" });

var port = 8080;        // set our port


function postImage(req, res) {

	var imgUrl = req["file"]["path"]
	var img_content;

	console.log("image url is", imgUrl);
	
//get words from the image
	var command = "python python/pytesseract.py -f /home/ec2-user/hackrice2016/"+imgUrl+" -t /usr/local/bin/tesseract"
	
	console.log("command "+command)

	child = exec(command, function(error, stdout, stderr) {
		sys.print('stdout: '+stdout);
		sys.print('stderr: '+stderr);
		//setTimeout(function() {
		console.log("waiting to print");
		img_content = stdout
		console.log(error)
		if (error !== null) {
			console.log('exec');
		}

		console.log(img_content);
		//get image url
		if (img_content){
			Bing.images(img_content, {skip: 50}, function(error, result, body) {
				if (typeof body["d"]["results"][0] !== "undefined") {
					response = body["d"]["results"][0]["MediaUrl"].toString();
					console.log(response);
					res.send({result:"success", imageUrl: response});
				} else {
					res.send({result:"error", imageUrl: null});
				}
			});
		} else {
			console.log("no img content received")
		}
	}); // end of exec()
}

function getSample(req, res) {
	console.log("console test");
	res.send("Test get");
}

app.get('/sample', getSample);


app.get('/test', postImage)
app.post('/image', uploadFile('post'), postImage);




app.listen(port);
console.log('Server on port ' + port);

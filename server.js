var request = require('request');
for(var i = 0; i <= 20; i++)
{
	request('http://10.0.12.128/temp', function (error, response, body) {
    	if (!error && response.statusCode == 200) {
        	console.log(body) 
     	}
	})

	request('http://10.0.12.128/humidity', function (error, response, body) {
    	if (!error && response.statusCode == 200) {
        	console.log(body) 
     	}
	})
}




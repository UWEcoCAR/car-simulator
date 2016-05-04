/* Simple subscriber testing */

var zmq = require('zmq');
var subscriber = zmq.socket('sub');
var myMap = [];
subscriber.on('message', queue_message);

function queue_message() {
	var msg = Array.prototype.slice.call(arguments).toString();
	var data = msg.split("= ");
	var parsedData = JSON.parse(data[1].trim());

	console.log(msg);


}



subscriber.connect('tcp://localhost:8690');
subscriber.subscribe('simulator=');

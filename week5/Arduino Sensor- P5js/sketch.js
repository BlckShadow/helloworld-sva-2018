var serial; // variable to hold an instance of the serialport library  // fill in your serial port name here
var sensorValue = 0;		// ellipse position
var col;

function setup() {
  col = color(255,0,0);
  createCanvas(500, 500);
  serial = new p5.SerialPort();  // make a new instance of  serialport library
// serial.on('list', printList);  // callback function for serialport list event
  serial.on('data', serialEvent);// callback for new data coming in
	serial.list();                         // list the serial ports
	serial.open("/dev/cu.usbserial-DN050GX");
	//serial.onData(gotData); // open a port
}

function draw() {
  background(col);
	fill(255);
	ellipse(sensorValue, height/10, 20, 20);
  text(sensorValue, 20, 20);
}

function gotData(data){
	println(data);
}

// get the list of ports:
function printList(portList) {
 for (var i = 0; i < portList.length; i++) {
	// Display the list the console:
 	println(i + " " + portList[i]);
 }
}

function serialEvent() {
	var inString = serial.readLine();
	if (inString.length > 0) {
	  inString = inString.trim();
		sensorValue = Number(inString/4);
		
		//if (sensorValue != null){
     //println(sensorValue);
		//}
	}
  
  if (sensorValue > 10 ) {
  	col = color(255,255,12);
  } else {
	  col = color(0,0,0);
	}
  
}
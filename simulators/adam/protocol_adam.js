'use strict';

const DataSamplingInterval = 5000; //5sec sampling interval
const interfacePort = require('./interface_serial');

let dataPacket = {};

/*
//cmd to be sent : '#01'
//sample data response
>+05.118+05.405+18.313+00.003+00.004+00.004+00.003+00.003



*/

const validateAndParseRawData = (data, config) => {
	data = data.split( '#' ); //remove intial garbage data received before the header.
	//console.log(data);
	if(data.length >= 2 ){
		data = data[1];
		//console.log(data);
	}else{
		data = "";
	}
	//console.log(data);
	
	let flag = false;
	if( data != ""  ) { 
	    //console.log(data.split(' '));
		
		//console.log(temp);
		if(data.length >= 1 ) {
			flag = true;
		}
		
	}
	return {raw_data:data, status:flag};
};

const prepareDataPacket = ( data, configuration, portName) => {
	let parameterDetails = [];

	if(  configuration.p_dt != undefined ){
		parameterDetails = configuration.p_dt;
	}
	let dataPacket = {};
	if(data == '') {
		console.log('#Error : No Command received!!!');
	}else{
		
		let dataPacket = '>+05.118+05.405+18.313+00.003+00.004+00.004+00.003+00.003';
		let comport =  interfacePort.getConnectionHandle(portName);
		comport.write(dataPacket, function(err) {
			if (err) {
				return console.log('Error on write: ', err.message);
			}
			console.log('Data Sent : ', dataPacket);
		});
	}
	return dataPacket;
}

const readData = async (configuration)=>{
	dataPacket = {};
	
	try{
		let timeout = DataSamplingInterval;
		let portName = '',
			deviceId = 1;
	    console.log('Openning comport...');
	    let stationDetails = {};
	    
	    if(configuration.s_dt != undefined){
	    	stationDetails = configuration.s_dt; //"COM3"
	    	if(configuration.s_dt.timeout != undefined){
		    	timeout = configuration.s_dt.timeout;
			}
			if(configuration.s_dt.serial_no != undefined){
				portName = configuration.s_dt.serial_no;
			}
			if(!isNaN(parseInt(configuration.s_dt.device_id))){
		    	deviceId = configuration.s_dt.device_id;
			}
	    }
	    
	    //check if comport is already connected or not
	    let comport = await interfacePort.initializeConnection(configuration);

		console.log("----------------");
		let data = await interfacePort.readRawData( timeout, validateAndParseRawData, portName);
	    console.log(`Data Received from COM : ${data}`);
		    
	    if(data != "" && data != undefined ) {
			dataPacket = prepareDataPacket(data, configuration, portName);
		}


	}catch(err){
		console.log('#Error : Exception -> ', err);
	}
    return 0;
}

module.exports = {
	validateAndParseRawData: validateAndParseRawData,
	prepareDataPacket: prepareDataPacket,
    readData: readData
}




      
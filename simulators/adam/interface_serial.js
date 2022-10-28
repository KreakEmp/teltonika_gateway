'use strict';

const DataSamplingInterval = 5000; //5sec sampling interval
const SerialPort = require('serialport');

const moment = require('moment-timezone');

let connectionPool = {};
//let connectionPoolDetails = {};
let connectionBuffer = {};
let gvComportData = '';
let serialPortCommandQueue = {};
let connectionStatus = {};

const initializeConnection = (config)=>{
	return new Promise( (resolve, reject)=> {
	     //initialize comport & raw serial logger for corresponding station if the same com port is not initialized already
		//console.log(' config : ', JSON.stringify(config));
		let portName = '';
		let comportConfig = {
			baudRate: 9600,
			dataBits: 8,
			parity: 'none',
			stopBits: 1
		};
	    if(config.s_dt != undefined ){
			if(config.s_dt.serial_no != undefined){
				let parityTypes = ['none', 'even', 'mark', 'odd', 'space'];
				let stopbitTypes = [1, 1.5, 2];
				let databitTypes = [5,6,7,8];
				portName = config.s_dt.serial_no;
				if(config.s_dt.stop_bit != undefined ){
					comportConfig.baudRate = parseInt(config.s_dt.baud_rate);
				}
				if(config.s_dt.stop_bit != undefined && stopbitTypes.includes(config.s_dt.stop_bit) == true ){
					comportConfig.stopBits = config.s_dt.stop_bit;
				}
				if(config.s_dt.data_bits != undefined && databitTypes.includes(config.s_dt.data_bit) == true){
					comportConfig.dataBits = config.s_dt.data_bit;
				}
				if(config.s_dt.parity != undefined &&  parityTypes.includes(config.s_dt.parity) == true ){
					comportConfig.parity = config.s_dt.parity;
				}

	    	}
	    }
	    else {
	    	// console.log('#Error: COM port details not provided in correctly');
	    	reject("Incorrect COM port");
	    }

	    let comport;
	    if(connectionPool != undefined && connectionPool[portName] == undefined) {
	        console.log(' comport : ' + portName);
	        comport = new SerialPort(portName, comportConfig, (err) => {
            console.log("here inside comport create");
		        if(err) {
		            console.log('#Error opening port: ', err);
		            reject("Error Opening COM port: "+portName);
		        } else {
              console.log("connected comport", portName);
		            // console.log('Listening for data on port');
		            //add comport to already initialized comport list
					connectionPool[portName] = comport;
					connectionBuffer[portName] = '';
		            resolve(connectionPool[portName]);
		        }
		    });

	     	comport.on('data', (data) => {
                connectionBuffer[portName] = connectionBuffer[portName] + data.toString();
                if(connectionBuffer[portName].length > 1000000){ //if buffer size is more than 1mb then clear buffer
                    connectionBuffer[portName] = '';
                }
	            //let rawSerialLog = '[Time: '+ moment.tz('Asia/Kolkata').format('DD MMM YYYY, HH:mm:ss') +'][Port: '+ portName +'] '+ gvComportData;
	            //rawSerialLogger.info(rawSerialLog);
	            //console.log(gvComportData);
	        });
	        comport.on('close', () => {
	            console.log('Comport closed -> ', portName);
				delete connectionPool[portName];
				delete connectionBuffer[portName];
	        });
	        comport.on('error', () => {
	            // console.log('#Error occurred in Comport -> ', portName);
	            comport.close();
				delete connectionPool[portName];
				delete connectionBuffer[portName];
	        });
	        comport.on('disconnect', (data) => {
	            console.log('Comport disconnected -> ', portName);
				delete connectionPool[portName];
				delete connectionBuffer[portName];
	        });
	    }else{
	    	resolve(connectionPool[portName]);
	    }
    });
}


const readRawData = ( timeout, validateAndParseRawData, portName, config = '')=>{
	return new Promise((resolve)=>{
		let data = '';
	    const handler = setInterval(()=>{
            data = validateAndParseRawData(connectionBuffer[portName], config);
            if( data.status == true){
				connectionBuffer[portName] = '';
				clearInterval(handler);
			    resolve(data.raw_data);
		    }
	    }, 100);
        setTimeout(()=>{
            clearInterval(handler);
            resolve(data.raw_data);
        }, timeout);

    });
};

const clearSerialBuffer = (portName)=> {
	connectionBuffer[portName] = '';
}
const getSerialBuffer = (portName)=> {
	return connectionBuffer[portName];
}
const getConnectionHandle = (portName) => {
	return connectionPool[portName];
};

const closeConnectionByPort = (portName) => {
  const comport = connectionPool[portName];
  delete connectionPool[portName];
  delete connectionBuffer[portName];
  comport.close();
}

const closeConnections = (portName = null) => {
  if(portName){
    closeConnectionByPort(portName);
  }else{
    for(let portName of Object.keys(connectionPool)){
      closeConnectionByPort(portName);
    }
  }
}
const setConnectionStatus = (portName, status) => {
  connectionStatus[portName] = status;
}
const getConnectionStatus = (portName) => {
  return connectionStatus[portName];
}
const pushToCommandQueue = (portName, cmd) => {
  // console.log("data to be pushed", cmd);
  if(!serialPortCommandQueue[portName]) serialPortCommandQueue[portName] = [];
  serialPortCommandQueue[portName].push(cmd);
}
const processCommandQueue = async (portName, executor) => {
  if(!serialPortCommandQueue[portName] || !serialPortCommandQueue[portName].length || getConnectionStatus(portName)) return;
  let stage = serialPortCommandQueue[portName][0];
 
}
module.exports = {
  initializeConnection: initializeConnection,
	readRawData: readRawData,
	clearSerialBuffer : clearSerialBuffer,
	getSerialBuffer: getSerialBuffer,
	getConnectionHandle: getConnectionHandle,
  closeConnections,
  getConnectionStatus,
  setConnectionStatus,
  processCommandQueue,
  pushToCommandQueue

}


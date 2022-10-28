'use strict';
const protocolAdam = require('./protocol_adam.js');
const fs = require('fs-extra');

fs.readJSON( './config_adam.json', 'utf8', (err, configuration) => {
    if (err) {
        console.log("File read failed:", err);
        return 0;
    }

    console.log('File data:',JSON.stringify( configuration) ); 
    protocolAdam.readData(configuration);

    setInterval( ()=>{ protocolAdam.readData(configuration); }, configuration.s_dt.timeout);
});


// let configuration = {
//     connection_pool : {},
//     s_dt:{s_n:1, no_p:2, timeout: 5000, hw_type:"serial", serial: "COM5", baud_rate:"9600"},
//     p_dt:[
//         {p_n:1, p_na:"wind_speed_ins"},
//         {p_n:2, p_na:"so2"}
//     ]
// };

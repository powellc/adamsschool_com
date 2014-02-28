var util = require('util'),
    colors = require('colors'),
    http = require('http'),
    httpProxy = require('http-proxy');

//
// Http Proxy Server with Proxy Table
//
httpProxy.createServer({
  router: {
    'parksidechurch.dev': 'localhost:8081',
    'www.parksidechurch.dev': 'localhost:8081',
  }
}).listen(80);

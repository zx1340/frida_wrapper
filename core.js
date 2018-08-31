
function hexToBytes(hex) {
    for (var bytes = [], c = 0; c < hex.length; c += 2)
        bytes.push(parseInt(hex.substr(c, 2), 16));
    return bytes;
}

function bytesToHex(b) {
    var uint8arr = new Uint8Array(b);
    if (!uint8arr) {
        return '';
    }
    var hexStr = '';
    for (var i = 0; i < uint8arr.length; i++) {
        var hex = (uint8arr[i] & 0xff).toString(16);
        hex = (hex.length === 1) ? '0' + hex : hex;
        hexStr += hex;
    }
    return hexStr;
}

function hexToStr(hex) {
    var str = '';
    for (var i = 0; i < hex.length; i += 2) {
        var v = parseInt(hex.substr(i, 2), 16);
        if (v) str += String.fromCharCode(v);
    }
    return str;
}

var c_exp = {
	b: function(method_name){
		setTimeout(function() {
			Java.perform(function() {
				traceMethod(method_name)
			});   
		}, 0);
	},
    sc: function() {
        if (typeof cContext['pc'] === 'undefined') {
            return;
        }
        sendContext();
    }
};

rpc.exports = c_exp;

// find and trace all methods declared in a Java Class
function traceClass(targetClass)
{
	var hook = Java.use(targetClass);
	var methods = hook.class.getDeclaredMethods();
	hook.$dispose;

	var parsedMethods = [];
	methods.forEach(function(method) {
		parsedMethods.push(method.toString().replace(targetClass + ".", "TOKEN").match(/\sTOKEN(.*)\(/)[1]);
	});

	var targets = uniqBy(parsedMethods, JSON.stringify);
	targets.forEach(function(targetMethod) {
		traceMethod(targetClass + "." + targetMethod);
	});
}

function to_str(byte_array){
	var result = "";
	for(var k = 0; k < byte_array.length; ++k){
			if( byte_array[k] > 32 && byte_array[k] < 126){
				result += (String.fromCharCode(byte_array[k]));
			}
	}
	return '\x1b[36m' +result +'\x1b[0m';
}


function to_hex(byte_array){
	var result = "";
	for (var k=0; k< byte_array.length; k++){
		var x = byte_array[k];
		result+= " ,"+x.toString();
	}
	return '\x1b[36m' +result +'\x1b[0m';
}

function toHexString(byteArray) {
	return Uint8Array.prototype.map.call(byteArray, function(byte) {
	  return ('0' + (byte & 0xFF).toString(16)).slice(-2);
	}).join('');
  }


function dored(result){
	return '\x1b[40m' +result +'\x1b[0m';
}


function makeid() {
	var text = "";
	var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  
	for (var i = 0; i < 10; i++)
	  text += possible.charAt(Math.floor(Math.random() * possible.length));
  
	return text;
  }
  


// trace a specific Java Method
function traceMethod(targetClassMethod)
{
	var delim = targetClassMethod.lastIndexOf(".");
	if (delim === -1) return;

	var targetClass = targetClassMethod.slice(0, delim)
	var targetMethod = targetClassMethod.slice(delim + 1, targetClassMethod.length)

	var hook = Java.use(targetClass);
	var overloadCount = hook[targetMethod].overloads.length;

	console.log("Tracing " + targetClassMethod + " [" + overloadCount + " overload(s)]");

    //clazz = Java.use("java.lang.Class");

	for (var i = 0; i < overloadCount; i++) {
		hook[targetMethod].overloads[i].implementation = function() {

			if (arguments.length) console.log();
			
			Java.perform(function() {
				bt = Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new());
			}); 

			//Create specical id when enter method
			var id = makeid();

			var send_data = "Enter::" + id + "::" + targetClassMethod;

			for(var j =0; j < arguments.length;j++){
				if (arguments[j] == null){
					
					send_data+="::null";
				}
				else if (arguments[j].toString()=="[object Object]"){
					
					//console.log(Object.prototype.toString.call(arguments[j]));
                    send_data+="::"+JSON.stringify(arguments[j]);
				}
				else{
					send_data+="::"+arguments[j];
				}
			}

			send(send_data);

			send("Backtrace::"+id+"::"+bt+"::"+"None\n");

			var retval = this[targetMethod].apply(this, arguments); // rare crash (Frida bug?)

			if (retval != undefined){
				send("RET::"+id+"::"+targetClassMethod+"::"+retval);
			}
			else{
				send("RET::"+id+"::"+targetClassMethod+"::undefined\n");

			}

			return retval;
		}
	}
}

function ba2hex(t) {
	
    var r = new Uint8Array(t);
	
	if (!r) return "";
	
	for (var e = "", n = 0; n < r.length; n++) {
        var a = (255 & r[n]).toString(16);
        e += a = 1 === a.length ? "0" + a : a
    }
	return e.toUpperCase()
}

// remove duplicates from array
function uniqBy(array, key)
{
        var seen = {};
        return array.filter(function(item) {
                var k = key(item);
                return seen.hasOwnProperty(k) ? false : (seen[k] = true);
        });
}

setTimeout(function() {
	Java.perform(function() {
		//traceMethod("android.location.Location.getLatitude");
	});   
}, 0);
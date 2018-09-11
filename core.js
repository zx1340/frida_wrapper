
var c_exp = {
	fh: function(method_name){
		setTimeout(function() {
			Java.perform(function() {
				traceMethod(method_name)
			});   
		}, 0);
	},
	ch: function(class_name){

		setTimeout(function() {
			Java.perform(function() {
				traceClass(class_name)
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


id = 0;
function makeid() {
	id += 1;
	return id;
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


function printByteArray(byteArray)
{
	//var byteArray = Memory.readByteArray(data, 16);
	var byteData = "";
	for (var i = 0; i !== byteArray.length; i++)
	{
		byteData += byteArray[i].toString(16);
	}
	send("Byte data: " + byteData);
	//send("Text :" + byteData.toString());
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

			//if (arguments.length) console.log();
			
			Java.perform(function() {
				bt = Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new());
			}); 

			//Create specical id when enter method
			var id = makeid();

			var send_data = "I::" + id + "::" + targetClassMethod;


			for(var j = 0; j < arguments.length;j++){

				if (arguments[j] == null){
					
					send_data+="::null";
				}
				else if (arguments[j].toString()=="[object Object]"){

					send_data+="::"+JSON.stringify(arguments[j]);
				}
				else{
					send_data+="::"+arguments[j];
				}
			}

			send(send_data+"\n");

			send("BACKTRACE::"+id+"::"+bt+"::"+"None\n");

			var retval = this[targetMethod].apply(this, arguments); 

			if (retval == undefined){
				send("O::"+id+"::"+targetClassMethod+"::no return value\n");
			}
			else if  (retval.toString()=="[object Object]"){
				send("O::"+id+"::"+targetClassMethod+"::"+JSON.stringify(retval));	
			}
			else{
				send("O::"+id+"::"+targetClassMethod+"::"+retval);
			}

			return retval;
		}
	}
}

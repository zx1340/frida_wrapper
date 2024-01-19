
var c_exp = {
	fh: function (method_name) {
		setTimeout(function () {
			Java.perform(function () {
				traceMethod(method_name)
			});
		}, 0);
	},
	ch: function (class_name) {

		setTimeout(function () {
			Java.perform(function () {
				traceClass(class_name)
			});
		}, 0);
	},
	sc: function () {
		if (typeof cContext['pc'] === 'undefined') {
			return;
		}
		sendContext();
	},
	fc: function () {
		
		setTimeout(function (args) {
			
			Java.perform(function () {
				Java.enumerateLoadedClasses({
					onMatch: function (className) {
						// Return if className start with blacklisted package name
						if (className.indexOf(args) != -1) {
							console.log(className);
						}
					},
					onComplete: function () { }
				});
			});
		}, 0);
	},

	rm: function (method_name, replace_argument) {
		setTimeout(function () {
			Java.perform(function () {
				traceMethod(method_name, replace_argument)
			});
		}, 0);
	},



};

rpc.exports = c_exp;

// find and trace all methods declared in a Java Class
function traceClass(targetClass) {
	var hook = Java.use(targetClass);
	var methods = hook.class.getDeclaredMethods();
	hook.$dispose;

	var parsedMethods = [];
	methods.forEach(function (method) {
		parsedMethods.push(method.toString().replace(targetClass + ".", "TOKEN").match(/\sTOKEN(.*)\(/)[1]);
	});

	var targets = uniqBy(parsedMethods, JSON.stringify);
	targets.forEach(function (targetMethod) {
		traceMethod(targetClass + "." + targetMethod);
	});
}


var id = 0;
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
function uniqBy(array, key) {
	var seen = {};
	return array.filter(function (item) {
		var k = key(item);
		return seen.hasOwnProperty(k) ? false : (seen[k] = true);
	});
}


function printByteArray(byteArray) {
	//var byteArray = Memory.readByteArray(data, 16);
	var byteData = "";
	for (var i = 0; i !== byteArray.length; i++) {
		byteData += byteArray[i].toString(16);
	}
	send("Byte data: " + byteData);
	//send("Text :" + byteData.toString());
}


// trace a specific Java Method
function traceMethod(targetClassMethod, replace_argument) {
	var delim = targetClassMethod.lastIndexOf(".");
	if (delim === -1) return;

	var targetClass = targetClassMethod.slice(0, delim)
	var targetMethod = targetClassMethod.slice(delim + 1, targetClassMethod.length)

	var hook = Java.use(targetClass);
	try {
		var overloadCount = hook[targetMethod].overloads.length;
	} catch (e) {
		console.log("Cannot found method", targetMethod);
		return;
	}

	console.log("Tracing " + targetClassMethod + " [" + overloadCount + " overload(s)]");


	for (var i = 0; i < overloadCount; i++) {
		hook[targetMethod].overloads[i].implementation = function () {

			var bt = Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new());

			//Create specical id when enter method
			var id = makeid();

			var send_data = "I::" + id + "::" + targetClassMethod;

			for (var j = 0; j < arguments.length; j++) {




				if (arguments[j] == null) {

					send_data += "::null";
				}
				else if (arguments[j].toString() == "[object Object]") {

					if (JSON.stringify(arguments[j]).toString().includes("java.util.Map, $className: java.util.HashMap>")) {

						var map = arguments[j];
						var mapKeys = map.keySet().toArray();
						console.log("HASH MAP SIZE", mapKeys.length);
						for (var i = 0; i < mapKeys.length; i++) {
							var key = mapKeys[i];
							var value = map.get(key);
							console.log("Map Entry: " + key + " -> " + value);
						}
					} else {
						console.log("GOT OBJECT", JSON.stringify(arguments[j]).toString())
					}

					send_data += "::" + JSON.stringify(arguments[j]);
				}
				else {
					send_data += "::" + arguments[j];
				}
			}

			send(send_data + "\n");

			send("BACKTRACE::" + id + "::" + bt + "::" + "None\n");

			if (replace_argument != undefined) {
				for (var a =0; a < replace_argument.length; a++) {
					console.log("Argument replace from " + arguments[a] + " to " + replace_argument)
					arguments[a] = replace_argument[a];
				}
			}

			var retval = this[targetMethod].apply(this, arguments);

			if (retval == undefined) {
				send("O::" + id + "::" + targetClassMethod + "::no return value\n");
			}
			else if (retval.toString() == "[object Object]") {
				send("O::" + id + "::" + targetClassMethod + "::" + JSON.stringify(retval));
			}
			else {
				send("O::" + id + "::" + targetClassMethod + "::" + retval);
			}

			return retval;
		}
	}
}


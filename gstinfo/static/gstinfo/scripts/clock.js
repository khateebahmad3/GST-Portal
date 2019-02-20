//Date And Time
var myVar = setInterval(myTimer, 1);
function myTimer() {
	var days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
	var months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    var d = new Date();
    var hr = d.getHours();
    var min = d.getMinutes();
    var sec = d.getSeconds();
    var secs;
    var day = d.getDay();
    var date = d.getDate();
    var month = d.getMonth();
    var year = d.getFullYear();
    var elem = document.getElementById("clock");
    if(sec < 10)
    	secs = "0" + sec;
    else
    	secs = sec;
    if(min < 10)
    	min = "0" + min;
    if(hr >= 0 && hr<12)
    {
    	if(hr == 0)
    		hr = 12;
    	elem.innerHTML = hr + ':' + min + ':' + secs + " AM" + ', ' + days[day] + ', ' + months[month] + ' ' + date + ' ' +year;
    }
    else if(hr>12)
    {
    	hr = hr - 12;
    	elem.innerHTML = hr + ':' + min + ':' + secs + " PM" + ', ' + days[day] + ', ' + months[month] + ' ' + date + ' ' +year;
    }
}

//Show Password in login page
function showPassword(id){
	var elem = document.getElementById("txtPassword");
	var icon = document.getElementById("iconn")
	if(elem.type == "password")
	{
		elem.type="text";
		icon.classList.replace("fa-square", "fa-check-square");
	}
	else
	{
		elem.type="password";
		icon.classList.replace("fa-check-square", "fa-square");
	}
}

function makeVisible()
{
	var hidden = document.getElementById("hidden");
	var option = document.getElementById("status");
	var gstin = document.getElementById("gstin");
	var unm = document.getElementById("unm");
	var upswd = document.getElementById("upassword");
	if(option.value == "Approved")
	{
		hidden.style.display = "block";
		gstin.setAttribute("required", "True");
		unm.setAttribute("required", "True");
		upswd.setAttribute("required", "True");
		gstin.removeAttribute("readonly");
		unm.removeAttribute("readonly");
		upswd.removeAttribute("readonly");
	}
	else
	{
		hidden.style.display = "none";
		gstin.setAttribute("readonly", "True");
		unm.setAttribute("readonly", "True");
		upswd.setAttribute("readonly", "True");
		gstin.removeAttribute("required");
		unm.removeAttribute("required");
		upswd.removeAttribute("required");
	}
}

function cnumber(id)
{
	var box = document.getElementById(id);
	box.setAttribute("onkeypress", "return event.charCode >= 48 && event.charCode <= 57");
}

function toggleActive(id)
{
  var nav=document.getElementById(id);
  nav.classList.toggle("active");
}
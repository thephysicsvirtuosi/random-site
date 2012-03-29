<html>
<style type="text/css">
body {
	background-color: whitesmoke;
}
#silly {
	font-color: white;
}


#namefield {
	border-style: solid;
	border-radius: 1em;
	-moz-border-radius: 1em;
	text-align: center;

}
#progressbar {
	visibility: hidden;
	background-color: whitesmoke;
	margin-left: auto;
	margin-right: auto;
	width: 30em;
	height: 1em;
	border-color: white;
	border-style: solid;
	border-width: 1px;
	border-radius: 1em;
	-moz-border-radius: 1em;

}
#progressbar > span {
	width: 4%;
	display: block;
	height: 100%;
	overflow: hidden;
	position: relative;
	background-color: #3399CC;
	border-radius: 1em;
	-moz-border-radius: 1em;
}
</style>

<script type="text/javascript">
var digits = '';
var total = 100.0;
var collect = 0;



function keycatch(e)
	{
	if (collect) {
		if (window.event)
			{
				keynum = e.keyCode;
			}
		else if(e.which)
			{
				keynum = e.which;
			}
		keychar = String.fromCharCode(keynum);
		numcheck = /\d/;
		var checkval =  numcheck.test(keychar);


		var spanguy = document.getElementById("progressfill");


		if (checkval)
		{
			digits = digits + keychar;
			document.getElementById("digitsspace").value = digits;
			var percentdone = 96*(digits.length/total) + 4;
			spanguy.style.width = percentdone + "%";

			if (percentdone >= 100) {
				collect = 0;
				document.forms["digitsform"].submit();
			}
		} 

		return checkval
		}
	}

function buttonclicked()
	{
		//document.body.onkeypress = keycatch(event);
		document.body.style.background = "black";
		document.getElementById("progressbar").style.visibility = "visible";
		document.getElementById("button").style.visibility = "hidden";
		
		var namefield = document.getElementById("namefield");
		namefield.style.background = "gray";
		namefield.readOnly = true;

		collect = 1;
	}
</script>



<body onkeypress="keycatch(event)">

<h3>Randomness Test</h3>

	We would like to see how well you do at coming up with random digits. <br>

	Please fill in your name, and once you are ready, click Go.  Note that once you click Go, you will not be finished until you type 1000 digits between 0 and 10, i.e. 0,1,2,3,4,5,6,7,8,9.

	<br>
	<br>
	<br> 


		<center>

	<form name="digitsform" method="POST" action="/datum">
		What's your name? <br>
		<input type="text" name="name" id="namefield" value="Anonymous"> <br>
		<input type="text" name="digits" id="digitsspace" hidden="true">
	</form>


	<input type="button" value="GO!" id="button" onClick="buttonclicked()">

	<br>

	</center>
	<div id="progressbar"><span id="progressfill"> </span></div>


</body>
</html>

<html>
<body>

<h3>The Database</h3>

This is a test.
<table border=1>
%for res in result:
	<tr>
	%for guy in res:
		<td> {{guy}}
	%end
%end
</table>

</body>
</html>

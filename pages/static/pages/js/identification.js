function collect_identifiant(event)
{
	let identifiantform = document.getElementById("identifiantInput");
	
	let mailInput = document.getElementById("mailAdress");
	let passwordInput = document.getElementById("password");

	console.log(identifiantform);
	console.log(mailInput);
	console.log(passwordInput);

	event.preventDefault();

	if(mailInput.value != "" && passwordInput != "")
	{
		fetch('/connexion',
		{
			method: "POST",
			body: new FormData(document.getElementById("identifiantInput"))
		})
		.then(response => 
		{
			return response.json();
		})
		.then(data => 
		{
		    console.log(data)
		})
		.catch(error =>
		{
			console.error(error);
		});
	}
}
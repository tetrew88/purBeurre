function collect_identifiant()
{
	let identifiant = {'mailAdress':'', 'password':''};

	const mailInput = document.getElementById("mailAdress");
	const passwordInput = document.getElementById("password");

	if(mailInput == null)
	{
		console.log(11);
	}
	if(passwordInput == null)
	{
		console.log(22);
	}

	let mail = mailInput.value;
	let password = passwordInput.value;

	event.preventDefault();

	if (mail == "" || password == "")
	{
		alert("identifiants invalide");
	}
	else
	{
		identifiant['mailAdress'] = mail;
		identifiant['password'] = password;

		console.log(identifiant['mailAdress']);
	}
}
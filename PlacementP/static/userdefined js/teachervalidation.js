function validateForm()
{
	//PERSONAL DETAILS VALIDATION ....	
	var firstname = document.myform.firstname.value;
	var middlename = document.myform.middlename.value;
	var lastname = document.myform.lastname.value;

	var letters = /^[A-Za-z]+$/;
	var space_letters=/^[A-Za-z\s]+$/;
	var loweCase=/[a-z]+/g;
	var upperCase= /[A-Z]+/g;
	var digit=/[0-9]+/g;
	var specialChar=/[!@#\$%\^&\*]+/g;
	var validEmail=/^([a-zA-Z0-9\.-]+)@([a-z0-9-]+).([a-z{2,3}])(.[a-z]{2,3})?$/;

	var mobileno = document.myform.mobileno.value;
	var alternetmobileno = document.myform.alternetmobileno.value;	
	var mobile = /^[789]\d{9}$/;
	var password=document.myform.password.value;
	var confirmpassword=document.myform.confirmpassword.value;	
	var email = document.myform.email.value;
	var selectcourse=document.myform.selectcourse.value;

	//empty field first,middle,last name validation
	
	if (firstname=="" || !firstname.match(letters))
	{
		alert("Please enter your firstname.");
		document.myform.firstname.focus();
		return false;
	}
	
	if (middlename=="" || !middlename.match(letters))
	{
		alert("Please enter your middlename.");
		document.myform.middlename.focus();
		return false;
	}
	if (lastname=="" || !lastname.match(letters))
	{
		alert("Please enter your lastname.");
		document.myform.lastname.focus();
		return false;
	}


	if(!mobileno.match(mobile))
	{
		alert("Enter valid 10 digit mob no start with 7,8 or 9");
		document.myform.mobileno.focus();
		return false;
	}

	if(!alternetmobileno.match(mobile))
	{
		alert("Enter valid 10 digit mob no start with 7,8 or 9");
		document.myform.alternetmobileno.focus();
		return false;
	}

	if(!email.match(validEmail))
	{
		alert("Enter valid email.");
		document.myform.email.focus();
		return false;
	}

	if(password.length<8 || !password.match(loweCase) || !password.match(upperCase) || !password.match(digit) || !password.match(specialChar))
	{
		alert("Weak Password.");
		document.myform.password.focus();
		return false;
	}

	if(password!=confirmpassword)
	{
		alert("Confirm Password does not matched");
		document.myform.confirmpassword.focus();
		return false;
	}
	var birthdate=document.myform.birthdate.value;
	var bdate=new Date(birthdate);
	var currentdate=new Date();
	var currentyear=currentdate.getFullYear();
	var byear=bdate.getFullYear();
	var difference=currentyear-byear;

	if(birthdate=="" || difference<21)
	{
		alert("Invalid birthdate."+difference);
		document.myform.birthdate.focus();
		return false;
	}

	if(selectcourse=="")
	{
		alert("Please select course.");
		document.myform.selectcourse.focus();
		return false;
	}


}
function validateForm()
{
//PERSONAL DETAILS VALIDATION ....	
	var firstname = document.myform.firstname.value;
	var middlename = document.myform.middlename.value;
	var lastname = document.myform.lastname.value;

	var letters = /^[A-Za-z]+$/;
	//var nodigit =/^([0-9])(.[0-9]{2,2})?$/;
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
	var address = document.myform.address.value;
	var birthdate=document.myform.birthdate.value;

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

	if(address.length==0 || !address.match(space_letters))
	{
		alert("Please enter valid residential address.");
		document.myform.address.focus();
		return false;
	}

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

// 10th CLASS DETAILS VALIDATION
	var schoolname=document.forms["myform"]["schoolname"].value;
	var tenthpercent=document.forms["myform"]["tenthpercent"].value;
	var tenthboard=document.forms["myform"]["tenthboard"].value;
	var passyear=document.forms["myform"]["passyear"].value;
	var selecttenthboard=document.forms["myform"]["selecttenthboard"].value;

	if(schoolname=="" || !schoolname.match(space_letters))
	{
		alert("Please enter valid school name.");
		document.myform.schoolname.focus();
		return false;
	}
	
	if(tenthpercent>100 || tenthpercent<=0 || tenthpercent=="")
	{
		alert("You might have left empty field or invalid 10th percentage."+tenthpercent);
		document.myform.tenthpercent.focus();
		return false;
	}

	
	if(selecttenthboard=="")
	{
		alert("Please select any one option.");
		document.myform.selecttenthboard.focus();
		return false;
	}

	if(tenthboard=="" || !tenthboard.match(letters))
	{
		alert("Invalid Exam Board name.");
		document.myform.tenthboard.focus();
		return false;
	}

	if(passyear<=2005 || passyear>=2022 || passyear=="")
	{
		alert("Invalid passing year or Empty field.");
		document.myform.passyear.focus();
		return false;
	}

	//10th Deatil Validation Ends Here
	//12th Detail Validation

	var twelvecollege=document.forms["myform"]["twelvecollege"].value;
	var twelvepercent=document.forms["myform"]["twelvepercent"].value;
	var twelvepassyear=document.forms["myform"]["twelvepassyear"].value;
	var twelveboard=document.forms["myform"]["twelveboard"].value;
	var twelveexamboard=document.forms["myform"]["twelveexamboard"].value;
	var diplomaflag=0;

	if(twelvecollege=="NA" && twelvepercent==0 && twelvepassyear==0 && twelveboard=="NA" && twelveexamboard=="" ) 
	{
		diplomaflag=1;
	}

	if(diplomaflag==0)
	{
		if(twelvecollege=="" || !twelvecollege.match(space_letters))
		{
			alert("Please enter valid 12th school name.");
			document.myform.twelvecollege.focus();
			return false;
		}

		if(twelvepercent>100 || twelvepercent<0 || twelvepercent=="")
		{
			alert("You might have left empty field or invalid 12th percentage."+diplomapercentage);
			document.myform.twelvepercent.focus();
			return false;
		}

		if(twelvepassyear<=2005 || twelvepassyear>=2022 || twelvepassyear=="")
		{
			alert("Invalid 12th passing year or Empty field.");
			document.myform.twelvepassyear.focus();
			return false;
		}

		if(twelveexamboard=="")
		{
			alert("Please select 12th Exam Board.");
			document.myform.twelveexamboard.focus();
			return false;
		}

		if(twelveboard=="" || !twelveboard.match(letters))
		{
			alert("Please enter valid 12th Exam Board.");
			document.myform.twelveboard.focus();
			return false;
		}

	}
	//12th Details Validation Ends Here.....
	
	//Diploma details validation 

	var diplomainstitute=document.forms["myform"]["diplomainstitute"].value;
	var diplomapercentage=document.forms["myform"]["diplomapercentage"].value;
	var diplomapassyear=document.forms["myform"]["diplomapassyear"].value;

	if(diplomaflag==1)
	{
		if(diplomainstitute=="" || !diplomainstitute.match(space_letters))
		{
			alert("You might have left empty field or invalid Diploma institute name."+diplomapercentage);
			document.myform.diplomainstitute.focus();
			return false;
		}

		if((diplomapercentage>100 || diplomapercentage<10 || diplomapercentage==""))
		{
			alert("You might have left empty field or invalid Diploma percentage.");
			document.myform.diplomapercentage.focus();
			return false;
		}

		if((diplomapassyear<=2005 || diplomapassyear>=2022 || diplomapassyear==""))
		{
			alert("Invalid Diploma passing year or Empty field.");
			document.myform.diplomapassyear.focus();
			return false;
		}

	}

	//Diploma details validation ends here.....


	//Garduation Details Validation
	var ugdegree=document.forms["myform"]["ugdegree"].value;
	var fypercent=document.forms["myform"]["fypercent"].value;
	var sypercent=document.forms["myform"]["sypercent"].value;
	var typercent=document.forms["myform"]["typercent"].value;
	var ugpassyear=document.forms["myform"]["ugpassyear"].value;
	var ugcollege=document.forms["myform"]["ugcollege"].value;
	var uguniversity=document.forms["myform"]["uguniversity"].value;
	var selectugdegree=document.forms["myform"]["selectugdegree"].value;

	if(selectugdegree=="")
	{
		alert("Please select valid UG Degree.");
		document.myform.selectugdegree.focus();
		return false;
	}


	if(ugdegree=="" || !ugdegree.match(letters))
	{
		alert("Please enter valid UG Degree.");
		document.myform.ugdegree.focus();
		return false;
	}

	if(fypercent>100 || fypercent<=10 || fypercent=="")
	{
		alert("You might have left empty field or invalid FY percentage."+fypercent);
		document.myform.fypercent.focus();
		return false;
	}

	if(sypercent>100 || sypercent<=10 || sypercent=="")
	{
		alert("You might have left empty field or invalid SY percentage."+sypercent);
		document.myform.sypercent.focus();
		return false;
	}

	if(typercent>100 || typercent<=10 || typercent=="")
	{
		alert("You might have left empty field or invalid TY percentage."+typercent);
		document.myform.typercent.focus();
		return false;
	}

	if(ugpassyear<=2005 || ugpassyear>=2022 || ugpassyear=="")
	{
		alert("Invalid UG passing year or Empty field.");
		document.myform.ugpassyear.focus();
		return false;
	}

	if(ugcollege=="" || !ugcollege.match(space_letters))
	{
		alert("Please enter valid UG College name.");
		document.myform.ugcollege.focus();
		return false;
	}

	if(uguniversity=="" || !uguniversity.match(space_letters))
	{
		alert("Please enter valid UG University name.");
		document.myform.uguniversity.focus();
		return false;
	}
	//GRADUATION DETAILS VALIDATION ENDS HERE.......
	//POST GARDUATION DETAILS VALIDATION 

	var pgfypercent=document.forms["myform"]["pgfypercent"].value;
	var pgsypercent=document.forms["myform"]["pgsypercent"].value;
	var pgpassyear=document.forms["myform"]["pgpassyear"].value;
	var yeargap=document.forms["myform"]["yeargap"].value;
	var pgdegree=document.forms["myform"]["pgdegree"].value;
	var pgcollegename=document.forms["myform"]["pgcollegename"].value;
	var pguniversity=document.forms["myform"]["pguniversity"].value;
	var isgap=document.forms["myform"]["isgap"].value;

	if(pgdegree=="")
	{
		alert("Please select post graduation degree.");
		document.myform.pgdegree.focus();
		return false;
	}


	if(pgfypercent>100 || pgfypercent<=10 || pgfypercent=="")
	{
		alert("You might have left empty field or invalid PG FY percentage."+pgfypercent);
		document.myform.pgfypercent.focus();
		return false;
	}

	if(pgsypercent>100 || pgsypercent<=10 || pgsypercent=="")
	{
		alert("You might have left empty field or invalid PG FY percentage.");
		document.myform.pgsypercent.focus();
		return false;
	}

	if(pgpassyear<=2005 || pgpassyear>=2022 || pgpassyear=="")
	{
		alert("Invalid PG passing year or Empty field.");
		document.myform.pgpassyear.focus();
		return false;
	}


	if(pgcollegename=="")
	{
		alert("Please select post graduation college.");
		document.myform.pgcollegename.focus();
		return false;
	}


	if(pguniversity=="")
	{
		alert("Please select post graduation university.");
		document.myform.pguniversity.focus();
		return false;
	}

	if(isgap=="")
	{
		alert("Please select post graduation college.");
		document.myform.isgap.focus();
		return false;
	}

	if(yeargap<=0 || yeargap>5 || yeargap=="")
	{
		alert("Invalid year gap.");
		document.myform.yeargap.focus();
		return false;
	}
 
 	//POST GRADUATION DETAILS VALIDATION ENDS HERE...
	//GRADUATION PROJECT DETAILS VALIDATION
	var ugproject=document.forms["myform"]["ugproject"].value;
	var ugprojecttech=document.forms["myform"]["ugprojecttech"].value;
	var ugprojectdesc=document.forms["myform"]["ugprojectdesc"].value;

	if(ugproject=="" || !ugproject.match(space_letters))
	{
		alert("Please enter valid UG Project Name.");
		document.myform.ugproject.focus();
		return false;
	}

	if(ugprojecttech=="" || !ugprojecttech.match(space_letters))
	{
		alert("Please enter valid UG Project Technology.");
		document.myform.ugprojecttech.focus();
		return false;
	}

	if(ugprojectdesc=="" || !ugprojectdesc.match(space_letters))
	{
		alert("Please enter valid UG Project Description.");
		document.myform.ugprojectdesc.focus();
		return false;
	}
	//GRADUATION PROJECT VALIDATION ENDS HERE....
	//POST GRADUATION PROJECT VALIDATION 


	var pgproject=document.forms["myform"]["pgproject"].value;
	var pgprojecttech=document.forms["myform"]["pgprojecttech"].value;
	var pgprojectdesc=document.forms["myform"]["pgprojectdesc"].value;

	if(pgproject=="" ||  !pgproject.match(space_letters))
	{
		alert("Please enter valid PG Project Name.");
		document.myform.pgproject.focus();
		return false;
	}

	if(pgprojecttech.length==0 || !pgprojecttech.match(space_letters))
	{
		alert("Please enter valid PG Project Technology.");
		document.myform.pgprojecttech.focus();
		return false;
	}

	if(pgprojectdesc.length==0 || !pgprojectdesc.match(space_letters))
	{
		alert("Please enter valid PG Project Description.");
		document.myform.pgprojectdesc.focus();
		return false;
	}
	//POST GRADUATION DETAILS VALIDATION ENDS HERE....

}//Validate Function Ends here.................

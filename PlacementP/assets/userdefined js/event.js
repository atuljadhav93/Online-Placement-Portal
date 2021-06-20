//start mouse hover navbar js code
	$(document).ready(function () {
$('.navbar-light .dmenu').hover(function () {
        $(this).find('.sm-menu').first().stop(true, true).slideDown(150);
    }, function () {
        $(this).find('.sm-menu').first().stop(true, true).slideUp(105)
    });
});
//end mouse hover navbar js code
//start index body panel
$(document).on('click', '.panel-heading span.clickable', function(e)
{
    var $this = $(this);
	if(!$this.hasClass('panel-collapsed')) 
	{
		$this.parents('.panel').find('.panel-body').slideUp();
		$this.addClass('panel-collapsed');
		$this.find('i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up');
	}
	else
	{
		$this.parents('.panel').find('.panel-body').slideDown();
		$this.removeClass('panel-collapsed');
		$this.find('i').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down');
		
	}
})
//end index body panel
//start calender js
$(function() {
$('.dates #usr1').datepicker({
'format': 'yyyy-mm-dd',
'autoclose': true
});
});
//stop calender js

//start submit button js
function myFunction() {
var txt;
if (confirm("Press a button!")) {
txt = "You pressed OK!";
} else {
txt = "You pressed Cancel!";
}
document.getElementById("demo").innerHTML = txt;
}
//stop submit button js

//start registration form validation
function validateForm()
{
//empty field first,middle,last name validation decalration
var fname = document.forms["myform"]["fname"];
var mname = document.forms["myform"]["mname"];
var lname = document.forms["myform"]["lname"];
//first,middle,last name validation decalration
var firstname = document.myform.fname.value;
var middlename = document.myform.mname.value;
var lastname = document.myform.lname.value;
var letters = /^[A-Za-z]+$/;
//mobile number validation variable declaration
var mno = document.myform.mobileno.value;
var mobileno = /^[789]\d{9}$/;
//email address validation variable declaration
var email = document.myform.email.value;
var atpos = email.indexOf("@");
var dotpos = email.lastIndexOf(".");
//empty field first,middle,last name validation
if (fname.value == "")
{
window.alert("Please enter your firstname.");
name.focus();
return false;
}
else
if(!firstname.match(letters))
{
alert("Enter valid first name.");
return false;
}
else
if (mname.value == "")
{
window.alert("Please enter your middlename.");
name.focus();
return false;
}
else
//first,middle,last name validation
if(!middlename.match(letters))
{
alert("Enter valid middle name.");
return false;
}
else
if (lname.value == "")
{
window.alert("Please enter your lastname.");
name.focus();
return false;
}
else
if(!lastname.match(letters))
{
alert("Enter valid last name.");
return false;
}
else
//mobile number validation
if(!mno.match(mobileno))
{
alert("Enter valid 10 digit mob no start with 7,8 or 9");
return false;
}
else
//email address validation
if (atpos<1 || dotpos<atpos+2 || dotpos+2>=email.length)
	{
	alert("Not a valid e-mail address");
	return false;
	}
	else
	//password and confiram password validation
	if(document.myform.password.value == "")
	{
	alert("Plese Enter Your Password");
	document.myform.password.focus();
	return false;
	}
	else
	if(document.myform.cpassword.value == "")
	{
	alert("Plese Enter Confirm Password");
	document.myform.cpassword.focus();
	return false;
	}
	else
	if(document.myform.password.value != document.myform.cpassword.value)
	{
	alert("Confirm Password does not matched");
	document.myform.cpassword.focus();
	return false;
	}
	//start registration form birth date validation
	var lblError = document.getElementById("lblError");
	//Get the date from the TextBox.
	var dateString = document.getElementById("txtDate").value;
	var regex = /(((0|1)[0-9]|2[0-9]|3[0-1])\/(0[1-9]|1[0-2])\/((19|20)\d\d))$/;
	//Check whether valid dd/MM/yyyy Date Format.
	if (regex.test(dateString)) {
	var parts = dateString.split("/");
	var dtDOB = new Date(parts[1] + "/" + parts[0] + "/" + parts[2]);
	var dtCurrent = new Date();
	lblError.innerHTML = "Eligibility 18 years only."
	if (dtCurrent.getFullYear() - dtDOB.getFullYear() < 18) 
	{
		return false;
	}
		if (dtCurrent.getFullYear() - dtDOB.getFullYear() == 18) 
		{
			//CD 11/06/2018 and DB 15/07/2000. will turned 18 on 15/07/2018.
			if (dtCurrent.getMonth() < dtDOB.getMonth()) 
			{
				return false;
			}
			if (dtCurrent.getMonth() == dtDOB.getMonth()) 
			{
			//CD: 11/06/2018 and DB 15/06/2000. will turned 18 on 15/06/2018.
				if (dtCurrent.getDate() < dtDOB.getDate()) 
				{
				return false;
				}
			}
		}
			lblError.innerHTML = "";
			return true;
		}
		else //start registration form birth date validation
		{
			lblError.innerHTML = "Enter date in dd/MM/yyyy format only."
			alert("Enter date in dd/MM/yyyy format only.");
			return false;
		}

		var fup = document.getElementById('filename');
		var fileName = fup.value;
		var ext = fileName.substring(fileName.lastIndexOf('.') + 1);
		if(ext == "gif" || ext == "GIF" || ext == "JPEG" || ext == "jpeg" || ext == "jpg" || ext == "JPG" || ext == "doc")
		{
			return true;
		} 
		else
		{
			alert("Upload Gif or Jpg images only");
			fup.focus();
			return false;
		}

	}
//end registration form birth date validation
//end registration form validation

//start dynamically add inputbox and textarea
var counterText = 0;
var counterTextArea = 0;
function addAllInputs(divName, inputType)
{
	var newdiv = document.createElement('div');
    switch(inputType) 
        {
            case 'text':
            newdiv.innerHTML = "Entry " + (counterText + 1) + " <br><input type='text' name='myInputs[]'>";
            counterText++;
            break;
            case 'textarea':
            newdiv.innerHTML = "Entry " + (counterTextArea + 1) + " <br><textarea name='myTextAreas[]'>Project discription here...</textarea>";
            counterTextArea++;
            break;
        }
        document.getElementById(divName).appendChild(newdiv);
}
//end dynamically add inputbox and textarea

//start file accept js code(teacher registration form)
$(document).ready(function() {
  $('input[type="file"]').on("change", function() {
    let filenames = [];
    let files = document.getElementById("customFile").files;
    if (files.length > 1) {
      filenames.push("Total Files (" + files.length + ")");
    } else {
      for (let i in files) {
        if (files.hasOwnProperty(i)) 
        {
          filenames.push(files[i].name);
        }
      }
    }
    $(this)
      .next(".custom-file-label")
      .html(filenames.join(","));
  });
});
//end file accept js code(teacher registration form)

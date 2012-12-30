function checkNewPass()
{
    //Store the password field objects into variables ...
    var pass1 = document.getElementById('new_password');
    var pass2 = document.getElementById('new_password_conf');
    //Store the Confimation Message Object ...
    var message = document.getElementById('confirmMessage2');
    //Set the colors we will be using ...
    var goodColor = "#66cc66";
    var badColor = "#ff6666";
    //Compare the values in the password field 
    //and the confirmation field
    if(pass1.value == pass2.value){
        //The passwords match. 
        //Set the color to the good color and inform
        //the user that they have entered the correct password 
        pass2.style.backgroundColor = goodColor;
        message.style.color = goodColor;
        message.innerHTML = "Passwords Match!"
    }else{
        //The passwords do not match.
        //Set the color to the bad color and
        //notify the user.
        pass2.style.backgroundColor = badColor;
        message.style.color = badColor;
        message.innerHTML = "Passwords Do Not Match!"
    }
}

 

function confirm_unfollow(){

	if(window.confirm('Do you want to unfollow this user?')){
		return true;
	}
	else{
		return false;
	}
}
 

function confirm_delete(){

	if(window.confirm('Do you want to delete this?')){
		return true;
	}
	else{
		return false;
	}
}
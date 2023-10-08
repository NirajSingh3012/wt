Practical – 1 

Aim: 

Create a home Page about you with an appropriate image and 15 lines introducing you with hyperlinks to 

About your + people who have made difference to your life 

About your friends 

Your dreams and aspirations 

10 things you wish in life 

10 things you don’t wish to do but you have to do! 

Unforgettable moments in your life! 

Your skills or services 

 

Code: 

Home page: 

<!doctype html> 

<html> 

<head> 

<title> My Home Page </title> 

</head> 

<body> 

<h4> name </h4> 

<h4>Roll No </h4> 

<h1> WELCOME TO MY HOME PAGE </h1> 

<a href="default.asp"> 

<img src="img url" alt="name" width="300" height="400"> 

</a> 

<h2> Want To Know About Me More! </h2> 

<p><a href="url"> Learn about me </a></p> 

<p><a href="url"> Discover people who have made a difference in my life </a></p> 

<p><a href="url"> Explore more about my friends </a></p> 

<p><a href="url"> Learn about my dreams and aspirations </a></p> 

<p><a href="url"> Explore my wishes </a></p> 

<p><a href="url"> Discover my list of things I have to do </a></p> 

<p><a href="url"> Relive some unforgettable moments with me </a></p> 

<p><a href="url"> Explore my skills and services </a></p> 

<h3> Thank You For Visiting My Page! </h3> 

</body> 

</html> 

 

About me: 

<!doctype html> 

<html> 

<head> 

<title> About Me </title> 

</head> 

<body> 

<h4> name </h4> 

<h4> Roll No </h4> 

<h1> LEARN ABOUT ME </h1> 

<p><strong> 

write here 

</p></strong> 

</body> 

</html> 

 

People who made difference: 

<!doctype html> 

<html> 

<head> 

<title> People Who Made Difference In My Life </title> 

</head> 

<body> 

<h4> name </h4> 

<h4> Roll No </h4> 

<h1> DISCOVER PEOPLE WHO HAVE MADE A DIFFERERNCE IN MY LIFE </h1> 

<p><strong> 

write here 

</p></strong> 

</body> 

</html> 

 

About my friends: 

<!doctype html> 

<html> 

<head> 

<title> About My Friends </title> 

</head> 

<body> 

<h4> name </h4> 

<h4> Roll No </h4> 

<h1> EXPLORE MORE ABOUT MY FRIENDS </h1> 

<p><strong> 

write here 

</p></strong> 

</body> 

</html> 

 

My dreams and aspirations: 

<!doctype html> 

<html> 

<head> 

<title> My Dreams And Aspirations </title> 

</head> 

<body> 

<h4> name </h4> 

<h4> Roll No </h4> 

<h1> LEARN ABOUT MY DREAMS AND ASPIRATIONS </h1> 

<p><strong> 

write here 

</p></strong> 

</body> 

</html> 

 

10 things I wish: 

<!doctype html> 

<html> 

<head> 

<title> 10 Things I Wish In My Life </title> 

</head> 

<body> 

<h4> name </h4> 

<h4> Roll No </h4> 

<h1> EXPLORE MY WISHES </h1> 

<p><strong> 

write here 

</p></strong> 

</body> 

</html> 

 

10 things I don’t: 

<!doctype html> 

<html> 

<head> 

<title> 10 Things I Don't Wish But Have To </title> 

</head> 

<body> 

<h4> name </h4> 

<h4> Roll No </h4> 

<h1> DISCOVER MY LIST OF THINGS I HAVE TO DO </h1> 

<p><strong> 

write here 

</p></strong> 

</body> 

</html> 

 

Unforgettable moments: 

<!doctype html> 

<html> 

<head> 

<title> Unforgettable Moments In My Life </title> 

</head> 

<body> 

<h4> name </h4> 

<h4> Roll No </h4> 

<h1> RELIVE SOME UNFORGETTABLE MOMENTS WITH ME </h1> 

<p><strong> 

write here 

</p></strong> 

</body> 

</html> 

 

My skills and aspirations: 

<!doctype html> 

<html> 

<head> 

<title> My Skills And Aspirations </title> 

</head> 

<body> 

<h4> name </h4> 

<h4> Roll No </h4> 

<h1> EXPLORE MY SKILLS AND SERVICES </h1> 

<p><strong> 

write here 

</p></strong> 

</body> 

</html>


````````````````````````````````````````````````````````````````````````````````````````````````


Practical – 2 

Aim: 

Create a registration form inside a table with no borders where people can register with you asking 

for your services. Registration form should have following information about person name, age, 

email, date of birth, gender (radio buttons), hobbies (checkboxes), address (text area), country (list 

box), required service (text area) and submit button. 

 

Code: 

<!DOCTYPE html> 

<html> 

<head> 

    <title>Registration Form</title> 

</head> 

<body> 

<body bgcolor="LightGrey"> 

<h2> your name </h2> 

<h3> Roll No </h3> 

    <h1>Registration Form</h1> 

    <form action="submit.php" method="POST"> 

        <table> 

            <tr> 

                <td>Name:</td> 

                <td><input type="text" name="name" required></td> 

            </tr> 

<tr> 

                <td>Middlename:</td> 

                <td><input type="text" name="name" required></td> 

            </tr> 

<tr> 

                <td>Lastname:</td> 

                <td><input type="text" name="name" required></td> 

            </tr> 

             

            <tr> 

                <td>Age:</td> 

                <td><input type="number" name="age" required></td> 

            </tr> 

             

            <tr> 

                <td>Email:</td> 

                <td><input type="email" name="email" required></td> 

            </tr> 

             

            <tr> 

                <td>Date of Birth:</td> 

                <td><input type="date" name="dob" required></td> 

            </tr> 

             

            <tr> 

                <td>Gender:</td> 

                <td> 

                    <input type="radio" name="gender" value="Male" required> Male 

                    <input type="radio" name="gender" value="Female" required> Female 

                    <input type="radio" name="gender" value="Other" required> Other 

                </td> 

            </tr> 

             

            <tr> 

                <td>Hobbies:</td> 

                <td> 

                    <input type="checkbox" name="hobbies[]" value="Reading"> Reading 

                    <input type="checkbox" name="hobbies[]" value="Traveling"> Traveling 

                    <input type="checkbox" name="hobbies[]" value="Sports"> Sports 

                    <input type="checkbox" name="hobbies[]" value="Art"> Art 

                </td> 

            </tr> 

             

            <tr> 

                <td>Address:</td> 

                <td><textarea name="address" rows="4" cols="40" required></textarea></td> 

            </tr> 

             

            <tr> 

                <td>Country:</td> 

                <td> 

                    <select name="country" required> 

                        <option value="INDIA">India</option> 

                        <option value="USA">United States</option> 

                        <option value="Canada">Canada</option> 

                        <option value="UK">United Kingdom</option> 

                        <option value="Other">Other</option> 

                    </select> 

                </td> 

            </tr> 

            

            <tr> 

                <td>Required Service:</td> 

                <td><textarea name="service" rows="4" cols="40" required></textarea></td> 

            </tr> 

             

            <tr> 

                <td colspan="2" align="center"> 

                   <input type="submit" value="Submit" style="background-color: #3498db; color: #fff; padding: 10px 20px; border: none; cursor: pointer;"> 

                </td> 

            </tr> 

        </table> 

    </form> 

</body> 

</html> 


 ``````````````````````````````````````````````````````````````````````````````````



 Practical – 3 

Aim: 

Create a home Page about you with an appropriate image and 15 lines introducing you with hyperlinks to 

About your + people who have made difference to your life 

About your friends 

Your dreams and aspirations 

10 things you wish in life 

10 things you don’t wish to do but you have to do! 

Unforgettable moments in your life! 

Your skills or services 

 

Code: 

Home page: 

<!doctype html> 

<html> 

<head> 

<title> My Home Page </title> 

<style> 

body { 

  background-color: lightblue; 

} 

</style> 

<style> 

h1 { 

  font-style: italic; 

} 

h1 { 

  color: green; 

} 

h2 { 

  font-style: italic; 

} 

h2 { 

  color: red; 

} 

h3 { 

  font-style: italic; 

} 

h3 { 

  color: blue; 

} 

</style> 

</head> 

<body> 

<h4> name </h4> 

<h4>Roll No </h4> 

<h1 class="italic"> WELCOME TO MY HOME PAGE </h1> 

<a href="default.asp"> 

<img src="img url" alt="name" width="300" height="400"> 

</a> 

<h2  class="italic"> Want To Know About Me More! </h2> 

<p><a href="url"> Learn about me </a></p> 

<p><a href="url"> Discover people who have made a difference in my life </a></p> 

<p><a href="url"> Explore more about my friends </a></p> 

<p><a href="url"> Learn about my dreams and aspirations </a></p> 

<p><a href="url"> Explore my wishes </a></p> 

<p><a href="url"> Discover my list of things I have to do </a></p> 

<p><a href="url"> Relive some unforgettable moments with me </a></p> 

<p><a href="url"> Explore my skills and services </a></p> 

<h3  class="italic"> Thank You For Visiting My Page! </h3> 

</body> 

</html> 

About me: 

<!doctype html> 

<html> 

<head> 

<title> About Me </title> 

<style> 

body { 

  background-color: lightgrey; 

} 

</style> 

<style> 

h1 { 

  font-style: italic; 

} 

</style> 

<style> 

h1 { 

  color: green; 

} 

 

p { 

  color: blue; 

} 

</style> 

<style> 

p { 

font-family: Tahoma, Verdana, sans-serif; 

} 

</style> 

</head> 

<body> 

<h4> name </h4> 

<h4> Roll No </h4> 

<h1 class="italic"> LEARN ABOUT ME </h1> 

<p><strong> 

Write here 

</p></strong> 

</body> 

</html> 

 

People who made difference: 

<!doctype html> 

<html> 

<head> 

<title> People Who Made Difference In My Life </title> 

<style> 

body { 

  background-color: lightgrey; 

} 

</style> 

<style> 

h1 { 

  font-style: italic; 

} 

</style> 

<style> 

h1 { 

  color: green; 

} 

 

p { 

  color: blue; 

} 

</style> 

<style> 

p { 

font-family: Tahoma, Verdana, sans-serif; 

} 

</style> 

</head> 

<body> 

<h4> name </h4> 

<h4> Roll No </h4> 

<h1 class="italic"> DISCOVER PEOPLE WHO HAVE MADE A DIFFERERNCE IN MY LIFE  </h1> 

<p><strong> 

Write here 

</p></strong> 

</body> 

</html> 

 

About friends: 

<!doctype html> 

<html> 

<head> 

<title> About My Friends </title> 

<style> 

body { 

  background-color: lightgrey; 

} 

</style> 

<style> 

h1 { 

  font-style: italic; 

} 

</style> 

<style> 

h1 { 

  color: green; 

} 

 

p { 

  color: blue; 

} 

</style> 

<style> 

p { 

font-family: Tahoma, Verdana, sans-serif; 

} 

</style> 

</head> 

<body> 

<h4> name </h4> 

<h4> Roll No </h4> 

<h1 class="italic"> EXPLORE MORE ABOUT MY FRIENDS </h1> 

<p><strong> 

Write here 

</p></strong> 

</body> 

</html> 

 

My dreams and aspirations: 

<!doctype html> 

<html> 

<head> 

<title> My Dreams And Aspirations </title> 

<style> 

body { 

  background-color:lightgrey; 

} 

</style> 

<style> 

h1 { 

  font-style: italic; 

} 

</style> 

<style> 

h1 { 

  color: green; 

} 

 

p { 

  color: blue; 

} 

</style> 

<style> 

p { 

font-family: Tahoma, Verdana, sans-serif; 

} 

</style> 

</head> 

<body> 

<h4> name </h4> 

<h4> Roll No </h4> 

<h1 class="italic"> LEARN ABOUT MY DREAMS AND ASPIRATIONS </h1> 

<p><strong> 

Write here 

</p></strong> 

</body> 

</html> 

 

10 things I wish: 

<!doctype html> 

<html> 

<head> 

<title> 10 Things I Wish In My Life </title> 

<style> 

body { 

  background-color: lightgrey; 

} 

</style> 

<style> 

h1 { 

  font-style: italic; 

} 

</style> 

<style> 

h1 { 

  color: green; 

} 

 

p { 

  color: blue; 

} 

</style> 

<style> 

p { 

font-family: Tahoma, Verdana, sans-serif; 

} 

</style> 

</head> 

<body> 

<h4> name </h4> 

<h4> Roll No </h4> 

<h1 class="italic"> EXPLORE MY WISHES </h1> 

<p><strong> 

Write here 

</p></strong> 

</body> 

</html> 

 

10 things I don’t: 

<!doctype html> 

<html> 

<head> 

<title> 10 Things I Don't Wish But Have To </title> 

<style> 

body { 

  background-color: lightgrey; 

} 

</style> 

<style> 

h1 { 

  font-style: italic; 

} 

</style> 

<style> 

h1 { 

  color: green; 

} 

 

p { 

  color: blue; 

} 

</style> 

<style> 

p { 

font-family: Tahoma, Verdana, sans-serif; 

} 

</style> 

</head> 

<body> 

<h4> name </h4> 

<h4> Roll No </h4> 

<h1 class="italic"> DISCOVER MY LIST OF THINGS I HAVE TO DO </h1> 

<p><strong> 

Write here 

</p></strong> 

</body> 

</html> 

Unforgettable moments: 

<!doctype html> 

<html> 

<head> 

<title> Unforgettable Moments In My Life </title> 

<style> 

body { 

  background-color: lightgrey; 

} 

</style> 

<style> 

h1 { 

  font-style: italic; 

} 

</style> 

<style> 

h1 { 

  color: green; 

} 

 

p { 

  color: blue; 

} 

</style> 

<style> 

p { 

font-family: Tahoma, Verdana, sans-serif; 

} 

</style> 

</head> 

<body> 

<h4> name </h4> 

<h4> Roll No </h4> 

<h1 class="italic"> RELIVE SOME UNFORGETTABLE MOMENTS WITH ME </h1> 

<p><strong> 

Write here 

</p></strong> 

</body> 

</html> 

 

My skills: 

<!doctype html> 

<html> 

<head> 

<title> My Skills And Aspirations </title> 

<style> 

body { 

  background-color: lightgrey; 

} 

</style> 

<style> 

h1 { 

  font-style: italic; 

} 

</style> 

<style> 

h1 { 

  color: green; 

} 

 

p { 

  color: blue; 

} 

</style> 

<style> 

p { 

font-family: Tahoma, Verdana, sans-serif; 

} 

</style> 

</head> 

<body> 

<h4> name </h4> 

<h4> Roll No </h4> 

<h1 class="italic"> EXPLORE MY SKILLS AND SERVICES </h1> 

<p><strong> 

Write here 

</p></strong> 

</body> 

</html>

``````````````````````````````````````````````````````````````````````````````````````````````


Practical -4  

Aim: 

Write a javascript code to find no is even or odd using prompt dialog box. 

Code: 

<!DOCTYPE html> 

<html> 

<head> 

<title>Even or Odd Checker</title> 

</head> 

<body> 

<h2> name </h2> 

<h3> Roll No </h3> 

<script> 

// Prompt the user for input 

var userInput = prompt("Enter a number:"); 

// Convert the input to a number 

var number = parseInt(userInput); 

// Check if the number is valid 

if (isNaN(number)) { 

alert("Invalid input. Please enter a valid number."); 

} else { 

// Check if the number is even or odd 

if (number % 2 === 0) { 

alert(number + " is an even number."); 

} else { 

alert(number + " is an odd number."); 

} 

} 

</script> 

</body> 

</html> 



 ``````````````````````````````````````````````````````````````````````````````````````````````


 Practical – 5 

Aim: 

Write a javascript code to find sum of first “n” numbers. Accept the value for n in prompt dialog box. 

Code: 

<!DOCTYPE html> 

<html> 

<head> 

<title>Sum of First n Numbers</title> 

</head> 

<body> 

<h2> name </h2> 

<h3> Roll No </h3> 

<script> 

// Prompt the user for input 

var userInput = prompt("Enter a value for 'n':"); 

// Convert the input to a number 

var n = parseInt(userInput); 

// Check if the input is valid 

if (isNaN(n) || n <= 0) { 

alert("Invalid input. Please enter a valid positive number."); 

} else { 

var sum = 0; 

// Calculate the sum of the first 'n' numbers 

for (var i = 1; i <= n; i++) { 

sum += i; 

} 

alert("The sum of the first " + n + " numbers is: " + sum); 

} 

</script> 

</body> 

</html> 



`````````````````````````````````````````````````````````````````````````````````````````

Practical – 6 

Aim: 

Write a JavaScript code to find factorial of a given number. 

Code: 

<!DOCTYPE html> 

<html> 

<head> 

<title>Factorial Calculator</title> 

</head> 

<body> 

<h2> name </h2> 

<h3> Roll No </h3> 

<script> 

// Prompt the user for input 

var userInput = prompt("Enter a number:"); 

// Convert the input to a number 

var number = parseInt(userInput); 

// Check if the input is valid 

if (isNaN(number) || number < 0) { 

alert("Invalid input. Please enter a non-negative number."); 

} else { 

// Calculate the factorial of the number 

var factorial = 1; 

for (var i = 1; i <= number; i++) { 

factorial *= i; 

} 

alert("The factorial of " + number + " is: " + factorial); 

} 

</script> 

</body> 

</html>


```````````````````````````````````````````````````````````````````````````````````````


Practical – 7 

Aim: 

Create a html page that accepts Principle Amount, No. of Years & Rate of Interest from 3 text fields, when you click “Calculate Interest” button, the data is sent to a function that returns the simple interest.  When you click on “Final Amount” button, the final amount by adding principle amount and interest should be displayed.  [ Use Functions] 

Code: 

<!DOCTYPE html> 

<html> 

<head> 

<title>Interest Calculator</title> 

</head> 

<body> 

<h2> Pradnya Dhopat </h2> 

<h3> Roll No: S079 </h3> 

<h1>Interest Calculator</h1> 

<label for="principal">Principle Amount:</label> 

<input type="number" id="principal" placeholder="Enter principle amount"><br><br> 

<label for="years">No. of Years:</label> 

<input type="number" id="years" placeholder="Enter number of years"><br><br> 

<label for="rate">Rate of Interest:</label> 

<input type="number" id="rate" placeholder="Enter rate of interest"><br><br> 

<button onclick="calculateInterest()">Calculate Interest</button> 

<button onclick="calculateFinalAmount()">Final Amount</button><br><br> 

<p id="result"></p> 

<script> 

function calculateInterest() { 

var principal = parseFloat(document.getElementById("principal").value); 

var years = parseFloat(document.getElementById("years").value); 

var rate = parseFloat(document.getElementById("rate").value); 

var interest = (principal * years * rate) / 100; 

document.getElementById("result").textContent = "Simple Interest: " +  

interest.toFixed(2); 

} 

function calculateFinalAmount() { 

var principal = parseFloat(document.getElementById("principal").value); 

var years = parseFloat(document.getElementById("years").value); 

var rate = parseFloat(document.getElementById("rate").value); 

var interest = (principal * years * rate) / 100; 

var finalAmount = principal + interest; 

document.getElementById("result").textContent = "Final Amount: " +  

finalAmount.toFixed(2); 

} 

</script> 

</body> 

</html> 



 ````````````````````````````````````````````````````````````````````````````````````

Practical – 8 

Aim: 

Design a webpage for validation of textbox. (Textbox must not be empty) 

Code: 

<!DOCTYPE html> 

<html lang="en"> 

<head> 

<meta charset="UTF-8"> 

<meta name="viewport" content="width=device-width, initial-scale=1.0"> 

<title>Textbox Validation</title> 

<script> 

 function validateTextbox() { 

 var textboxValue = document.getElementById("textbox").value; 

  

 if (textboxValue.trim() === "") { 

 alert("Textbox cannot be empty."); 

 return false; 

 } 

  

 return true; 

 } 

</script> 

</head> 

<body> 

<h2> Pradnya Dhopat </h2> 

<h3> Roll No: S079 </h3> 

<h3> MVLU College </h3> 

 <h1>Textbox Validation</h1> 

 <form onsubmit="return validateTextbox()"> 

 <input type="text" id="textbox" placeholder="Enter text here"> 

 <input type="submit" value="Submit"> 

 </form> 

</body> 

</html>


``````````````````````````````````````````````````````````````````````````````````````````````


Practical – 9 

Aim: 

Design a webpage for validating input a number between 1 and 10. 

Code: 

<!DOCTYPE html> 

<html lang="en"> 

<head> 

<meta charset="UTF-8"> 

<meta name="viewport" content="width=device-width, initial-scale=1.0"> 

<title>Number Validation</title> 

<script> 

 function validateNumber() { 

 var numberInput = document.getElementById("numberInput").value; 

  

 if (isNaN(numberInput) || numberInput < 1 || numberInput > 10) { 

 alert("Please enter a valid number between 1 and 10."); 

 return false; 

 } 

  

 return true; 

 } 

</script> 

</head> 

<body> 

<h2> Pradnya Dhopat </h2> 

<h3> Roll No: S079 </h3> 

<h3> MVLU College </h3> 

 <h1>Number Validation</h1> 

 <form onsubmit="return validateNumber()"> 

 <input type="text" id="numberInput" placeholder="Enter a number  

between 1 and 10"> 

 <input type="submit" value="Submit"> 

 </form> 

</body> 

</html> 


 ```````````````````````````````````````````````````````````````````````````````````````````````````

Practical – 9 

Aim: 

Design a webpage for validating input a number between 1 and 10. 

Code: 

<!DOCTYPE html> 

<html lang="en"> 

<head> 

<meta charset="UTF-8"> 

<meta name="viewport" content="width=device-width, initial-scale=1.0"> 

<title>Number Validation</title> 

<script> 

 function validateNumber() { 

 var numberInput = document.getElementById("numberInput").value; 

  

 if (isNaN(numberInput) || numberInput < 1 || numberInput > 10) { 

 alert("Please enter a valid number between 1 and 10."); 

 return false; 

 } 

  

 return true; 

 } 

</script> 

</head> 

<body> 

<h2> Pradnya Dhopat </h2> 

<h3> Roll No: S079 </h3> 

<h3> MVLU College </h3> 

 <h1>Number Validation</h1> 

 <form onsubmit="return validateNumber()"> 

 <input type="text" id="numberInput" placeholder="Enter a number  

between 1 and 10"> 

 <input type="submit" value="Submit"> 

 </form> 

</body> 

</html> 



 ``````````````````````````````````````````````````````````````````````````````````````````````


 Practical – 10 

Aim: 

Design a webpage for showing alert box in 3 seconds using setTimeout function. 

Code: 

<!DOCTYPE html> 

<html lang="en"> 

<head> 

<meta charset="UTF-8"> 

<meta name="viewport" content="width=device-width, initial-scale=1.0"> 

<title>Show Alert After 3 Seconds</title> 

<script> 

 function showAlert() { 

 setTimeout(function() { 

 alert("This is an alert box!"); 

 }, 3000); 

 } 

</script> 

</head> 

<body> 

<h2> Pradnya Dhopat </h2> 

<h3> Roll No: S079 </h3> 

<h3> MVLU College </h3> 

 <h1>Show Alert After 3 Seconds</h1> 

 <button onclick="showAlert()">Show Alert</button> 

</body> 

</html>



`````````````````````````````````````````````````````````````````````````````````````````````````````````



Practical – 11 

Aim: 

Design a webpage for counter using setTimeout and clearTimeout functions. 

Code: 

<!DOCTYPE html> 

<html lang="en"> 

<head> 

<meta charset="UTF-8"> 

<meta name="viewport" content="width=device-width, initial-scale=1.0"> 

<title>Counter with setTimeout</title> 

<script> 

 var counterValue = 0; 

 var timeoutId = null; 

 function startCounter() { 

 document.getElementById("startButton").disabled = true; 

 document.getElementById("stopButton").disabled = false; 

 timeoutId = setTimeout(function() { 

 counterValue++; 

 document.getElementById("counter").textContent = counterValue; 

 startCounter(); 

 }, 1000); 

 } 

 function stopCounter() { 

 clearTimeout(timeoutId); 

 document.getElementById("startButton").disabled = false; 

 document.getElementById("stopButton").disabled = true; 

 } 

</script> 

</head> 

<body> 

<h2> Pradnya Dhopat </h2> 

<h3> Roll No: S079 </h3> 

<h3> MVLU College </h3> 

 <h1>Counter with setTimeout</h1> 

 <p id="counter">0</p> 

 <button id="startButton" onclick="startCounter()">Start Counter</button> 

 <button id="stopButton" onclick="stopCounter()" disabled>Stop  

Counter</button> 

</body> 

</html>


````````````````````````````````````````````````````````````````````````````````````````````````````````




Practical – 12 

Aim: 

Design a Login Form containing User Name and password.  The password should contain max 8 characters.When user name and password match with predefined values, a welcome message should be displayed otherwise error message should be displayed.  Maximum 3 attempts should be allowed for wrong passwords otherwise the application should end. [Use If] 

Code: 

<!DOCTYPE html> 

<html lang="en"> 

<head> 

<meta charset="UTF-8"> 

<meta name="viewport" content="width=device-width, initial-scale=1.0"> 

<title>Login Form</title> 

<script> 

 var maxAttempts = 3; 

 var allowedAttempts = maxAttempts; 

 var predefinedUsername = "user"; 

 var predefinedPassword = "password"; 

 function validateLogin() { 

 var username = document.getElementById("username").value; 

 var password = document.getElementById("password").value; 

 var message = document.getElementById("message"); 

 if (username === predefinedUsername && password ===  

predefinedPassword) { 

 message.style.color = "green"; 

 message.textContent = "Welcome, " + username + "!"; 

 } else { 

 allowedAttempts--; 

 if (allowedAttempts > 0) { 

 message.style.color = "red"; 

 message.textContent = "Invalid username or password. " +  

allowedAttempts + " attempt(s) remaining."; 

 } else { 

 message.style.color = "red"; 

 message.textContent = "Maximum login attempts reached.  

Application will now end."; 

 document.getElementById("username").disabled = true; 

 document.getElementById("password").disabled = true; 

 document.getElementById("submitButton").disabled = true; 

 } 

 } 

 return false; 

 } 

</script> 

</head> 

<body> 

<h2> Pradnya Dhopat </h2> 

<h3> Roll No: S079 </h3> 

<h3> MVLU College </h3> 

 <h1>Login Form</h1> 

 <form onsubmit="return validateLogin()"> 

 <input type="text" id="username" placeholder="Username"  

required><br> 

 <input type="password" id="password" placeholder="Password (max 8  

characters)" maxlength="8" required><br> 

 <input type="submit" id="submitButton" value="Login"> 

 </form> 

 <p id="message"></p> 

</body> 

</html> 



`````````````````````````````````````````````````````````````````````````````````````````````````````


Practical – 13 

Aim: 

 Add JavaScript validations in registration form. Name text field should not accept any digit, age text field should not accept characters, perform validations on email on lost focus of text field. Empty fields should not be allowed. 

Code: 

<!DOCTYPE html> 

<html lang="en"> 

<head> 

<meta charset="UTF-8"> 

<meta name="viewport" content="width=device-width, initial-scale=1.0"> 

<title>Registration Form</title> 

<script> 

 function validateName() { 

 var nameInput = document.getElementById("name").value; 

  

 if (nameInput.match(/\d/)) { 

 alert("Name should not contain digits."); 

 return false; 

 } 

  

 return true; 

 } 

 function validateAge() { 

 var ageInput = document.getElementById("age").value; 

  

 if (isNaN(ageInput)) { 

 alert("Age should be a number."); 

 return false; 

 } 

  

 return true; 

 } 

 function validateEmail() { 

 var emailInput = document.getElementById("email").value; 

 if (!emailInput.match(/^\S+@\S+\.\S+$/)) { 

 alert("Invalid email format."); 

 return false; 

 } 

 return true; 

 } 

 function validateForm() { 

 return validateName() && validateAge() && validateEmail(); 

 } 

</script> 

</head> 

<body> 

<h2> Pradnya Dhopat </h2> 

<h3> Roll No: S079 </h3> 

<h3> MVLU College </h3> 

 <h1>Registration Form</h1> 

 <form onsubmit="return validateForm()"> 

 <input type="text" id="name" placeholder="Name" required><br> 

 <input type="text" id="age" placeholder="Age" required><br> 

 <input type="text" id="email" placeholder="Email" required  

onblur="validateEmail()"><br> 

 <input type="submit" value="Register"> 

 </form> 

</body> 

</html> 



`````````````````````````````````````````````````````````````````````````````````````````````````


Practical – 14 

Aim: 

Design xml file with record of CDs and display in table format using for each loop in XSLT. 

XSLT code: 

<?xml version="1.0" encoding="UTF-8"?> 

<xsl:stylesheet version="1.0" 

xmlns:xsl="http://www.w3.org/1999/XSL/Transform"> 

<xsl:template match="/"> 

  <html> 

  <body> 

    <h2>My CD Collection</h2> 

    <table border="1"> 

      <tr bgcolor="#9acd32"> 

        <th>Title</th> 

        <th>Artist</th> 

      </tr> 

      <xsl:for-each select="catalog/cd"> 

      <tr> 

        <td><xsl:value-of select="title" /></td> 

        <td><xsl:value-of select="artist" /></td> 

      </tr> 

      </xsl:for-each> 

    </table> 

  </body> 

  </html> 

</xsl:template> 

</xsl:stylesheet> 

 

XML CODE: 

<?xml version="1.0" encoding="UTF-8"?> 

<catalog> 

  <cd> 

    <title>Empire Burlesque</title> 

    <artist>Bob Dylan</artist> 

    <country>USA</country> 

    <company>Columbia</company> 

    <price>10.90</price> 

    <year>1985</year> 

  </cd> 

  <cd> 

    <title>Hide your heart</title> 

    <artist>Bonnie Tyler</artist> 

    <country>UK</country> 

    <company>CBS Records</company> 

    <price>9.90</price> 

    <year>1988</year> 

  </cd> 

  <cd> 

    <title>Greatest Hits</title> 

    <artist>Dolly Parton</artist> 

    <country>USA</country> 

    <company>RCA</company> 

    <price>9.90</price> 

    <year>1982</year> 

  </cd> 

  <cd> 

    <title>Still got the blues</title> 

    <artist>Gary Moore</artist> 

    <country>UK</country> 

    <company>Virgin records</company> 

    <price>10.20</price> 

    <year>1990</year> 

  </cd> 

  <cd> 

    <title>Eros</title> 

    <artist>Eros Ramazzotti</artist> 

    <country>EU</country> 

    <company>BMG</company> 

    <price>9.90</price> 

    <year>1997</year> 

  </cd> 

  <cd> 

    <title>One night only</title> 

    <artist>Bee Gees</artist> 

    <country>UK</country> 

    <company>Polydor</company> 

    <price>10.90</price> 

    <year>1998</year> 

  </cd> 

  <cd> 

    <title>Sylvias Mother</title> 

    <artist>Dr.Hook</artist> 

    <country>UK</country> 

    <company>CBS</company> 

    <price>8.10</price> 

    <year>1973</year> 

  </cd> 

  <cd> 

    <title>Maggie May</title> 

    <artist>Rod Stewart</artist> 

    <country>UK</country> 

    <company>Pickwick</company> 

    <price>8.50</price> 

    <year>1990</year> 

  </cd> 

  <cd> 

    <title>Romanza</title> 

    <artist>Andrea Bocelli</artist> 

    <country>EU</country> 

    <company>Polydor</company> 

    <price>10.80</price> 

    <year>1996</year> 

  </cd> 

  <cd> 

    <title>When a man loves a woman</title> 

    <artist>Percy Sledge</artist> 

    <country>USA</country> 

    <company>Atlantic</company> 

    <price>8.70</price> 

    <year>1987</year> 

  </cd> 

  <cd> 

    <title>Black angel</title> 

    <artist>Savage Rose</artist> 

    <country>EU</country> 

    <company>Mega</company> 

    <price>10.90</price> 

    <year>1995</year> 

  </cd> 

  <cd> 

    <title>1999 Grammy Nominees</title> 

    <artist>Many</artist> 

    <country>USA</country> 

    <company>Grammy</company> 

    <price>10.20</price> 

    <year>1999</year> 

  </cd> 

  <cd> 

    <title>For the good times</title> 

    <artist>Kenny Rogers</artist> 

    <country>UK</country> 

    <company>Mucik Master</company> 

    <price>8.70</price> 

    <year>1995</year> 

  </cd> 

  <cd> 

    <title>Big Willie style</title> 

    <artist>Will Smith</artist> 

    <country>USA</country> 

    <company>Columbia</company> 

    <price>9.90</price> 

    <year>1997</year> 

  </cd> 

  <cd> 

    <title>Tupelo Honey</title> 

    <artist>Van Morrison</artist> 

    <country>UK</country> 

    <company>Polydor</company> 

    <price>8.20</price> 

    <year>1971</year> 

  </cd> 

  <cd> 

    <title>Soulsville</title> 

    <artist>Jorn Hoel</artist> 

    <country>Norway</country> 

    <company>WEA</company> 

    <price>7.90</price> 

    <year>1996</year> 

  </cd> 

  <cd> 

    <title>The very best of</title> 

    <artist>Cat Stevens</artist> 

    <country>UK</country> 

    <company>Island</company> 

    <price>8.90</price> 

    <year>1990</year> 

  </cd> 

  <cd> 

    <title>Stop</title> 

    <artist>Sam Brown</artist> 

    <country>UK</country> 

    <company>A and M</company> 

    <price>8.90</price> 

    <year>1988</year> 

  </cd> 

  <cd> 

    <title>Bridge of Spies</title> 

    <artist>T`Pau</artist> 

    <country>UK</country> 

    <company>Siren</company> 

    <price>7.90</price> 

    <year>1987</year> 

  </cd> 

  <cd> 

    <title>Private Dancer</title> 

    <artist>Tina Turner</artist> 

    <country>UK</country> 

    <company>Capitol</company> 

    <price>8.90</price> 

    <year>1983</year> 

  </cd> 

  <cd> 

    <title>Midt om natten</title> 

    <artist>Kim Larsen</artist> 

    <country>EU</country> 

    <company>Medley</company> 

    <price>7.80</price> 

    <year>1983</year> 

  </cd> 

  <cd> 

    <title>Pavarotti Gala Concert</title> 

    <artist>Luciano Pavarotti</artist> 

    <country>UK</country> 

    <company>DECCA</company> 

    <price>9.90</price> 

    <year>1991</year> 

  </cd> 

  <cd> 

    <title>The dock of the bay</title> 

    <artist>Otis Redding</artist> 

    <country>USA</country> 

    <company>Stax Records</company> 

    <price>7.90</price> 

    <year>1968</year> 

  </cd> 

  <cd> 

    <title>Picture book</title> 

    <artist>Simply Red</artist> 

    <country>EU</country> 

    <company>Elektra</company> 

    <price>7.20</price> 

    <year>1985</year> 

  </cd> 

  <cd> 

    <title>Red</title> 

    <artist>The Communards</artist> 

    <country>UK</country> 

    <company>London</company> 

    <price>7.80</price> 

    <year>1987</year> 

  </cd> 

  <cd> 

    <title>Unchain my heart</title> 

    <artist>Joe Cocker</artist> 

    <country>USA</country> 

    <company>EMI</company> 

    <price>8.20</price> 

    <year>1987</year> 

  </cd> 

</catalog>



````````````````````````````````````````````````````````````````````````````````````````````````````````


Practical – 15 

Aim: 

Create a webpage to fetch and display the contents of a text file on click of a 

button using XMLHttpRequestObject. 

Code: 

<html> 

<head> 

<title>Ajax at work</title> 

<script language = "javascript"> 

var XMLHttpRequestObject = false; 

 

if (window.XMLHttpRequest) { 

XMLHttpRequestObject = new XMLHttpRequest(); 

} else if (window.ActiveXObject) { 

XMLHttpRequestObject = new ActiveXObject("Microsoft.XMLHTTP"); 

} 

 

function getData(dataSource, divID) 

{ 

if(XMLHttpRequestObject) { 

var obj = document.getElementById(divID); 

XMLHttpRequestObject.open("GET", dataSource); 

 

XMLHttpRequestObject.onreadystatechange = function() 

{ 

if (XMLHttpRequestObject.readyState == 4 && 

XMLHttpRequestObject.status == 200) { 

obj.innerHTML = XMLHttpRequestObject.responseText; 

} 

} 

XMLHttpRequestObject.send(null); 

} 

} 

 

</script> 

</head> 

<body> 

<H1>Fetching data with Ajax</H1> 

<form> 

<input type = "button" value = "Display Message" 

onclick = "getData('data.txt', 'targetDiv')"> 

</form> 

<div id="targetDiv"> 

<p>The fetched data will go here.</p> 

</div> 

</body> 

</html> 

 

 ```````````````````````````````````````````````````````````````````````````````````````````````````


 Practical – 16 

Aim: 

Create webpage using AJAX having 3 images. Fetch and display the content of text file when the mouse is moved over the image. 

Code: 

<html> 

<head> 

<title>Ajax at work</title> 

<script language = "javascript"> 

var XMLHttpRequestObject = false; 

if (window.XMLHttpRequest) { 

XMLHttpRequestObject = new XMLHttpRequest(); 

} else if (window.ActiveXObject) { 

XMLHttpRequestObject = new ActiveXObject("Microsoft.XMLHTTP"); 

} 

function getData(dataSource, divID) 

{ 

if(XMLHttpRequestObject) { 

var obj = document.getElementById(divID); 

XMLHttpRequestObject.open("GET", dataSource); 

XMLHttpRequestObject.onreadystatechange = function() 

{ 

if (XMLHttpRequestObject.readyState == 4 && 

XMLHttpRequestObject.status == 200) { 

obj.innerHTML = XMLHttpRequestObject.responseText; 

} 

} 

XMLHttpRequestObject.send(null); 

} 

} 

</script> 

</head> 

<body> 

<H1>Interactive mouseovers </H1> 

<img src='sandwich.jpg' onmouseover="getData('sandwiches.txt','targetDiv')"> 

<img src='pizza.gif' onmouseover="getData('pizza.txt','targetDiv')"> 

<img src='soup.jpg' onmouseover="getData('soups.txt','targetDiv')"> 

<div id="targetDiv"> 

<p>The fetched data will go here.</p> 

</div> 

</body> 

</html>

``````````````````````````````````````````````````````````````````````````````````````````````````````````````


Practical – 17 

Aim: 

A)Retrieve data from HTML form using PHP Design registration form using HTML and retrieve form data using php. 

Code: 

<html> 

<head> 

<title>Retrieving records </Title> 

</head> 

<body> 

<h2>User Registration</h2> 

<form name=f1 method=GET action="Retrieve.php"> 

<pre> 

First Name: <input name="fn" type="text"><br/> 

Last Name : <input name="ln" type="text"><br/> 

Age : <input name="Age" type="text"><br/> 

Hometown : <input name="Ht" type="text"><br/> 

Mobile No : <input name="mn" type="text" maxlength=10><br/> 

<input type="Submit" value="Submit"> 

</pre> 

</form> 

</body> 

</html> 

<?php 

 $fname=trim($_REQUEST["fn"]); 

 $lname=trim($_REQUEST["ln"]); 

 $Age=trim($_REQUEST["Age"]); 

 $Hometown=trim($_REQUEST["Ht"]); 

 $mobno=trim($_REQUEST["mn"]); 

echo "<H1> Retrieving Data from Server...<?h1>"; 

echo "<table border='1'> 

<tr> 

<th>First Name</th> 

<th>Last Name</th> 

<th>Age</th> 

<th>Hometown</th> 

<th>Mobile Number</th> 

</tr>"; 

echo "<tr>"; 

echo "<td>".$fname."</td>"; 

echo "<td>".$lname."</td>"; 

echo "<td>".$Age."</td>"; 

echo "<td>".$Hometown."</td>"; 

echo "<td>".$mobno."</td>"; 

echo "</tr>"; 

echo"</table>"; 

?> 

 

Create a table in mysql as follows: 

mysql> create database UserName; 

Query OK, 1 row affected (0.01 sec) 

mysql> use UserName; 

Database changed 

mysql> create table user1 (id Integer(2),firstname varchar(20),lastname varchar(20),Age  

Integer(2),HomeTown varchar(20),Job varchar(20)); 

Query OK, 0 rows affected (0.11 sec) 

mysql> insert into user1 values(1,'ria','bisht',22,'Mumbai','MD'); 

Query OK, 1 row affected (0.06 sec) 

 

B) Retrieve Employee Details/ Registration Details from the database using PHP 

Code: 

<html> 

<head> 

<title> Practical 9Retrieve Employee Details/ Registration Details from  

the database using PHP  

</title> 

</head> 

<body> 

<center> 

<form method=get action="getuser.php"> 

<input Type=textbox name="txtId"> 

<input type="Submit" value="Submit"> 

</form> 

<br /> 

</center> 

</body> 

</html> 

getuser.php 

<?php 

$q=$_GET["txtId"]; 

$con=mysql_connect('localhost','root',''); 

if(!$con) 

 { 

die('Could not connect:'.mysql_error()); 

 } 

mysql_select_db("db1",$con); 

 $sql="select * from register where ID='".$q."'"; 

 $result=mysql_query($sql); 

echo "<table border='1'> 

<tr> 

<th>ID</th> 

<th>First Name</th> 

<th>Last Name</th> 

<th>Age</th> 

<th>Hometown</th> 

<th>Mobile Number</th> 

</tr>"; 

while($row=mysql_fetch_array($result)) 

 { 

echo "<tr>"; 

echo "<td>".$row['ID']."</td>"; 

echo "<td>".$row['FName']."</td>"; 

echo "<td>".$row['LName']."</td>"; 

echo "<td>".$row['Age']."</td>"; 

echo "<td>".$row['HomeTown']."</td>"; 

echo "<td>".$row['MobileNo']."</td>"; 

echo "</tr>"; 

 } 

echo"</table>"; 

mysql_close($con); 

?> 

 

C) Add, Modify and Delete data from client side into table in MySQL 

Code: 

<html> 

<head> 

<title> Practical 10</title> 

</head> 

<body> 

<h3>Login Form</h3> 

<form name=f1 method ="POST" action="login.php"> 

<pre> 

Username:<input name="un" type="text"><br/> 

Password:<input name="ps" type="password"><br/> 

<input type="Submit" value="Login"><br> 

</form> 

<a href="insert.html">SignUp</a> <a href="update.html">Change  

password</a> <a href="delete.html">Remove Account</a><br/> 

</pre> 

</body> 

</html> 

login.php 

<?php 

$con=mysql_connect('localhost','root',''); 

 if(!$con) 

 { 

 die('could not connect:'.mysql_error()); 

 } 

mysql_select_db("db1",$con); 

 $uname=trim($_REQUEST["un"]); 

 $p=trim($_REQUEST["ps"]); 

 $sql="Select * from login where Uname='".$uname."'and Pass='".$p."'"; 

 $result=mysql_query($sql); 

 if(mysql_num_rows($result)) 

{ 

echo "<H1> Welcome you are a regitered User</h1>"; 

} 

 else 

{ 

echo "</H1>User Name Not FOund/Not a Registered User</h1>"; 

} 

mysql_close($con); 

?> 

 

<html> 

<head> 

<title>Inserting Records /Adding Records</title> 

</head> 

<body> 

<h2>User Registration</h2> 

<form name=f1 method=POST action="insert.php"> 

<pre> 

Username : <input name="un" type="text"><br/> 

Password : <input name="ps" type="password"><br/> 

<input type="Submit" value="Insert Records"> 

</pre> 

</form> 

</body> 

</html> 

insert.php 

<?php 

 $con=mysql_connect('localhost','root',''); 

 if(!$con) 

 { 

 die('could not connect:'.mysql_error()); 

 } 

mysql_select_db("db1",$con); 

$uname=trim($_REQUEST["un"]); 

 $p=trim($_REQUEST["ps"]); 

 $sql1="Select * from login where Uname='".$uname."'and Pass='".$p."'"; 

 $result=mysql_query($sql1); 

 if(!mysql_fetch_array($result)) 

 { 

 $sql="Insert into login values ('".$uname."','".$p."')"; 

 $r=mysql_query($sql); 

 echo "yes"; 

 } 

 else 

 {  

echo "no";  

} 

mysql_close($con); 

?> 

 

<html> 

<head> 

<title> Modifying/Update Record </title> 

</head> 

<body> 

<h2>Change Password</h2> 

<form name=f1 method=post action="update.php"> 

<pre> 

Username : <input name="un" type="text"><br/> 

Current Password: <input name="ps" type="password"><br/> 

New Password: <input name="nps" type="password"><br/> 

<input type="Submit" value="Update Record"> 

</pre> 

</form> 

</body> 

</html> 

update.php 

<?php 

$con=mysql_connect('localhost','root',''); 

if(!$con) 

 { 

die('could not connect:'.mysql_error()); 

 } 

mysql_select_db("db1",$con); 

 $uname=trim($_REQUEST["un"]); 

 $p=trim($_REQUEST["ps"]); 

 $np=trim($_REQUEST["nps"]); 

 $sql1="Update login set Pass='".$np."'whereUname='".$uname."'and Pass='".$p."'"; 

 $result=mysql_query($sql1); 

 $s="Select * from login where Uname='".$uname."'and Pass='".$p."'"; 

 $result=mysql_query($s); 

if(!mysql_fetch_array($result)) 

 { 

echo "Password Changed"; 

 } 

else 

 { 

echo "no";  

 } 

mysql_close($con); 

?> 

 

<html> 

<head> 

</head> 

<body> 

<h2>Deleting User</h2> 

<form name=f1 method=post action="delete.php"> 

<pre> 

User Name: <input name="un" type="text"><br> 

Password: <input name="ps" type="password"><br> 

<input type="Submit" value="Delete"> 

</pre> 

</form> 

</body> 

</html> 

delete.php 

<?php 

 $con=mysql_connect('localhost','root',''); 

if(!$con) 

 { 

die('could not connect:'.mysql_error()); 

 } 

mysql_select_db("db1",$con); 

 $uname=trim($_REQUEST["un"]); 

 $p=trim($_REQUEST["ps"]); 

$s1="Select * from login where Uname='".$uname."'and Pass='".$p."'"; 

 $result1=mysql_query($s1); 

if(!mysql_fetch_array($result1)) 

 { 

echo "Record could not be found or already Record Deleted"; 

 } 

else 

{ 

 $sql1="Delete from login where Uname='".$uname."'and Pass='".$p."'"; 

 $result=mysql_query($sql1); 

 $s="Select * from login where Uname='".$uname."'and Pass='".$p."'"; 

 $result=mysql_query($s); 

if(!mysql_fetch_array($result)) 

 { 

echo "Record Deleted"; 

 } 

 } 

mysql_close($con); 

?> 

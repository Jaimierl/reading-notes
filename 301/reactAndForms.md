# React and Forms

## Forms

1. A Controlled Component is a form input element that is controlled by a component React. The component that controls the form will also control what happens to the form as a reaction to the user input.
2. Using controlled components will update the state with the users responses as soon as they are entered. This is because React needs two parts to update forms called HandleChange and HandleSubmit. Usual forms only use handle submit or update when everything is completed. Becasue React also uses handlechange on every change (or every keystroke) the site saves the new information. This is how websites get your name and email even when you click away before filling out a full form.
3. If we have an event handler on an input field then we target what the user enters by through event.target.value

## The Conditional or Ternary Operator

1. We would use a terniary operator to write an if statement in one line of code.
2. Let's rewrite a statement as a terniary statement:
Starter Statement-
  if(x===y){
 console.log(true);
  } else {
 console.log(false);
  }

Terniary Statement-
let testing = x===y? console.log(true) :console.log(false);

[Reading Notes Home Page](README.md)
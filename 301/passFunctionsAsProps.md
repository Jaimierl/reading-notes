# Passing Functions As Props

## React Notes

1. .map() takes an array of numbers and doubles their value. 
2. JSX is essentially the modified mix of almost HTML and almost Javaascript that is used for React. The JSX to loop through an array and display each value is using the .map() function with the array in question surrounded by <li> tags.
3. When doing the above, each list item needs a unique key or identifier.
4. According to the React documentation [here](https://reactjs.org/docs/lists-and-keys.html) "Keys help React identify which items have changed, are added, or are removed."

## The Spread Operator

1. The spread operator looks like an ellipses ... and according to [Techie Diaries](https://www.techiediaries.com/react-spread-operator-props-setstate/#:~:text=The%20Spread%20operator%20lets%20you,of%20elemnts%20into%20one%20array.) is used to expand a string, object, or array into its elements. 
2. Four things the spread operator can do are add items to arrays, combine arrays, combine objects, and spread an array out into a functions arguments.
3. The Spread Operator can combine two arrays ex (Note for real code the numbers below would need to be words): 
const 1 = {1: "🧮"}
const 2 = {2: "✈"}
const 12 = {...1,...2}
console.log(12)//Object {1: "🧮", 2: "✈"}
4. The Spread Operator can add a new item to an array ex:
const 3 = {🍍}
const 4 = {🚌,...1}
console.log(4)//Object {🍍 🚌}
5. The Spread Operator can combine two objects into one ex:
const 5 = {1: "🍕 "}
const 6 = {2: "🐲"}
const 7 = {...5,...6, laugh:()=>{console.log("💙")}}
7.laugh()//💙

## Video Notes

1. In the video [here](https://www.youtube.com/watch?v=c05OL7XbwXU&ab_channel=SteveGriffith-Prof3ssorSt3v3) the first things the dev does to pass functions between the components is by creating a function where the state is that he was going to change.
2. The increment function is passed a person and adds one to the count for the person(Makes more sense when you watch the video).
3. A method can be passed from a parent to a child component by using a callback.
4. A child component can invoke a method passed to it by a parent component by using a call.

[Reading Notes Home Page](README.md)
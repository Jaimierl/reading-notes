# State and Props

## Reading Questions

1. Based off of the diagram on the react lifecycle found [here](https://medium.com/@joshuablankenshipnola/react-component-lifecycle-events-cb77e670a093), the render phase happens both during mounting (componentDidMount) and the updating (componentDidUpdate) life cycle phases. 

2. The very first thing to happen in the lifecycle of React is calling the constructor.

3. The order of react things happening is mounting the constructor, render, React Updates, componentDidMount, render, React Updates, componentDidUpdate, componentWillUnmount.

4. The componentDidMount is called after a component is mounted and according to the aforementioned article, it is used to load things from a network request or initialized from the DOM.

## Video Questions

1. The types of things that can be passed in the props are the things you would like your component to render such as a display image to the user or the initial count for a counter component. The analogy used was you pass the props the arguments to a function (such as the first two numbers in 1+2=3).

2. According to [this](https://www.youtube.com/watch?v=IYvD9oBCuJI&ab_channel=WebDevSimplified) video, the big difference between props and state is that props can be changed for the user based on changes in the application since they are handled outside of the component. State is handled inside of the component(so in the previous example, the answer of 3 would be stored in the state).Props and state must be changed outside and inside the component respectively.

3. We re-render our application when the props change and then send the updated value to the state.

4. Some examples of things we could store in state are values changed by the props, or things that need to be reloaded on the page based on what the user does.


[Reading Notes Home Page](README.md)
// FUNCTIONS IN TYPESCRIPT
// FOUR ways to declare functions

// 1. function declaration
//    traditional; most common
export function colorCode1(color: string) { return }

// 2. function expressions
//   function is assigned to variable
//   TO-DO: when do you use this? why?
export const colorCode2 = function(color: string) { return }

// 3. arrow function 
//    useful for short functions and/or nested/ callback functions
export const colorCode4 = (color: string) => { return }

// 4. function constructor
//    actually, don't use. security concerns.
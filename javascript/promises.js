// TO-DO: 
const fetch = require("node-fetch");

// ------------------------------------------------------------------
// Write JavaScript function that fetches data from an API; 
// cancels the request if it takes longer than a specified time

// SEE HERE: https://www.w3resource.com/javascript-exercises/asynchronous/javascript-asynchronous-exercise-9.php

// ------------------------------------------------------------------
// Write JavaScript function that fetches data from an API and 
// retries the request a specified number of times if it fails.

// SEE THESE RESOURCES (you have to construct your own recursive
//    fetchRetry method that basically just sets a timer and 
//    then retries after delay + reduces 'tries' count on each rt

// https://medium.com/@yshen4/javascript-fetch-with-retry-fb7e2e8f8cad
// https://stackoverflow.com/questions/46175660/fetch-retry-request-on-failure

// or actually, there's a `fetch-retry` package that essentially
// operates the same as the 'fetch' package, but you can specify
// retry #s and delay time: https://www.npmjs.com/package/fetch-retry

// ------------------------------------------------------------------
// Write a JavaScript program that converts a callback-based 
// function to a Promise-based function.

// function myFunction(callback) {
//     return new Promise((resolve, reject) => {
//       Promise.resolve(callback())
//       .then(data => {
//         if (data) {
//             console.log("data retrieved!");
//             resolve(data);
//         }
//         throw new Error("no data retrieved.");
//       })
//       .catch( error => reject(error) )
//      });
//     }
  
//   function cbFunction() {
//       let result = "hey!! this is the callback!";
//       console.log(result);
//       return result;
//   }
    
//   myFunction(cbFunction);

// ------------------------------------------------------------------
// Practice ASYNC / AWAIT

function getData(endpoint) {
    return new Promise((resolve, reject) => {
        fetch(endpoint)
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error("fetch attempt failed.")
        })
        .then(data   => { resolve(data); })
        .catch(error => { reject(error); });
    });
}

async function returnData() {
    // let endpoint = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita";
    let endpoint = "https://shazam.p.rapidapi.com/shazam-events/list";
    try {
        const result   = await getData(endpoint); // returns response.json()
        return result;
    } catch(error) {
        console.log(`ERROR: ${error}`)
    }
}

async function displayData() {
    try {
        const result = await returnData();
        const length = result.drinks.length;
        
        for (let i = 0; i < length; i++){
            console.log(result.drinks[i].strDrink);
        }
    } catch (error) {
        console.log(`ERROR: ${error}`);
    }
}

// async function displayData() {
//     let result = await returnData();
//     if (result) {
//         let length = result.drinks.length;
        
//         for (let i = 0; i < length; i++){
//             console.log(result.drinks[i].strDrink);
//         }
//     } else {
//         console.log("Error: No data received");
//     }
// }

// returnData();
displayData();


// promiseFunc("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita")
// .then(nextFunction)
// .catch(handleError);

// ------------------------------------------------------------------
// Practice writing Promise function from scratch

// function promiseFunc(endpoint) {
//     return new Promise((resolve, reject) => {
//         fetch(endpoint)
//         .then(response => {
//             if (response.ok) {
//                 return response.json();
//             }
//             throw new Error("fetch attempt failed.")
//         })
//         .then(data   => { resolve(data); })
//         .catch(error => { reject(error); });
//     });
// }

// promiseFunc("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita")
// .then(nextFunction)
// .catch(handleError);


// ------------------------------------------------------------------
// Promise with actual async function call (fetch) --
// implement error-handling within promise

// function promiseFunc(){
//     return new Promise((resolve, reject) => {
//         let endpoint = "https://shazam.p.rapidapi.com/shazam-events/list";
//         // let endpoint = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita";
//         fetch(endpoint)
//         .then(response => {
//             // console.log(response);
//             if (response.ok) {
//                 return response.json();
//             }
//             throw new Error('Failed to fetch ☹️');
//         })
//         .then(data   => { resolve(data); })
//         .catch(error => { reject(error); });
//     });
// }

function nextFunction(data) {
    console.log("THIS IS THE RESOLVED DATA");
    console.log(data);
    // console.log(Object.keys(data)[0][1]);
    return data;
}

function handleError(error) {
    console.log("Error:", error)
    return error
}

// promiseFunc()
//     .then(nextFunction)
//     .catch(handleError);

// ------------------------------------------------------------------
// Initial Promise attempt -- practice resolve/ reject
// and promise chaining (with catch)

//     function promiseFunc(){
//     return new Promise((resolve, reject) => {
//         // console.log("what the heck")
//         // async function call... 
//         let result = "async call data";
//         // let result;

//         if (result) {
//             resolve("hell yeah brother.");
//         } else {
//             reject("uh oh. you've got a problem, brother.");
//         }
//     });
// }

// promiseFunc()
//     .then(console.log("neat-o"))
//     .then(message => console.log(message))
//     .catch(error  => console.log(error));
// TWO WAYS to delcare a new array--
// 1
let rappers: string[] = ["Lil Dicky", "Kash Doll", "Rich Homie Quan"];
// 2
let famousRappers     = new Array<string>("Megan Thee Stallion", "Kanye West", "Future");

// console.log(rappers);
// console.log(famousRappers);

// --------------------------------------
// add new item to array
famousRappers.push("Cardi B");

// iteratively print items in array
for (let rapper of famousRappers) {
    console.log("Rapper: " + rapper);
}

// remove item from array
rappers.pop()   // removes LAST ITEM and returns
rappers.shift() // removes FIRST ITEM and returns

// print new array
console.log("rappers: " + rappers)

// print item at index of array
console.log("Famous rapper: " + famousRappers[1]);

// COME BACK -- FOLLOW LINK BELOW FOR MORE OPERATIONS
// https://www.tutorialsteacher.com/typescript/typescript-array
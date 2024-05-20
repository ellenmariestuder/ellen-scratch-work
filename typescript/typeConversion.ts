// number to string
const length : number = 5;
const strLen : string = String(length);

console.log("length: " + length);
console.log("length type: " + typeof length);
console.log("strLen: " + strLen);
console.log("strLen type: " + typeof strLen);

// string to number
const width : string = "10";
const strWd : number = +width;

console.log("width: " + width);
console.log("width type: " + typeof width);
console.log("strWd: " + strWd);
console.log("strWd type: " + typeof strWd);


export {}; // declares file as ES Module
// "If the file doesn’t have an import or export statement, 
// it is treated as a script whose contents are available 
// in the global scope."
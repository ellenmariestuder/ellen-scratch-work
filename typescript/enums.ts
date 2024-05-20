// ENUMS: "a set of named constants"...

// HIGH-LEVEL
//   - enums are technically more like dictionaries than arrays
//   - they are intended to be immutable (though properties _can_ be added/ changed)
//   - "used when a variable or parameter can only take one out of a small set of possible values"
//   - "[enums] convey that these values are closely related and exclusive"
//   - SPECIAL FEATURE: BACKWARDS MAPPING !!
//     ^^ you can get value from key (normal) ~ OR ~ key from value!!

// DECLARING ENUMS
//   - you can explicitly set values for members (like a dicitonary)
//   - if you don't set values, the value will default to the index
//     ^^ enums are ORDERED data structures!

// Revisiting the 'Resistor Color' exercise from Exercism...
// https://exercism.org/tracks/typescript/exercises/resistor-color

export enum COLORS {
    black,  // notice: 'keys' don't need to be put in quotes (even if strings)
    brown, 
    red, 
    orange, 
    yellow,
    green, 
    blue, 
    violet, 
    grey,
    white
}

// get value from color
export const colorCode = (color: string): number | object => { 
    if (color in COLORS) {
        return COLORS[color as keyof typeof COLORS]; // must explicityly declare that 'color' will be a key
    } else if (color === "COLORS") {
        const allColors = Object.keys(COLORS).filter(key => isNaN(Number(key))); // **
        return allColors;
    }
    throw new Error("Invalid color");
 }

console.log("black: "      + colorCode("black"));
console.log("all colors: " + colorCode("COLORS"));
// console.log("fuschia: " + colorCode("fuschia"));

// ** this filter...
//    > Number(key) converts any numeric keys that are numbers to Number type
//    > isNan() looks for keys that couldn't be converted to Number
//    > filter() grabs keys that match the conditions set above...
//      so here: if a key is NaN after converting keys -> Number, then 
//      return that key

// get color from value
export function colorValueMap(value: number) {
    return COLORS[value];
}

console.log("expected = green: " + colorValueMap(5));

// "Create a variable 'selectedColor' of type 'Color' and assign it one
//  of the enumeration values."
type color = string;
let selectedColor: color = COLORS[0];
console.log("selected color: " + selectedColor);
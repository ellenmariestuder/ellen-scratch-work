// TA vs Interface :
//   Interfaces only apply to 'object' types
//   Type Aliases are like interfaces, but they can be 
//     used for any type


type stageName = string;   // type alias
type numAlbums = number;   // type alias
type talented  = boolean;  // type alias

type Musician = {          // type alias
    name   : stageName,
    albums : numAlbums,
    good   : talented
}

// note ^^ not an interface because doesn't use 
//         'interface' keyword

const stageName = "Lil Dicky";
const numAlbums = 2;
const talented  = true;

const DaveBird = {
    name   : stageName,
    albums : numAlbums,
    good   : talented
}

console.log(DaveBird.name)
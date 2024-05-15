// TO-DO: ERROR-HANDLING??

function mainFunction(callback) {
    console.log("Main function!!");
    setTimeout(() => callback(), 1000);
    return " ";
}

function cbFunction() {
    console.log("Callback function!!");
}


mainFunction(cbFunction);
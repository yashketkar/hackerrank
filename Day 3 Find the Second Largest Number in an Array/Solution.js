function processData(myArray) {
    var max=0;
for(var i=0;i<myArray.length;i++)
    {
        if(myArray[i]>max)
            max=myArray[i];
    }
    var max2=0;
    for(var i=0;i<myArray.length;i++)
    {
        if(myArray[i]>max2&&myArray[i]<max)
            max2=myArray[i];
    }
    console.log(max2);
}


// tail starts here
process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input.split('\n')[1].split(' ').map(Number));
});

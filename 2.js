start = Date.now()
var i = 1;
while (i < 1001) {
    console.log(i);
    i++;
}
end = Date.now() - start
console.log(end + " ms")
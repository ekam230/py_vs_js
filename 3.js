start = Date.now()
function func(a,b) {
    console.log(a ** b);
}
func(123, 123);
end = Date.now() - start
console.log(end + " ms")
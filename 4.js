start = Date.now()
for (var i = 1; i < 1001; i++) {
    if (i % 5 == 0) {
        console.log(i ** 10)
    } else {
        console.log(i ** 123)
    }
}
end = Date.now() - start
console.log(end + " ms")
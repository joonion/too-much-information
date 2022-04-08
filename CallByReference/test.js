function swap(x, y) {
    return [y, x]
}
var x=1, y=2;
console.log(x+" "+y);
[x, y] = swap(x, y);
console.log(x+" "+y)
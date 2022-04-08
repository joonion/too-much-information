function swap(x, y) {
    return [y, x]
}

var x = 10, y = 20;
console.log('Before swap():' + x + ' ' + y);
[x, y] = swap(x, y)
console.log('After swap():' + x + ' ' + y);

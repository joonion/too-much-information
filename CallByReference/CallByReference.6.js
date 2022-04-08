function swap(x, y) {
    var t = x;
    x = y;
    y = t;
    console.log('Inside swap():' + x + ' ' + y)
}

let x = 10, y = 20;
console.log('Before swap():' + x + ' ' + y)
swap(x, y)
console.log('After swap():' + x + ' ' + y)

function swap(x, y) {
    return [y, x]    
}

var x = 10, y = 20;
console.log('Before swap():' + x + ' ' + y);
[x, y] = [y, x]
console.log('After swap():' + x + ' ' + y);

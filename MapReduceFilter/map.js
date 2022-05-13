const a1 = [1, 2, 3, 4, 5]
const a2 = a1.map(val => val * 2)
console.log(a1)
console.log(a2)

const a3 = a1.map((val, ind, arr) => {
    console.log(val, ind, arr);
    return val * 2;
})
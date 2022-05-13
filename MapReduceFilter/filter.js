const a1 = [1, 2, 3, 4, 5]
const a2 = a1.filter(val => val % 2 == 0)
console.log(a2)

const a3 = a1.filter((val, ind, arr) => {
    console.log(val, ind, arr);
    return val % 2 == 1;
})
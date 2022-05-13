const a1 = [1, 2, 3, 4, 5]
const a2 = a1.reduce((acc, curr) => {
    console.log(acc, curr, acc + curr);
    return acc + curr;
})
console.log(a2)

const a3 = a1.reduce((acc, curr) => {
    console.log(acc, curr, acc + curr);
    return acc + curr;
}, 1000)
console.log(a3)
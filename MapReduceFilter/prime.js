var N = 10
numbers = Array.from({length: N}, (v, i) => i + 1)
console.log(numbers)

divs = numbers.reduce((acc, curr) => {
    console.log(acc, curr);
    if (N % curr == 0) return acc + 1;
    else return acc;
}, 0)
console.log(divs)

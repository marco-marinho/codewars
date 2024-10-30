function fibonacci(n) {
    if (n < 2) return n;
    function aux(n) {
        let a = 0, b = 1, c;
        for (let i = 0; i < n - 1; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return b
    }
    return aux(n);
}
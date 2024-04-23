const asyncTimeout = (ms) => {
    return new Promise(() => {
      setTimeout(() => {
        console.log('done');
        process.exitCode = 1;
      }, ms);
    });
  };
function main() { 
    for (let i = 0; i >= 0; i++) {
        asyncTimeout(10)
        console.log(i);
    }
}
asyncTimeout(10)
main()
  
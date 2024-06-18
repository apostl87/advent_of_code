const delay = ms => new Promise(res => setTimeout(res, ms));

async function test() {
  console.log(Date.now())
  await delay(100)
  console.log(Date.now())
}
test()
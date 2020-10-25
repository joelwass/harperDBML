fs = require('fs')
const { ulid } = require('ulid')

const testData = () => {
  let input = 'id,temperature,clouds,rain,confidence\n'
  let output = 'id,skydiving\n'
  let trainingSize = 50000
  for (let i = 0; i < trainingSize; i++) {
    let id = ulid()
    let temp = Math.round(Math.random() * 100)
    let clouds = Math.round(Math.random())
    let rain = Math.round(Math.random())
    let confidence = Math.round(Math.random() * 10)

    input += `${id},${temp},${clouds},${rain},${confidence}\n`

    if (temp > 80 && clouds === 0 && rain === 0 && confidence > 7) {
      output += `${id},1\n`
    } else {
      output += `${id},0\n`
    }
  }
  return {
    input,
    output
  }
}

const { input, output } = testData()

fs.writeFile('testinput.csv', input, function (err) {
  if (err) return console.log(err)
  console.log('written')
})

fs.writeFile('testoutput.csv', output, function (err) {
  if (err) return console.log(err)
  console.log('written')
})
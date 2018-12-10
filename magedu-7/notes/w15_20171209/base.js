// console.log(1)

// 注释

// 单行注释

/*
多汗注释
多汗注释
多汗注释
*/

// 变量/常量

// var v = 3 ; // 兼容旧版本
// console.log(v)

// let x = 4 // ES6 新引入的
// console.log(x)

// const x = 5;
// let y = 6;
// y = 7;
// x = 7
// console.log(x)

// const x = 5
// const x = 6

// let x = 5
// let x = 6

// 无论常量还是变量 都不可以重新定义

// 数据类型
// - number
// - boolean
// - string
// - null/undefined
// - object
// - array

// const x = 3
// console.log(typeof(x))

// const y = 'hello world'
// console.log(typeof(y))

// const z = x + y
// console.log(typeof(z))

// console.log(typeof(3 + false)) // number
// console.log(typeof(false + 'hello world')) // string
// console.log(typeof(3 + null)) // number
// console.log(typeof('hello world' + null)) // string
// console.log(typeof(false + null)) // number
// console.log(typeof(null + undefined)) // number

// null/undefined < boolean < number < string
// 优先级低的和优先级高的进行运算后，隐式转换为优先级大的类型

// let x
// console.log(x == undefined)

// x = null
// console.log(x == null)

// console.log(null == undefined)

// let x = {
//     a: 3
// }

// console.log(x.b === undefined)
// console.log(x.b === null)

// 当一个变量已经定义，但是未赋值，或者一个对象不存在属性的时候，是undefined
// null 是需要显示赋值为null的

// 在bool 运算中，null 和undefined 都等价于fale

// 字符串

// let x = "this is a string"
// let y = 'this is also a string'
// let z = '''this is is string'''

// let z = `this is
// a
// br
// line
// pappa
// `
// console.log(z)

// let x = 'miracle'
// let z = `hello ${x}`
// console.log(z)

// 运算符和表达式
// console.log(3 + 5)
// console.log(3 - 5)
// console.log(3 * 5)
// console.log(3 / 5)
// console.log(3 % 5)

// console.log(3++)
// let y = 3
// console.log(++y)
// console.log(y)
// 自增运算只能作用在变量上，不能作用在常量上

// 比较运算
// console.log(3 < 5)
// console.log(3 <= 5)
// console.log(3 > 5)
// console.log(3 >= 5)
// console.log(3 == 5)
// console.log(3 != 5)

// console.log(3 === 5)
// console.log(3 !== 5)

// console.log('3' == 3) // 只做值比较
// console.log('3' === 3) // 还比较类型

// let a = {
//     x: 3
// }

// let b = {
//     x: 3
// }

// let c = a

// console.log(a == b)
// console.log(a === b)

// 逻辑运算符
// console.log(true && false) // and
// console.log(true || false) // or
// console.log(!false) // not

// function yes(){
//     console.log('yes')
//     return true
// }

// function no(){
//     console.log('no')
//     return false
// }

// console.log(yes() || no())
// console.log(yes() && no())
// console.log(no() && yes())

// 三元运算

// 条件 ? 真值 : 假值

// console.log(3 > 5 ? '3>5' : '3<=5')

// let x
// if (3 > 5) {
//     x = '3>5'
// }else{
//     x = '3 <= 5'
// }
// console.log(x)

// x, y = 1, 2

// let x = 3, y = 5
// let a, b, c
// console.log(x)
// console.log(y)

// del
// delete

// let x = 3
// console.log(x)

// {
//     let x = 4
//     console.log(`x in block is ${x}`)
// }
// console.log(`x is ${x}`)

/*
- 从ES6开始，es 开始支持块级作作用域
- 每对大括号定义一个新的语句块
- 每对大括号会开启一个新的作用域
*/

// 流程控制

// if (3 > 5) {
//     console.log('3 > 5')
// } else {
//     console.log('3 < 5')
// }

// let x = 5
// if (x < 3) {
//     console.log('x<3')
// }else if (x < 5){
//     console.log('less 5')
// }else{
//     console.log('not less 5')
// }

// let x = 2
// switch (x) {
//     case 1:
//         console.log(1)
//         break
//     case 2:
//         console.log(2)
//         break
//     default:
//         console.log(3)
//         break;
// }

// let y = 1
// switch (y) {
//     case y > 1:
//         console.log('y > 1')
//         break;
//     default:
//         console.log('err')
//         break;
// }

// switch (true) {
//     case y > 1:
//         console.log('y > 1')
//         break;

//     default:
//         console.log('err')
//         break;
// }

// switch (true) {
//     case y < 3:
//         console.log('y <3')
//         break;
//     case y == 1:
//         console.log('y = 1')
//         break
//     case y == 5:
//         console.log('y = 5')
//     default:
//         console.log('err')
//         break;
// }

// 循环语句

// C 风格的for 循环
// for (let x = 0; x < 10; x++) {
//     console.log(x)
    
// }

// for .. in 

// let arr = [1, 2, 3, 4]
// let obj = {
//     a: 1,
//     b: 2,
//     c: 3
// }

// for (let idx in arr){
//     console.log(`${idx} => ${arr[idx]}`)
// }

// for (let key in obj) {
//     console.log(`${key} => ${obj[key]}`)
// }

// for (let v of obj){
//     console.log(v)
// }


// while

// let x = 0
// while (x < 10) {
//     console.log(x)
//     x++
// }

// let x = 11
// do{
//     console.log(x)
//     x++
// }while(x < 10)

// 标签
// for (let x of [0, 1, 2, 3]){
//     for(let y of [2, 3, 4, 5]){
//         if (y > 2) {
//             break
//         }
//         console.log(`${x} -> ${y}`)
//     }
// }
// break 是break  最近的一层
// outter: for (let x of [0, 1, 2, 3]){
//     for(let y of [2, 3, 4, 5]){
//         if (y > 2) {
//             break outter
//         }
//         console.log(`${x} -> ${y}`)
//     }
// }
// 函数
// 函数的定义

// function add(x, y){
//     return x +  y
// }

// let val = add(1, 3)
// console.log(val)

// 匿名函数，函数表达式
// const add = function(x, y){
//     return x + y
// }
// let val = add(1, 3)
// console.log(val)

// let val = function(x, y){
//     return x + y
// }(1, 3)
// console.log(val)

// 命名函数表达式
// const add = function _add(x, y){
//     return x + y
// }
// const val = add(1, 3)
// console.log(val)

// function _add(x, y){
//     return x + y
// }

// const add = _add
// const val = add(1, 3)
// console.log(val)

// function fab(x){
//     if (x < 2){
//         return 1
//     }
//     return fab(x - 1) + fab(x - 2)
// }

// // console.log(fab(5))
// const fab2 = fab
// console.log(fab2(5))
// delete fab
// console.log(fab2(5))

// const fab = function(x) {
//     if (x < 2){
//         return 1
//     }
//     return fab(x - 1) + fab(x - 2)
// }

// let fab = function(x) {
//     if (x < 2){
//         return 1
//     }
//     return fab(x - 1) + fab(x - 2)
// }

// let fab = function _fab(x) {
//     if (x < 2){
//         return 1
//     }
//     return _fab(x - 1) + _fab(x - 2)
// }

// const fab2 = fab
// console.log(fab2(5))
// fab =function(){}

// console.log(fab2(5))

// 高阶函数
// const map = function(arr, fn){
//     const result = []
//     for (let v of arr) {
//         result.push(fn(v))
//     }
//     return result
// }

// const square = function(x){
//     return x * x
// }

// const val = map([1, 2, 3, 4], square)
// console.log(val)

// const val = map([1, 2, 3, 4], function(x){
//     return x * x
// })
// console.log(val)

// 箭头函数
// const square = (x) => {
//     return x * x
// }
// console.log(square(4))

// const square = x => {
//     return x * x
// }

// const square = x => x * x

// const map = function(arr, fn){
//     const result = []
//     for (let v of arr) {
//         result.push(fn(v))
//     }
//     return result
// }

// const val = map([1, 2, 3, 4], x => x * x)
// const val = map([1,2, 3, 4], x => {
//     console.log(x)
//     return x * x
// })

// const counter = function(){
//     let c = 0
//     return function(){
//         return ++c
//     }
// }

// const c = counter()
// for (let x in [1, 2, 3, 4]){
//     console.log(c())
// }

// 函数参数
// const add = function(x, y){
//     return x + y
// }
// add(1, 4)

// 默认参数
// const add = function(x, y=6){
//     return x + y
// }
// console.log(add(1))

// const add = function(x=6, y){
//     return x + y
// }
// console.log(add(y=1))

// 目前还没有关键字canshu

// 可变位置参数
// const sum = function(...args){
//     console.log(args)
// }
// sum(1,2,3)

// const sum = function(...args){
//     let ret = 0
//     for (let v of args){
//         ret += v
//     }
//     return ret
// }
// const val = sum(1, 2, 3)
// console.log(val)

// 没有可变关键字参数

// const add = function(x, y){
//     return x + y
// }

// // 参数解构
// console.log(add(...[1, 2]))
// // 不能解构字典
// console.log(add(...{x: 1, y: 2}))

// const fn = function(...args){
//     console.log(arguments)
//     console.log(args)
// }
// fn(1,2, 3, 4)
// 在ES6 之前， js 都是通过一个叫做arguments 的 关键字

// const fn = function(){
//     // 只会返回最后一个结果
//     return [1, 2]
// }
// console.log(fn())

// function Point(x, y){
//     this.x = x
//     this.y = y
//     this.print = function(){
//         console.log(`<${this.x}, ${this.y}>`)
//     }
// }

// let point = new Point(3, 5)
// console.log(point.x)
// point.print()

// function Point3D(x, y, z){
//     Point.call(this, x, y)
//     this.z = z
// }
// let point3d = new Point3D(1,2, 3)
// console.log(point3d.x)
// console.log(point3d.y)
// console.log(point3d.z)
// point3d.print()

// class Point{
//     // def __init__(self, x, y):
//         // self.x = x
//         // self.y = y
//     constructor(x, y){
//         this.x = x
//         this.y = y
//     }
//     print(){
//         console.log(`${this.x}, ${this.y}`)
//     }

//     static info(){
//         console.log('this is a static method')
//     }
// }

// let point = new Point(1, 2)
// point.info()
// Point().info()
// Point.info()
// (new Point(1, 2)).info()

// point.constructor.info()

// console.log(point.x)
// console.log(point.y)
// point.print()

// ES类 没有私有属性

// 静态方法

// 静态属性/类变量
// class Point{
//     static offset = {
//         x: 1,
//         y: 2
//     }
// }

// console.log(Point.offset)

// this 的坑

// class Point{
//     constructor(x, y){
//         this.x = x
//         this.y = y
//     }

//     print(format) {
//         console.log(format())
//     }

//     format(){
//         return `<${this.x}, ${this.y}>`
//     }
// }

// let point = new Point(3, 5)
// point.print(point.format)
// point.format()
// console.log(point.format())

// class Point{
//     constructor(x, y){
//         this.x = x
//         this.y = y
//     }

//     print(format) {
//         console.log(this)
//         console.log(format())
//     }

//     format(){
//         console.log(this)
//         return ''
//         // return `<${this.x}, ${this.y}>`
//     }
// }

// let point = new Point(3, 5)
// point.print(point.format)


// class Point{
//     constructor(x, y){
//         this.x = x
//         this.y = y
//     }

//     print(format) {
//         console.log(this)
//         console.log(format())
//     }

//     format(self){
//         console.log(self)
//         // return ''
//         return `<${self.x}, ${self.y}>`
//     }
// }

// let point = new Point(3, 5)
// point.print(point.format)
// // console.log(point.format(point))

// class Point{
//     constructor(x, y){
//         this.x = x
//         this.y = y

//         this.format = this.format.bind(this)
//     }

//     print(format) {
//         console.log(this)
//         console.log(format())
//     }

//     format(){
//         console.log(this)
//         // return ''
//         return `<${this.x}, ${this.y}>`
//     }
// }

// let point = new Point(3, 5)
// point.print(point.format)
// console.log(point.format(point))


// class Point{
//     constructor(x, y){
//         this.x = x
//         this.y = y

//         this.format = () => {
//             return `<${this.x}, ${this.y}>`
//         }
//     }

//     print(format) {
//         console.log(this)
//         console.log(format())
//     }

//     // format(){
//     //     console.log(this)
//     //     // return ''
//     //     return `<${this.x}, ${this.y}>`
//     // }
// }

// let point = new Point(3, 5)
// point.print(point.format)
// console.log(point.format(point))

// class Point{
//     constructor(x, y){
//         this.x = x
//         this.y = y

//         this.format = () => {
//             return `<${this.x}, ${this.y}>`
//         }
//     }

//     print(format) {
//         console.log(this)
//         console.log(format())
//     }

// }

// class Point3D extends Point {
//     constructor(x, y, z){
//         super(x, y)
//         this.z = z
//     }
// }

// class Point3D extends Point {
//     constructor(x, y, z){
//         console.log(`<x: ${x}, y: ${y}>`)
//         // this.z = x + y // this 不能再super 之前使用
//         super(x, y)
//         this.z = z
//     }
// }

// class Point3D extends Point {
//     constructor(x, y, z){
//         console.log(`<x: ${x}, y: ${y}>`)
//         // this.z = x + y // this 不能再super 之前使用
//         super(x, y)
//         this.z = z
//     }

//     // print(format) {
//     //     super.print(format)
//     //     console.log(this.z)
//     // }

//     format(){
//         return super.format() + 'xxx'
//     }
// }

// class Point{
//     constructor(x, y){
//         this.x = x
//         this.y = y

//         this.format = this.format.bind(this)

//     }

//     print(format) {
//         console.log(this)
//         console.log(format())
//     }

//     format(){
//         console.log(this)
//         return `<${this.x}, ${this.y}>`
//     }
// }

// class Point3D extends Point {
//     constructor(x, y, z) {
//         console.log(`<x: ${x}, y: ${y}>`)
//         super(x, y)
//         this.z = z
//         this.format = this.format.bind(this)
//     }

//     format(){
//         return super.format() + 'xxx'
//     }
// }


// let p = new Point3D(3, 5, 8)
// p.print(p.format)

// 高阶对象 MixIn

// class Serializable {
//     constructor(){
//         if (typeof(this.constructor.stringify) !== 'function'){
//             throw new ReferenceError('must be define stringify')
//         }
//         if(typeof(this.constructor.parse) !== 'function'){
//             throw new ReferenceError('must be define parse')
//         }
//     }

//     toString(){
//         return this.constructor.stringify(this)
//     }
// }

const Serializable = Sup => class extends Sup {
    constructor(...arg){
        super(...arg)
        if (typeof(this.constructor.stringify) !== 'function'){
            throw new ReferenceError('must be define stringify')
        }
        if(typeof(this.constructor.parse) !== 'function'){
            throw new ReferenceError('must be define parse')
        }
    }

    toString(){
        return this.constructor.stringify(this)
    }
}

class Point {
    constructor(x, y) {
        // super()
        this.x = x
        this.y = y
    }

    // static stringify(instance) {
    //     return `${instance.x}, ${instance.y}`
    // }

    // static parse(data) {
    //     const arr = data.split(',')
    //     return Point(Number.parseInt(arr[0]). Number.parseInt(arr[1]))
    // }
}

// class Point3D extends Serializable(Point) {
//     constructor(x, y, z) {
//         super(x, y)
//         this.z = z
//     }
    
//     static stringify(instance) {
//         return `${instance.x}, ${instance.y}`
//     }

//     static parse(data) {
//         const arr = data.split(',')
//         return Point(Number.parseInt(arr[0]). Number.parseInt(arr[1]))
//     }

// }

@Serializable
class Point3D extends Point {
    constructor(x, y, z) {
        super(x, y)
        this.z = z
    }
    
    static stringify(instance) {
        return `${instance.x}, ${instance.y}`
    }

    static parse(data) {
        const arr = data.split(',')
        return Point(Number.parseInt(arr[0]). Number.parseInt(arr[1]))
    }

}

let p3 = new Point3D(1, 2, 3)
console.log(p3.toString())

// let p = new Point3D()
// console.log(p.toString())

// let point = new Point(1, 3)
// console.log(point.toString())
var app = new Vue({
    delimiters: ['[[', ']]'],
    el:'#app',
    data:{
       count: 0,
       hello: 'world',
    },
    methods:{
     plus:function(){
      this.count++
     }
    }
 })

 var app2 = new Vue({
    delimiters: ['[[', ']]'],
    el:'#edits',
    data:{
    },
    methods:{
    edit:function(){
      console.log("test")
      app.count++
     }
    }
 })
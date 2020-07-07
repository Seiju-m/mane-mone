Vue.component('modal', {
   template: '#modal-template'
})

var md = new Vue({
   el: '#modal',
   data: {
      food_st_e: 0,
      food_ex_e: 0,
      showModal: false,
      formData: {
         food_st_e: 0,
         food_ex_e: 0
      }
   },
   methods: {
      test: function (test, test2) {
         this.showModal = 1
         console.log("tessssss" + test + test2)
         this.food_st_e = test
         this.food_ex_e = test2
      },
      submit: function () {
         this.formData.food_ex_e = 444
         this.formData.food_st_e = 8000
         axios.post('/food', this.formData)
            .then(response => {
               console.log("response" + response)
            })
            .catch(error => {
               console.log("error" + error)
            })
         console.log("submitted")
      }
   }
})


var app = new Vue({
   delimiters: ['[[', ']]'],
   el: '#app',
   data: {
      count: 0,
      hello: 'world',
   },
   methods: {
      plus: function () {
         this.count++
      }
   }
})

var app2 = new Vue({
   delimiters: ['[[', ']]'],
   el: '#edits',
   data: {
   },
   methods: {
      edit: function () {
         console.log("test")
         app.count++
      }
   }
})


// var fs = new Vue({
//    delimiters: ['[[', ']]'],
//    el:'#food_submit',
//    methods: {
//       submit: function() {
//          console.log("submitted")
//       }
//    }
// })
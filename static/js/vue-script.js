Vue.component('modal', {
   template: '#modal-template'
})

function toggle_clicked(checked, food_data, daily_data, hobby_data) {
   if (md.checked == true) {
      md.per = '週'
      md.food_data = parseInt(food_data.split(",").join("") / 4)
      md.daily_data = parseInt(daily_data.split(",").join("") / 4)
      md.hobby_data = parseInt(hobby_data.split(",").join("") / 4)
      md.checked = false
   } else {
      md.per = '月'
      md.checked = true
   }
}

var md = new Vue({
   delimiters: ['[[', ']]'],
   el: '#modal',
   data: {
      st_val: 0,
      ex_val: 0,
      checkedd: true,
      checked: true,
      per: '月',
      food_data: 0,
      daily_data: 0,
      hobby_data: 0,
      showModal: false,
      formData: {
         st_val: 0,
         ex_val: 0,
         cat: ''
      },
   },
   methods: {
      f_edit: function (st_val, ex_val) {
         this.showModal = 1
         this.st_val = st_val
         this.ex_val = ex_val
      },
      d_edit: function (st_val, ex_val) {
         this.showModal = 2
         this.st_val = st_val
         this.ex_val = ex_val
      },
      h_edit: function (st_val, ex_val) {
         this.showModal = 3
         this.st_val = st_val
         this.ex_val = ex_val
      },
      r_edit: function (st_val) {
         this.showModal = 4
         this.st_val = st_val
      },
      s_edit: function (st_val) {
         this.showModal = 5
         this.st_val = st_val
      },
      u_edit: function (st_val) {
         this.showModal = 6
         this.st_val = st_val
      },
      o_edit: function (st_val) {
         this.showModal = 7
         this.st_val = st_val
      },
      i_edit: function (st_val) {
         this.showModal = 8
         this.st_val = st_val
      },
      submit: function (cat) {
         this.formData.cat = cat
         switch (cat) {
            case 'food':
               this.formData.ex_val = document.forms.food_e.food_ex_e.value
               this.formData.st_val = document.forms.food_e.food_st_e.value
               break;
            case 'daily':
               this.formData.ex_val = document.forms.daily_e.daily_ex_e.value
               this.formData.st_val = document.forms.daily_e.daily_st_e.value
               break;
            case 'hobby':
               this.formData.ex_val = document.forms.hobby_e.hobby_ex_e.value
               this.formData.st_val = document.forms.hobby_e.hobby_st_e.value
               break;
            case 'rent':
               this.formData.st_val = document.forms.rent_f_e.rent_e.value
               break;
            case 'scholar':
               this.formData.st_val = document.forms.scholar_f_e.scholar_e.value
               break;
            case 'util':
               this.formData.st_val = document.forms.util_f_e.util_e.value
               break;
            case 'other':
               this.formData.st_val = document.forms.other_f_e.other_e.value
               break;
            case 'income':
               this.formData.st_val = document.forms.income_f_e.income_e.value
               break;
         }
         console.log("formdata" + JSON.stringify(this.formData))
         $.LoadingOverlay("show");
         axios.post('/update', this.formData)
            .then(response => {
               console.log("response" + response)
               // setTimeout(() => {
               $.LoadingOverlay("hide");
               this.showModal = false
               document.location.reload()
               // }, 3000)
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

// var wm_toggle = new Vue({
//    delimiters: ['[[', ']]'],
//    el: '#w-m-toggle',
//    data: {
//       checked: true
//    },
//    methods: {
//       setEditEnable: function () {
//          console.log("toggleee")
//       }
//    }
// })


// var fs = new Vue({
//    delimiters: ['[[', ']]'],
//    el:'#food_submit',
//    methods: {
//       submit: function() {
//          console.log("submitted")
//       }
//    }
// })
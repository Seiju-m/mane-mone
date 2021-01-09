Vue.component('modal', {
   template: '#modal-template'
})

const path = location.pathname ;

date = new Date();
date.setMonth(date.getMonth() - 1 );
now_month = date.getFullYear() + ("0" + (date.getMonth() + 1)).slice(-2);

sessionStorage['month'] = now_month;

function toggle_clicked(checked, food_data, daily_data, hobby_data, transport_data, other_data) {
   if (md.checked == true) {
      md.per = '週'
      md.food_data = parseInt(food_data.split(",").join("") / 4).toLocaleString()
      md.daily_data = parseInt(daily_data.split(",").join("") / 4).toLocaleString()
      md.hobby_data = parseInt(hobby_data.split(",").join("") / 4).toLocaleString()
      md.transport_data = parseInt(transport_data.split(",").join("") / 4).toLocaleString()
      md.other_data = parseInt(other_data.split(",").join("") / 4).toLocaleString()
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
      transport_data: 0,
      other_data: 0,
      commu_data: 0,
      calc_obj: 0,
      showModal: false,
      EnterFlag: false,
      formData: {
         st_val: 0,
         ex_val: 0,
         cat: ''
      },
   },
   methods: {
      disp: function (n, food_ex) {
         var obj = document.getElementById("result");
         obj.value += n;
      },
      disp0: function (n, food_ex) {
         var obj = document.getElementById("result");
         obj.value = obj.value + n + n;
      },
      del: function () {
         var obj = document.getElementById("result");
         obj.value = obj.value.slice(0, -1);
      },
      enter: function () {
         var obj = document.getElementById("result");
         document.getElementById("food_ex_e").value = eval(obj.value);
         this.EnterFlag = true;
      },
      enter_d: function () {
         var obj = document.getElementById("result");
         document.getElementById("daily_ex_e").value = eval(obj.value);
         this.EnterFlag = true;
      },
      enter_h: function () {
         var obj = document.getElementById("result");
         document.getElementById("hobby_ex_e").value = eval(obj.value);
         this.EnterFlag = true;
      },
      enter_u: function () {
         var obj = document.getElementById("result");
         document.getElementById("util_e").value = eval(obj.value);
         this.EnterFlag = true;
      },
      enter_o: function () {
         var obj = document.getElementById("result");
         document.getElementById("other_ex_e").value = eval(obj.value);
         this.EnterFlag = true;
      },
      enter_c: function () {
         var obj = document.getElementById("result");
         document.getElementById("commu_e").value = eval(obj.value);
         this.EnterFlag = true;
      },
      enter_t: function () {
         var obj = document.getElementById("result");
         document.getElementById("transport_ex_e").value = eval(obj.value);
         this.EnterFlag = true;
      },
      enter_i: function () {
         var obj = document.getElementById("result");
         document.getElementById("income_e").value = eval(obj.value);
         this.EnterFlag = true;
      },
      clear: function (food_ex) {
         document.getElementById("result").value = 0
      },
      clear2: function (food_ex) {
         this.calc_obj = 0;
         this.calc_obj = document.getElementById("food_ex_e").value + '+';
      },
      clear_d: function (food_ex) {
         this.calc_obj = 0;
         this.calc_obj = document.getElementById("daily_ex_e").value + '+';
      },
      clear_c: function (food_ex) {
         this.calc_obj = 0;
         this.calc_obj = document.getElementById("commu_e").value + '+';
      },
      clear_h: function (food_ex) {
         this.calc_obj = 0;
         this.calc_obj = document.getElementById("hobby_ex_e").value + '+';
      },
      clear_t: function (food_ex) {
         this.calc_obj = 0;
         this.calc_obj = document.getElementById("transport_ex_e").value + '+';
      },
      clear_u: function (food_ex) {
         this.calc_obj = 0;
         this.calc_obj = document.getElementById("util_e").value + '+';
      },
      clear_o: function (food_ex) {
         this.calc_obj = 0;
         this.calc_obj = document.getElementById("other_ex_e").value + '+';
      },
      clear_i: function (food_ex) {
         this.calc_obj = 0;
         this.calc_obj = document.getElementById("income_e").value + '+';
      },
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
      c_edit: function (st_val) {
         this.showModal = 7
         this.st_val = st_val
      },
      i_edit: function (st_val) {
         this.showModal = 8
         this.st_val = st_val
      },
      t_edit: function (st_val, ex_val) {
         this.showModal = 9
         this.st_val = st_val
         this.ex_val = ex_val
      },
      o_edit: function (st_val, ex_val) {
         this.showModal = 10
         this.st_val = st_val
         this.ex_val = ex_val
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
            case 'transport':
               this.formData.ex_val = document.forms.transport_e.transport_ex_e.value
               this.formData.st_val = document.forms.transport_e.transport_st_e.value
               break;
            case 'other':
               this.formData.ex_val = document.forms.other_e.other_ex_e.value
               this.formData.st_val = document.forms.other_e.other_st_e.value
               break;
            case 'commu':
               this.formData.st_val = document.forms.commu_f_e.commu_e.value
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
      },
   }
})




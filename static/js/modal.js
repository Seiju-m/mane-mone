var createReport = new Vue({
    delimiters: ['[[', ']]'],
    el: '#navbar',
    data: {
        count: 0,
        hello: 'world',
        formData: {
            month: 000000,
            last: 0
        },
    },
    methods: {
        createReport: function (last) {
            // this.formData.cat = cat
            //   console.log("formdata" + JSON.stringify(this.formData))
            //   console.log("dataa" + data.food_ex)
            //   let now_month = sessionStorage.getItem('month')
            //   console.log("now_month" + now_month)
            //   this.formData.month = now_month
            //   $.LoadingOverlay("show");
            //   axios.post('/createReport', this.formData)
            //      .then(response => {
            //         if(response.data.status_code == '500'){
            //            console.log("already data")
            //         } else {
            //            if(path == '/monthly/'){
            //               reloads(response.data)
            //            console.log("reload")
            //            }
            //         }
            //         console.log("response" + JSON.stringify(response))
            //         // setTimeout(() => {
            //         $.LoadingOverlay("hide");
            //         this.showModal = false
            //         // document.location.reload()
            //         // }, 3000)
            //      })
            //      .catch(error => {
            //         console.log("error" + error)
            //      })
            Swal.fire({
                // title: 'Are you sure?',
                html:
                    '<b>2020年07月のレポートを作成しますか？</b>',
                icon: 'question',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: '作成',
                cancelButtonText: 'キャンセル'
            }).then((result) => {

                if (result.value) {

                    let now_month = sessionStorage.getItem('month')
                    console.log("now_month" + now_month)
                    this.formData.month = now_month
                    this.formData.last = last
                    $.LoadingOverlay("show");
                    axios.post('/createReport', this.formData)
                        .then(response => {
                            if (response.data.status_code == '500') {
                                console.log("already data")
                                $.LoadingOverlay("hide");
                                Swal.fire(
                                    '',
                                    '<b>既にレポートが存在しています</b>',
                                    'error'
                                )
                            } else {
                                if (path == '/monthly/') {
                                    // response.data.last = last
                                    // report.last = last
                                    // console.log("lastttttt" + last)
                                    reloads(response.data)
                                    $.LoadingOverlay("hide");
                                    Swal.fire(
                                        '<b>作成完了!</b>',
                                        '',
                                        'success'
                                    )
                                } else {
                                    Swal.fire(
                                        '<b>作成完了!</b>',
                                        '',
                                        'success'
                                    ),
                                    // report.last = last,
                                    $.LoadingOverlay("hide");
                                }
                            }
                            console.log("response" + JSON.stringify(response))
                            // setTimeout(() => {

                            // document.location.reload()
                            // }, 3000)
                        })
                        .catch(error => {
                            console.log("error" + error)
                        })
                }

                // if (result.value) {
                //     Swal.fire(
                //         '',
                //         '<b>作成完了</b>',
                //         'success'
                //     )
                // }
            })
        },
    }
})


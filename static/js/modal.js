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
            Swal.fire({
                html: '<b>' + now_month.slice(0,4) + '年' + now_month.slice(-2) + '月のレポートを作成しますか？</b>',
                icon: 'question',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: '作成',
                cancelButtonText: 'キャンセル'
            }).then((result) => {
                if (result.value) {
                    let now_month = sessionStorage.getItem('month')
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
                                    reloads(response.data)
                                    $.LoadingOverlay("hide");
                                    Swal.fire(
                                        '<b>作成完了!</b>',
                                        '',
                                        'success'
                                    )
                                } else {
                                    $.LoadingOverlay("hide");
                                    Swal.fire(
                                        '<b>作成完了!</b>',
                                        '',
                                        'success'
                                    )
                                }
                            }
                            console.log("response" + JSON.stringify(response))
                        })
                        .catch(error => {
                            console.log("error" + error)
                        })
                }
            })
        },
        info: function (last) {
            Swal.fire({
                html: '<h3>Operation Rule</h3>' + 
                '<div align="left" style="padding-left: 30px;">' +
                 '<br>【収入】交通費を含める' + 
                 '<br>【食費】Suicaでの使用分も計上する' +
                 '<br>【交通費】通勤代も計上する' +
                 '<br>【その他】美容院・トラノコ手数料など' +
                 '<br>【通信費】スマホ代・J-COM' +
                 '<br>【残高】トラノコへの投資も含む' +
                 '</div>' ,
                icon: 'question',
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'OK',
            })
        },
    }
})


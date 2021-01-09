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
            console.log('testtttttttt')
            console.log('now month:' + now_month)
            Swal.fire({
                html: '<b>' + now_month.slice(0,4) + '年' + now_month.slice(-2) + '月のレポートを作成しますか？</b>',
                icon: 'question',
                showCancelButton: true,
                confirmButtonColor: '#17A2B8',
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
                                Swal.fire({
                                    html:'<b>既にレポートが存在しています</b>',
                                    icon:'error',
                                    confirmButtonColor: '#17A2B8',
                                })
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
                html: '<h3>Operation Rule</h3> <br>' + 
                '<div align="left" style="padding-left: 30px;" class="info-box">' +
                 '<div class="info-text">【収入】交通費を含める</div>' + 
                 '<div class="info-text">【食費】Suicaでの使用分も計上する</div>' +
                 '<div class="info-text">【交通費】通勤代も計上する</div>' +
                 '<div class="info-text">【その他】美容院・トラノコ手数料など</div>' +
                 '<div class="info-text">【通信費】スマホ代・J-COM</div>' +
                 '<div class="info-text">【残高】トラノコへの投資も含む</div>' +
                 '</div>' ,
                icon: 'question',
                confirmButtonColor: '#17A2B8',
                confirmButtonText: 'OK',
            })
        },
    }
})


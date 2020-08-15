let income = document.getElementById('chart_income').value;
let food = document.getElementById('chart_food').value;
let daily = document.getElementById('chart_daily').value;
let hobby = document.getElementById('chart_hobby').value;
let transport = document.getElementById('chart_transport').value;
let other = document.getElementById('chart_other').value;
let last = document.getElementById('chart_last').value;
let rent = document.getElementById('chart_rent').value;
let scholar = document.getElementById('chart_scholar').value;
let utility = document.getElementById('chart_utility').value;
let commu = document.getElementById('chart_commu').value;
let month = document.getElementById('chart_month').value;

let date = new Date();
let now_month = date.getFullYear() + ("0" + (date.getMonth())).slice(-2);
sessionStorage['month'] = now_month;

var report = new Vue({
    delimiters: ['[[', ']]'],
    el: '#report',
    data: {
        formData: {
            month: 000000
        },
        title_month: sessionStorage.getItem('month').slice(0, 4) + '年' + sessionStorage.getItem('month').slice(-2) + '月',
        food: parseInt(food).toLocaleString(),
        daily: parseInt(daily).toLocaleString(),
        hobby: parseInt(hobby).toLocaleString(),
        transport: parseInt(transport).toLocaleString(),
        other: parseInt(other).toLocaleString(),
        rent: parseInt(rent).toLocaleString(),
        scholar: parseInt(scholar).toLocaleString(),
        utility: parseInt(utility).toLocaleString(),
        commu: parseInt(commu).toLocaleString(),
        last: last,
    },
    methods: {
        prev_month: function () {
            $.LoadingOverlay("show");
            let now_month = sessionStorage.getItem('month')
            this.formData.month = now_month

            // 年またぎ処理
            const pattern = /01$/g;
            const result = now_month.match(pattern);
            if (result != null) {
                sessionStorage['month'] = parseInt(now_month) - 89;
            } else {
                sessionStorage['month'] = parseInt(now_month) - 1;
            }

            axios.post('/prev-month', this.formData)
                .then(response => {
                    if (response.data.status_code == '201') {
                        no_reloads(response.data)
                    } else {
                        reloads(response.data)
                        console.log("response" + JSON.stringify(response.data))
                    }
                    $.LoadingOverlay("hide");
                })
                .catch(error => {
                    console.log("error" + error)
                })
        },
        next_month: function () {
            $.LoadingOverlay("show");
            let now_month = sessionStorage.getItem('month')
            this.formData.month = now_month

            // 年またぎ処理
            const pattern = /12$/g;
            const result = now_month.match(pattern);
            if (result != null) {
                sessionStorage['month'] = parseInt(now_month) + 89;
            } else {
                sessionStorage['month'] = parseInt(now_month) + 1;
            }

            axios.post('/next-month', this.formData)
                .then(response => {
                    if (response.data.status_code == '201') {
                        no_reloads(response.data)
                    } else {
                        reloads(response.data)
                        console.log("response" + JSON.stringify(response.data))
                    }
                    $.LoadingOverlay("hide");
                })
                .catch(error => {
                    console.log("error" + error)
                })
        }
    }
})

var chart = c3.generate({
    data: {
        columns: [
            ['食費', food],
            ['日用品', daily],
            ['趣味・娯楽', hobby],
            ['交通費', transport],
            ['その他', other],
            ['家賃', rent],
            ['奨学金', scholar],
            ['光熱費', utility],
            ['通信費', commu]
        ],
        bindto: '#chart',
        type: 'donut',
        empty: { label: { text: "データがありません" } },
    },
    color: {
        pattern: ['#ad2f20', '#1b9b50', '#7c369b', '#3949AB', '#df8c06', '#6D4C41', '#F4511E', '#D81B60', '#00897B']
    },
});

function reloads(data) {
    let month = sessionStorage.getItem('month');
    report.title_month = month.slice(0, 4) + '年' + month.slice(-2) + '月';
    report.last = data.last,
    report.food = parseInt(data.food).toLocaleString(),
    report.daily = parseInt(data.daily).toLocaleString(),
    report.hobby = parseInt(data.hobby).toLocaleString(),
    report.transport = parseInt(data.transport).toLocaleString(),
    report.other = parseInt(data.other).toLocaleString(),
    report.rent = parseInt(data.rent).toLocaleString(),
    report.scholar = parseInt(data.scholar).toLocaleString(),
    report.utility = parseInt(data.utility).toLocaleString(),
    report.commu = parseInt(data.commu).toLocaleString(),

    //元のグラフの削除
    chart.unload({
        ids: '食費'
    });
    chart.unload({
        ids: '日用品'
    });
    chart.unload({
        ids: '趣味・娯楽'
    });
    chart.unload({
        ids: '交通費'
    });
    chart.unload({
        ids: 'その他'
    });
    chart.unload({
        ids: '家賃'
    });
    chart.unload({
        ids: '奨学金'
    });
    chart.unload({
        ids: '光熱費'
    });
    chart.unload({
        ids: '通信費'
    });

    //新たなグラフの読み込み
    chart.load({
        columns: [
            ['食費', data.food],
            ['日用品', data.daily],
            ['趣味・娯楽', data.hobby],
            ['交通費', data.transport],
            ['その他', data.other],
            ['家賃', data.rent],
            ['奨学金', data.scholar],
            ['光熱費', data.utility],
            ['通信費', data.commu]
        ],
        empty: { label: { text: "No Data Available" } },
    })

}

function no_reloads(data) {
    let month = sessionStorage.getItem('month');
    report.title_month = month.slice(0, 4) + '年' + month.slice(-2) + '月';
    report.last = data.last,
    report.food = parseInt(data.food).toLocaleString(),
    report.daily = parseInt(data.daily).toLocaleString(),
    report.hobby = parseInt(data.hobby).toLocaleString(),
    report.transport = parseInt(data.transport).toLocaleString(),
    report.other = parseInt(data.other).toLocaleString(),
    report.rent = parseInt(data.rent).toLocaleString(),
    report.scholar = parseInt(data.scholar).toLocaleString(),
    report.utility = parseInt(data.utility).toLocaleString(),
    report.commu = parseInt(data.commu).toLocaleString(),

        //元のグラフの削除
    chart.unload({
        ids: '食費'
    });
    chart.unload({
        ids: '日用品'
    });
    chart.unload({
        ids: '趣味・娯楽'
    });
    chart.unload({
        ids: '交通費'
    });
    chart.unload({
        ids: 'その他'
    });
    chart.unload({
        ids: '家賃'
    });
    chart.unload({
        ids: '奨学金'
    });
    chart.unload({
        ids: '光熱費'
    });
    chart.unload({
        ids: '通信費'
    });
}

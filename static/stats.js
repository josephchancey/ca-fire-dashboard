// Load Data
d3.json(`/inactive/fires`).then(function (data) {
    console.log(data)
});

d3.json(`/active/fires`).then(function (data) {
    console.log(data)
});

d3.json(`/ca_burned`).then(function (data) {
    console.log(data)
});

// var burned_total = 

// var myChart = new Chart("myChart", {
//     type: "line",
//     data: {},
//     options: {}
//   });
var layout = {
    title: {
        text: 'Recorded Acreage Burnt By Year',
        font: {
            family: 'Courier New, monospace',
            size: 24
        },
        xref: 'paper',
        x: 0.05,
    },
    xaxis: {
        title: {
            text: 'Year',
            font: {
                family: 'Courier New, monospace',
                size: 18,
                color: '#7f7f7f'
            }
        },
    }
};

// ping route & Store data
d3.json(`/ca_burned`).then(function (myData) {
    console.log("Init now")
    let data = [
        {
            x: myData.map(x => x["Year"]),
            y: myData.map(x => x["Total_Recorded_Burnt_Acres"]),
            mode: 'markers',
            type: 'scatter'
        }
    ]
    console.log("let data = is now logged")
    // draw plot
    console.log("Plot should be drawn")
    Plotly.newPlot("myChart", data, layout);
    
});

// Render plot
d3.json(`/ca_burned`).then(function (myData) {
    console.log("We're in the active fires plot")
    // map values
    let newX = myData.map(x => x["Year"]);
    let newY = myData.map(x => x["Total_Recorded_Burnt_Acres"]);

    // restyle existing type plot
    Plotly.restyle("myChart", 'x', [newX]);
    Plotly.restyle("myChart", 'y', [newY]);

});

// //
// //
// //

// var layout2 = {
//     title: {
//         text: 'California Fire Total Acres Burned',
//         font: {
//             family: 'Courier New, monospace',
//             size: 24
//         },
//         xref: 'paper',
//         x: 0.05,
//     },
//     xaxis: {
//         title: {
//             text: 'Fire (Name)',
//             font: {
//                 family: 'Courier New, monospace',
//                 size: 18,
//                 color: '#7f7f7f'
//             }
//         },
//     },
//     yaxis: {
//         title: {
//             text: 'Acres Burned (acres)',
//             font: {
//                 family: 'Courier New, monospace',
//                 size: 18,
//                 color: '#7f7f7f'
//             }
//         }
//     }
// };

// // ping route & Store data
// d3.json(`/inactive/fires`).then(function (myData) {
//     console.log("Init now")
//     let data = [
//         {
//             x: myData.map(x => x.Name),
//             y: myData.map(x => x.AcresBurned),
//             mode: 'markers',
//             type: 'scatter'
//         }
//     ]
//     console.log("let data = is now logged")
//     // draw plot
//     console.log("Plot should be drawn")
//     Plotly.newPlot('test_stat_two', data, layout2);
    
// });

// // Render plot
// d3.json(`/inactive/fires`).then(function (myData) {
//     console.log("We're in the active fires plot")
//     // map values
//     let newX = myData.map(x => x.Name);
//     let newY = myData.map(x => x.AcresBurned);

//     // restyle existing type plot
//     Plotly.restyle('test_stat_two', 'x', [newX]);
//     Plotly.restyle('test_stat_two', 'y', [newY]);

// });

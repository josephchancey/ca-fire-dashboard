//Load Data
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

var test_stat_three = new Chart("test_stat_three", {
    type: "line",
    data: {},
    options: {}
  });
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
            y: myData.map(x => x["Total Recorded Burnt Acres"]),
            mode: 'markers',
            type: 'scatter'
        }
    ]
    console.log("let data = is now logged")
    // draw plot
    console.log("Plot should be drawn")
    Plotly.newPlot("test_stat_three", data, layout);
    
});

// Render plot
d3.json(`/ca_burned`).then(function (myData) {
    console.log("We're in the active fires plot")
    // map values
    let newX = myData.map(x => x["Year"]);
    let newY = myData.map(x => x["Total_Recorded_Burnt_Acres"]);

    // restyle existing type plot
    Plotly.restyle("test_stat_three", 'x', [newX]);
    Plotly.restyle("test_stat_three", 'y', [newY]);

});


var layout2 = {
    title: {
        text: 'California Fire Total Acres Burned',
        font: {
            family: 'Courier New, monospace',
            size: 24
        },
        xref: 'paper',
        x: 0.05,
    },
    xaxis: {
        title: {
            text: 'Fire (Name)',
            font: {
                family: 'Courier New, monospace',
                size: 18,
                color: '#7f7f7f'
            }
        },
    },
    yaxis: {
        title: {
            text: 'Acres Burned (acres)',
            font: {
                family: 'Courier New, monospace',
                size: 18,
                color: '#7f7f7f'
            }
        }
    }
};

// ping route & Store data
d3.json(`/inactive/fires`).then(function (myData) {
    console.log("Init now")
    let data = [
        {
            x: myData.map(x => x.Name),
            y: myData.map(x => x.AcresBurned),
            mode: 'markers',
            type: 'scatter'
        }
    ]
    console.log("let data = is now logged")
    // draw plot
    console.log("Plot should be drawn")
    Plotly.newPlot('test_stat_two', data, layout2);
    
});

// Render plot
d3.json(`/inactive/fires`).then(function (myData) {
    console.log("We're in the active fires plot")
    // map values
    let newX = myData.map(x => x.Name);
    let newY = myData.map(x => x.AcresBurned);

    // restyle existing type plot
    Plotly.restyle('test_stat_two', 'x', [newX]);
    Plotly.restyle('test_stat_two', 'y', [newY]);

});


//Trying 3D plot

var test_stat_four = new Chart("test_stat_four", {
    type: "line",
    data: {},
    options: {}
  });
var layout4 = {
    title: {
        text: 'Recorded Acreage Burnt By Year',
        font: {
            family: 'Courier New, monospace',
            size: 24
        },
        xref: 'paper',
        x: 0.05,
    },
    scene: {
    xaxis: {title: "Year",
            backgroundcolor: "green",
            gridcolor: "green",
            showbackground: true,
            zerolinecolor: "green"},
    yaxis: {title: "Total Recorded Burnt Acres",
            gridcolor: "purple",
            backgroundcolor: "purple",
            showbackground: true,
            zerolinecolor: "purple"},
    zaxis: {title: "Total % of CA Burned",
    gridcolor: "red",
    backgroundcolor: "red",
    showbackground: true,
    zerolinecolor: "red"}

    },
    autosize: false,
    width: 800,
    height: 500
        
};

d3.json(`/ca_burned`).then(function (myData) {
    console.log("Init now")
    let data = [
        {
            x: myData.map(x => x["Year"]),
            y: myData.map(x => x["Total Recorded Burnt Acres"]),
            z: myData.map(z => z["Total % of CA Burned"]),
            mode: 'markers',
            type: 'scatter3d',
            color: 'red'
        }
    ]
    console.log("let data = is now logged")
    // draw plot
    console.log("Plot should be drawn")
    Plotly.newPlot("test_stat_four", data, layout4);
    
});

















// var layout4 = {
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
//             text: 'Year',
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

//ping route & store data
// d3.json(`/ca_burned`).then(function (myData) {
//     console.log("Init now")
//     let data = [
//         {
//             newX: myData.map(x => x.Year),
//             newY: myData.map(y => y["Total Recorded Burnt Acres"]),
//             newZ: myData.map(z => z["Total % of CA Burned"]),
//             mode: 'lines+markers',
//             type: 'scatter3d',
//             x: newX,
//             y: newY,
//             z:newZ
//         }
//     ]
//     console.log("let data = is now logged")
//     // draw plot
//     console.log("Plot should be drawn")
//     Plotly.newPlot('test_stat_four', data, layout4);

// });

// Render plot
// d3.json(`/ca_burned`).then(function (myData) {
//     console.log("We're in the active fires plot")
//     // map values
//     console.log("We're in the active fires plot")
//     // map values
//     let newX = myData.map(x => x.Year);
//     let newY = myData.map(x => x["Total Recorded Burnt Acres"]);;
//     let newZ = myData.map(x => x["Total % of CA Burned"])

//     // restyle existing type plot
//     Plotly.restyle('test_stat_four', 'x', [newX]);
//     Plotly.restyle('test_stat_four', 'y', [newY]);
//     Plotly.restyle('test_stat_four', 'z', [newZ]);

// });
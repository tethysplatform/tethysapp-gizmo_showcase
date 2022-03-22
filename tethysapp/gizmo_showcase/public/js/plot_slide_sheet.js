let m_plot_id = 'slide-sheet-plot';
let m_plot_id_config = {scrollZoom: true};

function init_plot() {
    let trace1 = {
        x: [1, 2, 3, 4],
        y: [10, 15, 13, 17],
        mode: 'markers',
        name: 'Scatter'
    };
    
    let trace2 = {
        x: [2, 3, 4, 5],
        y: [16, 5, 11, 9],
        mode: 'lines',
        name: 'Lines'
    };
    
    let trace3 = {
        x: [1, 2, 3, 4],
        y: [12, 9, 15, 12],
        mode: 'lines+markers',
        name: 'Scatter + Lines'
    };
    
    let data = [trace1, trace2, trace3];

    let layout = {
        autosize: true,
        height: 415,
        margin: {l: 80, r: 80, t: 20, b: 80},
        xaxis:  {
            title: {
              text: 'X Axis Title',
            }
        },
        yaxis: {
            title: {
              text: 'Y Axis Title',
            }
        }
    };

    // Create initial plot
    update_plot(data, layout);

    // Setup plot resize when window changes size
    $(window).resize(function() {
        fit_plot();
    });

    // Resize plot when nav is opened or closed
    $('.toggle-nav').on('tethys:toggle-nav', function(e) {
        fit_plot();
    });
}

function fit_plot() {
    let plot_container_width = $('#plot-slide-sheet').width();
    Plotly.relayout(m_plot_id, {width: plot_container_width});
}

function update_plot(data, layout) {
    let out = Plotly.validate(data, layout);
    if (out) {
        $(out).each(function(index, item) {
            console.warn(`PlotlyValidationWarning: ${item.msg}`);
        });
    }

    // Update plot
    Plotly.react(m_plot_id, data, layout, m_plot_id_config).then(function(p) {
        // Resize plot to fit after rendering the first time
        fit_plot();
    });
}

// Initialization
init_plot();
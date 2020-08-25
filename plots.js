// Trace1 for the Zip Code Data
var trace1 = {
  x: data.map(row => row.zipcode),
  y: data.map(row => row.population),
  text: data.map(row => row.Population),
  name: "Population",
  type: "bar"
};

// Trace 2 for the Zip Code Data
var trace2 = {
  x: data.map(row => row.zipcode),
  y: data.map(row => row.population),
  text: data.map(row => row.Population),
  name: "Population",
  type: "bar"
};

// Combining both traces
var data = [trace1, trace2];

// Apply the group barmode to the layout
var layout = {
  title: "Population by Zip Code"
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot", data, layout);

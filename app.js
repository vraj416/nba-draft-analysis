var svg = d3.select("svg"),
margin = 200,
width = svg.attr("width") - margin,
height = svg.attr("height") - margin;


var xScale = d3.scaleBand().range ([0, width]).padding(0.4),
    yScale = d3.scaleLinear().range ([height, 0]);

var g = svg.append("g")
    .attr("transform", "translate(" + 100 + "," + 100 + ")");

d3.csv("player_info.csv", function(error, data) {
    console.log(data[0]);

    var draftAvgByTeam = d3.nest()
    .key(function(d) { return d.TEAM_ABBREVIATION; })
    .rollup(function(v) { return d3.mean(v, function(d) { return d.DRAFT_NUMBER; }); })
    .entries(data)
    .sort((a, b) => d3.descending(a.value, b.value));

    console.log(JSON.stringify(draftAvgByTeam));
    console.log(draftAvgByTeam.length);

    xScale.domain(draftAvgByTeam.map(function(d) { return d.key; }));
    yScale.domain([0, d3.max(draftAvgByTeam, function(d) { return d.value; })]);

    g.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(xScale));

    g.append("g")
    .call(d3.axisLeft(yScale).tickFormat(function(d){
        return d;
    }).ticks(10))
    .append("text")
    .attr("y", 6)
    .attr("dy", "0.71em")
    .attr("text-anchor", "end")
    .text("value");


    g.selectAll(".bar")
    .data(draftAvgByTeam)
    .enter().append("rect")
    .attr("class", "bar")
    .attr("x", function(d) { return xScale(d.key); })
    .attr("y", function(d) { return yScale(d.value); })
    .attr("width", xScale.bandwidth())
    .attr("height", function(d) { return height - yScale(d.value); });

    });
 // SETUP
 var data;
 var svg = d3.select("#svg"),
   margin = { top: 20, right: 20, bottom: 30, left: 40 },
   x = d3.scalePoint()
   y = d3.scaleLinear();


 var bounds = svg.node().getBoundingClientRect(),
   width = bounds.width - margin.left - margin.right,
   height = bounds.height - margin.top - margin.bottom;


 var g = svg.append("g")
   .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

 g.append("g")
   .attr("class", "axis axis--x");

 g.append("g")
   .attr("class", "axis axis--y");

 g.append("text")
   .attr("transform", "rotate(-90)")
   .attr("y", 6)
   .attr("dy", "0.71em")
   .attr("text-anchor", "end") // attribute: start, middle, end
   .text("Frequency");

 
 d3.tsv("data.tsv", function (d) {
   x.domain(d.map(function (d, i) { return d.letter; })); // [A, B, C, D...]
   y.domain([0, d3.max(d, function (d, i) { return d.preference; })]);
   draw(d);
 })


 function draw(d) {
   x.rangeRound([0, width]);
   y.rangeRound([height, 0]);

   g.select(".axis--x")
     .attr("transform", "translate(0," + height + ")")
     .call(d3.axisBottom(x));

   g.select(".axis--y")
     .call(d3.axisLeft(y).ticks(10, "%"));

 var line = d3.line()
     .x(function(d, i) { return x(d.letter); }) 
     .y(function(d, i) { return y(d.frequency); }) 

 g.data(d);
 data = d
 g.append("path")
     .datum(d) 
     .attr("class", "line") 
     .attr("stroke", "steelblue")
     .attr("stroke-width", 3)
     .attr("fill", "none")
     .attr("d", line); 

 var div = d3.select("body").append("div") 
   .attr("class", "tooltip")       
   .style("opacity", 0);

 g.selectAll(".dot")
     .data(d)
   .enter().append("circle") 
     .attr("class", "dot") 
     .attr("cx", function(d, i) { return x(d.letter) })
     .attr("cy", function(d, i) { return y(d.frequency) })
     .attr("r", 5)
     .on("mouseover", function(d) {    
           div.transition()    
               .duration(200)    
               .style("opacity", .9);    
           div.html((d.letter) + ":"  + d.frequency)  
               .style("left", (d3.event.pageX) + "px")   
               .style("top", (d3.event.pageY - 28) + "px");
           })          
     .on("mouseout", function(d) {   
           div.transition()    
               .duration(500)    
               .style("opacity", 0); 
       });


 }


d3.select("#selectButton").on("change", function(d) {
  var selectedOption = d3.select(this).property("value")
   updateLine(data, selectedOption)
})


function updateLine(d, selectedOption) {
   // create line function specifying x position only
   var line = d3.line();
     line.x(function(d, i){return x(d.letter)});    
   if (selectedOption == "preference") {
     // assign y attribute to the line function, return y value of preference 
     line.y(function(d,i) {return y(d.preference)});
   } else if (selectedOption == "frequency") {
     // assign y attribute to the line function, return y value of frequency 
     line.y(function(d,i) {return y(d.frequency)});
   }

   svg.selectAll(".line")
     .transition()
     .delay(function (d, i) {return i * 50;})
     .duration(1000)
     .attr("d", line); 

 // transit dots

}
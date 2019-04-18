$(document).ready(function() {
$("#get-dep-btn").click(function() {

var sentenceEntered = $("#sentence").val();
        $.ajax({
            type: "GET",
            url: "/explanation/parse_sentence/",
            data: {'sentence':sentenceEntered
            },
            success: function(data) {

            var nodes = new vis.DataSet(data['nodes']);
            var edges = new vis.DataSet(data['edges']);
            var container = document.getElementById('dep-network');
            console.log(nodes);
            console.log(edges);
            // provide the data in the vis format
            var data = {
                nodes: nodes,
                edges: edges
            };
            var options = {
                      layout: {
                        randomSeed: undefined,
                        improvedLayout:true,
                        hierarchical: {
                          enabled:true,
                          levelSeparation: 150,
                          nodeSpacing: 100,
                          treeSpacing: 200,
                          blockShifting: true,
                          edgeMinimization: true,
                          parentCentralization: true,
                          direction: 'LR',        // UD, DU, LR, RL
                          sortMethod: 'directed'   // hubsize, directed
                        }
                      }
                    };

            // initialize your network!
            var network = new vis.Network(container, data, options);

              }
        });

    // create a network

});
});
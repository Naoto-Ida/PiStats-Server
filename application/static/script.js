$(function() {

	var preferences = {
		"disk": true
	};

	if (preferences["disk"])  {
		getInfo("disk");
	}

	function getInfo(target)
	{
		$.ajax({
            url: "/" + target,
            type: "GET",
            success: function(data) {
				var html = "<table class='table table-striped'><thead><tr><th>Device</th><th>Total</th><th>Used</th><th>Free</th><th>Use %</th><th>Type</th><th>Mount</th></tr></thead><tbody>";
				for (var i = 0; i < data["results"].length; i++) {
					html += "<tr>";
					html += "<td>" + data["results"][i]["device"] + "</td>";
					html += "<td>" + data["results"][i]["total"] + "</td>";
					html += "<td>" + data["results"][i]["used"] + "</td>";
					html += "<td>" + data["results"][i]["free"] + "</td>";
					html += "<td>" + data["results"][i]["percent"] + "</td>";
					html += "<td>" + data["results"][i]["fstype"] + "</td>";
					html += "<td>" + data["results"][i]["mountpoint"] + "</td>";
					html += "</tr>";
				}
				html += "</tbody></table>";
                $("#grid").append("<div class='row'><div class='col-md-6'>" + html + "</div></div>");
            }
        });
	}

});

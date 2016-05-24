material_sub_html_template = "<div class='col-md-4 material_sub' id='material_1'>\n\
					<h4>Material 1</h4>\n\
					<fieldset class='form-group'>\n\
						<label for='mat_name_1'>Material 1 Name</label>\n\
						<input type='text' class='form-control' id='mat_name_1' placeholder='Example input'>\n\
					</fieldset>\n\
					<fieldset class='form-group'>\n\
						<label for='depth_1'>Material 1 Depth (in microns)</label>\n\
						<input type='text' class='form-control' id='depth_1' placeholder='Another input'>\n\
					</fieldset>\n\
				</div>";

function addLayer(){
	var length = $(".material_sub").length;
	var material_html = material_sub_html_template.replace(new RegExp('1','g'), (length + 1).toString());
	console.log("Number of materials currently in profile:" + length);
	if(length % 3 !== 0){
		$(("#material_" + length)).after(material_html);
	} else {
		$(".material_row").last().after("<div class='row material_row'>" + material_html + "</div");
	}
}

function removeLayer(){
	var length = $(".material_sub").length;
	var material_html = material_sub_html_template.replace(new RegExp('1','g'), (length + 1).toString());
	console.log("Number of materials currently in profile:" + length);
	var appendDestination;
	if(length > 1) {
		if(length % 3 == 1){
			$(".material_row").last().remove();
		} else {
			$(("#material_" + length)).remove();
		}
	}
}
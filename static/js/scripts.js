$( document ).ready(function() {
	$.getJSON( "/get_settings", function( data ) {
		alarms = data.settings.alarms;

		sunday_alarm    = alarms[0].time;
		monday_alarm    = alarms[1].time;
		tuesday_alarm   = alarms[2].time;
		wednesday_alarm = alarms[3].time;
		thursday_alarm  = alarms[4].time;
		friday_alarm    = alarms[5].time;
		saturday_alarm  = alarms[6].time;
				
		$("#sunday_time").val(sunday_alarm);
		$("#monday_time").val(monday_alarm);
		$("#tuesday_time").val(tuesday_alarm);
		$("#wednesday_time").val(wednesday_alarm);
		$("#thursday_time").val(thursday_alarm);
		$("#friday_time").val(friday_alarm);
		$("#saturday_time").val(saturday_alarm);
	});
	
	$("#toggle_lights_button").click(function(){ 
// 		var button_colour = $("#toggle_lights_button").css( "background-color");
// 		$("#toggle_lights_button").css( "background-color", "#e7e7e7");
		$("#toggle_lights_button").fadeOut(100);
		$("#toggle_lights_button").fadeIn(100);
		
	});
	
});
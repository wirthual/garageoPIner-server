$( document ).ready(function(){

	$( "#btnopenclose" ).click(toggleRelais);
	$( "#btntime" ).click(timeControl);

	var myswitch = $("#tgltime");

	var timeControlEnabled = myswitch[0].selectedIndex == 1 ? true:false;
	showTimeProperties(timeControlEnabled);


	$('#tgltime').change(function(event) {
	    event.stopPropagation();
	    var timeControlEnabled= myswitch[0].selectedIndex == 1 ? true:false;
	    showTimeProperties(timeControlEnabled);
	});

});

function toggleRelais(){
var gpio = $("#txtgpio").val();
var intgpio = parseInt(gpio);

$.get(
    document.location.href + "controlRelay/"+gpio);
}



function timeControl(){
var gpio = $("#txtgpio").val();

$.get(
    document.location.href + "timeControl?seconds=10&pin="+gpio);
}


function showTimeProperties(show){
    if(show) {            
        $('#timefield').fadeIn('slow');
    } else {            
        $('#timefield').fadeOut();
    }
}

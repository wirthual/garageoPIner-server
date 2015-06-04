


$( document ).ready(function(){
	initialize();
});

function initialize(){
	//Initialize global vaiables
	button1 = $( "#btnopenclose1" );
	buttonTime1 = $( "#btntime1" );
	
	button2 = $( "#btnopenclose2" );
	buttonTime2 = $( "#btntime2" );
	
	myswitch = $("#tgltime");
	
	timefield = $('#timefield');
	
	toggleTime = $('#tgltime');

	var timeControlEnabled = myswitch[0].selectedIndex == 1 ? true:false;
	showTimeProperties(timeControlEnabled);

	toggleTime.change(function(event) {
	    event.stopPropagation();
	    var timeControlEnabled= myswitch[0].selectedIndex == 1 ? true:false;
	    showTimeProperties(timeControlEnabled);
	});
	
	button1.click(toggleIN1);
	buttonTime1.click(timeControlIN1);

	button2.click(toggleIN2);
	buttonTime2.click(timeControlIN2);
	

}

function toggleIN1(){
	$.get(document.location.href + "toggleIN1");
}

function toggleIN2(){
	$.get(document.location.href + "toggleIN2");
}

function timeControlIN1(){
	$.get(document.location.href + "timeControlIN1?seconds=240");
}

function timeControlIN2(){
	$.get(document.location.href + "timeControlIN2?seconds=240");
}

function stopTimeControlIN1(){
	$.get(document.location.href + "stopTimeControlIN1");
}

function stopTimeControlIN2(){
	$.get(document.location.href + "stopTimeControlIN2");
}


function showTimeProperties(show){
    if(show) {            
       	timefield.hide(); //Hack. Never show timefield. Until time selection is implemented in js.
        buttonTime1.fadeIn('slow');
        buttonTime2.fadeIn('slow');
    } else {            
        timefield.hide();
        buttonTime1.hide();
        buttonTime2.hide();
    }
}

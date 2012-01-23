$(document).ready(function(){

	$('#fc').keypress(function(event){
		if (event.which == '13'){
			event.preventDefault();
			search();
		}
	});
	//Первый запуск - получаем Главного Тестового Юзера
	$.ajax({url:'/ajax?do_what=mainuser',
			dataType:'json',
			success: function(data,s){
						// var dd = __makeJSON(data);
						var str = $('#main').html();
						// str += "<hr\/>"+data;
						$.each(data,function(k,v){
							str += "<hr\/>"+k+"=>"+v;
						});

						$('#main').html(str);

// var george=JSON.parse(jsonstr) //convert JSON string into object
// alert(george.age) //alerts 29						
			}
	});//getJSON
	// $.ajax({
	// 	url : '/ajax',
	// 	success: function(data){
	// 		//alert('ajax return:' + data);
	// 	}
	// });

});	

function search(){
	alert('go search' + $('#fc').val()+'!');
}

function __makeJSON(str){
	str = str.replace(/'/g,"\"");
	return JSON.parse(str);
}
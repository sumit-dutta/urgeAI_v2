$(document).ready(function(){

//    $.get( "http://127.0.0.1:5000", function( data ) {
//    var obj = jQuery.parseJSON(data.result);
//     console.log(obj)
//     $.each(obj, function(k, v) {
//    //display the key and value pair
//    console.log(k + ' is ' + v);
//    $( ".result" ).append( "<div class='item'><img class='image' src='" + v.image + "'><span class='msg'>"+ v.msg +"</span></div>" );
//

    $.get( "http://127.0.0.1:5000/getColors", function( data ) {
        var colors = data["Color"]
        for (col in colors){
            var color = colors[col]
            $(".color").append("<span><input type='checkbox' name='colors' value='" + color + "'>"+ color +" &nbsp;</span>")
        }

    });


    $.get( "http://127.0.0.1:5000/getTypes", function( data ) {
        var types = data["Type"]
        for (typ in types){
            var type = types[typ]
            $(".type").append("<span><input type='checkbox' name='types' value='" + type + "'>"+ type +" &nbsp;</span>")
        }

    });


    $( ".toggle" ).click(function() {
        $(".input").slideToggle();
    })


    $( ".close" ).click(function() {
        $(".input").slideUp();
    })




    $( ".submit" ).click(function() {
      $(".input").slideUp();
      $(".result").empty();
      var colors = []
      var types = []
      var accentuate = []

      $('input[name="colors"]:checked').each(function() {
         console.log(this.value);
         colors.push(this.value)

      });

      $( document ).ajaxStart(function() {
        $(".loading").show()
      });

      $( document ).ajaxStop(function() {
        $(".loading").hide()
      });


      $('input[name="types"]:checked').each(function() {
         console.log(this.value);
         types.push(this.value)

      });



      $('input[name="accentuate"]:checked').each(function() {
         console.log(this.value);
         accentuate.push(this.value)

      });

      var json = {
        skinTone: $(".skTone").val(),
        colors: colors,
        types : types,
        accentuate: accentuate
      };

      console.log(JSON.stringify(json));
      $.ajax({
        url:"http://127.0.0.1:5000/getFeed",
        type:"POST",
        data:JSON.stringify(json),
        contentType:"application/json",
        dataType:"json",
        success: function(data){
         var obj = jQuery.parseJSON(data.result);
             console.log(obj)
             $.each(obj, function(k, v) {
            //display the key and value pair
            console.log(k + ' is ' + v);
            $( ".result" ).append( "<div class='item'><a href='" +v.url+ "' target='_blank'><img class='image' src='" + v.image + "'><span class='msg'>"+ v.msg +"</span></a></div>" );
            });
        }
      })

      console.log(json)
    });

});
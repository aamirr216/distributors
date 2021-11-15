$(document).ready(function() {

    var MaxInputs = 200; //maximum extra input boxes allowed
    var InputsWrapper = $("#InputsWrapper"); //Input boxes wrapper ID
    var AddButton = $("#AddMoreFileBox"); //Add button ID
  
    var x = InputsWrapper.length; //initlal text box count
    var FieldCount = 1; //to keep track of text box added
  
    //on add input button click
    $(AddButton).click(function(e) {
          //max input box allowed
      if (x <= MaxInputs) {
        FieldCount++; //text box added ncrement
        //add input box
        $(InputsWrapper).append('<div>Product:<input type="text" name="createmultiple" id="field_' + FieldCount + '" class="form-control form-control-sm"/><br>Qty:<input type="text" name="qty" id="field_' + FieldCount + '" class="form-control form-control-sm"/><a href="#" class="removeclass">Remove</a></div>');
        x++; //text box increment
  
        $("#AddMoreFileId").show();
  
        $('AddMoreFileBox').html("Add field");
  
        // Delete the "add"-link if there is 3 fields.
        // if (x == 3) {
        //   $("#AddMoreFileId").hide();
        //   $("#lineBreak").html("<br>");
        // }
      }
      return false;
    });
  
    $("body").on("click", ".removeclass", function(e) { //user click on remove text
      if (x > 1) {
        $(this).parent('div').remove(); //remove text box
        x--; //decrement textbox
  
        $("#AddMoreFileId").show();
  
        $("#lineBreak").html("");
  
        // Adds the "add" link again when a field is removed.
        $('AddMoreFileBox').html("Add field");
      }
      return false;
    })
  
  });
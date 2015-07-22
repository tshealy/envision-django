$(function() {

    var charCounts = {
        'No Added Value': 0,
        'Improved': 100,
        'Enhanced': 150,
        'Superior': 200,
        'Conserving': 250,
        'Restorative': 300,
        'Exclude': 50,
    }
    //character count for textarea
    $("textarea").keyup(function(){
        var text_and_span = $(this).siblings();
        var current_span = text_and_span.siblings('.current-count');

        current_span.text( $(this).val().length );

        //$(this).siblings($(".current-count").text( $(this).val().length ));

    });

    $("select").change(function(){
        var row = $(this).parent().siblings(".row");
        console.log($(this).parent().siblings("h4").find("select"));
        var text = $(this).children(':selected').text();
        if (text === "Include") {
            text = $(this).parent().siblings("h4").find("select").children(':selected').text()
        }
        row.find(".required-count").text(charCounts[text]);
    });

    //function writeCharacterCount(textArea, write) {
    //    write.text(textArea.val().length)
    //};
    //
    //function characterCounts(){
    //    $("#id_QL1_1_exp").keyup(function(){
    //        //writeCharacterCount($("#id_QL1_1_exp"), $(".current-count"));
    //    });
    //    $("#id_QL1_2_exp").keyup(function(){
    //        writeCharacterCount($("#id_QL1_2_exp"), $("#ql12"));
    //    });
    //    $("#id_QL2_3_exp").keyup(function(){
    //        writeCharacterCount($("#id_QL2_3_exp"), $("#ql23"));
    //    });
    //    $("#id_QL2_5_exp").keyup(function(){
    //        writeCharacterCount($("#id_QL2_5_exp"), $("#ql25"));
    //    });
    //    $("#id_QL2_6_exp").keyup(function(){
    //        writeCharacterCount($("#id_QL2_6_exp"), $("#ql26"));
    //    });
    //    $("#id_QL3_3_exp").keyup(function(){
    //        writeCharacterCount($("#id_QL3_3_exp"), $("#ql33"));
    //    });
    //    $("#id_LD1_2_exp").keyup(function(){
    //        writeCharacterCount($("#id_LD1_2_exp"), $("#ld12"));
    //    });
    //    $("#id_LD1_4_exp").keyup(function(){
    //        writeCharacterCount($("#id_LD1_4_exp"), $("#ld14"));
    //    });
    //    $("#id_LD2_2_exp").keyup(function(){
    //        writeCharacterCount($("#id_LD2_2_exp"), $("#ld22"));
    //    });
    //    $("#id_NW1_2_exp").keyup(function(){
    //        writeCharacterCount($("#id_NW1_2_exp"), $("#nw12"));
    //    });
    //    $("#id_NW2_2_exp").keyup(function(){
    //        writeCharacterCount($("#id_NW2_2_exp"), $("#nw22"));
    //    });
    //    $("#id_NW2_3_exp").keyup(function(){
    //        writeCharacterCount($("#id_NW2_3_exp"), $("#nw23"));
    //    });
    //
    //};

    function getLastValue(dropdown) {
        // takes in the selector for the dropdown
        return dropdown.children().last().val();
    };

    function writePossiblePoints(selector, points) {
        // takes in the selector for the place to write
        selector.text(points);
    };

    function possiblePoints() {
        var points = getLastValue( $("#id_QL1_1_loa"));
        writePossiblePoints( $("#ql11-possible-points"), points);

        var points = getLastValue( $("#id_QL1_2_loa"));
        writePossiblePoints( $("#ql12-possible-points"), points);

        var points = getLastValue( $("#id_QL2_3_loa"));
        writePossiblePoints( $("#ql23-possible-points"), points);

        var points = getLastValue( $("#id_QL2_5_loa"));
        writePossiblePoints( $("#ql25-possible-points"), points);

        var points = getLastValue( $("#id_QL2_6_loa"));
        writePossiblePoints( $("#ql26-possible-points"), points);

        var points = getLastValue( $("#id_QL3_3_loa"));
        writePossiblePoints( $("#ql33-possible-points"), points);

        var points = getLastValue( $("#id_LD1_2_loa"));
        writePossiblePoints( $("#ld12-possible-points"), points);

        var points = getLastValue( $("#id_LD1_4_loa"));
        writePossiblePoints( $("#ld14-possible-points"), points);

        var points = getLastValue( $("#id_LD2_2_loa"));
        writePossiblePoints( $("#ld22-possible-points"), points);

        var points = getLastValue( $("#id_NW1_2_loa"));
        writePossiblePoints( $("#nw12-possible-points"), points);

        var points = getLastValue( $("#id_NW2_2_loa"));
        writePossiblePoints( $("#nw22-possible-points"), points);

        var points = getLastValue( $("#id_NW2_3_loa"));
        writePossiblePoints( $("#nw23-possible-points"), points);

    };

    function selectedPoints(){
        // dropdown
        // h4 id  ----------------------- dropdown + :selected
        $("#id_QL1_1_loa").change(function() {
            $("#ql11-selected-points").text($("#id_QL1_1_loa :selected").val());
        });
        $("#id_QL1_2_loa").change(function() {
            $("#ql12-selected-points").text($("#id_QL1_2_loa :selected").val());
        });
        $("#id_QL2_3_loa").change(function() {
            $("#ql23-selected-points").text($("#id_QL2_3_loa :selected").val());
        });
        $("#id_QL2_5_loa").change(function() {
            $("#ql25-selected-points").text($("#id_QL2_5_loa :selected").val());
        });
        $("#id_QL2_6_loa").change(function() {
            $("#ql26-selected-points").text($("#id_QL2_6_loa :selected").val());
        });
        $("#id_QL3_3_loa").change(function() {
            $("#ql33-selected-points").text($("#id_QL3_3_loa :selected").val());
        });
        $("#id_LD1_2_loa").change(function() {
            $("#ld12-selected-points").text($("#id_LD1_2_loa :selected").val());
        });
        $("#id_LD1_4_loa").change(function() {
            $("#ld14-selected-points").text($("#id_LD1_4_loa :selected").val());
        });
        $("#id_LD2_2_loa").change(function() {
            $("#ld22-selected-points").text($("#id_LD2_2_loa :selected").val());
        });
        $("#id_NW1_2_loa").change(function() {
            $("#nw12-selected-points").text($("#id_NW1_2_loa :selected").val());
        });
        $("#id_NW2_2_loa").change(function() {
            $("#nw22-selected-points").text($("#id_NW2_2_loa :selected").val());
        });
        $("#id_NW2_3_loa").change(function() {
            $("#nw23-selected-points").text($("#id_NW2_3_loa :selected").val());
        });

    };


    function included(){
        $("#id_QL1_1_inc").change(function(){
           if ($("#id_QL1_1_inc :selected").val() == 1) {
               $("#id_QL1_1_loa").val(0);
               $("#id_QL1_1_loa").prop("disabled", true);
               writePossiblePoints( $("#ql11-selected-points"), 0 );
               writePossiblePoints( $("#ql11-possible-points"), 0 );
           } else {
               $("#id_QL1_1_loa").prop("disabled", false);
               writePossiblePoints( $("#ql11-possible-points"), getLastValue($("#id_QL1_1_loa")) );
               $("#ql11-selected-points").text($("#id_QL1_1_loa :selected").val());
           };
        });
         $("#id_QL1_2_inc").change(function(){
           if ($("#id_QL1_2_inc :selected").val() == 1) {
               $("#id_QL1_2_loa").prop("disabled", true);
               writePossiblePoints( $("#ql12-selected-points"), 0 );
               writePossiblePoints( $("#ql12-possible-points"), 0 );
           } else {
               $("#id_QL1_2_loa").prop("disabled", false);
               writePossiblePoints( $("#ql12-possible-points"), getLastValue($("#id_QL1_2_loa")) );
               $("#ql12-selected-points").text($("#id_QL1_2_loa :selected").val());
           };
        });
         $("#id_QL2_3_inc").change(function(){
           if ($("#id_QL2_3_inc :selected").val() == 1) {
               $("#id_QL2_3_loa").prop("disabled", true);
               writePossiblePoints( $("#ql23-selected-points"), 0 );
               writePossiblePoints( $("#ql23-possible-points"), 0 );
           } else {
               $("#id_QL2_3_loa").prop("disabled", false);
               writePossiblePoints( $("#ql23-possible-points"), getLastValue($("#id_QL2_3_loa")) );
               $("#ql23-selected-points").text($("#id_QL2_3_loa :selected").val());
           };
        });
         $("#id_QL2_5_inc").change(function(){
           if ($("#id_QL2_5_inc :selected").val() == 1) {
               $("#id_QL2_5_loa").prop("disabled", true);
               writePossiblePoints( $("#ql25-selected-points"), 0 );
               writePossiblePoints( $("#ql25-possible-points"), 0 );
           } else {
               $("#id_QL2_5_loa").prop("disabled", false);
               writePossiblePoints( $("#ql25-possible-points"), getLastValue($("#id_QL2_5_loa")) );
               $("#ql25-selected-points").text($("#id_QL2_5_loa :selected").val());
           };
        });
         $("#id_QL2_6_inc").change(function(){
           if ($("#id_QL2_6_inc :selected").val() == 1) {
               $("#id_QL2_6_loa").prop("disabled", true);
               writePossiblePoints( $("#ql26-selected-points"), 0 );
               writePossiblePoints( $("#ql26-possible-points"), 0 );
           } else {
               $("#id_QL2_6_loa").prop("disabled", false);
               writePossiblePoints( $("#ql26-possible-points"), getLastValue($("#id_QL2_6_loa")) );
               $("#ql26-selected-points").text($("#id_QL2_6_loa :selected").val());
           };
        });
         $("#id_LD1_2_inc").change(function(){
           if ($("#id_LD1_2_inc :selected").val() == 1) {
               $("#id_LD1_2_loa").prop("disabled", true);
               writePossiblePoints( $("#ld12-selected-points"), 0 );
               writePossiblePoints( $("#ld12-possible-points"), 0 );
           } else {
               $("#id_LD1_2_loa").prop("disabled", false);
               writePossiblePoints( $("#ld12-possible-points"), getLastValue($("#id_LD1_2_loa")) );
               $("#ld12-selected-points").text($("#id_LD1_2_loa :selected").val());
           };
        });
         $("#id_LD1_4_inc").change(function(){
           if ($("#id_LD1_4_inc :selected").val() == 1) {
               $("#id_LD1_4_loa").prop("disabled", true);
               writePossiblePoints( $("#ld14-selected-points"), 0 );
               writePossiblePoints( $("#ld14-possible-points"), 0 );
           } else {
               $("#id_LD1_4_loa").prop("disabled", false);
               writePossiblePoints( $("#ld14-possible-points"), getLastValue($("#id_LD1_4_loa")) );
               $("#ld14-selected-points").text($("#id_LD1_4_loa :selected").val());
           };
        });
         $("#id_LD2_2_inc").change(function(){
           if ($("#id_LD2_2_inc :selected").val() == 1) {
               $("#id_LD2_2_loa").prop("disabled", true);
               writePossiblePoints( $("#ld22-selected-points"), 0 );
               writePossiblePoints( $("#ld22-possible-points"), 0 );
           } else {
               $("#id_LD2_2_loa").prop("disabled", false);
               writePossiblePoints( $("#ld22-possible-points"), getLastValue($("#id_LD2_2_loa")) );
               $("#ld22-selected-points").text($("#id_LD2_2_loa :selected").val());
           };
        });
         $("#id_NW1_2_inc").change(function(){
           if ($("#id_NW1_2_inc :selected").val() == 1) {
               $("#id_NW1_2_loa").prop("disabled", true);
               writePossiblePoints( $("#nw12-selected-points"), 0 );
               writePossiblePoints( $("#nw12-possible-points"), 0 );
           } else {
               $("#id_NW1_2_loa").prop("disabled", false);
               writePossiblePoints( $("#nw12-possible-points"), getLastValue($("#id_NW1_2_loa")) );
               $("#nw12-selected-points").text($("#id_NW1_2_loa :selected").val());
           };
        });
         $("#id_NW2_2_inc").change(function(){
           if ($("#id_NW2_2_inc :selected").val() == 1) {
               $("#id_NW2_2_loa").prop("disabled", true);
               writePossiblePoints( $("#nw22-selected-points"), 0 );
               writePossiblePoints( $("#nw22-possible-points"), 0 );
           } else {
               $("#id_NW2_2_loa").prop("disabled", false);
               writePossiblePoints( $("#nw22-possible-points"), getLastValue($("#id_NW2_2_loa")) );
               $("#nw22-selected-points").text($("#id_NW2_2_loa :selected").val());
           };
        });
         $("#id_NW2_3_inc").change(function(){
           if ($("#id_NW2_3_inc :selected").val() == 1) {
               $("#id_NW2_3_loa").prop("disabled", true);
               writePossiblePoints( $("#nw23-selected-points"), 0 );
               writePossiblePoints( $("#nw23-possible-points"), 0 );
           } else {
               $("#id_NW2_3_loa").prop("disabled", false);
               writePossiblePoints( $("#nw23-possible-points"), getLastValue($("#id_NW2_3_loa")) );
               $("#nw23-selected-points").text($("#id_NW2_3_loa :selected").val());
           };
        });
         $("#id_QL3_3_inc").change(function(){
           if ($("#id_QL3_3_inc :selected").val() == 1) {
               $("#id_QL3_3_loa").prop("disabled", true);
               writePossiblePoints( $("#ql33-selected-points"), 0 );
               writePossiblePoints( $("#ql33-possible-points"), 0 );
           } else {
               $("#id_QL3_3_loa").prop("disabled", false);
               writePossiblePoints( $("#ql33-possible-points"), getLastValue($("#id_QL3_3_loa")) );
               $("#ql33-selected-points").text($("#id_QL3_3_loa :selected").val());
           };
        });
    };

    function disable(one, two) {

    };

     function totalPossibelPoints() {
        var arr = $(".possible-points");
        var total = 0;
        for (var i = 0; i < arr.length; i++) {
            total += parseInt(arr[i].innerHTML);
        };
        $("#total-possible").text(total);
    };

    function totalSelectedPoints() {
        var arr = $(".selected-points");
        var total = 0;
        for (var i = 0; i < arr.length; i++) {
            total += parseInt(arr[i].innerHTML);
        };
        $("#total-selected").text(total);
    };

    $("select").change(function(){
        setTimeout(function(){
            totalPossibelPoints();
            totalSelectedPoints();
        }, 1);
    });

    if (parseInt($(".data").html()) === 1){
        $(".version-one").show();
    };


    //characterCounts();
    possiblePoints();
    selectedPoints();
    included();
    totalPossibelPoints();
    totalSelectedPoints();

});


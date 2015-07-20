$(function() {

    var charCounts = {
        'Improved': 100,
        'Test': 200
    }
    function writeCharacterCount(textArea, write) {
        write.text(textArea.val().length)
    };

    function characterCounts(){
        $("#id_QL1_1_exp").keyup(function(){
            writeCharacterCount($("#id_QL1_1_exp"), $("#ql11"));
        });
    };

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
        console.log(points);
        writePossiblePoints( $("#ql11-possible-points"), points);
    };


    function selectedPoints(){
        // dropdown
        // h4 id  ----------------------- dropdown + :selected
        $("#id_QL1_1_loa").change(function() {
            $("#ql11-selected-points").text($("#id_QL1_1_loa :selected").val());
        });
    };


    function included(){
        $("#id_QL1_1_inc").change(function(){
           if ($("#id_QL1_1_inc :selected").val() == 1) {
               $("#id_QL1_1_loa").prop("disabled", true);
               writePossiblePoints( $("#ql11-selected-points"), 0 );
               writePossiblePoints( $("#ql11-possible-points"), 0 );
           } else {
               $("#id_QL1_1_loa").prop("disabled", false);
               writePossiblePoints( $("#ql11-possible-points"), getLastValue($("#id_QL1_1_loa")) );
               $("#ql11-selected-points").text($("#id_QL1_1_loa :selected").val());
           };
        });
    };

    function disable(one, two) {

    };






    characterCounts();
    possiblePoints();
    selectedPoints();
    included();

});


"use strict";

$('input[name="search"]').on('input propertychange paste', function() { 
    /*
    .on('input propertychange paste', ... ) handles input via typing or pasting.
    Also detects when text is erased or cut.
    */

    // Vairable declaration
    var input, filter, tr, td, i;

    // Variable definition
    input  = $(this);
    filter = input.val().toLowerCase();
    tr     = $("table tr");

    // Iterate through table, filtering by column 0
    // toLowerCase used to achieve case-insensitive search
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0]; // <-- change number to filter using other columns
        if (td) {
            if (td.innerHTML.toLowerCase().indexOf(filter) > -1) {
                // Display
                tr[i].style.display = "";
            } else {
                // Don't display
                tr[i].style.display = "none";
            }
        }
    }
});
(function() {
    var ref_type = document.querySelector(".ref-type select");

    // Get the value of select box
    function typeSelect() {
        var value = ref_type.options[ref_type.selectedIndex].value;

        return value;
    }
    function changeType() {
        var value = typeSelect();
        var ref_info = document.querySelectorAll(".ref-info ul");
        
        if (value === "none") {
            ref_info[0].style.display = "none";
            ref_info[1].style.display = "none";
            ref_info[2].style.display = "none";
            ref_info[3].style.display = "none";
            ref_info[4].style.display = "none";
            ref_info[5].style.display = "none";
            ref_info[6].style.display = "none";
            ref_info[7].style.display = "none";
            ref_info[8].style.display = "none";
            ref_info[9].style.display = "none";
            ref_info[10].style.display = "none";
            ref_info[11].style.display = "none";
            ref_info[12].style.display = "none";
        } else if (value === "article") {
            ref_info[0].style.display = "block";
            ref_info[1].style.display = "none";
            ref_info[2].style.display = "none";
            ref_info[3].style.display = "none";
            ref_info[4].style.display = "none";
            ref_info[5].style.display = "none";
            ref_info[6].style.display = "none";
            ref_info[7].style.display = "none";
            ref_info[8].style.display = "none";
            ref_info[9].style.display = "none";
            ref_info[10].style.display = "none";
            ref_info[11].style.display = "none";
            ref_info[12].style.display = "none";
        } else if (value === "book") {
            ref_info[0].style.display = "none";
            ref_info[1].style.display = "block";
            ref_info[2].style.display = "none";
            ref_info[3].style.display = "none";
            ref_info[4].style.display = "none";
            ref_info[5].style.display = "none";
            ref_info[6].style.display = "none";
            ref_info[7].style.display = "none";
            ref_info[8].style.display = "none";
            ref_info[9].style.display = "none";
            ref_info[10].style.display = "none";
            ref_info[11].style.display = "none";
            ref_info[12].style.display = "none";
        } else if (value === "booklet") {
            ref_info[0].style.display = "none";
            ref_info[1].style.display = "none";
            ref_info[2].style.display = "block";
            ref_info[3].style.display = "none";
            ref_info[4].style.display = "none";
            ref_info[5].style.display = "none";
            ref_info[6].style.display = "none";
            ref_info[7].style.display = "none";
            ref_info[8].style.display = "none";
            ref_info[9].style.display = "none";
            ref_info[10].style.display = "none";
            ref_info[11].style.display = "none";
            ref_info[12].style.display = "none";
        }　else if (value === "inbook") {
            ref_info[0].style.display = "none";
            ref_info[1].style.display = "none";
            ref_info[2].style.display = "none";
            ref_info[3].style.display = "block";
            ref_info[4].style.display = "none";
            ref_info[5].style.display = "none";
            ref_info[6].style.display = "none";
            ref_info[7].style.display = "none";
            ref_info[8].style.display = "none";
            ref_info[9].style.display = "none";
            ref_info[10].style.display = "none";
            ref_info[11].style.display = "none";
            ref_info[12].style.display = "none";
        }　else if (value === "incollection") {
            ref_info[0].style.display = "none";
            ref_info[1].style.display = "none";
            ref_info[2].style.display = "none";
            ref_info[3].style.display = "none";
            ref_info[4].style.display = "block";
            ref_info[5].style.display = "none";
            ref_info[6].style.display = "none";
            ref_info[7].style.display = "none";
            ref_info[8].style.display = "none";
            ref_info[9].style.display = "none";
            ref_info[10].style.display = "none";
            ref_info[11].style.display = "none";
            ref_info[12].style.display = "none";
        }　else if (value === "inproceedings") {
            ref_info[0].style.display = "none";
            ref_info[1].style.display = "none";
            ref_info[2].style.display = "none";
            ref_info[3].style.display = "none";
            ref_info[4].style.display = "none";
            ref_info[5].style.display = "block";
            ref_info[6].style.display = "none";
            ref_info[7].style.display = "none";
            ref_info[8].style.display = "none";
            ref_info[9].style.display = "none";
            ref_info[10].style.display = "none";
            ref_info[11].style.display = "none";
            ref_info[12].style.display = "none";
        }　else if (value === "conference") {
            ref_info[0].style.display = "none";
            ref_info[1].style.display = "none";
            ref_info[2].style.display = "none";
            ref_info[3].style.display = "none";
            ref_info[4].style.display = "none";
            ref_info[5].style.display = "none";
            ref_info[6].style.display = "block";
            ref_info[7].style.display = "none";
            ref_info[8].style.display = "none";
            ref_info[9].style.display = "none";
            ref_info[10].style.display = "none";
            ref_info[11].style.display = "none";
            ref_info[12].style.display = "none";
        }　else if (value === "manual") {
            ref_info[0].style.display = "none";
            ref_info[1].style.display = "none";
            ref_info[2].style.display = "none";
            ref_info[3].style.display = "none";
            ref_info[4].style.display = "none";
            ref_info[5].style.display = "none";
            ref_info[6].style.display = "none";
            ref_info[7].style.display = "block";
            ref_info[8].style.display = "none";
            ref_info[9].style.display = "none";
            ref_info[10].style.display = "none";
            ref_info[11].style.display = "none";
            ref_info[12].style.display = "none";
        }　else if (value === "masterthesis") {
            ref_info[0].style.display = "none";
            ref_info[1].style.display = "none";
            ref_info[2].style.display = "none";
            ref_info[3].style.display = "none";
            ref_info[4].style.display = "none";
            ref_info[5].style.display = "none";
            ref_info[6].style.display = "none";
            ref_info[7].style.display = "none";
            ref_info[8].style.display = "block";
            ref_info[9].style.display = "none";
            ref_info[10].style.display = "none";
            ref_info[11].style.display = "none";
            ref_info[12].style.display = "none";
        }　else if (value === "phdthesis") {
            ref_info[0].style.display = "none";
            ref_info[1].style.display = "none";
            ref_info[2].style.display = "none";
            ref_info[3].style.display = "none";
            ref_info[4].style.display = "none";
            ref_info[5].style.display = "none";
            ref_info[6].style.display = "none";
            ref_info[7].style.display = "none";
            ref_info[8].style.display = "none";
            ref_info[9].style.display = "block";
            ref_info[10].style.display = "none";
            ref_info[11].style.display = "none";
            ref_info[12].style.display = "none";
        }　else if (value === "proceedings") {
            ref_info[0].style.display = "none";
            ref_info[1].style.display = "none";
            ref_info[2].style.display = "none";
            ref_info[3].style.display = "none";
            ref_info[4].style.display = "none";
            ref_info[5].style.display = "none";
            ref_info[6].style.display = "none";
            ref_info[7].style.display = "none";
            ref_info[8].style.display = "none";
            ref_info[9].style.display = "none";
            ref_info[10].style.display = "block";
            ref_info[11].style.display = "none";
            ref_info[12].style.display = "none";
            ref_info[13].style.display = "none";
        }　else if (value === "techreport") {
            ref_info[0].style.display = "none";
            ref_info[1].style.display = "none";
            ref_info[2].style.display = "none";
            ref_info[3].style.display = "none";
            ref_info[4].style.display = "none";
            ref_info[5].style.display = "none";
            ref_info[6].style.display = "none";
            ref_info[7].style.display = "none";
            ref_info[8].style.display = "none";
            ref_info[9].style.display = "none";
            ref_info[10].style.display = "none";
            ref_info[11].style.display = "block";
            ref_info[12].style.display = "none";
            ref_info[13].style.display = "none";
        }　else if (value === "unpublished") {
            ref_info[0].style.display = "none";
            ref_info[1].style.display = "none";
            ref_info[2].style.display = "none";
            ref_info[3].style.display = "none";
            ref_info[4].style.display = "none";
            ref_info[5].style.display = "none";
            ref_info[6].style.display = "none";
            ref_info[7].style.display = "none";
            ref_info[8].style.display = "none";
            ref_info[9].style.display = "none";
            ref_info[10].style.display = "none";
            ref_info[11].style.display = "none";
            ref_info[12].style.display = "block";
            ref_info[13].style.display = "none";
        }　else if (value === "misc") {
            ref_info[0].style.display = "none";
            ref_info[1].style.display = "none";
            ref_info[2].style.display = "none";
            ref_info[3].style.display = "none";
            ref_info[4].style.display = "none";
            ref_info[5].style.display = "none";
            ref_info[6].style.display = "none";
            ref_info[7].style.display = "none";
            ref_info[8].style.display = "none";
            ref_info[9].style.display = "none";
            ref_info[10].style.display = "none";
            ref_info[11].style.display = "none";
            ref_info[12].style.display = "none";
            ref_info[13].style.display = "block";
        }
    }
    ref_type.addEventListener("change", changeType, false);
}());
function showEditForm(clickedButton) {
    document.getElementById("tournamentEditForm").style.display = "flex";

    var buttonParentArticle = clickedButton.parentElement
    var tournamentNameDateDiv = buttonParentArticle.children[0]
    var tournamentDateTimeDiv = tournamentNameDateDiv.children[1]

    var tournamentName = tournamentNameDateDiv.children[0].innerHTML
    var tournamentDato = tournamentDateTimeDiv.children[0].innerHTML
    var tournamentTime = tournamentDateTimeDiv.children[1].innerHTML
    var tournamentOrganizer = buttonParentArticle.children[1].innerHTML
    var tournamentLink = buttonParentArticle.children[2].getAttribute("href")
    var tournamentIDElement = buttonParentArticle.children[5].innerHTML
    

    document.getElementById("tournamentNameForm").value = tournamentName
    document.getElementById("tournamentDateForm").value = tournamentDato
    document.getElementById("tournamentTimeForm").value = tournamentTime
    document.getElementById("tournamentOrganizerForm").value = tournamentOrganizer
    document.getElementById("tournamentLinkForm").value = tournamentLink
    document.getElementById("tournamentIDForm").value = tournamentIDElement
};
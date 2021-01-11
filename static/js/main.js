let windowURL = document.URL;
let page = windowURL.split("/")[3];
// page = page != "" ? page : "home";
if (page === "") {
	page = "home";
}

menuList = document.querySelectorAll(".head-nav-menu ul li a");
for (let list of menuList) {
	let menuItem = list.textContent.toLowerCase();
	if (menuItem === page) {
		console.log("match");
		if (list.className != "current") {
			list.className = "current";
		}
	} else {
		list.className = "";
	}
}

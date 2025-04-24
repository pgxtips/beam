function dropdownSelect(event) {
    event.preventDefault();

    const item = event.target.closest(".dropdown-item");
    const dropdown = item.closest(".dropdown")
    const button = dropdown.querySelector("button");
    const text = event.target.innerHTML

    button.innerHTML = text;
}

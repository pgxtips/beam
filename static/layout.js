lucide.createIcons();

let activeDict = { 
    "/dashboard": () => document.getElementById("home-item").classList.add("active"), 
    "/dashboard/datasource": () => document.getElementById("datasource-item").classList.add("active"), 
    "/dashboard/monitor": () => document.getElementById("monitor-item").classList.add("active"),
    "/dashboard/settings": () => document.getElementById("settings-item").classList.add("active"),
};

// Get current URL path
let path = window.location.pathname;

// Lookup object and execute function if it exists
if (activeDict[path]) {
    activeDict[path]();
}

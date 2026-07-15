const themeStorageKey = "theme";

function getPreferredTheme() {
    const storedTheme = window.localStorage.getItem(themeStorageKey);

    if (storedTheme === "light" || storedTheme === "dark") {
        return storedTheme;
    }

    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}

function applyTheme(theme: "light" | "dark") {
    document.documentElement.classList.toggle("dark", theme === "dark");
    window.localStorage.setItem(themeStorageKey, theme);
}

function toggleTheme() {
    applyTheme(document.documentElement.classList.contains("dark") ? "light" : "dark");
}

applyTheme(getPreferredTheme());

document.addEventListener("click", (event) => {
    const target = event.target;

    if (target instanceof Element && target.closest("[data-theme-toggle]")) {
        toggleTheme();
    }
});

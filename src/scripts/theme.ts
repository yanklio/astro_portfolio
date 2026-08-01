const themeStorageKey = "theme";

function syncThemeControls(isDark: boolean) {
    document.querySelectorAll<HTMLElement>("[data-theme-toggle]").forEach((toggle) => {
        toggle.setAttribute("aria-pressed", String(isDark));
        toggle.setAttribute("aria-label", isDark ? "Switch to light theme" : "Switch to dark theme");
    });
}

function applyTheme(theme: "light" | "dark") {
    const isDark = theme === "dark";
    document.documentElement.classList.toggle("dark", isDark);
    try {
        window.localStorage.setItem(themeStorageKey, theme);
    } catch {}
    syncThemeControls(isDark);
}

function toggleTheme() {
    applyTheme(document.documentElement.classList.contains("dark") ? "light" : "dark");
}

document.addEventListener("DOMContentLoaded", () =>
    syncThemeControls(document.documentElement.classList.contains("dark")),
);

document.addEventListener("click", (event) => {
    const target = event.target;

    if (target instanceof Element && target.closest("[data-theme-toggle]")) {
        toggleTheme();
    }
});

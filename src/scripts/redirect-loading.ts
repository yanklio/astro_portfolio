const SETUP_KEY = "__redirectLoadingSetup";
const PRESSED_TARGET_KEY = "redirect-pressed-target";
const LOADING_STARTED_KEY = "redirect-loading-started";
const MINIMUM_LOADING_TIME = 900;
const REDIRECT_CONTROL_SELECTOR = ".redirect-control";

declare global {
    interface Window {
        [SETUP_KEY]?: boolean;
    }
}

function getLinkUrl(link: HTMLAnchorElement) {
    return new URL(link.href);
}

function isRoutedLinkClick(event: PointerEvent, link: HTMLAnchorElement) {
    const url = getLinkUrl(link);

    return (
        event.button === 0 &&
        !event.metaKey &&
        !event.ctrlKey &&
        !event.shiftKey &&
        !event.altKey &&
        url.origin === window.location.origin &&
        url.pathname !== window.location.pathname
    );
}

function getLoadingTarget(link: HTMLAnchorElement) {
    return link.closest<HTMLElement>(REDIRECT_CONTROL_SELECTOR);
}

function getTargetSelector(link: HTMLAnchorElement) {
    const href = link.getAttribute("href");
    if (!href) return null;

    return `a[href="${CSS.escape(href)}"]`;
}

function clearRedirectLoading() {
    document.querySelectorAll<HTMLElement>(".redirect-loading").forEach((target) => {
        target.classList.remove("redirect-loading");
        target.removeAttribute("aria-busy");
    });
}

function applyStoredPressedTarget() {
    const selector = sessionStorage.getItem(PRESSED_TARGET_KEY);
    if (!selector) return;

    sessionStorage.removeItem(PRESSED_TARGET_KEY);

    const link = document.querySelector<HTMLAnchorElement>(selector);
    const target = link ? getLoadingTarget(link) : null;
    target?.classList.add("pressed");
}

export function initRedirectLoading() {
    if (window[SETUP_KEY]) return;
    window[SETUP_KEY] = true;

    let loadingStartedAt = 0;
    let loadingTimer: number | undefined;

    function setRedirectLoading(link: HTMLAnchorElement) {
        window.clearTimeout(loadingTimer);
        clearRedirectLoading();

        loadingStartedAt = performance.now();
        sessionStorage.setItem(LOADING_STARTED_KEY, String(loadingStartedAt));

        const target = getLoadingTarget(link);
        if (!target) return;

        target.classList.add("pressed", "redirect-loading");
        target.setAttribute("aria-busy", "true");

        const selector = getTargetSelector(link);
        if (selector) sessionStorage.setItem(PRESSED_TARGET_KEY, selector);
    }

    function finishRedirectLoading() {
        const storedStartedAt = Number(
            sessionStorage.getItem(LOADING_STARTED_KEY) || loadingStartedAt,
        );
        const elapsed = performance.now() - storedStartedAt;
        const remaining = Math.max(MINIMUM_LOADING_TIME - elapsed, 0);

        loadingTimer = window.setTimeout(() => {
            sessionStorage.removeItem(LOADING_STARTED_KEY);
            clearRedirectLoading();
        }, remaining);
    }

    document.addEventListener(
        "pointerdown",
        (event) => {
            if (!(event.target instanceof Element)) return;

            const link = event.target.closest<HTMLAnchorElement>("a[href]");
            if (!link || !isRoutedLinkClick(event, link)) return;
            if (!getLoadingTarget(link)) return;

            setRedirectLoading(link);
        },
        { capture: true },
    );

    applyStoredPressedTarget();
    document.addEventListener("astro:page-load", () => {
        finishRedirectLoading();
        applyStoredPressedTarget();
    });
    window.addEventListener("pageshow", finishRedirectLoading);
}

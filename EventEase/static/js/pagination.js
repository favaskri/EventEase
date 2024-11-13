document.addEventListener('click', (evt) => {
    const link = evt.target.closest('a');
    if (!link || !link.closest('nav.pagination')) return;

    const allPageLinks = Array.from(document.querySelectorAll('nav.pagination ul.pages a'));
    let currentPageIndex = allPageLinks.findIndex(link => link.classList.contains('current'));

    if (link.classList.contains('previous')) {
        if (currentPageIndex > 0) currentPageIndex--;
    } else if (link.classList.contains('next')) {
        if (currentPageIndex < allPageLinks.length - 1) currentPageIndex++;
    } else if (link.closest('li.page')) {
        currentPageIndex = allPageLinks.indexOf(link);
    }

    allPageLinks.forEach(pageLink => pageLink.classList.remove('current'));
    allPageLinks[currentPageIndex].classList.add('current');
    allPageLinks[currentPageIndex].setAttribute('aria-current', 'page');

    evt.preventDefault();
});